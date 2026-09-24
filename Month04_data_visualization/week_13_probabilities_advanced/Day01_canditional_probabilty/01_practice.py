#1 canditional probabilty

total_remote = 40
completed_remote  = 30

probability = completed_remote / total_remote

print(probability)



p_A_and_B = 0.15
p_B = 0.30

p_A_given_B = p_A_and_B / p_B

print(p_A_given_B)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

intersection = A & B

probability = len(A&B) / len(B)

print(intersection,probability)


p_A = 0.4
p_B = 0.5

p_A_and_B = p_A * p_B

print(p_A_and_B)


red = 8
total = 10

p_first_red = red / total

red_after_draw = 7
total_after_draw = 9

p_second_red = red_after_draw / total_after_draw

print("First:", p_first_red)
print("Second:", p_second_red)



p_A = 0.6
p_B = 0.5
p_A_and_B = 0.3

expected = p_A * p_B

print(expected)

print( p_A_and_B == expected )




