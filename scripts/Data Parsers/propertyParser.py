props = ['objectName', 'IrigTime', 'IrigTimeStatus', 'BCStatus', 'RTStatus', 'BMStatus', 'RPLStatus']


template  = """                self.{&} = {&&}\n"""

newData = []

for item in props:
    newData.append(template.replace("{&}", item).replace("{&&}", "None"))


with open(r"C:\Users\smtau\Desktop\PBApro\scripts\output.txt", "w") as dataFile:
    dataFile.writelines(newData)