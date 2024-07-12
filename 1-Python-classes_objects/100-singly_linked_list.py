#!/usr/bin/python3

class Node:
    """
    Reprsents a node in a linked list (in increasing order).

    Attributes:

        data (int): data to be inserted in the new node.
        next_node (node): the next node of the current node
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Parameters:
            data (int): data to be inserted
            next_node (node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Sets or gets the data of the new node."""
        return self.__data
    
    def data(self, value):
        """ 
        Sets the data.

        Parameters:
            value (int): value of data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer.")
        self.__data = value

    def next_node(self):
        """ Sets/gets the next node of the linked list."""
        return self.__next_node
    
 
    def next_node(self, value):
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object.")
        self.__next_node = value
    

class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes a new singly linked list."""
        self.__head = None
    
    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position. 
         
        The node is inserted into the list at the correct
        ordered numerical position.

        Parameters:
            value (int): value of data.
        """
        NewNode = Node(value)
        # 1) if the list is empty.
        if self.__head is None:
            NewNode.next_node = None
            self.__head = NewNode
        
        # 2) if the value to be inserted is < data that exists => insert at the beginning.
        elif self.__head.data > value:
            NewNode.next_node = self.__head
            self.__head = NewNode

        else:
            # insertion at the end
            temp = self.__head
            while (temp.next_node is not None and
                    temp.data < value):
                temp = temp.next_node
            NewNode.next_node = temp.next_node # next_node is None "Null"
            temp.next_node = NewNode

    def __str__(self):
        """ Prints the data of the linked list."""
        ValPrint = []
        temp = self.__head
        while temp is not None:
            ValPrint.append(str(temp.data))
            temp = temp.next_node
        print("Data in the linked list: ", end="")
        return (', '.join(ValPrint))
        
        

    




    

    