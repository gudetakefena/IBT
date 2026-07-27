# 4 different for loop syntax
for i in range(3):
	print(i)
print("____________")	
for i in range(0,10,2):
	print(i)
print("____________")
fruits =["banan","apple","orange"]
for fruit in fruits:
	print(fruit)
print("____________")
for index , fruit in enumerate (fruits):
	print(f"index:{index} fruits {fruit}")
print("____________")	
	
#  while loop syntax 
count =0
while count<5:
	print(f"current count is {count}")
	count +=1	
print("____________")	

#loop real world example
user_input ="start"
while user_input.lower() != "quit":
	user_input =input("enter quit to exit")
	print ("try again")
print ("you are out of the system")
print("____________")	

num=int (input("enter your guess to"))
while num != 7:
	if num < 7:
		print ("try higher")
	else:
		print("try lower")
	num =int(input("enter quit to exit"))
print ("your guess is correct ")
print("____________")	


#loop control  break, continue, pass
for i in range (5):
	if i==3:
		break
	print(i)
print("____________")	
init =0
while init<5:
	if init==2:
		continue
	print(init)
	init +=1
print("____________")	

for i in range(30):
	if i%3==0:
		print("fizz")
	elif i%5==0:
		print("buzz")
	elif i%3==0 and i%5==0:
		print("fizzbuzz")	
	else:
		print(i)