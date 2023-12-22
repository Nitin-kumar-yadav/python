# f = open('myfile.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()


# f = open('myfile.txt', 'w')
# f.write("Hello, world!")

# f.close()
# print(f)

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of students {i} in mathis is: {m1}")
    print(f"Marks of students {i} in mathis is: {m2}")
    print(f"Marks of students {i} in mathis is: {m3}")

    print(type(line))
    print(line)