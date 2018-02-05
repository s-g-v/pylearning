#!/usr/bin/env python

import socket
import random
import time
import argparse
from geoip import geolite2


def create_receiver(port, timeout=1):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
    s.settimeout(timeout)
    try:
        s.bind(('', port))
    except socket.error as e:
        raise IOError("Can't bind receiver socket: {}".format(e))
    return s


def create_sender(ttl):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
    return s


def get_location(ip):
    result = geolite2.lookup(ip)
    location = []
    if result:
        location.append(result.country)
        if result.subdivisions:
            location.extend(result.subdivisions)
        if result.timezone != 'None':
            location.append(result.timezone)
        location.append(result.location)
    return location


def trace(dst, hops=30):
    port = random.choice(range(33434, 33535))
    try:
        dst_ip = socket.gethostbyname(dst)
    except socket.error as e:
        raise IOError('Unable to resolve {}:\n{}'.format(dst, e))
    print('Trace to {}({}) in max {} hops'.format(dst, dst_ip, args.hops))

    for ttl in range(1, hops + 1):
        start_time = time.time()
        receiver = create_receiver(port)
        sender = create_sender(ttl)
        sender.sendto(b'', (dst, port))
        try:
            data, addr = receiver.recvfrom(1024)
            end_time = time.time()
            duration = round((end_time - start_time) * 1000, 2)
        except socket.timeout:
            duration = None
        finally:
            receiver.close()
            sender.close()

        if addr and duration:
            location = get_location(addr[0])
            str_location = ', '.join(location[:-1]) + ', ({:.3f}, {:.3f})'.format(*location[-1]) if location else ''
            print('{:<4} {:<15} \t{:<6}ms \t{}'.format(ttl, addr[0], duration, str_location))
            if addr[0] == dst_ip:
                break
        else:
            print('{:<4} * \t*'.format(ttl))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Simple traceroute implementation')
    parser.add_argument('host', metavar='host', type=str, help='Destination host to trace route')
    parser.add_argument('--hops', '-n', type=int, help='Max number of hops', required=False, default=30)
    args = parser.parse_args()

    trace(args.host, args.hops)
