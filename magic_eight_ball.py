# prompt user to ask question

#randomly answer question from response file
# ask user if they have another question or if they would like to exit

# return random answer to user
my_file=open("response.rtf")
responses=my_file.readlines()
my_file.close()

import random 

def response(question):
	print question1=raw_input("Would you like to play?")
	if True:
		question2=raw_input("What is your question?")
		random.choice(responses)
		question3=raw_input("Do you have another question?")
	else:
		return "Goodbye"

