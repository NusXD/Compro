import struct as st

with open("records.bin", "rb") as file:

    record_size = st.calcsize('i20sif')
    file_size = file.seek(0, 2)
    file.seek(0)

    for _ in range(file_size // record_size):
        data = file.read(record_size)

        id_num, name, age, gpa = st.unpack('i20sif', data)

        name = name.decode().strip("\x00")

        print(f"ID: {id_num}, Name: {name}, Age: {age}, GPA: {gpa}")