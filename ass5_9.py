sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys=list(sampleDict.keys())
values=list(sampleDict.values())
l1=[]
for i in values:
    if type(i)==int:
        l1.append(i)
maximum=max(l1)
k=0
for i in l1:
    k+=1
    if i==maximum:
        break
print("The max value is ",keys[k])