class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_before_element(self, element:Node, data: int):
        if element is None:
            print("Вузла не існує.")
            return
        new_node = Node(data)

        if self.head == element:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev = None
        cur = self.head
        while cur:
            if cur.next == element:
                prev = cur
                cur = cur.next
                prev.next = new_node
                new_node.next = cur
                return
            cur = cur.next
        if cur is None:
            return
        
    def reverse_linked_list(self):
        prev = None
        cur = self.head
        while cur:
            next_el = cur.next
            cur.next = prev
            prev = cur
            cur = next_el
        self.head = prev

    def get_middle_of(self, head):
        if head == None:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sorted_lists(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        
        if left.data <= right.data:
            left.next = self.merge_sorted_lists(left.next, right)
            return left
        else:
            right.next = self.merge_sorted_lists(left, right.next)
            return right

    def sort_linked_list(self, head:Node=None)->Node:
        if head is None:
            head = self.head

        if head is None or head.next is None:
            return head
        
        middle = self.get_middle_of(head)
        next_to_middle = middle.next
        middle.next = None

        return self.merge_sorted_lists(self.sort_linked_list(head), self.sort_linked_list(next_to_middle))
    
    def merge_sort(self):
        self.head=self.sort_linked_list()

    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        new_list1 = list1.copy()
        new_list2 = list2.copy()

        new_list = LinkedList()
        head1 = new_list1.head
        head2 = new_list2.head
        new_list.head = new_list1.merge_sorted_lists(head1, head2)
        return new_list
    
    @staticmethod
    def merge_two_unsorted_lists_to_sorted_list(list1, list2):
        new_list1 = list1.copy()
        new_list2 = list2.copy()
        
        new_list1.merge_sort()
        new_list2.merge_sort()

        new_list = LinkedList()
        head1 = new_list1.head
        head2 = new_list2.head
        new_list.head = new_list1.merge_sorted_lists(head1, head2)
        return new_list

    def copy(self):
        copied_list = LinkedList()
        if self.head is None:
            return copied_list

        current_original = self.head
        copied_list.head = Node(current_original.data)
        current_copied = copied_list.head

        while current_original.next:
            current_original = current_original.next
            current_copied.next = Node(current_original.data)
            current_copied = current_copied.next

        return copied_list
      
# Створення однозв’язного списку
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 5:")
element = llist.search_element(5)
if element:
    print(element.data)

# Вставка елементу
print()
llist.insert_before_element(element,111)
llist.print_list()

# Реверсування однозв'язного списку, змінюючи посилання між вузлами
llist.reverse_linked_list()
print("\nЗв'язний список після реверсу даних:")
llist.print_list()

# Сортування однозв'язного списку
llist.merge_sort()
print("\nЗв'язний список після сортування даних:")
llist.print_list()

# Створення ще одного однозв’язного списку
llist1 = LinkedList()

# Вставляємо вузли в початок
llist1.insert_at_beginning(5)
llist1.insert_at_beginning(10)
llist1.insert_at_beginning(15)
llist1.insert_at_beginning(30)
llist1.insert_at_beginning(12)
llist1.insert_at_beginning(15)
llist1.insert_at_beginning(20)
print("\nДругий зв'язний список:")
llist1.print_list()

# Об’єднання двох не сортованих однозв’язних списки в один сортовний
llist2 = LinkedList.merge_two_unsorted_lists_to_sorted_list(llist, llist1)
print("\nОб’єднані два не сортованих однозв’язних списки в один сортований:")
llist2.print_list()

# Сортування другого однозв'язного списку
llist1.merge_sort()
print("\nДругий зв'язний список після сортування даних:")
llist1.print_list()


# Об’єднання двох сортованих однозв’язних списки
llist3 = LinkedList.merge_two_sorted_lists(llist, llist1)
print("\nОб’єднані два сортованих однозв’язних списки:")
llist3.print_list()

# Немутовані зв’язані списки
print("\nНемутований перший зв'язний список:")
llist.print_list()
print("\nНемутований другий зв'язний список:")
llist1.print_list()
