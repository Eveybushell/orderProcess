class Order:
    def __init__(self, id, name="Jane Doe", details="default order"):
        self.id = id
        self.name = name
        self.details = details
        self.next = None

class OrderList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, id, name="Jane Doe", details="default order"):
        newNode = Order(id, name, details)

        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def display(self):
        if not self.head:
            print("No Orders currently")
        else:
            current = self.head
            while current:
                print(current.id)
                print(current.name)
                print(current.details)
                current = current.next
    
    def reverse(self):
        oldhead = self.head

        prev = None
        current = self.head
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        self.tail = oldhead
        self.head = prev