import random
def lambdaa():
    try:
        size = int(input("size - "))
        begin = int(input("begin - "))
        end = int(input("finish - "))
        list = []
        list1 = []
        for i in range(size):
            list.append(random.randint(begin, end))
        list.sort()
        for item in list:
            print(item, end=" ")
        print()
        for item in list:
            for j in range(1, i -1):
                if item // j:
                    list1.append(item)
        data = {1: lambda lst: max(lst), 2: lambda lst: min(lst), 3: lambda lst: list[::-1], 4: lambda sie: all(size % i != 0 for i in range(2, int(size ** .5) + 1))}
        print(f"max = {data[1](list)}, min = {data[2](list)}")
        print(data[3](list))
        print()
        print(f"easy num = {data[4](list)}")
    except Exception as ex:
        print(f"Error: {ex}")


lambdaa()