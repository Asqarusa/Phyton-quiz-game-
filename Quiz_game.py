print("welcome to my computer quiz!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay Let's start:) " )
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central proccessing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer2 = input("What does GPU stand for? ")
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer3 = input("What does RAM stand for? ")
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer4 = input("What does PU stand for? ")
if answer4.lower() == "power suply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer5 = input("How old am I? ")
if answer5.lower() == "22":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got" ,(score), " answers correct")
print("You got" ,(score/5*100), "%.")

