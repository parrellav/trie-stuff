import unittest
from src.linked_list_node import *


class TestLinkedListNode(unittest.TestCase):

    def test_reverse_list(self):
        head = None
        for i in reversed(range(7)):
            head = Node(i + 1, head)

        printList("Original Linked List", head)
        head = reverse(head)
        printList("Reversed Linked List", head)

    # doesn't work yet
    # def test_longest_common(self):
    #     head = None
    #     for i in reversed(range(7)):
    #         head = Node(i + 1, head)
    #
    #     (m, n) = (2, 5)
    #
    #     printList("Original Linked List", head)
    #     head = reverse_partial(head, m, n)
    #     # printList("Reversed Linked List", head)

    def test_has_cycle(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        self.assertFalse(has_cycle(head))
        head.next.next.next.next.next.next = head.next.next
        self.assertTrue(has_cycle(head))

    def test_is_palindromic(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(2)
        self.assertTrue(is_palindromic_linked_list(head))
        head.next.next.next.next.next = Node(2)
        self.assertFalse(is_palindromic_linked_list(head))

    def test_reverse_sub_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        printList('normal', head)
        printList('sub list reversed', reverse_sub_list(head, 2, 4))