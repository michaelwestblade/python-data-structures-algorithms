class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return True
    def prepend(self, value) -> bool:
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True



    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        previous = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next

        self.tail = previous
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def set(self, index, value):
        temp = self.get(index)

        if temp is None:
            return False

        temp.value = value
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        previous = self.get(index - 1)
        temp = previous.next

        previous.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(1)

my_linked_list.print_list()

my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(0))

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

another_linked_list = LinkedList(1)
another_linked_list.append(2)
another_linked_list.append(3)
another_linked_list.append(4)
another_linked_list.append(5)
another_linked_list.append(6)
another_linked_list.append(7)

another_linked_list.reverse()