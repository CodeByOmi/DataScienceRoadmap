outcomes = ["Heads", "Tails"]
print(outcomes)



outcomes = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in outcomes if x%2 == 0] 
print(even_numbers)



favorable = 2
total = 6
probability = favorable / total
print(probability)


p_failure = 0.08

p_no_failure = 1 - p_failure
print(p_no_failure)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

intersection = A & B
union = A | B

print(intersection)
print(union)

