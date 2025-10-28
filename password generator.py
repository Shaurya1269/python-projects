#password generator
import random     #brings randomness in a code
import string     #involves strings 
length = int(input("ENTER THE PASSWORD LENGTH: "))
# ascii for alphabets,punctuations involves all symbols and special characters
characters = string.ascii_letters + string.digits + string.punctuation
password =''.join(random.choice(characters) for _ in range(length))     #use the iterations just like this,spaces characters and all 
print(password)


6

#more advanced one
import random
import string
length = int(input("ENTER THE PASSWORD LENGTH: "))
upper_case= int(input("THE NUMBER OF UPPER CASE LETTERS: "))
digits = int(input("NUMBER OF DIGITS YOU WOULD LIKE IN IT: "))
character= string.ascii_letters + string.digits + string.punctuation

if upper_case >= 1:
    final= character+upper_case
if digits >= 1:
    final=character+digits
password= ''.join(random.choice(final) for _ in range(length))
print(password)
    
