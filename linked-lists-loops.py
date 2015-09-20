class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # To build a circular linked list
    def insert_node(self, node):
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next()
        # Does python not do auto returns?
        return size

    def has_loop(self):
        # options:
        #   - incorrect
        #     1. go through the loop and check for the end (infinite loop issue if loop exists)
        #     2. mark extra data in each node as having been here already
        #          -> problem: marking `seens` as false to start out?? (in stricture langs anyway)
        #   - correct
        #     1. reverse the list
        previous_node = None
        start_node = self.head
        current_node = self.head
        next_node = None

        if not current_node.get_next():
            return false

        while current_node:
            next_node = current_node.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node
            self.print_list()

        return previous_node == start_node

    def print_list(self):
        current = self.head
        values = ""
        # TODO: don't attempt print if there is a cycle?
        i = 1
        while current and i < 4:
            values += str(current.get_data())
            current = current.get_next()
            if current:
                values += ", "
        print(values)

head = Node(5)
loopy_list = LinkedList(head)
loopy_list.insert(6)
loopy_list.insert(1)
# loopy_list.insert_node(head)
print(loopy_list.has_loop())

