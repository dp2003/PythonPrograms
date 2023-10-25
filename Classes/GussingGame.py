class Error(Exception):
	pass

class ValueTooSmallError(Error):
	pass

class ValueTooLargeError(Error):
	pass

number=10
while True:

	try:
		num = int(input("Enter a number:"))
		if num<number:
			raise ValueTooSmallError
		elif num>number:
			raise ValueTooLargeError
		break

	except ValueTooSmallError:
		print("This value is too small, try again!")

	except ValueTooLargeError:
		print("This value is too lerge, try again!")

print("Congratulations! You guessed it right!!!!!!!!!")
