# Water Jug problem using BFS
from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))
    while queue:
        (a, b), path = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]
        if a == target or b == target:
            return path
        next_state = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b), (a, 0),
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))
        ]
        for state in next_state:
            if state not in visited:
                queue.append((state, path))
    return None

jug_a = int(input("Enter capacity of jug A: "))
jug_b = int(input("Enter capacity of jug B: "))
target = int(input("Enter the target: "))

solution = water_jug_bfs(jug_a, jug_b, target)

if solution:
    print("Solution found!")
    step = 0
    for state in solution:
        print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
        step += 1
else:
    print("No solution exist")

# Sample Output:
# Enter capacity of jug A: 5
# Enter capacity of jug B: 3
# Enter the target: 4
# Solution found!
# Step 0: Jug A = 0, Jug B = 0
# Step 1: Jug A = 5, Jug B = 0
# Step 2: Jug A = 2, Jug B = 3
# Step 3: Jug A = 2, Jug B = 0
# Step 4: Jug A = 0, Jug B = 2
# Step 5: Jug A = 5, Jug B = 2
# Step 6: Jug A = 4, Jug B = 3
