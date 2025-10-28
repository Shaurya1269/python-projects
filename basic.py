n = 5
#i controls the rows and j controls the number of stars in the row
for i in range(1, n+1):
    for j in range(i):
        print("*",end="")     #print star without new line
    print()                   #move to next line after each row
