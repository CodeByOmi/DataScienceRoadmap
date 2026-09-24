# prior probabbility

premium_customers = 20
total_customers = 200

prior = premium_customers / total_customers

print(prior)



# liklehood

p_purchase_given_premium = 0.8

print(p_purchase_given_premium)



# evidence

p_premium = 0.3
p_not_premium = 0.7

p_purchase_given_premium = 0.6
p_purchase_given_not_premium = 0.1

p_purchase = (
    p_purchase_given_premium * p_premium
    + p_purchase_given_not_premium * p_not_premium
)

print(p_purchase)


# posterior probability

p_premium = 0.1
p_purchase_given_premium = 0.8
p_purchase = 0.26

posterior = (
    p_purchase_given_premium * p_premium
) / p_purchase

print(posterior)



p_premium = 0.1
p_not_premium = 0.9

p_purchase_given_premium = 0.8
p_purchase_given_not_premium = 0.2

# Evidence
p_purchase = (
    p_purchase_given_premium * p_premium
    + p_purchase_given_not_premium * p_not_premium
)

# Posterior
p_premium_given_purchase = (
    p_purchase_given_premium * p_premium
) / p_purchase

print("Prior:", p_premium)
print("Evidence:", p_purchase)
print("Posterior:", p_premium_given_purchase)


p_returning = 0.4 
p_new = 0.6 

p_purchase_given_returning = 0.7
p_purchase_given_new = 0.2


#evidence 

p_purchase = p_returning * p_purchase_given_returning + p_new * p_purchase_given_new

# posterior 

p_returning_given_purchase = p_purchase_given_returning * p_returning / p_purchase

print("evidence :",p_purchase)
print("posteriror :",p_returning_given_purchase)