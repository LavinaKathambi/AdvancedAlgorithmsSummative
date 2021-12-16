# PYTHON CODE FOR ENCRYPTION IMPLEMENTATION
# Assign original text to a variable
encryptionText = 'Plain Text'
# Define key value
keyValue = 3 
# Function to take the encryptionText and keyValue
def encryption(encryptionText,keyValue):
    # Variable to store encrpyted message
    encryptedMessage = ""
    # Variable to define starting point of encryption
    startingPoint = 0
    # Looping through the keyValue via the encryption text 
    while startingPoint < keyValue:
        for i in range(startingPoint,len(encryptionText),keyValue):
            # Adding characters from the keyValue
            encryptedMessage += encryptionText[i]
            #Incrementing the starting point variable and returning the answer gotten from the encryption
        startingPoint += 1
    return encryptedMessage
encryptedText = encryption(encryptionText,keyValue)
# Decryption Function 
def decryption(encryptedText,keyValue):
    currentPoint = 0
    decryptedMessage = ''
    #Checking if length of the encryption text and key value is even 
    if len(encryptedText) % 2 == 0 and keyValue % 2 == 0: 
        # Determining next point 
        nextPoint = len(encryptedText)//keyValue 
        while currentPoint < nextPoint:
            # Looping through the length of message
            for i in range(currentPoint,len(encryptedText),nextPoint):
                # Adding characters to the decrypted Message variable
                decryptedMessage += encryptedText[i]
            # Incrementing currentPoint in every step
            currentPoint+=1  
    # Checking if length of the encryptedText is even and keyValue is odd   
    if len(encryptedText) % 2 == 0 and keyValue % 2 != 0:
        # Defining next point
        nextPoint = len(encryptedText)//keyValue 
        # Checking if current Point is lesser than the next point
        while currentPoint < nextPoint:
            nextPoint += 1
            # Adding characters to the decrypted Message
            decryptedMessage += encryptedText[currentPoint] 
            # Looping through the length of the message 
            for i in range(currentPoint,len(encryptedText)):
                # Getting the next index to add to the decrypted Message
                j = i + nextPoint
                decryptedMessage += encryptedText[j]
                # Getting the next index to add to the decrypted Message
                decryptedMessage += encryptedText[j+keyValue]
                break
            # Reseting the nextPoint
            nextPoint = len(encryptedText)//keyValue 
            # Incrementing currentPoint to start at the next index 
            currentPoint+=1 
        # Adding the last character of nextPoint to the answer
        decryptedMessage+= encryptedText[nextPoint]
    return decryptedMessage

decryptedText = decryption(encryptedText,keyValue)

print("Plain Text: " + encryptionText)
print("Encrypted Text: "+ encryptedText)
print("Decrypted Text: "+ decryptedText)