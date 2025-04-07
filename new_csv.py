import random

def createFile():
    with open("db.csv", "w") as file:
        for i in range(200):
            number = random.randint(1, 5050)
            if number < 500:
                file.write("aaa\n")
            else:
                file.write(str(number) + "\n")

        file.close()

def readFile():
    file = open("db.csv", "r")
    print(file.readlines()[0][:-1])


createFile()