Q1. Why do we call Python as a general purpose and high-level programming language?

   Python has vast application in various domains like Data science,Data Analytics
 web development and Machine learning and many more, hence it is called as general purpose.
 and it is a programming language which is human readable hence it is a high level programming language.

Q2. Why is Python called a dynamically typed language?

   In python the values will be stored in memory randomly irrespective of its data type and 
variable name will bind with the memory location. There is no need to declare the data type 
to the variable

Q3. List some pros and cons of Python programming language?

  	pros                               cons

	1.Easy to understand              1.Indentation 
	2.Vast applications  		    2.High memory consumption
 	 Ex. Data science,
      	web development
	3.Open source			    3.Complex multi threding
	4.Huge set of libraries           4.Dynamically typed
	5.Large Community                 5.Security

Q4. In what all domains can we use Python?
Data science, web development, gaming

Q5. What are variable and how can we declare them?

	Variable is name given to the memory location. Variables can be declared by following some set of rules.
    the rules are:
		1.Should start with the alphabet
		2.Should not use any special character except underscore (_)

Q6. How can we take an input from the user in Python?

	input from user can be taken by using input() function.


Q7. What is the default datatype of the value that has been taken as an input using input() function?

	Always a string

Q8. What is type casting?
	
	Convertion of one data type into another data type 

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

	yes, taking multiple inputs is possible with the input() function by using split method or list comprehension method
    Ex: # taking three inputs at a time
	x, y, z = input("Enter three values: ").split()
	print("Total number of students: ", x)
	print("Number of boys is : ", y)
	print("Number of girls is : ", z)
	

	
Q10. What are keywords?

	key words in python are reserved words that can not be used as a variable name, function name,
     or any other identifier.	
     Ex: True,False,if,else etc..	

Q11. Can we use keywords as a variable? Support your answer with reason.

	Keywords are predefined, reserved words used in Python programming that have special meanings to the compiler.

We cannot use a keyword as a variable name, function name, or any other identifier. They are used to define the syntax and structure of the Python language.

Q12. What is indentation? What's the use of indentaion in Python?

		Indentation refers to the spaces at the beginning of a code line.
     Where in other programming languages the indentation in code is for readability only,  
     the indentation in Python is very important.

     Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?

	output can be throwned in python using print() function

Q14. What are operators in Python?

Python Operators in general are used to perform operations on values and variables.
These are standard symbols used for the purpose of logical and arithmetic operations
Arthematic operators:
 Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division.

	
Operator	Description							Syntax

+	        Addition: adds two operands					x + y
–	        Subtraction: subtracts two operands				x – y
*		Multiplication: multiplies two operands				x * y
/		Division (float): divides the first operand by the second	x / y
//		Division (floor): divides the first operand by the second	x // y
%		Modulus: returns the remainder when the first operand is 
	                 divided by the second					x % y
**		Power: Returns first raised to power second			x ** y

Comparison Operators:
                    Comparison of Relational operators compares the values. 
		    It either returns True or False according to the condition.
		
Operator	Description								Syntax
>		Greater than: True if the left operand is greater than the right	x > y
<		Less than: True if the left operand is less than the right		x < y
==		Equal to: True if both operands are equal				x == y
!=		Not equal to – True if operands are not equal				x != y
>=		Greater than or equal to True if the left operand is
		greater than or equal to the right					x >= y
<=		Less than or equal to True if the left operand is less than 
		or equal to the right							x <= y
is 		x is the same as y							x is y
is not		x is not the same as y							x is not y

Logical Operators:
Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

Operator	Description						Syntax
and		Logical AND: True if both the operands are true		x and y
or		Logical OR: True if either of the operands is true 	x or y
not		Logical NOT: True if the operand is false 		not x

	
	
Q15. What is difference between / and // operators?

	/ is an opearator used for float division
	// is an operator used for integer division
	
Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

x = "iNeuron"
print(x*4)


Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

int_num = int(input("Enter the number"))
if int_num % 2 == 0:
    print(int_num," is Even")
else:
    print(int_num, " is odd" ) 
Q18. What are boolean operator?

 	 The opearators representing or gives an idea wheather it is true or false to an condition, the boolean key words are:
		"True","False"
	
Q19. What will the output of the following?
```
1 or 0  >>>> True

0 and 0  >>>> False

True and False and True >>> False

1 or 0 or 0  >>>> True

Q20. What are conditional statements in Python?

	There comes situations in real life when we need to do some specific task and based on some specific conditions and,
	we decide what should we do next. Similarly there comes a situation in programming where a specific task is to be 
	performed if a specific condition is True. In such cases, conditional statements can be used. 
	The following are the conditional statements provided by Python. 

if
if..else
Nested if
if-elif statements.

Q21. What is use of 'if', 'elif' and 'else' keywords?

 These key words are used to apply various conditions to the expression. filtering can be done by these key words.


Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

		age = int(input("Enter your age"))

		if age >= 18:
   		    print("I can vote")
		else:
    		    print("I can't vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]

code:
numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for i in numbers:
    if i % 2 == 0:
        sum += i
print("sum of even numbers in the list is",sum) 


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

num1,num2,num3 = input("Enter 3 values").split()
if num1 > num2 and num1 > num3:
  print(num1,"is the largest number ")
elif num2 > num1 and num2 > num3:
   print(num2,"is the largest number ")
else:
  print(num3,"is the largest number")


       OR

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print(maximum(1,2,3))

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
list = []
for i in numbers:
  if i > 150:
    
    if i > 500:
      break
    continue
  if i % 5 == 0:
    list.append(i)
print(list)   
   

				
				
				
			
			
