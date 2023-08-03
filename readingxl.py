
filepath = 'C:\\Users\\gino.depaoli\\Desktop\\assets.txt'

with open(filepath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line.split()
        print(line)
        
    