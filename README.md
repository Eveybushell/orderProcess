# orderProcess

## Questions
1. It seems counter-intuitive for a business to prioritize most recent orders first. The usual intuition is a first in first out mindset.
2. Keeping orders in a singly linked list is not the ideal data structure. A more standard structure would be a queue for first in first out or a stack if you want most recent orders first.

## Complexity
Append: Time is O(1) and Space is O(1). A new node is created and added to the end of the linked list via its tail
Display: Time is O(n) and Space is O(1). The entire list is traversed, however no new structures or objects are added.
Reverse: Time is O(n) and Spaace is O(1). Again, the list is reversed a single time with pointers being changed. No structures or objects are created.

