from collections import deque

class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.c_max = capacity
        self.c = 0
        self.head = Node(-1)
        self.tail = Node(-1, prev=self.head)
        self.head.next = self.tail
        self.h = {}
        self.h_n = {}
        

    def get(self, key: int) -> int:
        if key in self.h_n:
            if self.c == 1:
                return self.h[key]
            else:
                node = self.h_n[key]
                prv = node.prev
                nxt = node.next
                prv.next = nxt
                nxt.prev = prv

                h = self.head.next
                node.prev = self.head
                node.next = h
                h.prev = node
                self.head.next = node
                return self.h[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.h_n:
            if self.c == 0:
                node = Node(key, prev=self.head, next=self.tail)
                self.head.next = node
                self.tail.prev = node
            else:
                node = Node(key, prev=self.head, next=self.head.next)
                self.head.next.prev = node
                self.head.next = node
            self.c += 1
            if self.c > self.c_max:
                to_del = self.tail.prev
                to_del.prev.next = self.tail
                self.tail.prev = to_del.prev
                del self.h[to_del.key]
                del self.h_n[to_del.key]
                self.c -= 1
            self.h[key] = value
            self.h_n[key] = node
        else:
            node = self.h_n[key]
            prev = node.prev
            nxt = node.next
            
            # Убрал из середины
            prev.next = nxt
            nxt.prev = prev

            # Вставил в начало
            h = self.head.next
            h.prev = node
            self.head.next = node
            node.prev = self.head
            node.next = h

            self.h[key] = value


            




        