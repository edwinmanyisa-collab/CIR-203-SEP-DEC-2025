class Node:
    def _init_(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def _init_(self):
        self.head = None

    def insert(self, name, admission, grades):
        new_data = {
            "Name": name,
            "Admission": admission,
            "Grades": grades 
        }
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


students = LinkedList()

students.insert("Mantissa", "CIT/00067/024", {"Python": 75, "Java": 60, "Visual basic": 58})
students.insert("Skim", "CIT/00099", {"Python": 80, "Java": 78, "Visual basic": 76})
students.insert("Kale", "CIT/000032", {"Python": 82, "Java": 90, "Visual basic": 72})

students.display()