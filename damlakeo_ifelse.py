from random import randint

print("[Rock] [Paper] [Scissor]")
print("---------------------")
print(" ")

while True:
	player = input("You Select: ")
	if player == "Dam" or player == "La" or player == "Keo":
		break

computer = randint(0,3)

if computer == 0:
	computer = "Dam"
if computer == 1:
	computer = "La"
if computer == 2:
	computer = "Keo"

print("Computer select: " + computer)

if player == computer:
	print("Hoa")

elif player == "Dam":
	if computer == "La":
		print("Thua")
	else:
		print("Thang")

elif player == "La":
	if computer == "Dam":
		print("Thang")
	else:
		print("Thua")

else:
	if computer == "Dam":
		print("Thua")
	else:
		print("Thang")

