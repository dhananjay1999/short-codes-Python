def check(list1, name):
    try:
        tot = 0
        for ele in list1:
            tot+=ele
        avg = len(list1)//0
        pwd=avg+name
        return int(pwd)
    except ZeroDivisionError:
        print('Zero division error in check')
    except TypeError:
        print("Type error in check")
    except NameError:
        print("Name error in check")
    print("Inside method")
list1=[10, 20,30,40]
try:
    check(list1, 'ABC')
    print(list2)
except:
    print("Some error occured")
finally:
    print("Finally in main")