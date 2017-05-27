import smtplib
import getpass

#We can use this service if and only if less security apps are allowed in user's security settings 
print("Check Whether Less security apps are allowed for user Gmail account. If not, then allow less security apps") 


#getting user mail-id and password
#password is taken using getpass for security purpose so that it will not visible on command line 
gmail_user = input("Enter Your Gmail: ")
gmail_pwd = getpass.getpass()

#getting subject input from sender
subject = input("Enter Subject: ")

#getting message input from user either entering directly on command line or as file input
choice = int(input("**Message** -> choose one Method:\n\t1.) Enter Here\n\t2.) Give File input\n"));
if(choice == 1):
	TEXT = input("Enter Message: ")
else:
	file_name = input("Enter filename: ");
	fo = open(file_name, "r+");
	data = fo.read();
	TEXT = data.strip() 

#Getting receiver's mail-id, either single receiver or multiple
receiver = []
option = 'Y'
choice = input("Do You want to give list of receiver's as file input ( Y / N ):")

if(choice == "y" or choice == "Y"):
	#Taking mailing list from file name provided as input
	file_name = input("Enter filename: ")
	fo = open(file_name, "r+")
	data = fo.read().split()
	for mail in data:
		receiver.append(mail)
else:
	#Getting the mail adresses entered from user one by one
	while option == "Y" or option == "y":
		receiver.append(input("Enter receiver's email: "))
		option = input("Do you want to add more receiver's ( Y / N ): ")


#Finally sending the mails to respective mail id's
for ADDR in receiver: 
	message = "\r\n".join(["From:"+gmail_user, "To:"+ADDR, "Subject:"+subject,"", TEXT])

	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(gmail_user,receiver,message)
	except:
		print("Mail cannot be send due to one of the following reason:")
		print("\t1.User password is wrong")
		print("\t2.Less secured apps are not allowed from google security. Allow less security apps in google security");
		print("\t3.Check Network");
		print("\n Try Again");
