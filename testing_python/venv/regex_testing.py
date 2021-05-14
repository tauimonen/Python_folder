"""Playing with Python RegEx"""

import re

Nameage = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''
ages = re.findall(r'\d{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)
agedict = {}
x=0
for n in names:
    agedict[n] = ages[x]
    x+=1
print(agedict)

# ======================================================

print(80*"=")
if re.search("inform", "we need to inform himm with the latest information"):
    print("Founded!")

# ======================================================

print(80*"=")
allinform = re.findall("inform", "we need to inform himm with the latest information")
for i in allinform:
    print(i)

# ======================================================

print(80*"=")
str = "we need to inform himm with the latest information"
for i in re.finditer("inform", str):
    tup = i.span()
    print(tup)

# ======================================================

print(80*"=")
str = "St, hat, mat, pat"
all = re.findall("[shmp]at", str)
for i in all:
    print(i)

# ======================================================

print(80*"=")
str = "St, hat, mat, pat"
some = re.findall("[h-m]at", str)
for i in some:
    print(i)

# ======================================================

print(80*"=")
str = "St, hat, mat, pat"
some = re.findall("[^h-m]at", str)  # ^ means not
for i in some:
    print(i)

# ======================================================

print(80*"=")
food = "hat rat mat pat"
regex = re.compile("[r][a]t")
food = regex.sub("food", food)
print(food)

# ======================================================

print(80*"=")
str = "here is \\drogba"
print(re.search(r"\\drogba", str))

# ======================================================

print(80*"=")
str = """Keep the blue flag 
flying high 
Chelsea"""
print(str)
regex = re.compile("\n")
str = regex.sub("", str)
print(str)

# ======================================================

print(80*"=")
str = "12345"
print("Matches:", len(re.findall("\d", str)))

# ======================================================

print(80*"=")
num = "123 1234 12345 123456 1234567"
print("Matches:", len(re.findall("\d{5,7}", num)))

# ======================================================

print(80*"=")