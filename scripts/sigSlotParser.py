with open(r"C:\Users\smtau\Desktop\PBApro\scripts\data.txt", "r") as dataFile:
    data = dataFile.readlines()


methods = []
calls = []
template = """        def _{&}(self, *args, **kwargs):
            '''{&&}'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#"""


template2 = "                self.{&} = self._{&&}\n"

for line in data:
    if line != "":
        if " (" in line:
            methodName = line.split(" (")[0]
            methods.append("""        def _{&}(self, *args, **kwargs):\n""".replace("{&}", methodName))
            try:
                if not " (" in data[data.index(line) + 1]:
                    calls.append(template2.replace("{&}", methodName).replace("{&&}", methodName))
                else:
                     calls.append(template2.replace("{&}", methodName).replace("{&&}", "blankSignalSlot"))
            except IndexError:
                calls.append(template2.replace("{&}", methodName).replace("{&&}", "blankSignalSlot"))


        else:
            methods.append("""            '''{&&}'''\n""".replace("{&&}", line.replace("\n", "")))
            methods.append("""\n""")
            methods.append("""            pass\n""")
            methods.append("""            #----------------------------------------------------------------------------------------------------------------------------------------#\n""")
            methods.append("\n")
            methods.append("\n")

calls.append("\n")
calls.append("\n")
calls.append("\n")
newData = calls + methods

with open(r"C:\Users\smtau\Desktop\PBApro\scripts\output.txt", "w") as dataFile:
    dataFile.writelines(newData)