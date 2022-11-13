"""
This is a password validation and security program.
It stores a password in a global variable and
counts down to zero when the user enters the wrong password.
"""
attempts = 0 # count begins at zero
password = 'learningPython12345' # a given password

while attempts < 5: # while loop accepts up to 5 attempts
    print('Please Enter Your Password:')
    inp = input() # variable that reads user input
    if inp == password:
        print('Access Granted.') # condition printed when password is correct
        break # exit program
    elif (attempts+1)==5: # elif loop counts wrong attempts to 5
        print('You ran out of attempts.') # condition printed when all attempts failed
        break # exit program
    else:
        attempts+=1 # specifies outputs for each wrong attempt before limit is reached
        print('Access Denied') # condition printed when password is incorrect
        print('You have', 5-attempts, 'attempts left.') # informs user how many attempts left
        continue # proceed to the next attempt