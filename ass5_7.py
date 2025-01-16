def isPresent(dict1,key):
    l1=list(dict1.values())
    if(key in l1):
        return True
    else:return False
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(("Item Not Found", "Item Found")[isPresent(sampleDict,200)])