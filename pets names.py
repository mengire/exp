petNames = []
while True:
    print('Enter the name of pet ' + str(len(petNames)+ 1) + ' (Or enter nothing to stop.):' )
    name = input()
    if name == '':
        break
    petNames = petNames + [name]
print('The pet Names are:')
for i in petNames:
    print(i, end=', ')