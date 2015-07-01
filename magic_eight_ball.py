# prompt user to ask question

#randomly answer question from response file
# ask user if they have another question or if they would like to exit

# return random answer to user
my_file=open("response.txt")
responses=my_file.readlines()
my_file.close()
import random
question=raw_input("Do you have a question for me? ")

def response():
	while (question=="yes" or question=="Yes"):
		raw_input("What is your question? ")
		print random.choice(responses)
		question1=raw_input("Do you have another question? ")
		if (question1=="no" or question1=="No"):
			print "Goodbye"
			exit()
		elif (question1=="yes" or question1=="Yes"):
			response()
		else:
			print "Goodbye"
			exit()

response()

# need to figure out how to exit program with out asking "What is your question?" after printing "Goodbye"
# and how to print response without / after answer


