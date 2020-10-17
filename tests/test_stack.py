import pytest
from pyalgo.stack import Stack
from pyalgo.stack import StackIsFullError

# Stack Integration Test


class TestStack:
    def test_push_element(self):
        stack = Stack([1, 2, 3], max_size=5)
        stack.push(6)
        assert stack == [1, 2, 3, 6]

    def test_peak_element(self):
        stack = Stack([1, 4, 6], max_size=5)
        assert stack.peek()

    def test_size(self):
        stack = Stack([2, 6, 3], max_size=5)
        assert stack.size == 3

    def test_pop(self):
        stack = Stack([3, 4, 5], max_size=5)
        assert stack.pop() == 5
        assert stack == [3, 4]

    def test_raise_stack_full_error(self):
        # TEST CORRECT ERROR MESSAGE WHEN STACK IS FULL
        stack = Stack([5, 7, 8], max_size=3)
        with pytest.raises(StackIsFullError) as e:
            assert stack.push(9)
        assert str(
            e.value) == "Stack is full, cannot add any more elements to stack."
