def index(list):
    try:
        listindex=list[6]
        return listindex
    except IndexError:
        print("Please access the available one!!")
result=index([1,2,3,4,5])
print(f"After indexing is {result}")