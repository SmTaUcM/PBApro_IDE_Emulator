"""#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        module1
# Purpose:
# Version:     v1.00
# Author:      Sgt. S. Macintosh - MSC System Engineers
#
# Created:     18/03/2020
# Copyright:   (c) Crown Copyright - MSC System Engineers 2020
# Licence:     MSC System Engineers
#-------------------------------------------------------------------------------------------------------------------------------------------------#"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
try:
    from PBApro import *
except ImportError:
    pass


# ----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
class Test(object):

    def __init__(self):

        self.string = "Stu"
        self.string
        self.assign = PbaProObject("AssignRoot")
        connect(self.assign, 'Activated(bool)', self, "func")
        connect(self.assign, 'Activated(bool)', self, "func")
        connect(self.assign, 'Activated(bool)', self, "func")

    def func(self, sender, value):

        print "did something"
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                    #
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
def mbFunc(sender, value):

    print "did something"

# ----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
# ----------------------------------------------------------------------------------------------------------------------------------------------------#
test = Test()

mb1 = PbaProObject("ResourceList.MIL-Board1")
connect(mb1, "ChildAdded(QObject*)", None, "mbFunc")
connect(mb1, "ChildAdded(QObject*)", None, "mbFunc")

CleanPythonReceiver(test)

RL = PbaProObject("ResourceList")
print RL.childrenNames()

MB1 = RL.GetChild("MIL-Board1")
print MB1.childrenNames()

a = PbaProObject("dialog")
print a.objectName, a.objectPath(), a.classname()

param = PbaProObject("AssignRoot.LS-RT1-TX-SA1-0")
import ConfigParser
c = ConfigParser.ConfigParser()
param2 = PbaProObject("AssignRoot.LS-RT1-TX-SA1-0")
pba = PbaProObject("PBApro")
