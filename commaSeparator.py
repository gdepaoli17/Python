import readline


filepath = "C:\\users\\gino.depaoli\\desktop\\test.txt"

with open(filepath, 'r') as fp:
    
    values = fp.readlines()
    
    values.replace(" ", ",")
    print(values)
