import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements.
# Current runtime is 0(n^2)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        cur_node = self
        right_node = self.right
        left_node = self.left
        loop = True
        while loop == True:
            loop = False
            if value == cur_node.value:
                duplicates.append(value)
            elif value[0] > cur_node.value[0]:
                if right_node == None:
                    cur_node.right = BinarySearchTree(value)
                else:
                    cur_node = right_node
                    right_node = cur_node.right
                    left_node = cur_node.left
                    loop = True
            elif value[0] < cur_node.value[0]:
                if left_node == None:
                    cur_node.left = BinarySearchTree(value)
                else:
                    cur_node = left_node
                    right_node = cur_node.right
                    left_node = cur_node.left
                    loop = True

        # if value[0] > self.value[0]:
        #     cur_node = self.right
        #     if cur_node == None:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        # else:
        #     if self.left == None:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)
search_tree = BinarySearchTree('M')
for name_1 in names_1:
    search_tree.insert(name_1)

# for name_2 in names_2:
#     search_tree.insert(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
