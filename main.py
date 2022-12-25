from getpass import getpass as input

print("Rock, Paper, Scissors")
print("---------------------")
print()
print("Player One")
p1Choice = input("Press R for Rock, P for Paper and S for Scissors: ").upper()
print()
print("Player Two")
p2Choice = input("Press R for Rock, P for Paper and S for Scissors: ").upper()
print()
# Testing purposes = print(p1Choice) print(p2Choice)
print("---------------------")

# Rock
if p1Choice == "R" and p2Choice == "R":
  print("Player One's Rock collied with Player Two's Rock! That was one rocky experience!")
elif p1Choice == "R" and p2Choice == "P":
  print("Player One's Rock has been wrapped by Player Two's Paper! Player One just witnessed Origami!")
elif p1Choice == "R" and p2Choice == "S":
  print("Player One's Rock just obliterated Player Two's Scissors. Those scissors wont be cutting anymore!")
  
# Paper
if p1Choice == "P" and p2Choice == "R":
  print("Player Two's Rock has been wrapped by Player One's Paper! Player Two just witnessed Origami!")
elif p1Choice == "P" and p2Choice == "P":
  print("Player One's Paper has slapped into Player Two's Paper! No paper cuts were seen!")
elif p1Choice == "P" and p2Choice == "S":
  print("Player Two's Scissors cut up Player One's Paper! Player One's Paper is shredded!")

# Scissors
if p1Choice == "S" and p2Choice == "R":
  print("Player Two's Rock just obliterated Player One's Scissors. Those scissors wont be cutting anymore!")
elif p1Choice == "S" and p2Choice == "P":
  print("Player One's Scissors cut up Player Two's Paper! Player Two's Paper is shredded!")
elif p1Choice == "S" and p2Choice == "S":
  print("Player One's Scissors clashed with Player Two's Scissors. That's cutting edge experience!")

# If an incorrect input was typed.
else: 
  print("Error, please type the required letters, R, P or S.")
