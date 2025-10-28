# more advanced one and maybe more irritating too
import random
import string
length = int(input("ENTER THE PASSWORD LENGTH: "))
upper_case = int(input("THE NUMBER OF UPPER CASE LETTERS: "))
lower_case = int(input("THE NUMBER OF LOWER CASE LETTERS: "))
digits = int(input("NUMBER OF DIGITS YOU WOULD LIKE IN IT: "))

characters = string.ascii_letters + string.digits + string.punctuation

if upper_case >= 1:
    final = characters+str(upper_case)
if digits >= 1:
    final = characters+str(digits)
if lower_case >= 1:
    final = characters+str(lower_case)
error_shown = int(upper_case+lower_case+digits)
if error_shown >= length:
    print("EXCEEDED THE INITIAL LENGTH SET BY YOU!!")

password = ''.join(random.choice(final) for _ in range(length))
print(password)








#rthis is an actual working model unlike mine from chatgpt
import random
import string

length = int(input("ENTER THE PASSWORD LENGTH: "))
upper_case = int(input("THE NUMBER OF UPPER CASE LETTERS: "))
lower_case = int(input("THE NUMBER OF LOWER CASE LETTERS: "))
digits = int(input("NUMBER OF DIGITS YOU WOULD LIKE IN IT: "))

# Check if the total exceeds length
if upper_case + lower_case + digits > length:
    print("EXCEEDED THE INITIAL LENGTH SET BY YOU!!")
    exit()

password_list = []

# Add required uppercase letters
password_list.extend(random.choice(string.ascii_uppercase) for _ in range(upper_case))

# Add required lowercase letters
password_list.extend(random.choice(string.ascii_lowercase) for _ in range(lower_case))

# Add required digits
password_list.extend(random.choice(string.digits) for _ in range(digits))

# Fill the rest with random characters (can be any type)
remaining = length - len(password_list)
all_characters = string.ascii_letters + string.digits + string.punctuation
password_list.extend(random.choice(all_characters) for _ in range(remaining))

# Shuffle so the pattern isn't predictable
random.shuffle(password_list)

# Join into final string
password = ''.join(password_list)
print(password)

