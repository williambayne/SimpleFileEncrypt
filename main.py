print("Welcome to your Encryption Program.")
def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    #file = open("Encrypt_" + filename, "wb") #Will create a copy of the original that is encrypted.
    file = open(filename, "wb") #Will overwrite original file with encryted version.
    file.write(data)
    file.close()
    print("***File Successfully Encrypted.***")
    print("")

def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()

choice = " "
while choice != "3":
    print("Please select your option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("Enter a key as int:\n"))
        filename = input("Enter filename with extension:\n")
    if choice == "1":
        Encrypt(filename, key)
    if choice =="2":
            Decrypt(filename, key)
