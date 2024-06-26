#Recursive Factorial
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
number = int(input("Enter a number: "))
result = fac(number)
print(f"The factorial of {number} is {result}.")


#Palindrome Linked List
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, value):
        if not self.head:  
            self.head = Node(value)  
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = Node(value)  

    def is_palindrome(self):
        values = []  
        current = self.head
        while current: 
            values.append(current.value)  
            current = current.next
        
        return values == values[::-1]  
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def create_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)  
    return linked_list

# Example 1: Linked list is a palindrome
values1 = [1, 2, 3, 2, 1]
linked_list1 = create_linked_list(values1)
print("Linked list 1:")
linked_list1.display()
if linked_list1.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")

# Example 2: Linked list is not a palindrome
values2 = [1, 2, 3, 4, 5]
linked_list2 = create_linked_list(values2)
print("\nLinked list 2:")
linked_list2.display()
if linked_list2.is_palindrome():
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")


# Merge Sorted Arrays
def merge(arr1, arr2):
    merged_array = []
    
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1  
        else:
            merged_array.append(arr2[j])
            j += 1  
    
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    
    return merged_array

def input_array(prompt):
    user_input = input(prompt)
    return list(map(int, user_input.split()))  

def main():
    arr1 = input_array("Enter the  first sorted array : ")

    arr2 = input_array("Enter  second sorted array  ")
    
    result = merge(arr1, arr2)
    
    print("Merged array:", result)
main()

#Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp_val = self._min_value_node(root.right)
            root.val = temp_val.val
            root.right = self._delete(root.right, temp_val.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, root):
        if root:
            self._in_order_traversal(root.left)
            print(root.val, end=" ")
            self._in_order_traversal(root.right)

def input_array(prompt):
    while True:
        try:
            user_input = input(prompt)
            return list(map(int, user_input.split()))  
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

def main():
    bst = BinarySearchTree()

    elements = input_array("Enter the elements : ")
    for element in elements:
        bst.insert(element)

    while True:
        print("\nCurrent BST in-order traversal: ")
        bst.in_order_traversal()
        print("\nChoose an operation:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            value = input_array("Enter the value to insert: ")
            for val in value:
                bst.insert(val)
        elif choice == '2':
            value = input_array("Enter the value to search: ")
            for val in value:
                result = bst.search(val)
                if result:
                    print(f"Value {val} found in the BST.")
                else:
                    print(f"Value {val} not found in the BST.")
        elif choice == '3':
            value = input_array("Enter the value to delete: ")
            for val in value:
                bst.delete(val)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()


#Merge Intervals
def merge_intervals(intervals):
    if not intervals or len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    merged = []
    current_interval = intervals[0]

    for i in range(1, len(intervals)):
        if current_interval[1] >= intervals[i][0]:
            current_interval = (current_interval[0], max(current_interval[1], intervals[i][1]))
        else:
            merged.append(current_interval)
            current_interval = intervals[i]
    merged.append(current_interval)
    return merged

def input_intervals():
    while True:
        try:
            user_input = input("Enter intervals : ")
            values = list(map(int, user_input.split()))
            if len(values) % 2 != 0:
                raise ValueError("Please enter pairs of values.")
            intervals = [(values[i], values[i + 1]) for i in range(0, len(values), 2)]
            return intervals
        except ValueError as e:
            print("Invalid input.", e)

def main():
    intervals = input_intervals()
    print("Original intervals:", intervals)
    merged_intervals = merge_intervals(intervals)
    print("Merged intervals:", merged_intervals)

main()


#Minimum Edit Distance
def min_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    
            elif j == 0:
                dp[i][j] = i    
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    
                                  dp[i - 1][j],    
                                  dp[i - 1][j - 1]) 

    return dp[m][n]

def input_strings():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1, str2

def main():
    str1, str2 = input_strings()
    result = min_edit_distance(str1, str2)
    print(f"The minimum edit distance between '{str1}' and '{str2}' is {result}")

main()

#Boggle Game
class Boggle:
    def __init__(self, board, words):
        self.board = board
        self.words = set(words)
        self.found_words = set()
        self.rows = len(board)
        self.cols = len(board[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and not self.visited[x][y]

    def dfs(self, x, y, current_word):
        if current_word in self.words:
            self.found_words.add(current_word)

        self.visited[x][y] = True

        for direction in self.directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if self.is_valid(new_x, new_y):
                self.dfs(new_x, new_y, current_word + self.board[new_x][new_y])

        self.visited[x][y] = False

    def find_words(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, self.board[i][j])
        return self.found_words

def input_boggle_data():
    board = []
    print("Enter the Boggle board row by row :")
    while True:
        row = input()
        if row == "":
            break
        board.append(row.split())

    words = input("Enter the words : ").split()
    return board, words

def main():
    board, words = input_boggle_data()
    boggle_game = Boggle(board, words)
    found_words = boggle_game.find_words()
    print("Words found in the Boggle board:", found_words)

main()
