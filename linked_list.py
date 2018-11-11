#!/usr/bin/env python3
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert(self, data):
        self.head.data = data
        new_head = Node()
        new_head.next = self.head
        self.head = new_head
        self.length += 1

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

    def remove_from_end(self, k):
        cur = self.head
        shift = self.head
        for _ in range(k + 1):
            shift = shift.next
        while shift.next:
            cur = cur.next
            shift = shift.next
        cur.next = cur.next.next
        self.length -= 1

    def printer(self):
        elems = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def reverse(self):
        self._reverse(self.head.next)

    def _reverse(self, cur):
        if cur.next:
            self._reverse(cur.next)
            cur.next.next = cur
            cur.next = None
        else:
            self.head = Node()
            self.head.next = cur


if __name__ == "__main__":
    ll = LinkedList()
    print("Empty list")
    ll.printer()
    print("Length %s" % ll.length)
    print("Add elements")
    for i in [1, 'a', 0.5, {}]:
        ll.append(i)
    ll.printer()
    print("Length %s" % ll.length)
    print("Get 2nd element: %s" % ll.get(1))
    print("Remove 3rd element")
    ll.remove(2)
    ll.printer()
    print("Length %s" % ll.length)
    ll.remove_from_end(2)
    ll.printer()
    print("Length %s" % ll.length)
    ll.insert(0)
    ll.printer()
    ll.reverse()
    ll.printer()
