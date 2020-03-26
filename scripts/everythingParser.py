with open(r"C:\Users\smtau\Desktop\PBApro\scripts\data.txt", "r") as dataFile:
    data = dataFile.readlines()

properties = []
signals = []
slots = []

mode = None

for line in data:

    index = data.index(line)
    line = line.replace("\n", "") # Strip out all new lines.

    # Detect which part of the help text we are looking at.
    if line == "Properties" or line == "Signals" or line == "Slots":
        mode = line
        continue

    # ------------ PROPERTIES LIST
    if mode == "Properties":
        if line != "" and " " not in line and "." not in line and line != "bool" and line != "int" and line != "QSize" and line != "Qt::LayoutDirection" and \
           line != "QString" and line != "QIcon":

           properties.append(line)

    # ------------ SIGNALS LIST
    elif mode == "Signals":
        prevLine = data[index - 1].replace("\n", "")
        if preLine == "void\n":
            signals.append(line.replace(" ", ""))

    # ------------ SLOTS LIST
    elif mode == "Slots":
        prevLine = data[index - 1].replace("\n", "")
        if line != "" and "." not in line and line != "QObjectList"  and line != "void" and line != "PPComponent *" \
            and line != "QStringLIst" and line != "QString" and line != "bool" and line != "int":

            slots.append(line.replace(" ", ""))


print properties
print  "\n"
print signals
print  "\n"
print slots
print  "\n"
