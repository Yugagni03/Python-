a={"key": "value",
   "harry": "the coder",
   "marks": "100",
   "lists": [100,90,99,89]}

print(a["harry"])

print(a["lists"])

print(a.items())

print(a.values())

updatedict={
    "bff":"Subhajit"
}
a.update(updatedict)
print(a)

print(a.get("bff"))