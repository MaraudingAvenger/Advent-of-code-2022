from typing import Any


lines = open('input.txt').read()

def recurse_get(d: dict|list, key: Any) -> Any|None:
    if isinstance(d, dict):
        if key in d:
            return d[key]
        for key in d:
            item = recurse_get(d[key], key)
            if item is not None:
                return item
    elif isinstance(d, list):
        for element in d:
            item = recurse_get(element, key)
            if item is not None:
                return item
    return None

class Node:
    '''
    a node in a NodeTree.
    Each node can have one parent and many children.
    '''
    def __init__(self, name: str, parent=None, type: str='folder', size: int=0):
        self.name = name
        self.type = type
        self.parent = parent
        self.children = []
        self._setsize(size)

    def _setsize(self, amount: int):
        self._girth = amount

    def _getsize(self) -> int:
        return self._girth + sum(child.size for child in self.children if self.children)

    size = property(_getsize, _setsize)

    def add_child(self, name, type='folder', size=0):
        self.children.append(Node(name, self, type, size))

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def __repr__(self):
        return self.name

def get_line(lines) -> str:
    try:
        return next(lines)
    except StopIteration:
        return ''

root = Node('/')
lines = iter(lines.split('\n'))
curr_node = root
while (line := get_line(lines)) != '':
    match line.split():
        case ["$", "ls"]:
            while (line := get_line(lines)) and not line.startswith('$'):
                match line.split():
                    case ['dir', name]:
                        curr_node.add_child(name) # type: ignore
                    case [size, name]:
                        curr_node.add_child(name, 'file', int(size)) # type: ignore
    match line.split():
        case ["$", "cd", path]:
            if path == '/':
                curr_node = root
            
            elif path == '..':
                curr_node = curr_node.parent

            else:
                curr_node = curr_node.get_child(path)
    
def flatten(x): # yes this is python specific, but whatever, it's translateable
    return sum(map(flatten, x), []) if isinstance(x, list) else [x]

# recursively get the size of each node in the tree
def get_size(node: Node) -> list[tuple[Node, int]]:
    return flatten([(node, node.size)] + [get_size(child) for child in node.children])

from functools import reduce

folders_under_100k = reduce(lambda x, y: (x[1] if isinstance(x,  tuple) else x) + y[1], list(
    filter(lambda x: x[0].type == 'folder' and x[1] < 100_000, get_size(root)))) # type: ignore

print(f"part 1: {folders_under_100k}")
print(f"total used space: {root.size:,} bytes")
print(f"total free space: {70_000_000 - root.size:,} bytes")
needed = 30_000_000-(70_000_000-root.size)
print(f"       still need {needed:,} bytes to get to 30mb free")

to_delete = min(filter(lambda x: x[0].type == 'folder' and x[1] >= needed , get_size(root)), key=lambda k: k[1])
print(f"part 2: {to_delete[0].name} is the smallest folder that can be deleted to free up {needed:,} bytes")
print(f"        {to_delete[0].name} is {to_delete[1]:} bytes")