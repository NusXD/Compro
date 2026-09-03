with open("nut.txt", "r") as infile:
    lines = infile.readlines() #.readline and .readlines() are different, .readline() reads one line at a time, while .readlines() reads all lines and returns a list of lines. 
    for line in lines:
        print(line.strip())