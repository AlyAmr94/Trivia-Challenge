input("Welcome to Trivia Challenge! Press Enter to Start!")
input("This quiz will test your knowledge on six different knowledge areas and will determine if you Truly are the Trivia Champion!\nPress Enter to start the game!")

score = 0

#Question 1
print("The first question is about Science! What is meteorology the study of?")
print("1-Meteors and Asteroids \n2-Weather \n3-Deep-Sea Creatures \n4-Rare Earth Metals")
answer = input()
if answer == "2" or answer == "Weather":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 2
print("The Second question is about History! Who founded Protestantism?")
print("1-Martin Luther \n2-Johannes Calvin \n3-Pope Clement V \nEmperor Charles V")
answer = input()
if answer == "1" or answer == "Martin Luther":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 3
print("The Third question is about Geography! What is the capital of Peru?")
print("1-Bogota \n2-Lima \n3-Port Au Prince \nCaracas")
answer = input()
if answer == "2" or answer == "Lima":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")