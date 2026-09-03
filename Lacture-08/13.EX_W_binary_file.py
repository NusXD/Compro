import struct as st

num_records = int(input("Enter number of records: "))
with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id_num = int(input("Enter ID number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))

        data = st.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)

print("Records written to file.")