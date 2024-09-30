# Writing to the file
with open('D:/Python online class/example.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a sample text file.\n')

# Reading from the file
with open('D:/Python online class/example.txt', 'r') as file:
    content = file.read()

content
