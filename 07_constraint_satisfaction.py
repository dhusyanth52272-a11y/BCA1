# Constraint Satisfaction Technique
variables = ["A", "B", "C"]
colors = ["Red", "Green", "Blue"]
solution = {}

def is_valid(variable, color):
    for other in solution:
        if variable != other and solution[other] == color:
            return False
    return True

def solve(index):
    if index == len(variables):
        return True
    variable = variables[index]
    for color in colors:
        print("Trying", variable, "=", color)
        if is_valid(variable, color):
            solution[variable] = color
            print("Valid")
            if solve(index + 1):
                return True
            print("BackTrack:", variable, "=", color)
            del solution[variable]
        else:
            print("Constraint violated")
    return False

if solve(0):
    print("\nFinal Solution")
    for variable in variables:
        print(variable, "=", solution[variable])
else:
    print("No solution exists")

# Output:
# Trying A = Red
# Valid
# Trying B = Red
# Constraint violated
# Trying B = Green
# Valid
# Trying C = Red
# Constraint violated
# Trying C = Green
# Constraint violated
# Trying C = Blue
# Valid
# Final Solution
# A = Red
# B = Green
# C = Blue
