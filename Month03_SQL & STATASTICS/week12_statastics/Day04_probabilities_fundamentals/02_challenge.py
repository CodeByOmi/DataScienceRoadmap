outcomes = {1, 2, 3, 4, 5, 6}

a = {x for x in outcomes if x % 2 == 0}

b = {x for x in outcomes if x > 3}

print(a)
print(b)

intersection = a & b
print(intersection)

union = a|b
print(union)


p_a = len(a) / len(outcomes)
p_b = len(b) / len(outcomes)
p_intersection = len(intersection) / len(outcomes)
p_union = len(union) / len(outcomes)
print(p_a,p_b,p_intersection,p_union)


complement_a = outcomes - a
p_complement = len(complement_a) / len(outcomes)
print(p_complement) 

#other methode
p_c = 1 - p_a
print(p_b)


p_union1 = p_a + p_b - p_intersection

print(p_union1)



