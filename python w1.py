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

	
Q10. What are keywords?

	key words in python are reserved words that can not be used as a variable name, function name,
     or any other identifier.	
     Ex: True,False,if,else etc..

Q11. Can we use keywords as a variable? Support your answer with reason.


Q12. What is indentation? What's the use of indentaion in Python?

		Indentation refers to the spaces at the beginning of a code line.
     Where in other programming languages the indentation in code is for readability only,  
     the indentation in Python is very important.

     Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?

	output can be throwned in python using print() function

Q14. What are operators in Python?

Arthematic operators

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
x = 0
for i in numbers:
    if i % 2 == 0:
        x += i
print("sum of even numbers in the list is",x)         


	
				
				
				
			
			
