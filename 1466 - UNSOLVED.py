# -*- coding: utf-8 -*-

'''
Percurso em Árvore por Nível
'''


from queue import Queue


class Leaf():

    '''
    Folha.
    '''

    value: int
    left: None
    right: None

    def __init__(self, new_value: int) -> None:

        self.value = new_value
        self.left = None
        self.right = None

    def add(self, new_value: int) -> None:
        '''
        Adiciona um valor.
        '''

        if new_value < self.value:

            if self.left is not None:
                self.left.add(new_value)
            else:
                self.left = Leaf(new_value)
        else:

            if self.right is not None:
                self.right.add(new_value)
            else:
                self.right = Leaf(new_value)

    def get_value(self, values_list: list, leaf_queue: Queue) -> None:
        '''
        Adiciona os valores pelo nível
        '''

        values_list.append(self.value)

        if self.left is not None:
            leaf_queue.put(self.left)

        if self.right is not None:
            leaf_queue.put(self.right)

        if not leaf_queue.empty():
            leaf_queue.get().get_value(values_list, leaf_queue)


class BinaryTree():

    '''
    Árvore.
    '''

    root: None
    queue: Queue

    def __init__(self, max_queue_size: int) -> None:
        self.root = None
        self.queue = Queue(max_queue_size)

    def add(self, new_value: int) -> None:
        '''
        Adiciona um valor na árvore.
        '''

        if self.root is not None:
            self.root.add(new_value)
        else:
            self.root = Leaf(new_value)

    def get_values(self) -> list:
        '''
        Retorna todos os valores da árvore em uma lista.
        '''

        values = []

        if self.root is not None:
            self.root.get_value(values, self.queue)

        return values


test_count = int(input())

for i in range(test_count):

    size = int(input())
    input_values = list(map(int, input().split()))

    binary_tree = BinaryTree(size)

    for value in input_values:
        binary_tree.add(value)

    print(f"Case {i + 1}:")
    print(" ".join([str(value) for value in binary_tree.get_values()]))
    print()
