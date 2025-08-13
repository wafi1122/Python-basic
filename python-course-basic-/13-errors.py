# try:
#     print("opned")

#     a = int(input('~'))
# except ValueError as error:
#     print("Invalid user input")
# except TypeError:
#     print("type error")
# except KeyboardInterrupt:
#     print("keyboard interrupt")
# finally:
#     print('closed')

try:
    a = int(input("one : " ))
    b = int(input("two: "))
    print(a/b)
except ValueError:
    print('invalid error')
except ZeroDivisionError:
    print('nothing be divided by 0 ')
