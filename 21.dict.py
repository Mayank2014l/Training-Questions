d1 = dict()
print(type(d1))

d = {
    "id":1,
    "name":"Mayank",
    "course":"Btech",
    "age":20,
    "city":"Gurgaon"
}  
print(d)

keys = [1,2,3,4,5]
values = ["pitter","david","warner","parker"]
dic = dict(zip(keys,values))
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

k = ["id","name","post","salary"]
v = [101,"Mayank","developer",40000]
d2 = dict(zip(k,v))
print(d2)
print(d2["name"])
print(d2.get("salary"))

d3 = {
    "id":11,
    "name":"Mayank",
}
print(d3)
d3["course"]="java"
print(d3)
d3["course"] = "python"
print(d3)
d3.pop("id")
print(d3)