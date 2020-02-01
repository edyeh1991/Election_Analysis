names = ["eD", "KiM", "aLe", "ElAiNe"]
print (names)

lowernames = [name.lower()for name in names]
print (lowernames)

titlename = [name[0].upper()+name[1:] for name in lowernames]
print (titlename)


