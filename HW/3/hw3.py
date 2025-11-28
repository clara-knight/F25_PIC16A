class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return repr(self.data)

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.data == other.data:
                return True
        return False


class LinkedList:
    def __init__(self, initializer_list=[]):
        self.first = None
        self.last = None
        self.len = 0
        try:
            for d in initializer_list:
                self.append(d)
        except Exception as e:
            print(f"Error: {e}")

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        current_self_node = self.first
        current_other_node = other.first
        while current_self_node and current_other_node:
            if current_self_node != current_other_node:
                return False
            current_self_node = current_self_node.next
            current_other_node = current_other_node.next
        return current_self_node == current_other_node

    def __len__(self):
        return self.len

    def __str__(self):
        if self.first:
            self_list = []
            current_node = self.first
            while current_node:
                self_list.append(str(current_node) + " -> ")
                current_node = current_node.next
            return "[" + "".join(self_list) + "]"
        return "Error: no nodes in linked list."

    def __repr__(self):
        if self.first:
            self_list = []
            current_node = self.first
            while current_node:
                self_list.append(str(current_node))
                current_node = current_node.next
            return "LinkedList([" + ", ".join(self_list) + "])"
        return "Linkedlist([])"

    def append(self, data):
        newNode = Node(data)
        if self.len:
            self.last.next = newNode
        else:
            self.first = newNode
        self.last = newNode
        self.len += 1

    def prepend(self, data):
        newNode = Node(data)
        if self.len:
            newNode.next = self.first
        else:
            self.last = newNode
        self.first = newNode
        self.len += 1

    def insert(self, data, idx):
        if not idx:
            self.prepend(data)
        elif idx >= self.len:
            self.append(data)
        else:
            j = 1
            current_node = self.first
            while j < idx:
                current_node = current_node.next
                j += 1
            newNode = Node(data)
            newNode.next = current_node.next
            current_node.next = newNode
            self.len += 1


LL = LinkedList([1, 2, "3", 4])
print(LL)
print(repr(LL))
