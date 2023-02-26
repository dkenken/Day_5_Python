# Exercises Day #5

# Using the For Loop with Python Lists

fruits = ["apple", "cherry", "watermelon", "banana"]

for fruit in fruits:
    print(fruit)

    print(fruit + " Pie")

# You are going to write a program that calculates the average student height from a List of heights.

total_height = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


for height in student_heights:
   total_height += height
   average = total_height / (len(student_heights))
print(round(average))

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# My Own Program
# Create a program to calculate the mean of the basketball players' score

player_score = input("Enter each palyer score for tonight "). split()
for n in range(0, len(player_score)):
    player_score[n] = int(player_score[n])

total_score = 0
for score in player_score:
   total_score += score
   mean = total_score / (len(player_score))
print(mean)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# You are going to write a program that calculates the max score from a List of scores.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for score in student_scores:
    if score > max:
        max = score
print(f"The highest score is the class is: {max}")     

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# My Own Exercise

# Create a program to calculate the highest player score

individual_score = input("Enter each player's score " ).split()
for n in range(0, len(individual_score)):
   individual_score[n] = int(individual_score[n])

highest_score = 0

for score in individual_score:
   if score > highest_score:
      highest_score = score
print(f"He has the highest score and it is: {highest_score}")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# For Loops and the Range() Function

total = 0
for number in range(1, 101):
   total += number
print(total)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum+= number
print(sum)

# My Own Exercise

# Create a program to calculates the sum of the even numbers from 1 to 200 range.

sum = 0
for i in range(1, 201):
   if number % 2 == 0:
      sum += i
print(sum)     

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range (1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# My Own Exercise

# You are going to write a program that automatically prints the solution to the CoolBeans game.
# Your program should print each number from 1 to 50 in turn.
# When the number is divisible by 2 then instead of printing the number it should print "Cool".
# When the number is divisible by 4, then instead of printing the number it should print "Beans".`
# And if the number is divisible by both 2 and 4 e.g. 8 then instead of the number it should print "CoolBeans"

for number in range (1, 51):
    if (number % 2 == 0) and (number % 4 == 0):
        print('CoolBeans')
    elif number % 2 == 0:
        print('Cool')
    elif number % 4 == 0:
        print('Beans')
    else:
        print(number)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ' '
# nr_letters = 4
for char in range(1, nr_letters + 1):
    # 1 - 4
    random_char = random.choice(letters)
    password += random_char
    
for char in range(1, nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_char

for char in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
# nr_letters = 4
for char in range(1, nr_letters + 1):
    # 1 - 4
    password_list.append(random.choice(letters))
    
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char


print(f'Your password is: {password}')