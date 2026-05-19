import unittest
from orderSystem import Order, OrderList

class TestOrderSystem(unittest.TestCase):

    def linkify(self, array):
        if not array:
            return None
        head = Order(array[0])
        current = head
        for value in array[1:]:
            current.next = Order(value)
            current = current.next
        return head
    
    def listify(self, head):
        result = []
        current = head
        while current:
            result.append(current.id)
            current = current.next
        return result
    
    def testAppend(self):
        newList = OrderList()
        newList.append(1)
        newList.append(2)
        self.assertEqual(self.listify(newList.head),[1,2])
