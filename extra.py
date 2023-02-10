# import logging

# logging.warning("be careful")


# from multiprocessing import Pool

# def f(x):
#     return x * x

# with Pool(3) as p:
#     print(p.map(f, [2, 4, 5, 7]))

# import multiprocessing

# print(multiprocessing.cpu_count())

# from multiprocessing import Process, current_process

# def testing():
#     print("Works")

# def square(n):
#     print("The number squares to ", n**2)

# def cube(n):
#     print("The number cubes to ", n**3)
#     print(current_process().name)

# if __name__ == "__main__":
#     p1 = Process(target=square, args=(7,))
#     p2 = Process(target=cube, args=(7,))
#     p3 = Process(target=testing)
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print("We're done")

# print('_________')
# import os

# def child1():
#     print(current_process().name)

# def child2():
#     print(current_process().name)

# if __name__ == "__main__":
#     print("Parent ID", os.getpid())
#     p1 = Process(target=child1, name="Child 1")
#     p2 = Process(target = child2)
#     p1.start()
#     p2.start()
#     p2.join()
#     p1.join()
#     print("Done, bye!")


# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)


# def validate_password(password):
#     if len(password) < 8:
#         raise ValueError("Password characters less than 8")
#     return password


# try:
#     user_password = input('Enter a password: ')
#     validate_password(user_password)
# except ValueError:
#     print('Passwoard should have more characters')

# try:
#     with open('robots.txt', 'r', encoding='UTF-8') as f:
#         first_line = f.readline()
#         print(first_line)
# except IOError: 
#     print('File not found!')
# else:
#     upper_case = first_line.upper()
#     print(upper_case.index('x'))
# finally:
#     print('The Python program ends here!')


print(2 + 'eee')