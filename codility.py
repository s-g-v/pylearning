def bitxor(M, N):
    arr = [i ^ (i+1) for i in range(M, N)]
    while len(arr) > 2:
        arr = [arr[i] ^ arr[i + 1] for i in range(len(arr) - 1)]
    return arr[0]


def bitxor_rec(M, N):
    if M == N:
        return 0
    if M == N-1:
        print(M, N, "=", M ^ N)
        return M ^ N
    avg = (M + N) // 2
    return bitxor_rec(M, avg) ^ bitxor_rec(avg + (M + N) % 2, N)


def f(a):
    res = [a, 1, a + 1, 0]
    return res[a % 4]


def getXor(a, b):
    return f(b) ^ f(a - 1)


def solution(A, B):
    mapping = {'t': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    digital_A = map(lambda x: int(x) if x.isdigit() else mapping[x.lower()], A)
    digital_B = map(lambda x: int(x) if x.isdigit() else mapping[x.lower()], B)
    return len([a for a, b in zip(digital_A, digital_B) if a > b])


if __name__ == '__main__':
    print(solution('a586qk23a84q', 'jj653kk2q25j'))
    print(solution('23a84q', 'k2q25j'))
    print(bitxor(5, 11))
    print(bitxor_rec(5, 11))
