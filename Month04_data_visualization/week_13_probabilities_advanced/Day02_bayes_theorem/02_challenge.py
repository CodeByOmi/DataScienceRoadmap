# A company uses an AI system to identify high-value customers.

# data

# |                            | High Value | Normal |
# | -------------------------- | ---------: | -----: |
# | Clicked Recommendation |         40 |     60 |
# | Didn't Click          |         10 |     90 |


# Total = 200 customers.

# Let:

# H = High Value
# C = Clicked Recommendation



p_h = 50/200 

p_c_given_h = 40/50

p_c = 100/200

p_h_given_c = (p_c_given_h * p_h ) / p_c

print(p_h,p_c_given_h,p_c,p_h_given_c)

