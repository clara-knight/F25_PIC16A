class Box:

    def __init__(self, box_label, box_capacity):
        self.label = box_label
        self.capacity = box_capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            print("Not enough capacity")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not in box")

    def list_items(self):
        for item in self.items:
            print(item)


testbox1 = Box("test box 1", 3)
s = ["a", "b", "c", "d"]
for item in s:
    testbox1.add_item(item)
testbox1.list_items()
testbox1.remove_item("b")
testbox1.list_items()
testbox1.add_item("e")
testbox1.list_items()
