def Solution(string):
    all_string = {}
    for i in string:
        if i in all_string:
            all_string[i] += 1
        else:
            all_string[i] = 1
    res = max(all_string, key=all_string.get)
    return (str(res))


print(Solution("HelloWorld"))
    
