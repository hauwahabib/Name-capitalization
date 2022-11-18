listName=[]
def printList():
  print()
  for i in listName:
    print(i)
print()
while True:
  namefirst = input("First name? ").strip().capitalize()
  namelast = input("Last Name? ").strip().capitalize()
  name = f"{namefirst} {namelast}"
  if name not in listName:
    listName.append(name)
  else:
    print("Error: Duplicate name")
  printList()  