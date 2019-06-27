dash = '_ '*3
print (dash)

secretword= ['r', 'e', 'd']
print (secretword[0])

guess= input('guess a letter: ')

for i in range(len(secretword)):
    if secretword[i]== guess:
        newdash()
        print ('you guessed correctly!')

#define newdash(dash, )