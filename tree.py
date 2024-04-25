from typing import Optional, TypeVar
from node import Node

T = TypeVar('T')


class BinaryTree:
    def __init__(self, data: T):
        self.__root: Optional[Node] = Node(data)
        self.current = self.__root
        self.pos = 0
        self.word = ''
        self.filles = ''

    @property
    def root(self):
        return self.__root

    def insert_left(self, data: T, ref: T):
        node = self.search(ref)
        if node is not None:
            new_node = Node(data)
            if node.left is None:
                node.left = new_node
            else:
                raise Exception("The left side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def insert_right(self, data: T, ref: T):
        node = self.search(ref)
        if node is not None:
            new_node = Node(data)
            if node.right is None:
                node.right = new_node
            else:
                raise Exception("The right side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def insert_at(self, data: T):
        if self.current.data is None:
            raise ReferenceError('No existe arbol')

        elif self.current.data[self.pos] == data[self.pos]:
            self.pos += 1
            self.insert_at(data)

        elif self.current.data[self.pos] > data[self.pos]:
            if self.current.left is None:
                self.insert_left(data, self.current.data)
                self.current = self.__root
                self.pos = 0

            else:
                self.current = self.current.left
                self.insert_at(data)

        elif self.current.data[self.pos] < data[self.pos]:
            if self.current.right is None:
                self.insert_right(data, self.current.data)
                self.current = self.__root
                self.pos = 0

            else:
                self.current = self.current.right
                self.insert_at(data)
    def print_inorder(self, root):
        if root is not None:
            self.print_inorder(root.left)
            print(root.data)
            self.print_inorder(root.right)

    def print_preorder(self, root):
        if root is not None:
            print(root.data)
            self.print_inorder(root.left)
            self.print_inorder(root.right)

    def print_postorder(self, root):
        if root is not None:
            self.print_inorder(root.left)
            self.print_inorder(root.right)
            print(root.data)

    def min(self):
        if self.current is not None:
            if self.current.left is None:
                return self.current.data
            else:
                self.current = self.current.left
                self.min()

    def max(self):
        if self.current is not None:
            if self.current.right is None:
                return self.current.data
            else:
                self.current = self.current.right
                self.max()

    def depth(self, ref: T, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]
        if node is None:
            return -1
        elif node.data == ref:
            return 0
        else:
            # Retornar a 27
            left = self.depth(ref, node.left)
            right = self.depth(ref, node.right)
            if left == -1 and right == -1:
                # No existe en ningún lado
                return -1
            else:
                # Existe en algún lado
                return max(left, right) + 1

    def search(self, word: T, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.data == word:
                return node
            else:
                result = self.search(word, node.left)
                if result is None:
                    result = self.search(word, node.right)
                    return result
                else:
                    return result
        else:
            return None

    def search_file(self, word: T):
        if self.current is not None:
            for i in self.current.data:
                self.word += i
                if i == ' ':
                    if self.word == word:
                        for j in range(1, 11):
                            with open(f'{i}', 'r') as archivo:
                                contenido = archivo.read()
                                if self.current.data == contenido:
                                    self.filles += str(f'La palabra esta en el archivo {i}\n')

                        self.word = ''
                    else:
                        self.word = ''

            if self.current.left is not None:
                self.current = self.current.left
                self.search_file(word)
            elif self.current.right is not None:
                self.current = self.current.right
                self.search_file(word)
            else:
                return self.filles

        else:
            return None

    def height(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is None:
            return 0
        else:
            altura = max(self.height(node.left), self.height(node.right)) + 1
            return altura