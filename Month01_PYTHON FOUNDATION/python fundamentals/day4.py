# # # # # # # # # fuctions
# # # # # # def add(a, b):
# # # # # #     return a + b

# # # # # # sum = add(563,837)
# # # # # # print(sum)


# # # # # # # def sqr(a):
# # # # # # #     return a * a

# # # # # # # ans = sqr(19)
# # # # # # # print(ans)


# # # # # # def check_num(n):
# # # # # #     if n % 2 == 0:
# # # # # #         print("even")
# # # # # #     else:
# # # # # #         print("odd")
    
# # # # # # check_num(7)

# # # # # def largest_num(a,b,c):
# # # # #     if a > b and a > c:
# # # # #         print(a, "is largest number")
# # # # #     elif b > c:
# # # # #         print(b, "is largest number")
# # # # #     else:
# # # # #         print(c, "is largest number")

# # # # # # largest_num(7,6,8)

# # # # def voting_eligible(age):
# # # #     if age >= 18 :
# # # #      print("you are eligible to vote")
# # # #     else:
# # # #        print("not eligible to vote")

# # # # voting_eligible(5)


# # # # def check_num(n):
# # # #     if n > 0 :
# # # #         print("positive")
# # # #     elif n < 0:
# # # #         print("negative")
# # # #     else:
# # # #         print("zero")

# # # # check_num(-2)

# # # # def show_num(n):
# # # #     for i in range(1, n+1):
# # # #         print(i)
# # # # show_num(10)
# # # def sum_num(n):
# # #   sum = 0    
# # #   for i in range(1,n+1):
# # #            sum += i
# # #   return sum


# # # sum = sum_num(100)
# # # print(sum)


# def check_digit(n):
#     count = 0

#     if n == 0:
#         return 1
    
#     while n > 0:
#         count += 1
#         n = n // 10

#     return count


# print(check_digit(1234))



# def check_prime(n):

#      if n <= 1:
#           return False
     
#      for i in range(2,n):
#           if n % i == 0:
#                return False
#      return True

# print(check_prime(15))

# def check_pattern(n):
#     for i in range(1, n + 1):
#         print("*" * i)
    
# check_pattern(150)



    
