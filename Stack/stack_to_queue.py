"""
Stack to queue converter.
"""

from lab_10.Queue.arrayqueue import ArrayQueue
from arraystack import ArrayStack

def stack_to_queue(stack):
    """Stack to Queue converter."""
    queue = ArrayQueue()
    storage_stack = ArrayStack()
    while not stack.isEmpty():
        popped = stack.pop()
        storage_stack.add(popped)
        queue.add(popped)
    while not storage_stack.isEmpty():
        stack.add(storage_stack.pop())
    return queue
