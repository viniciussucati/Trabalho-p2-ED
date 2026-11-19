"""
Implementação de Referência: Árvore Binária de Busca (BST - Binary Search Tree)
Disciplina: Estrutura de Dados — Fatec Ribeirão Preto (2026.2)
"""

from __future__ import annotations
from typing import Optional, List


class Node:
    """Representa um nó individual na Árvore Binária de Busca."""

    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BST:
    """
    Árvore Binária de Busca (BST) instrumentada com contador de operações.
    Mantém a invariante: esquerda < raiz < direita.
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None
        self.comparisons: int = 0

    def reset_metrics(self) -> None:
        """Zera o contador de comparações para medir operações isoladas."""
        self.comparisons = 0

    def insert(self, key: int) -> bool:
        """
        Insere uma nova chave na BST.
        Retorna True se inserido com sucesso, ou False se a chave já existir.
        """
        inserted = False

        def _insert(current: Optional[Node], value: int) -> Node:
            nonlocal inserted
            if current is None:
                inserted = True
                return Node(value)

            self.comparisons += 1
            if value < current.key:
                current.left = _insert(current.left, value)
            elif value > current.key:
                self.comparisons += 1
                current.right = _insert(current.right, value)
            else:
                self.comparisons += 1
            return current

        self.root = _insert(self.root, key)
        return inserted

    def search(self, key: int) -> bool:
        """
        Busca uma chave na BST.
        Retorna True se encontrada, False caso contrário.
        """
        current = self.root
        while current is not None:
            self.comparisons += 1
            if key == current.key:
                return True
            self.comparisons += 1
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, key: int) -> bool:
        """
        Remove uma chave da BST tratando os 3 casos clássicos:
        1. Nó folha (sem filhos)
        2. Nó com apenas 1 filho
        3. Nó com 2 filhos (substituição pelo sucessor in-order)
        """
        deleted = False

        def _min_value_node(node: Node) -> Node:
            current = node
            while current.left is not None:
                self.comparisons += 1
                current = current.left
            return current

        def _delete(current: Optional[Node], value: int) -> Optional[Node]:
            nonlocal deleted
            if current is None:
                return None

            self.comparisons += 1
            if value < current.key:
                current.left = _delete(current.left, value)
            elif value > current.key:
                self.comparisons += 1
                current.right = _delete(current.right, value)
            else:
                self.comparisons += 1
                deleted = True
                if current.left is None:
                    return current.right
                if current.right is None:
                    return current.left

                successor = _min_value_node(current.right)
                current.key = successor.key
                current.right = _delete(current.right, successor.key)

            return current

        self.root = _delete(self.root, key)
        return deleted

    def height(self) -> int:
        """
        Calcula a altura da árvore (número de arestas do maior caminho raiz -> folha).
        Árvore vazia retorna -1; árvore apenas com raiz retorna 0.
        """
        def _height(node: Optional[Node]) -> int:
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def in_order(self) -> List[int]:
        """Travessia Em-Ordem (Esquerda -> Raiz -> Direita): retorna chaves ordenadas."""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is not None:
                _traverse(node.left)
                result.append(node.key)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def pre_order(self) -> List[int]:
        """Travessia Pré-Ordem (Raiz -> Esquerda -> Direita): útil para clonar a árvore."""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is not None:
                result.append(node.key)
                _traverse(node.left)
                _traverse(node.right)

        _traverse(self.root)
        return result

    def post_order(self) -> List[int]:
        """Travessia Pós-Ordem (Esquerda -> Direita -> Raiz): útil para desalocar nós."""
        result: List[int] = []

        def _traverse(node: Optional[Node]) -> None:
            if node is not None:
                _traverse(node.left)
                _traverse(node.right)
                result.append(node.key)

        _traverse(self.root)
        return result


if __name__ == "__main__":
    print("=" * 65)
    print("DEMONSTRAÇÃO PRÁTICA: ÁRVORE BINÁRIA DE BUSCA (BST)")
    print("=" * 65)

    # CENÁRIO 1: Caso Médio (Inserção Equilibrada / Aleatória)
    print("\n[CENÁRIO 1] Caso Médio — Inserção Equilibrada (O(log n))")
    bst_media = BST()
    elementos_equilibrados = [50, 30, 70, 20, 40, 60, 80]

    for num in elementos_equilibrados:
        bst_media.insert(num)

    print(f"Elementos inseridos : {elementos_equilibrados}")
    print(f"Altura da árvore    : {bst_media.height()} (Ideal para 7 nós = 2)")
    print(f"Comparações (Insert): {bst_media.comparisons}")
    print(f"Travessia In-Order  : {bst_media.in_order()}")
    print(f"Travessia Pre-Order : {bst_media.pre_order()}")
    print(f"Travessia Post-Order: {bst_media.post_order()}")

    bst_media.reset_metrics()
    encontrado = bst_media.search(80)
    print(f"Busca pelo valor 80 : {encontrado} | Comparações realizadas: {bst_media.comparisons}")

    # CENÁRIO 2: Pior Caso (Inserção Ordenada -> Árvore Degenerada O(n))
    print("\n[CENÁRIO 2] Pior Caso — Inserção Ordenada / Degenerada (O(n))")
    bst_pior = BST()
    elementos_ordenados = [10, 20, 30, 40, 50, 60, 70]

    for num in elementos_ordenados:
        bst_pior.insert(num)

    print(f"Elementos inseridos : {elementos_ordenados}")
    print(f"Altura da árvore    : {bst_pior.height()} (Degenerada = n - 1 = 6)")
    print(f"Comparações (Insert): {bst_pior.comparisons}")

    bst_pior.reset_metrics()
    encontrado_pior = bst_pior.search(70)
    print(f"Busca pelo valor 70 : {encontrado_pior} | Comparações realizadas: {bst_pior.comparisons}")

    # CENÁRIO 3: Casos de Borda (Remoção de nó com 2 filhos e chave inexistente)
    print("\n[CENÁRIO 3] Casos de Borda — Remoção (Nó com 2 filhos) e Busca Falha")
    bst_media.reset_metrics()
    busca_falha = bst_media.search(999)
    print(f"Busca inexistente (999): {busca_falha} | Comparações: {bst_media.comparisons}")

    bst_media.reset_metrics()
    removido = bst_media.delete(30)
    print(f"Remoção do nó 30 (2 filhos): {removido} | Comparações: {bst_media.comparisons}")
    print(f"In-Order após remoção      : {bst_media.in_order()}")
    print("=" * 65)
