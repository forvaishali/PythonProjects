print("Welcome to my computer game")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay, Lets Play :)")
score = 0

answer = input("What does CPU stand for? ")  # space after question important
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does US stand for? ")
if answer.lower() == "united states":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")  # space after question i
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else:
   print("Incorrect")

answer = input("What does RAM stand for? ")  # space after question i
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
   print("Incorrect")

print("You got " + str(score) + "  questions correct")
print("You got " + str( (score / 4) * 100 ) + "%.")
