# Missionaries and Cannibals Problem using BFS
from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    rm = 3 - m
    rc = 3 - c
    if rm > 0 and rc > rm:
        return False
    return True

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([(start, [start])])
    visited = {start}
    moves = [
        (1, 0),
        (0, 1),
        (2, 0),
        (0, 2),
        (1, 1)
    ]
    while queue:
        state, path = queue.popleft()
        m, c, boat = state
        if state == goal:
            return path
        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)
            if is_valid(new_state[0], new_state[1]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    return None

solution = solve()

print("Solution:")
for state in solution:
    m, c, boat = state
    side = "Left" if boat == 0 else "Right"
    print("Missionaries:", m, "Cannibals:", c, "Boat:", side)

# Output:
# Solution:
# Missionaries: 3 Cannibals: 3 Boat: Left
# Missionaries: 3 Cannibals: 1 Boat: Right
# Missionaries: 3 Cannibals: 2 Boat: Left
# Missionaries: 3 Cannibals: 0 Boat: Right
# Missionaries: 3 Cannibals: 1 Boat: Left
# Missionaries: 1 Cannibals: 1 Boat: Right
# Missionaries: 2 Cannibals: 2 Boat: Left
# Missionaries: 0 Cannibals: 2 Boat: Right
# Missionaries: 0 Cannibals: 3 Boat: Left
# Missionaries: 0 Cannibals: 1 Boat: Right
# Missionaries: 1 Cannibals: 1 Boat: Left
# Missionaries: 0 Cannibals: 0 Boat: Right
