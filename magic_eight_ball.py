# prompt user to ask question

#randomly answer question from response file
# ask user if they have another question or if they would like to exit

# return random answer to user
my_file=open("response.rtf")
responses=my_file.readlines()
my_file.close()
# responses2=responses.strip()

import random 

question1=raw_input("Would you like to play? ")

def response(question):
	while(True):
		question2=raw_input("What is your question? ")
		print random.choice(responses)
		if (raw_input("Do you have another question? ")=="yes"):
			response(question)
		else:
			print "Goodbye"

response(question1)

# need to figure out how to exit program with out asking "What is your question?" after printing "Goodbye"


