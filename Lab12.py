print ("Michael Mordec, 7/19/22, Lab 12, CSC 242:")
from random import sample
# the set definitions

# the list of team members
team = ["Daisy", "Edward", "Kay", "Mirna", "Sidney", "Tina", "Zachary"]
print (team)
# define the member's qualifications 
member1 = set(["D", "M", "T", "U"])
print (team[0], "\t", member1)
member2 = set(["D", "E", "M", "R", "V"])
print (team[1], "\t", member2)
member3 = set(["E" , "M" , "S" , "V" , "U"])
print (team[2], "\t", member3)
member4 = set(["A" , "E", "O" , "P" , "S"])
print (team[3], "\t", member4)
member5 = set(["Q" , "R" , "V"])
print (team[4], "\t", member5)
member6 = set(["A" , "M" , "O" , "P" , "S"])
print (team[5], "\t", member6)
member7 = set(["P" , "Q" , "O" , "T" , "U"])
print (team[6], "", member7)
memberlist=[member1, member2, member3, member4, member5, member6, member7]

print('1) Set Intersection')
setIntersect1 = member1.intersection(member2)
setIntersect1 = sorted(setIntersect1)
print ("set operation:", team[0], "intersect", team[1], setIntersect1)
print ("\n")

print ("2) An Empty Set")
setIntersect2 = member4.intersection(member5)
setIntersect2 = sorted(setIntersect2)

print ("set operation:", team[3], "intersect", team[4], setIntersect2)

print('3) Set Union')
setUnion1 = member1.union(member2)
setUnion1 = sorted(setUnion1)
print ("\n")
print ("set operation:", team[0], "union", team[1], setUnion1)

print('4) Single Attribue Subset')
listD = []
index = 0
for member in memberlist:
    if ("D" in member):
        listD.append(team[index])
    index = index + 1

sorted(listD)
print(listD)
commonSet_D = set([])
commonSet_D.update(listD)
sorted(commonSet_D)
print (commonSet_D)

print('5) Set Complement')
uset = member1.union(member2).union(member3).union(member4).union(member5).union(member6).union(member7)
print(uset)
programming = {'P','R'}
pureManagement = uset - programming;
print(pureManagement)

print('6) set difference')
uset = member1.union(member2).union(member3).union(member4).union(member5).union(member6).union(member7)
print(uset)
rsample1 = sample(team,5)
rsample2 = sample(team,5)
result = set(rsample1) - set(rsample2)
print(result)
