class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return repr(self.data)

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def print_data(self):
        print(self.get_data())


class LinkedList:
    def __init__(self, initializer_list=[]):
        self.first = None
        self.last = None
        self.len = 0
        if isinstance(initializer_list, list):
            for d in initializer_list:
                self.append(d)

    def __len__(self):
        return self.len

    def __str__(self):
        if self.first:
            self_list = []
            current_node = self.first
            while current_node:
                self_list.append(str(current_node) + " -> ")
                current_node = current_node.get_next()
            return "[" + "".join(self_list) + "]"
        else:
            return "Error: no nodes in linked list."

    def __repr__(self):
        if self.first:
            self_list = []
            current_node = self.first
            while current_node:
                self_list.append(str(current_node))
                current_node = current_node.get_next()
            return "LinkedList([" + ",".join(self_list) + "])"
        else:
            return "[]"

    def append(self, data):
        newNode = Node(data)
        if self.len:
            self.last.set_next(newNode)
            self.set_last(newNode)
            self.len += 1

        else:
            self.set_first(newNode)
            self.set_last(self.first)
            self.len = 1

    def prepend(self, data):
        newNode = Node(data)
        if self.len:
            newNode.set_next(self.first)
            self.set_first(newNode)
            self.len += 1

        else:
            self.set_first(newNode)
            self.set_last(self.first)
            self.len = 1

    def insert_idx(self, data, idx):
        if not idx:
            self.prepend(data)
        elif idx == self.len:
            self.append(data)

    def set_first(self, node):
        self.first = node

    def set_last(self, node):
        self.last = node

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_length(self):
        return self.len
