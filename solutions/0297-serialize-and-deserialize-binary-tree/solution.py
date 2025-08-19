# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        idx = 0
        q = deque([root])

        while q:
            next_node = q.popleft()
            if next_node is None:
                output.append("NONE")
            else:
                output.append(str(next_node.val))
                q.append(next_node.left)
                q.append(next_node.right)

        serial = ",".join(output)
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "NONE":
            return None
        d = data.split(",")
        root = TreeNode(d[0])

        
        q = deque([root])
        index = 1
        while q:
            current_node = q.popleft()
            
            if d[index] != "NONE":
                current_node.left = TreeNode(d[index])
                q.append(current_node.left)
            index += 1

            if index < len(d) and d[index] != "NONE":
                current_node.right = TreeNode(d[index])
                q.append(current_node.right)
            index += 1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
