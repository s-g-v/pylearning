#!/usr/bin/env python3
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def append(self, data):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            print("ERROR: Index out of range")
            return
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.data

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("ERROR: Index out of range")
            return
        last = self.head
        cur = self.head
        for _ in range(index + 1):
            last = cur
            cur = cur.next
        last.next = cur.next
        self.length -= 1

    def print(self):
        elems = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elems.append(cur.data)
        print(elems)


if __name__ == "__main__":
    ll = LinkedList()
    print("Empty list")
    ll.print()
    print("Length %s" % ll.length)
    print("Add elements")
    for i in [1, 'a', 0.5, {}]:
        ll.append(i)
    ll.print()
    print("Length %s" % ll.length)
    print("Get 2nd element: %s" % ll.get(1))
    print("Remove 3rd element")
    ll.remove(2)
    ll.print()
    print("Length %s" % ll.length)
