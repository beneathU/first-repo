Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input("Q1) Do you like Dawn or Dusk? \n  1) Dawn\n  2) Dusk\n Enter your answer: "))
if q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")

q2 = int(input("Q2) When I'm dead, I want people to remember me as: \n  1) The Good\n  2) The Great\n  3) The Wise\n  4) The Bold\n Enter your answer:"))
if q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif q2 == 2:
  Slytherin = Slytherin + 2
elif q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print("wrong input")

q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n  1) The violin\n  2) The trumpet\n  3) The piano\n  4) The drum\n Enter your answer:"))
if q3 == 1:
  Slytherin = Slytherin + 3
elif q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print("wrong input")

print(f"🦁 Gryffindor: {Gryffindor}")
print(f"🦅 Ravenclaw: {Ravenclaw}")
print(f"🦡 Hufflepuff: {Hufflepuff}")
print(f"🐍 Slytherin: {Slytherin}")