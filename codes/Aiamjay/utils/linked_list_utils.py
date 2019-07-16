class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_linked_list(l):
    head = ListNode(l[0])
    temp = head
    for item in l[1:]:
        temp.next = ListNode(item)
        temp = temp.next
    return head


def lists_to_lists_of_linked_list(lists):
    return [list_to_linked_list(l) for l in lists]


def print_link_list(head):
    while head:
        print("%d->" % head.val, end="")
        head = head.next
    print("Null\n")
