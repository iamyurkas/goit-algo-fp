import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#CCCCCC"
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def color_gradient(step, total_steps):
    ratio = step / total_steps
    shade = int(255 * (1 - ratio))
    return f'#{shade:02x}{shade:02x}ff'

def dfs_visualize(root):
    stack, visited_order = [root], []
    while stack:
        node = stack.pop()
        visited_order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    visualize_traversal(visited_order, "Depth-First Search")

def bfs_visualize(root):
    queue, visited_order = deque([root]), []
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    visualize_traversal(visited_order, "Breadth-First Search")

def visualize_traversal(order, title):
    total_steps = len(order)
    for i, node in enumerate(order):
        node.color = color_gradient(i, total_steps)

    tree = nx.DiGraph()
    pos = {order[0].id: (0, 0)}
    tree = add_edges(tree, order[0], pos)

    colors = [n[1]['color'] for n in tree.nodes(data=True)]
    labels = {n[0]: n[1]['label'] for n in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# example tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# visualize DFS
dfs_visualize(root)

# reset node colors
for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]:
    node.color = "#CCCCCC"

# visualize BFS
bfs_visualize(root)