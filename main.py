import os, time, random

title = "TOP TRUMPS"

characters = {}

characters["Himayat"] = {"Energy": 150, "Stubborn": 90, "Cuteness": 80, "Beauty": 200, "Anger": 200}
characters["Rumaysa"] = {"Energy": 170, "Stubborn": 50, "Cuteness": 150, "Beauty": 100, "Anger": 30}
characters["Zehra"] = {"Energy": 140, "Stubborn": 180, "Cuteness": 100, "Beauty": 140, "Anger": 90}
characters["Haroon"] = {"Energy": 50, "Stubborn": 200, "Cuteness": 100, "Beauty": 50, "Anger": 78}

while True:
  print(f"{title}")
  print()
  print("Characters")
  print()
  for key in characters:
    print(key)
  user = input("Pick your character: ")
  comp = random.choice(list(characters.keys()))
  print("Computer picked: ", comp)

  print("Choose your stat: Energy, stubborn, Cuteness, Beauty, Anger")

  answer = input("> ")

  print(f"{user}: {characters[user][answer]}")
  print(f"{comp}: {characters[comp][answer]}")

  if characters[user][answer] < characters[comp][answer]:
    print(comp, "wins")
  elif characters[user][answer] > characters[comp][answer]:
    print(user, "wins")
  else:
    print("Draw")

  time.sleep(2)
  os.system("clear")