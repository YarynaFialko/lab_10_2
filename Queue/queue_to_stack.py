"""
Queue to stack converter.
"""

from lab_10.Stack.arraystack import ArrayStack

def  queue_to_stack(queue):
    """Stack to Queue converter."""
    storage_stack = ArrayStack()
    stack = ArrayStack()
    count = len(queue)
    while count > 0:
        popped = queue.pop()
        storage_stack.add(popped)
        queue.add(popped)
        count -= 1
    while not storage_stack.isEmpty():
        stack.add(storage_stack.pop())
    return stack
