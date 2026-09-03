def ex_mode_plus():
    with open("nut+.txt", "a+") as infile:
        infile.seek(0)
        content = infile.read()
        print(f"Current content:\n{content}")
        infile.write("New line added in append mode.\n")
        infile.seek(0)
        updated_content = infile.read()
        print(f"Updated content:\n{updated_content}")

if __name__ == "__main__":
    ex_mode_plus()
