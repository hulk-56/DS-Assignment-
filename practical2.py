class doublylinklist:
  class _Node:
    def __init__(self,element,prev,next):
      self._element=element
      self._prev=prev
      self._next=next

  def __init__(self):
    self._head=self.Node(None,None,None)
    self._tail=self.Node(None,None,None)
    self._head._next=self._tail
    self._tail._prev=self._head
    self._size=0
class Node: 

    def __init__ (self, element, next = None ):
        self.element = element
        self.next = next
        self.previous = None
    def display(self):
        print(self.element)

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0



    def _len_(self):
        return self.size

  def __len__(self):
    return self._size
    def get_head(self):
        return self.head

  def is_empty(self):
    return self._size == 0

  def add_first(self,e):
    newest = self._Node(e,None,None)
    if self.is_empty():
      self._head=newest
      self._tail=newest
    else:
      newest._next=self._head
      self._head._prev=newest
    self._head=newest
    self._size += 1
    def is_empty(self):
        return self.size == 0 

  def add_last(self,e):
    newest=self._Node(e,None,None)
    if self.is_empty():
      self._head=newest
      self._tail=newest
    else:
      self._tail._next=newest
      newest._prev=self._tail
    self._tail=newest
    self._size +=1
    def display(self):
        if self.size == 0:
            print("No element")
            return 
        first = self.head
        print(first.element.element)
        first = first.next
        while first:
            if type(first.element) == type(list1.head.element):
                print(first.element.element)
                first = first.next
            print(first.element)
            first = first.next

    def reverse_display(self):
        if self.size == 0:
            print("No element")
            return None
        last = list1.get_tail()
        print(last.element)
        while last.previous:
            if type(last.previous.element) == type(list1.head):
                print(last.previous.element.element)
                if last.previous == self.head:
                    return None
                else:
                    last = last.previous
            print(last.previous.element)
            last = last.previous


  def add_any(self,e,pos):
    newest=self._Node(e,None,None)
    thead=self._head
    i=1
    while i < pos:
      thead = thead._next
      i += 1
    newest._next = thead._next
    thead._next = newest
    thead._next._prev = newest
    newest._prev = thead
    self._size += 1

  def remove_first(self):
    if self.is_empty():
      raise Empty('list is Empty')
    value = self._head._element
    self._head = self._head._next
    self._head._prev = None
    self._size -= 1
    if self.is_empty():
      self._tail = None
    return value
    def add_head(self,e):
        #temp = self.head 
        self.head = Node(e)
        #self.head.next = temp
        self.size += 1 

    def get_tail(self):
        last_object = self.head
        while (last_object.next != None):
            last_object = last_object.next
        return last_object


  def remove_last(self):
    if self.is_empty():
      raise Empty('list is empty')
    thead = self._head
    i = 0
    while i < len(self)-2:
      thead = thead._next
      i += 1
    self._tail = thead
    thead = thead._next
    value = thead._element
    self._tail._next = None
    self._size -= 1
    return value

  def remove_any(self,pos):
    if self.is_empty():
      raise Empty('list is empty')
    thead = self._head
    i = 1
    while i < pos - 1:
      thead = thaed._next
      i += 1
      thead._next = thead._next._next
      thead._next._next._prev = thead
      self._size -= 1

  def display(self):
    thead = self._head
    while thead:
      print(thead._element,end = '->')
      thead = thead._next
    print()

L = doublylinkedlist()
L.add_add(10)
L.add_add(20)
L.add_add(30)
L.display()
print('delete:',L.remove_first())
L.display()
L.add_first(70)
L.display()
print('delete:',L.remove_last())
L.display()
L.add_any(100,2)
L.display()
L.remove_any(2)
L.display()
    def remove_head(self):
        if self.is_empty():
            print("Empty Singly linked list")
        else:
            print("Removing")
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1

    def add_tail(self,e):
        new_value = Node(e)
        new_value.previous = self.get_tail()
        self.get_tail().next = new_value
        self.size += 1

    def find_second_last_element(self):
        #second_last_element = None


        if self.size >= 2:
            first = self.head 
            temp_counter = self.size -2
            while temp_counter > 0:
                first = first.next 
                temp_counter -= 1 
            return first


        else:
            print("Size not sufficient")

        return None



    def remove_tail(self):
        if self.is_empty():
            print("Empty Singly linked list")
        elif self.size == 1:
            self.head == None
            self.size -= 1
        else: 
            Node = self.find_second_last_element()
            if Node:
                Node.next = None
                self.size -= 1

    def get_node_at(self,index):
        element_node = self.head
        counter = 0
        if index == 0:
            return element_node.element
        if index > self.size-1:
            print("Index out of bound")
            return None
        while(counter < index):
            element_node = element_node.next
            counter += 1
        return element_node

    def get_previous_node_at(self,index):
        if index == 0:
            print('No previous value')
            return None
        return list1.get_node_at(index).previous

    def remove_between_list(self,position):
        if position > self.size-1:
            print("Index out of bound")
        elif position == self.size-1:
            self.remove_tail()
        elif position == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(position-1)
            next_node = self.get_node_at(position+1)
            prev_node.next = next_node
            next_node.previous = prev_node
            self.size -= 1

    def add_between_list(self,position,element):
        element_node = Node(element)
        if position > self.size:
            print("Index out of bound")
        elif position == self.size:
            self.add_tail(element)
        elif position == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(position-1)
            current_node = self.get_node_at(position)
            prev_node.next = element_node
            element_node.previous = prev_node
            element_node.next = current_node
            current_node.previous = element_node
            self.size += 1

    def search (self,search_value):
        index = 0 
        while (index < self.size):
            value = self.get_node_at(index)
            if type(value.element) == type(list1.head):
                print("Searching at " + str(index) + " and value is " + str(value.element.element))
            else:
                print("Searching at " + str(index) + " and value is " + str(value.element))
            if value.element == search_value:
                print("Found value at " + str(index) + " location")
                return True
            index += 1
        print("Not Found")
        return False

    def merge(self,linkedlist_value):
        if self.size > 0:
            last_node = self.get_node_at(self.size-1)
            last_node.next = linkedlist_value.head
            linkedlist_value.head.previous = last_node
            self.size = self.size + linkedlist_value.size

        else:
            self.head = linkedlist_value.head
            self.size = linkedlist_value.size

l1 = Node('element 1')
list1 = LinkedList()
list1.add_head(l1)
list1.add_tail('element 2')
list1.add_tail('element 3')
list1.add_tail('element 4')
list1.get_head().element.element
list1.add_between_list(2,'element between')
list1.remove_between_list(2)

list2 = LinkedList()
l2 = Node('element 5')
list2.add_head(l2)
list2.add_tail('element 6')
list2.add_tail('element 7')
list2.add_tail('element 8')
list1.merge(list2)
list1.get_previous_node_at(3).element
list1.reverse_display()
list1.search('element 6')
