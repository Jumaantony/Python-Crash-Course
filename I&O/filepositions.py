data = open("juma.txt", "r+")
file_data = data.read(18)  # read 18 bytes only
print("current position after reading 18 bytes is: ", data.tell(), "\n")
data.seek(0)  # here the current position is set to zero
full_data = data.read()  # read all bytes
print(file_data, "\n")
print(full_data, "\n")
print("position after reading file:", data.tell())
