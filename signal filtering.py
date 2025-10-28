signal = input("enter the signal sent seperated by comma IN CAPITAL LETTERS: ")

print(signal)
signal = signal.split(",")
useful_signal = []
for object in signal:
    if object != 'N':
        useful_signal.append(object)
print(useful_signal)

# think of it as a code where you are a NASA scientist and you have to filter out a signal from the noise in order to get useful results.
# This code filters out noise ('N') from a signal input by the user.
# line 1 takes input from the user ..line 4 converts users string data type input into a list,line 5 creates an empty list, line 6 checks if the object is not equal to 'N', if true it appends the object to the useful_signal list, line 8 prints the useful_signal list.
