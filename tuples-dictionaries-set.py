#Tuples
#Tuples
coordinates =(1,2)
print (coordinates)
print (coordinates[0])

#dictionaries 
profile ={
"name":"henok",
"gender":"male",
"maritual_status":"married",
}

print(f"your name is with out get function {profile ["name"] } ")
print(f"your name is with get function  {profile.get("name")} ")

print(f"your name is with get function  {profile.get("age" , "not specified ")} ")

profile["age"]="31"
print(f"your are {profile.get("age")} years old")

del profile["age"]  #delete age from dictionary 
#print(profile["age"])


#set  
tool ={"multimeter", "hammer", "osilloscope"}
pdf={"efi", "hvac","abs", "hammer"}

print(tool.union(pdf) )
print(tool.intersection(pdf))
print(tool.difference(pdf))
