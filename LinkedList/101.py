class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # type: ignore

    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head  # type: ignore
        self.head = new_node

    def delete_value(self, value):
        current = self.head
        # Check if the list is empty
        if not current:
            print("The list is empty!")
            return
        # Check if the head node is the one to delete
        if current.value == value:
            self.head = current.next
            return
        # Traverse to find the node to delete
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        # If we reach here, the value was not found
        print(f"{value} is not found in the linked list!")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # define next node since current node is not None
            current.next = prev  # type: ignore # 翻转链表 从current到prev
            prev = current  # 移动窗口：current变下一次执行的prev
            current = next_node  # 移动窗口：next_node变下一次执行的current
        self.head = prev  # 执行完毕后，把head设置为最后一个非None的node（这是current是None）

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def return_middle(self):
        sn1 = self.head
        sn2 = self.head
        while sn2 and sn2.next:  # if sn2 node is None or sn2 next node is None. stop loop.

            sn1 = sn1.next        # every loop go next node.(1 step jump)
            sn2 = sn2.next.next   # every loop go next next node.(2 step jump)

        return sn1.value        # return the middle value, which is sn1.value


sll = SinglyLinkedList()
sll.delete_value(2)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.append(7)
sll.append(7)
sll.append(7)
sll.append(7)
sll.append(7)
sll.append(7) 
sll.prepend(1)
print(sll.return_middle())
sll.display()
print("After reversed!!!\n")
sll.reverse()
sll.display()  # 输出: 0 -> 1 -> 2 -> 3 -> None

sll.delete_value(2)
sll.delete_value(4)
sll.delete_value(5)
sll.display()  # 输出: 0 -> 1 -> 3 -> None

print(True and False)
print(True or False)
print(0 and 1)
print(0 or 1)
