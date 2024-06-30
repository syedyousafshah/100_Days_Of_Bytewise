#QuickSort Algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort(left) + middle + quicksort(right)

input_array = [4, 6, 7, 12, 1, 2, 4]

sorted_array = quicksort(input_array)

print("Sorted array:", sorted_array)

#Knapsack Problem
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        current_weight = weights[i - 1]
        current_value = values[i - 1]
        for w in range(1, capacity + 1):
            if current_weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - current_weight] + current_value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

weights = [1, 2, 3, 8]
values = [1, 5, 8, 9]
capacity = 7
max_value = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)

#Graph Traversal (BFS and DFS)
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph:  
                for neighbor in graph[vertex]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

    return visited

graph = {0: [1, 3], 1: [3], 2: [0, 4], 3: [4]}
bfs_result = bfs(graph, 2)
print("BFS traversal:", bfs_result)

#Dijkstra's Algorithm
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_dist > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 2, 'D': 7},
    'C': {'D': 5},
    'D': {}
}
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths:", shortest_paths)

#Longest Common Subsequence (LCS)
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs_length = L[m][n]
    lcs = [""] * (lcs_length + 1)

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

X = "ACADB"
Y = "CBDA"
print("Longest Common Subsequence:", lcs(X, Y))
