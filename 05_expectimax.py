# Expectimax algorithm
def expectimax(node, depth, is_max):
    if depth == 0 or not isinstance(node, list):
        return node
    if is_max:
        return max(expectimax(child, depth-1, False) for child in node)
    else:
        value = [expectimax(child, depth-1, True) for child in node]
        return sum(value) / len(value)

game_tree = [
    [3, 5],
    [2, 9]
]

result = expectimax(game_tree, 2, True)
print("Result:", result)

# Output:
# Result: 5.5
