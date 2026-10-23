# Hill Climbing Algorithm
heur = {
    'A': 5, 'B': 8, 'C': 4, 'D': 10, 'E': 7, 'F': 3, 'G': 2, 'H': 12,
    'I': 9, 'J': 6, 'K': 9, 'L': 15, 'M': 11, 'N': 8, 'O': 18, 'P': 4
}

graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'],
    'C': ['F', 'G'], 'D': ['H', 'I'],
    'E': ['J'], 'F': ['K'],
    'G': [], 'H': ['L', 'M'],
    'I': ['J'], 'J': ['N'],
    'K': [], 'L': ['O'],
    'M': [], 'N': ['P'],
    'O': [], 'P': []
}

def hill_climb(start):
    current = start
    visited = [current]
    while True:
        neigh = graph[current]
        if not neigh:
            break
        best = max(neigh, key=lambda x: heur[x])
        if heur[best] > heur[current]:
            current = best
            visited.append(best)
        else:
            break
    print("Visited state")
    for i in visited:
        print(i, "->", heur[i])
    return current

goal = hill_climb('A')
print("Goal reached:", goal)

if goal == 'P':
    print("The goal is reached successfully")
else:
    print("No solution found")

print("Result:")
print("The hill climbing algorithm is executed successfully")

# Output:
# Visited state
# A -> 5
# B -> 8
# D -> 10
# H -> 12
# L -> 15
# O -> 18
# Goal reached: O
