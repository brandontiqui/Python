jamcoins = []

def isComposite (number):
    status = False
    for i in range(2, number):
        if number % i == 0:
            status = True
            break

    return status #return i?

def convertFromBinaryToBase(number, base):
    sum = 0 
    digits = list(str(number))
    for i in range (0,len(digits)):
        digit = int(digits.pop(0))
        if digit > 0:
            sum += base ** len(digits)
            
    return sum

# needed only for incrementing binary by 1
def convertBase10ToBinary(number):    
    quotient = number
    digits = []
    while quotient > 0:
        remainder = quotient % 2
        quotient = int(quotient / 2)
        digits.append(remainder)
    digits.reverse()
    return int(''.join(map(str,digits)))

def getDivisor(number):
    for i in range(2, number):
        if number % i == 0:
            return i




def getComposites():
    outfile = open("output.txt", "w")
    counter = 1
    global jamcoins
    #number = 1000000000000001 # first possible jamcoin of length N = 16
    number = 1000000000001110
    while len(jamcoins) < 51: # J = 50
        status = True
        for base in range(2, 11): 
            if not isComposite(convertFromBinaryToBase(number, base)):
                status = False
                break

        if status == True:
            lastdigit = list(str(number)).pop()
            if lastdigit != '0':
                jamcoins.append(number)
                #outfile.write(str(number) + '\n')
                print(jamcoins)
                print("length" + str(len(jamcoins)))
        
        number = convertBase10ToBinary(convertFromBinaryToBase(number, 2) + 1)
        counter += 1
        print(counter)

    outfile.close()



