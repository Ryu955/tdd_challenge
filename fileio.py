with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == "": break
        print(str(line).strip())
