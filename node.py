class Node(object):

    child = None
    sibling = None

    # Constructor.
    def __init__(self, name):
        self.name = name

    # Print out node name and call performAction on children and siblings.
    def perform_action(self):
        print(self.name)

        if self.has_child():
            self.child.perform_action()

        if self.has_sibling():
            self.sibling.perform_action()

    # Add a child node.
    def add_child(self, node):
        if self.has_child():
            self.child.add_sibling(node)
        else:
            self.child = node

    # Check if this node has child nodes.
    def has_child(self):
        return self.child is not None

    # Add a sibling node.
    def add_sibling(self, node):
        if self.has_sibling():
            self.sibling.add_sibling(node)
        else:
            self.sibling = node

    # Check if this node has sibling nodes.
    def has_sibling(self):
        return self.sibling is not None