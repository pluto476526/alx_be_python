# Read a sepcified file

def readFile(filename) :
    try :
        with open(filename, 'r') as file :
            content = file.read()
            print("\nFile Content:\n")
            print(content)

    except FileNotFoundError :
        print(f"{filename} " , "- No such file!")

if __name__ == "__main__" :
    filename = input("Enter filename... ")
    readFile(filename)
