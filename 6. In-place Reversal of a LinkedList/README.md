In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem. In the following chapters, we will solve a bunch of problems using this pattern.

Let's jump on to our first problem to understand this pattern.

```
def reverse(head):
    current = head
    previous = None
    next = None
    while current:
        next = current.next #store next value
        current.next = previous #store this for next
        previous = current # previous > previous.next.
        current = next #increment current
    return previous
```

