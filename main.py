# Apollos Eastman
# 10/22
# Random Lists

import random
# randrange method

# Random color

colors = ['red','green','blue','yellow','purple']

color_len = len(colors)

rand_color = random.randrange(0, color_len)

print (f'Your random color is {colors[rand_color]}.\n')

# Random animal

animals = ['dog','cat','elephant','giraffe','lion']

animal_len = len(animals)

print(f'Random animal 1: {animals[random.randrange(0, animal_len)]}')
print(f'Random animal 2: {animals[random.randrange(0, animal_len)]}')
print(f'Random animal 3: {animals[random.randrange(0, animal_len)]}\n')

# Random number

numbers = [1,2,3,4,5,6,7,8,9,10]

number_len = len(numbers)

rand_num = random.randrange(0, number_len)

print(f'Your random number is {numbers[rand_num]} and it\'s index number is {rand_num}.\n')

# randint() method

# Random fruit

fruits = ['apple','banana','cherry','date','fig']

fruit_len = len(fruits)

print(f'Your random fruit is {fruits[random.randint(0,fruit_len-1)]}\n')

# Random score

students = ['Thayer','Apollos','Isaac','Lucas','Bryce']

student_len = len(students) -1

print(f'{students[0]} got a score of {random.randint(0, 100)}.')
print(f'{students[1]} got a score of {random.randint(0, 100)}.')
print(f'{students[2]} got a score of {random.randint(0, 100)}.')
print(f'{students[3]} got a score of {random.randint(0, 100)}.')
print(f'{students[4]} got a score of {random.randint(0, 100)}.\n')

# Random movie

movies = ['Ironman','Captain America','Avengers','Spiderman','Black Panther']

movie_len = len(movies)-1

rand_movie = random.randint(0,movie_len)

print(f'Your random movie is {movies[rand_movie]} and it\'s index number was {rand_movie}.')
