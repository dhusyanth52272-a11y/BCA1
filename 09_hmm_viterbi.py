# Hidden Markov Model - most likely state sequence
state = ["rainy", "sunny"]

ini = {"rainy": 0.6, "sunny": 0.4}

trans = {
    "rainy": {"rainy": 0.7, "sunny": 0.3},
    "sunny": {"rainy": 0.4, "sunny": 0.6}
}

emission = {
    "rainy": {"walk": 0.1, "shop": 0.4},
    "sunny": {"walk": 0.6, "shop": 0.3}
}

obser = ["walk", "shop"]

best_state = ""
best_prob = 0

for f in state:
    for s in state:
        p = (ini[f] * emission[f][obser[0]] * trans[f][s] * emission[s][obser[1]])
        if p > best_prob:
            best_prob = p
            best_state = f + "->" + s

print("Observations:", obser)
print("Most likely states:", best_state)
print("Probability:", best_prob)

# Output:
# Observations: ['walk', 'shop']
# Most likely states: sunny->sunny
# Probability: 0.043199999999999995
