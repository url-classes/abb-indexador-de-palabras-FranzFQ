from __future__ import annotations
from typing import Optional, TypeVar


T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def is_leaf(self):
        return self.left is None and self.right is None