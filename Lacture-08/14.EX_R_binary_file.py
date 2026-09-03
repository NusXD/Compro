import struct as st 

with open("records.bin", "rb") as file:
    data = file.read(st.calcsize('i20sif'))
    id_num, name, age, gpa = st.unpack('i20sif', data)
    name = name.decode().strip("\x00")
    print(f"ID: {id_num}, Name: {name}, Age: {age}, GPA: {gpa}")
