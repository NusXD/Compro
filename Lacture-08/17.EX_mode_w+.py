def ex_w_plus_mode():
    with open("nutW+.txt", "w+") as infile:
        infile.write("This is a new line in write mode.\n")
        infile.write("Another line in write mode.\n")
        infile.seek(0)
        content = infile.read()
        print(f"Current content:\n{content}")

if __name__ == "__main__":
    ex_w_plus_mode()