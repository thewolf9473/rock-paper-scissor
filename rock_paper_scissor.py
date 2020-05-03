#1=rock
#3=paper
#2=scissor
import random 
def gamer():
	game=input("enter the choices : rock,paper or scissor:")
	
	a=random.randint(1,3)
	if game =='rock':
		if a==1:
			print('tie')
		elif a==2:
			print('it was scissor,you lost')
		else:
			print('it was paper,you won')
	elif game=='scissors':
		if a==1:
			print('rock,you lost')
		elif a==2:
			print('tie')
		else :
			print('paper,you won')
	else:
		if a==1:
			print('rock,you won')
		elif a==2:
			print('scissors,you lost')
		else:
			print('you won')
	w=input('wanna play again?:y/n')
	
	if  w=='y':
		gamer()
	elif w=='n'
		print("Thank You For playing!")
	else:
		print("Error!")
gamer()

