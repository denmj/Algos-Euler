class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        end = LinkedList(data)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def delete(self, data):
        n = self
        if n.data == data:
            return n.next
        while n.next != None:
            if n.next.data == data:
                n.next = n.next.next
                return self
            n = n.next
        return self

    def print_list(self):
        n = self
        while n.next != None:
            print(n.data)
            n = n.next
        print(n.data)