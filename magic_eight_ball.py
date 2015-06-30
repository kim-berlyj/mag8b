# prompt user to ask question

#randomly answer question from response file
# ask user if they have another question or if they would like to exit

# return random answer to user
my_file=open("response.rtf")
responses=my_file.readlines()
my_file.close()
# responses2=responses.strip("\n")
import random
question=raw_input("Do you have a question for me? ")

def response():
	while (question=="yes"):
		raw_input("What is your question? ")
		print random.choice(responses)
		if (raw_input("Do you have another question? ")=="no"):
			print "Goodbye"
			return
		else:
			response()

response()

# need to figure out how to exit program with out asking "What is your question?" after printing "Goodbye"
# and how to print response without / after answer


