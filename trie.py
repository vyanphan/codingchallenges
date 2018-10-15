from typing import Tuple

class TrieNode(object):
    def __init__(self, c: str):
        self.c = c
        self.children = []
        self.end = False
        self.counter = 1
    

def add(root, word):
    node = root
    for c in word:
        in_child = False
        for child in node.children:
            if child.c == c:
                child.counter += 1
                node = child
                in_child = True
                break
        if not in_child: # can also add in sorted order
            new_node = TrieNode(c)
            node.children.append(new_node)
            node = new_node
    node.end = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    node = root
    if not root.children:
        return False, 0
    for c in prefix:
        c_not_found = True
        for child in node.children:
            if child.c == c:
                c_not_found = False
                node = child
                break
        if c_not_found:
            return False, 0
    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))