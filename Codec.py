class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                return []
            serialized = [str(node.val)]
            for child in node.children:
                serialized.extend(dfs(child))
            serialized.append("#")  # Mark end of children for this node
            return serialized

        return " ".join(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        tokens = iter(data.split())
        return self._build_tree(tokens)

    def _build_tree(self, tokens):
        node_val = next(tokens)
        if node_val == "#":
            return None
        node = Node(int(node_val), [])
        while tokens:
            peek = next(tokens)
            if peek == "#":
                break
            node.children.append(self._build_tree(tokens))
        return node

# Example Usage:
tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
codec = Codec()
serialized = codec.serialize(tree)
print("Serialized:", serialized)
deserialized = codec.deserialize(serialized)
print("Deserialized Root Value:", deserialized.val)  # Outputs: 1
