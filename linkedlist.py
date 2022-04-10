class Node:
    def __init__(self, data, nex=None):
        self.data = data
        self.next = nex


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        data = Node(val)
        tail.next = data

    def count(self, val):
        current = self.head
        counter = 0
        while current:
            if current.data == val:
                counter += 1
            current = current.next
        return counter

    def pop(self, index):
        if index < 0:
            index += len(self)
        if len(self) <= index or index < 0:
            raise Exception("...You are Popping out of the range...")
        counter = 0
        current = self.head
        prev = None
        while counter < index:
            counter += 1
            prev = current
            current = current.next
        if prev:
            prev.next = current.next
            return current.data
        temp = current
        self.head = current.next
        del current
        return temp.data

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        self.head = prev

    def index(self, val, ind=0):
        if ind < 0:
            ind = len(self)
        current = self.head
        counter = 0
        index = 0
        while current and (current.data != val or counter < ind):
            if current.data == val:
                counter += 1
            current = current.next
            if not current:
                return index
            index += 1
        return index

    def clear(self):
        del self.head
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __str__(self):
        res = "["
        current = self.head
        while current:
            res += str(current.data)
            if current.next:
                res += ","
                res += " "
            current = current.next
        res += "]"
        return res


if __name__ == "__main__":
    b = LinkedList()

    b.append(10)
    b.append(10)
    b.append(20)
    b.append(30)
    b.append(10)

    print(b)
