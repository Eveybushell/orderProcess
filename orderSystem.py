class Order:
    def __init__(self, id, customerName="Jane Doe", description="default order"):
        self.id = id
        self.customerName = customerName
        self.description = description
        self.next = None
    
class OrderList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, id, customerName="Jane Doe", description="default order"):
        newNode = Order(id, customerName, description)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def display(self):
        if not self.head:
            print("No list detected")
            return
        else:
            current = self.head
            while current:
                print(f"Order ID: {current.id}")
                print(f"Customer Name: {current.customerName}")
                print(f"Description: {current.description}")
                current = current.next
    
    def reverse(self):
        if not self.head:
            print("No list detected")
            return
        else:
            originalHead = self.head

            previous = None
            current = self.head
            while current:
                nextNode = current.next
                current.next = previous
                previous = current
                current = nextNode
            
            self.tail = originalHead
            self.head = previous


