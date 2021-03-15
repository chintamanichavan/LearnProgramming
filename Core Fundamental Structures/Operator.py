# Arithmetic Operators
# Examples of Arithmetic Operator 
a = 9
b = 4

# Addition of numbers 
add = a + b 

# Subtraction of numbers 
sub = a - b 

# Multiplication of number 
mul = a * b 

# Division(float) of number 
div1 = a / b 

# Division(floor) of number 
div2 = a // b 

# Modulo of both number 
mod = a % b 

# Power 
p = a ** b 

# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod) 
print(p)

# Relational Operators
# Examples of Relational Operators 
a = 13
b = 33

# a > b is False 
print(a > b) 

# a < b is True 
print(a < b) 

# a == b is False 
print(a == b) 

# a != b is True 
print(a != b) 

# a >= b is False 
print(a >= b) 

# a <= b is True 
print(a <= b)

# Logical Operators
# Examples of Logical Operator 
a = True
b = False

# Print a and b is False 
print(a and b) 

# Print a or b is True 
print(a or b) 

# Print not a is False 
print(not a)

# Bitwise Operators
# Examples of Bitwise operators 
a = 10
b = 4

# Print bitwise AND operation 
print(a & b) 

# Print bitwise OR operation 
print(a | b) 

# Print bitwise NOT operation 
print(~a) 

# print bitwise XOR operation 
print(a ^ b) 

# print bitwise right shift operation 
print(a >> 2) 

# print bitwise left shift operation 
print(a << 2)

# Assignment Operators


# Special Operators
    # Identity
    # Examples of Identity operators 
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3] 


print(a1 is not b1) 


print(a2 is b2) 

# Output is False, since lists are mutable. 
print(a3 is b3) 

    # Membership
    # Examples of Membership operator 
x = 'Geeks for Geeks'
y = {3:'a',4:'b'} 


print('G' in x) 

print('geeks' not in x) 

print('Geeks' not in x) 

print(3 in y) 

print('b' in y) 


# Precedence and Associativity of Operators
    # Operator Precedence
    # Examples of Operator Precedence 

# Precedence of '+' & '*' 
expr = 10 + 20 * 30
print(expr) 

# Precedence of 'or' & 'and' 
name = "Alex"
age = 0
	
if name == "Alex" or name == "John" and age >= 2 : 
	print("Hello! Welcome.") 
else : 
	print("Good Bye!!") 

    # Operator Associativity
    # Examples of Operator Associativity 

# Left-right associativity 
# 100 / 10 * 10 is calculated as 
# (100 / 10) * 10 and not 
# as 100 / (10 * 10) 
print(100 / 10 * 10) 
	
# Left-right associativity 
# 5 - 2 + 3 is calculated as 
# (5 - 2) + 3 and not 
# as 5 - (2 + 3) 
print(5 - 2 + 3) 
	
# left-right associativity 
print(5 - (2 + 3)) 
	
# right-left associativity 
# 2 ** 3 ** 2 is calculated as 
# 2 ** (3 ** 2) and not 
# as (2 ** 3) ** 2 
print(2 ** 3 ** 2) 
