class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def print_data(self):
        print(self.get_data())


class LinkedList:
    def __init__(self, initializer_list):
        if isinstance(initializer_list, list):
            self.len = 0
            for d in initializer_list:
                self.append(d)

    def append(self, data):
        if self.len:
            newNode = Node(data)
            self.last.set_next(newNode)
            self.set_last(newNode)
            self.len += 1

        else:
            self.set_first(Node(data))
            self.set_last(self.first)
            self.len = 1

    def prepend(self, data):
        if self.len:
            newNode = Node(data)
            self.first.set_next(newNode)
            self.set_first(newNode)
            self.len += 1

        else:
            self.set_first(Node(data))
            self.set_last(self.first)
            self.len = 1

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

    def print_ll(self):
        current_node = self.first
        while True:
            current_node.print_data()
            if current_node.get_next() is not None:
                current_node = current_node.get_next()
            else:
                break
