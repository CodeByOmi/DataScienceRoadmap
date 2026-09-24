# A company has 100 customers:

#                    Purchased   Not Purchased
#Clicked Ad              30            20
#Didn't Click            10            40

# A = Purchased
# B = Clicked Ad


p_A = 40 / 100
print(p_A)

p_B = 50 / 100
print(p_B)


p_A_and_B = 30 / 100
print(p_A_and_B)


p_A_given_B = 30 / 50
print(p_A_given_B)

p_B_given_A = 30 / 40
print(p_B_given_A)


expected = p_A * p_B

print("P(A ∩ B):", p_A_and_B)
print("P(A) × P(B):", expected)
print(p_A_and_B == expected)
