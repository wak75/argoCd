import os



file = os.listdir("./")
print(file)


fileExists = False
if os.path.exists("./all/yaml"):
    fileExists = True
else:
    fileExists = False

print(fileExists)

print("Checking if the file exists")
if os.path.exists("TheKingSlayer"):
    print("Removing already existing file")
    os.removedirs("TheKingSlayer")
else:
    print("the file does not exist already")

print("==========================================")
print("Creating new directories names as TheKingSlayer")
print(os.makedirs("TheKingSlayer"))

print("==========================================")

print("Printing the list of the files")
print(os.listdir())

print("==========================================")

print("deleting the file")
print(os.removedirs("TheKingSlayer"))

print("==========================================")

print("Printing the list of the files")
print(os.listdir())