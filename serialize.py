class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    def helper(node):
        if not node:
            return "null,"
        left_serialized = helper(node.left)
        right_serialized = helper(node.right)
        return str(node.val) + "," + left_serialized + right_serialized
    return helper(root)

def deserialize(data):
    def helper(data_list):
        if data_list[0] == "null":
            data_list.pop(0)
            return None
        node = TreeNode(data_list[0])
        data_list.pop(0)
        node.left = helper(data_list)
        node.right = helper(data_list)
        return node
    data_list = data.split(',')
    return helper(data_list)
