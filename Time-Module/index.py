import time

# def usingWhile():
#     i = 0
#     while i<5000:
#         i = i+1
#         print(i)
# def usingFor():
#     i = 0
#     for i in range(5000):
#         print(i)


# init = time.time()
# usingWhile()
# t1 = time.time()-init
# init = time.time()
# usingFor()
# print(time.time() - init)
# print(t1)

# print(3)
# time.sleep(3)
# print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time)