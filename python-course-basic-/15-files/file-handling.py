# with open('15-files\data.txt', 'r') as file:
#     data = file.readline(5) # read read the whole data file
#     print(data)

# userInput = input('Enter your message that you wish to save :')

# with open('15-files\data.txt', 'a') as file:# the method "w" will change the file means update the whole thing but when we write a "a insted of we will add text without update whole"
#     file.write(userInput + '\n')



# how we can make our file privite which anyonne cannot see usinf a binary files
import pickle
phonebook = {
    'a' : '1',
    'b' : '2',
    'c' : '3'
}

with open('15-files\phonbook.dat' , 'wb') as bin:
    pickle.dump(phonebook, bin)

