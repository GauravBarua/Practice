from Node import Node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    @staticmethod
    def create_node(data):
        return Node(data)

    def insert_head(self, data):
        """
        Creates a new node at the Head of the Linked List

        This has a time complexity of O(1) as we are simply changing
        the current head of the Linked List and no indices have to
        change
        """

        # create a new node to hold the data
        new_node = self.create_node(data)

        # set the next of the new node to the current head
        new_node.set_next(self.head)

        # set the head of the Linked List to the new head
        self.head = new_node

        # add 1 to the count
        self.count += 1

    def insert_tail(self, data):
        """
        Creates a new node at the tail of the linked list.
        Basically it behaves like append() in lists.

        This has a time complexity of O(n) as we need to traverse
        from head to the last node.
        """
        # new node creation
        new_node = self.create_node(data)

        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        # starting with the first node in Linked List
        current = self.head

        # iterating over the nodes to find the last node
        while current.get_next() is not None:
            current = current.get_next()

        # You are at the last node now so give this node the ref of new node
        current.set_next(new_node)
        self.count += 1

    def __str__(self):
        """
        Traverse the Linked list and print it!

        Time complexity is O(1) as in worst case scenario
        have to iterate over whole Linked List.
        """

        # start with the first item in the Linked List
        item = self.head
        result = ''
        # then iterate over the next nodes
        # but if item = None then end search
        while item is not None:
            result += str(item.get_data()) + '->'
            item = item.get_next()

        return result[:-2]

    def __len__(self):
        """
        Return the length of the Linked List

        Time complexity O(1) as only returning a single value
        """

        return self.count

    def is_empty(self):
        """
        Returns whether the Linked List is empty or not
        Time complexity O(1) as only returns True or False
        """
        # we only have to check the head if is None or not
        return self.head is None

    def insert_after(self, after, data):
        new_node = self.create_node(data)
        curr_node = self.head

        while curr_node is not None:
            if curr_node.get_data() == after:
                break
            curr_node = curr_node.get_next()

        if curr_node is not None:
            new_node.set_next(curr_node.get_next())
            curr_node.set_next(new_node)
            self.count += 1
        else:
            return 'Item Not Found!'

    def clear(self):
        """
        This will use to empty a linked list
        :return:an empty linked list
        """
        self.head = None
        self.count = 0

    def delete_head(self):
        if self.head is None:
            return 'Empty LL'

        self.head = self.head.get_next()
        self.count -= 1

    def pop(self):
        if self.head is None:
            return 'Empty LL'

        curr_node = self.head

        if curr_node.get_next() is None:
            self.delete_head()
            return

        while curr_node.get_next().get_next() is not None:
            curr_node = curr_node.get_next()

        curr_node.set_next(None)
        self.count -= 1

    def remove(self, value):

        if self.head is None:
            return 'Empty Linked list'

        if self.head.get_data() == value:
            # you want to remove the head node
            return self.delete_head()

        curr_node = self.head

        while curr_node.get_next() is not None:
            if curr_node.get_next().get_data() == value:
                break
            curr_node = curr_node.get_next()

        # 2 cases
        # Item not found!
        if curr_node.get_next() is None:
            return 'Not Found!'
        else:
            curr_node.set_next(curr_node.get_next().get_next())

    def search(self, value):
        """
        searching a node in the linked list
        :param value: what value you want to search
        :return: index value where the value is found
        """

        curr_node = self.head
        pos = 0

        while curr_node is not None:
            if curr_node.get_data() == value:
                return pos
            curr_node = curr_node.get_next()
            pos = pos + 1
        return 'Not Found!'

    def __getitem__(self, index):
        """
        Finding Node by index value
        :param index:
        :return:
        """
        curr_node = self.head
        pos = 0

        while curr_node is not None:
            if pos == index:
                return curr_node.get_data()
            curr_node = curr_node.get_next()
            pos += 1
        raise IndexError
