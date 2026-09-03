import struct as st 

recorde_size = st.calcsize('i20sif')
record_format = 'i20sif'

with open("records.bin", "rb") as file:
    file.seek(recorde_size)
    data = file.read(recorde_size)
    id_num, name, age, gpa = st.unpack(record_format, data)
    name = name.decode().strip("\x00")
    print(f"ID: {id_num}, Name: {name}, Age: {age}, GPA: {gpa}")
