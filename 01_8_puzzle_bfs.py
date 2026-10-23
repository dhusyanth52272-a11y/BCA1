# 8 Puzzle Problem using BFS
from collections import deque

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    moves = {
        0: [1, 3], 1: [0, 2, 4],
        2: [1, 5], 3: [0, 4, 6],
        4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8],
        8: [5, 7]
    }
    for move in moves[blank]:
        new_state = state[:]
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        neighbors.append(new_state)
    return neighbors

def bfs(initial, goal):
    queue = deque()
    queue.append((initial, []))
    visited = set()
    while queue:
        current, path = queue.popleft()
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))
        if current == goal:
            return path + [current]
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                queue.append((neighbor, path + [current]))
    return None

# Get initial values from user
print("Enter initial state:")
initial = list(map(int, input().split()))

# Get goal values from user
print("Enter goal state:")
goal = list(map(int, input().split()))

solution = bfs(initial, goal)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)
    for i, state in enumerate(solution):
        print("\nStep", i)
        print_board(state)
else:
    print("No solution found.")

# Sample Output:
# Enter initial state:
# 1 2 3 4 5 6 7 0 8
# Enter goal state:
# 1 2 3 4 5 6 7 8 0
# Solution found!
# Number of moves: 1
# Step 0
# [1, 2, 3]
# [4, 5, 6]
# [7, 0, 8]
# Step 1
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 0]
