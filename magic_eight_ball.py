my_file=open("response.txt")
responses=my_file.readlines()
my_file.close()
import random
question=raw_input("Do you have a question for me? ").lower()



def response():
	while (question=="yes"):
		raw_input("What is your question? ")
		print "       /\\"
		print "      /  \\"
		print "     /    \\"
		print "    /      \\"
		print random.choice(responses)
		print " /            \\"
		print "/              \\"
		print " ---------------"
		question1=raw_input("Do you have another question? ").lower()
		if (question1=="no"):
			print "Goodbye"
			exit()
		elif (question1=="yes"):
			response()
		else:
			print "Goodbye"
			exit()

response()