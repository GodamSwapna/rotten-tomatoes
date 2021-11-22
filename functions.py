# def add(num1,num2):
#     sum=num1+num2
#     return sum
# print(add(2,3))

# i=0
# while 0:
#     print(i)
#     break
    


# str1="madam"
# str2=""
# i=-1
# while i>=-len(str1):
#     str2+=str1[i]
#     i=i-1
# if str1==str2:
#     print("polydrom")
# else:
#     print("Not polydrom")

# num=int(input("enter a number"))
# num2=num%100
# num3=num2//10
# str=str(num3)
# if str=="7":
#     print("right")
# else:
#     print("wrong")

# i=1
# eve_num=[]
# odd_num=[]
# while i<=100:
#     if i%2==0:
#         eve_num.append(i)
#     else:
#         odd_num.append(i)
#     i+=1
# print("even numbers:",eve_num)
# print("odd numbers:",odd_num)



# def power(x, y):

#   if y == 0:

#     return 1

#   else:

#     return x * power(x, y-1)

		

# print(power(2, 3))

# nums = (55, 44, 33, 22)
# # 
# # print(max(min(nums[:2]), abs(-42)))
# print(max(min(nums[:2]),abs(-42)))


  
# with open("test.txt") as f:
#     print(f.read())



# print("Error")
# print(8**(1/3))

# a=888//60
# b=888%60
# print("hours for 888 minuts ",a)
# print("remaining minuts ",b)

# print("1.\n 2.ln")

# spam = 2 

# eggs = 3 

# del spam 

# print(spam * eggs)

# def addition(a,b):
#     return a+b
# def substraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#     return a%b
# def main(num1,num2):
#     print(addition(num1,num2))
#     print(substraction(num1,num2))
#     print(multiplication(num1,num2))
#     print(division(num1,num2))
# number1=int(input("Enter a number user input1:"))
# number2=int(input("Enter a number user input2:"))
# main(number1,number2)

# def print_msg(msg):
#     # This is the outer enclosing function

#     def printer():
#         # This is the nested function
#         print(msg)

#     printer()

# # We execute the function
# # Output: Hello
# print_msg("Hello")

# def print_msg(msg):
#     # This is the outer enclosing function

#     def printer():
#         # This is the nested function
#         print(msg)

#     return printer  # returns the nested function


# # Now let's try calling this function.
# # Output: Hello
# another = print_msg("Hello")
# another()

def make_multiplier_of(n):
    # print(n)
    def multiplier(x):
        # print(x)
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# # Output: 27
print(times3(9))

# # Output: 15
print(times5(3))

# # Output: 30
print(times5(times3(2)))