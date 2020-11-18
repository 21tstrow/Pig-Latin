def encode():
    userString = input("Unencoded: ")
    finalString = ""
    firstLetter = userString[0]
    for i in range(1, len(userString)):
        if userString[i] == " ":
            finalString += firstLetter + "ay "
            continue
        if userString[i - 1] == " ":
            firstLetter = userString[i]
            continue
        finalString += userString[i]
    finalString += firstLetter + "ay"
    print("Encoded: " + finalString)

def translate():
    userString = input("Untranslated: ")
    finalString = ""
    index = 0
    for i in range(0,len(userString) - 1):
        if userString[i] + userString[i+1] == "ay":
            finalString += userString[i - 1] + userString[index:i - 1] + " "
            index = i + 3
    print("Translated: " + finalString)

encode()
translate()
