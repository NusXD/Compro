def main():
    infile = open("nut.txt", "r")
    file_conntent = infile.read()
    infile.close()

    print(file_conntent)

if __name__ == "__main__":
    main()