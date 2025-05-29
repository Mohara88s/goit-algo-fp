import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, tree_title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(num=tree_title, figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def dfs(root):
    # Ініціалізація стеку з коренем
    stack = [root]  
    # ініціалізую колір та обчислюю крок кольору
    color_level=0
    color_step = 255//count_nodes(root)
    while stack:
        # Вилучаємо вузол зі стеку
        node = stack.pop()  
        # Відвідуємо вузол і змінюємо його колір
        node.color = '#{:02X}{:02X}{:02X}'.format(int(color_level), 255, int(color_level))
        color_level+=color_step
        # Додаємо дочірні вузли до стеку
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    # Повертаємо множину відвіданих вузлів після завершення обходу

def bfs(root):
    # Ініціалізація черги з коренем
    queue = deque([root])
    # ініціалізую колір та обчислюю крок кольору
    color_level=0
    color_step = 255//count_nodes(root)
    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо вузол з черги
        node = queue.popleft()
        # Відвідуємо вузол і змінюємо його колір
        node.color = '#{:02X}{:02X}{:02X}'.format(int(color_level), int(color_level), 255)
        color_level+=color_step
        # Додаємо дочірні вузли до черги
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    # Повертаємо множину відвіданих вузлів після завершення обходу

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


# Відображення дерева dfs
dfs(root)
draw_tree(root, 'Обхід дерева в глибину')

# Відображення дерева bfs
bfs(root)
draw_tree(root, 'Обхід дерева в ширину')



