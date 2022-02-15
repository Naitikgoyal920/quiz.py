print ("Welcome to my computer quiz!")
playing = input ("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Lets play!")
score = 0

answer = input("When was the first computer invented?")
if answer == "1943":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What was the name of the first computer invented?")
if answer == "Electronic Numerical Integrator and Computer":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("Who is known as the father of computers?")
if answer == "Charles Babbage":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What was the first computer system that used color display?")
if answer == "Apple 1":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("What was the first mass-produced computer?")
if answer == "IBM 650":
    print("correct")
    score += 1
else:
    print("incorrect")

print("You got " + str(score) + " question correct!")
print("You got " + str(score/5 *100) + "% question correct!")
