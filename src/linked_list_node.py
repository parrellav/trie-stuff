class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(desc, linked_list):
    my_list = []
    while linked_list.next is not None:
        my_list.append(str(linked_list.data))
        linked_list = linked_list.next
    my_list.append(str(linked_list.data))
    bleh = ','.join(my_list)
    print(f'{desc} - {bleh}')


def reverse(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def reverse_sub_list(head, p, q):
    prev, current, next = None, head, None
    while current:
        if current.data < p or current.data > q:
            prev = current
            current = current.next
        else:
            next = current.next
            current.next = prev
            prev = current
            current = next
    return head


def has_cycle(head):
    result = False
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            result = True
            break

    return result


def is_palindromic_linked_list(head):
    slow, fast = head, head
    left_stack = []
    while fast is not None and fast.next is not None:
        left_stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    # slow should be at middle now
    while slow is not None and slow.next is not None:
        if left_stack.pop() != slow.next.data:
            return False
        slow = slow.next
    return True
