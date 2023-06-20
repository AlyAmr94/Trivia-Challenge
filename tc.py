
print("""
------------------------------------------------------------------------------------
████████╗██████╗░██╗██╗░░░██╗██╗░█████╗░
╚══██╔══╝██╔══██╗██║██║░░░██║██║██╔══██╗
░░░██║░░░██████╔╝██║╚██╗░██╔╝██║███████║
░░░██║░░░██╔══██╗██║░╚████╔╝░██║██╔══██║
░░░██║░░░██║░░██║██║░░╚██╔╝░░██║██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝

░█████╗░██╗░░██╗░█████╗░██╗░░░░░██╗░░░░░███████╗███╗░░██╗░██████╗░███████╗
██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░░░░██╔════╝████╗░██║██╔════╝░██╔════╝
██║░░╚═╝███████║███████║██║░░░░░██║░░░░░█████╗░░██╔██╗██║██║░░██╗░█████╗░░
██║░░██╗██╔══██║██╔══██║██║░░░░░██║░░░░░██╔══╝░░██║╚████║██║░░╚██╗██╔══╝░░
╚█████╔╝██║░░██║██║░░██║███████╗███████╗███████╗██║░╚███║╚██████╔╝███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝
------------------------------------------------------------------------------------


    """)
input("Welcome to Trivia Challenge! Press Enter to Start!")
input("This quiz will test your knowledge on six different knowledge areas and will determine if you truly are the Trivia Champion!\nPress Enter to start the game!")

score = 0

#Question 1
print("\nThe first question is about Science! What is meteorology the study of?")
print("1-Meteors and Asteroids \n2-Weather \n3-Deep-Sea Creatures \n4-Rare Earth Metals")
answer = input()
if answer == "2" or answer.lower() == "weather":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 2
print("\nThe Second question is about History! Who founded Protestantism?")
print("1-Martin Luther \n2-Johannes Calvin \n3-Pope Clement V \nEmperor Charles V")
answer = input()
if answer == "1" or answer.lower() == "martin luther":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 3
print("\nThe Third question is about Geography! What is the capital of Peru?")
print("1-Bogota \n2-Lima \n3-Port Au Prince \n4-Caracas")
answer = input()
if answer == "2" or answer.lower() == "lima":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 4
print("\nThe Fourth question is about Sports! Which team has the most wins at Le Mans?")
print("1-Porsche \n2-Ferrari \n3-Ford \n4-Toyota")
answer = input()
if answer == "1" or answer.lower() == "porsche":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 5
print("\nThe Fifth question is about Music! What is Eminem's real name?")
print("1-Marshall Mathers \n2-Mark Maddox \n3-Mike Mccoy \n4-Mickey Mantle")
answer = input()
if answer == "1" or answer.lower() == "marshall mathers":
    score += 1
    input("That's Correct! Press Enter to go to the next question!")
else: input("Wrong answer. Press Enter to go to the next question")

#Question 6
print("\nThe Sixth question is about Literature! Which British Author created the character of James Bond?")
print("1-Arthur Conan Doyle \n2-Joseph Conrad \n3-Ian Fleming \n4-Daniel Defoe")
answer = input()
if answer == "3" or answer.lower() == "ian fleming":
    score += 1
    input("That's Correct! Press Enter to continue!")
else: input("Wrong answer. Press Enter to continue")

#End messages
print("\nYou have reached the end of the quiz! Let's see how you have fared!")
print("Calculating...")
if score == 6 or score == 5:
    print("Wow! You are the king of Trivia Challenge!")
elif score == 3 or score == 4:
    print("Great job! But you still have a long way to go before you are Trivia Champion!")
elif score == 1 or score == 2:
    print("That wasn't too bad! But you can do better")
elif score == 0:
    print("Copy and paste this link in your browser: \nhttps://www.youtube.com/watch?v=bp1NP4HAs94&ab_channel=Cocomelon-NurseryRhymes")