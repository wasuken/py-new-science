from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        return (self == other)
    def __lt__(self, other: Any) -> bool:
        return (self < other) and self != other
    def __gt__(self, other: Any) -> bool:
        return (not self < other) and self != other
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other
    def __ge__(self: C, other: C) -> bool:
        return not self < other

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

def dfs(initial: T, goal_test: Collable[[T], bool], successors: Collable[[T], List[T]]) -> Optional[Node[T]]:
    frontiner: Stack[Node[T]] = Stack()
    frontiner.push(Node(initial, None))
    explored: Set[T] = {initial}

    while not frontiner.empty:
        current_node: Node[T] = frontiner.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontiner.push(Node(child, current_node))
    return None

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    @property
    def empty(self) -> bool:
        return not self.container
    def push(self) -> T:
        self._container.append(item)
    def pop(self) -> T:
        return self_container.pop()
    def __repr__(self) -> self:
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost:float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

if __name__== '__main__':
    print(linear_contains([1, 5, 15, 15, 20], 5))
    print(linear_contains(["a", "d", "e", "f", "z"], "f"))
    print(binary_contains(["john","mark","ronald","sarah"], "shelia"))
