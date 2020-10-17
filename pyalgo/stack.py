from typing import Union, List


class StackIsFullError(Exception):
    """Used to raise an error when Stack is full."""
    pass


class Stack(list):
    """Python implementation of a Stack Data Structure.

    Args:
        elements: List of elements in stack.
        max_size: Maximum capacity of stack.

    Attributes:
        max_size: Maximum capacity of stack.
        size: Size of Stack object.

    Raises:
        StackIsFullError: If number of elements exceeds max_size.

    Examples:
        >>> s = Stack()
        >>> s.push(3)
        >>> print(s)
        [3]
        >>> s.empty()
        False
    """

    def __init__(self, elements: List[Union[str, int]], max_size: int = 10) -> None:
        if len(elements) > max_size:
            raise StackIsFullError(
                f"Number of elements in stack must be less than {max_size}"
            )
        super(Stack, self).__init__(elements)
        self.max_size = max_size

    def empty(self) -> bool:
        """Returns True if Stack is empty."""
        return len(self) == 0

    @property
    def size(self) -> int:
        """Returns the size of stack.
        Getter property decorator makes this method
        accessible as an attribute.
        """
        return len(self)

    def peek(self) -> Union[int, str, None]:
        """Returns value at top of stack"""
        if not self.empty():
            return self[-1]

    def push(self, value: Union[int, str]) -> None:
        """Adds element to top of stack.

        Parameters
        ----------
        value:
            This value will be added to end of stack.

        Returns
        -------
        None
        """
        if self.size == self.max_size:
            raise StackIsFullError(
                "Stack is full, cannot add any more elements to stack."
            )
        self.append(value)
