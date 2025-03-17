class Node:
    def __init__(self, data):
        self.data = data  # 节点存储的数据
        self.next = None  # 指向下一个节点的指针


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # assgin head to the new node if head is empty
        if not self.head:
            self.head = new_node
            return
        # assgin last node to the new node if head is not empty
        # start from header first, then loop to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        """打印链表所有节点"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # 表示链表结束


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(7)
my_list.display()  # 输出: 1 -> 2 -> 3 -> 4 -> None
