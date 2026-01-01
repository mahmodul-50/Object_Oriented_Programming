# Concepts
# File write ("w")
# File read ("r")
# Manual open & close

# write to a file
file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("Learning File Handling\n")
file.close()

# read from a file
file = open("data.txt", "r")
content = file.read()
file.close()

print(content)
