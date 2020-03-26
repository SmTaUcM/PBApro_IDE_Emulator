'''#-------------------------------------------------------------------------------------------------------------------------------------------------#
# Name:        PBApro.py
# Purpose:     Detects if PBA.Pro is running and if not imports the emulated version of _PbaProObject.
# Version:     v1.00
# Author:      Sgt. S. Macintosh - MSC System Engineers
#
# Created:     18/03/2020
# Copyright:   (c) Crown Copyright - MSC System Engineers 2020
# Licence:     MSC System Engineers
#-------------------------------------------------------------------------------------------------------------------------------------------------#'''

#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Imports.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
from pydoc import help
import os
import xmltodict
import inspect


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Classes.                                                                      #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
if "PbaProObject" not in dir():

    class _PbaProObject(object):
        '''This class encapsulates a PBA.pro Object.
    - Create a Object with _PbaProObject(Path)
    - Simple setting Properties by Object.Prop = Value
    - Simple reading Properties by Object.Prop
    - Calling Slots Object.Slot(Parameters)
    e.g.
    MyObject = _PbaProObject("ResourceList.MIL-Board1")
    # Get a Property
    print(MyObject.objectName)
    # Set a Property
    MyObject.objectName = "MyResource"
    # Call a Slot
    MyObject.Init()

    Restrictions:
      You cannot deal with objects which have characters in the name, which are interpreted
      as operator from python.
      e.g. ResourceList.MIL-Board1 cannot be used due to the interpreter try s to evaluate :
      ResourceList.MIL   Board1 which is not valid
      In this case you should call:
      MyRes = ResourceList.GetChild("MIL-Board1")
      and do the further operations on "MyRes".
      You may also replace invalid characters (-+/*#%&!()? ) by an underscore:
      ResourceList.MIL_Board1'''

        # Declare and initialise class vairables.
        _instances = []
        _frameworkVersion = "V??.?? Build ???"

        def __init__(self, objectPath, className):

            # Add this object the the class variable instances.
            _PbaProObject._instances.append(self)

            # Declare and initialise instance variables.
            self._objectPath = objectPath
            self.objectName = None
            self._className = className
            self._children = []
            self._parent = None
            self._objectFlag = None
            self._ssData = None

            # Class specific attributes
            #----------------------------------------------------------------#
            #                           PDBSManager                          #
            #----------------------------------------------------------------#
            if className == "PDBSManager":

                # Properties.
                self._properties = ['objectName']

                self.objectName = "DBSManager"

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'sigLoadStreamAssign(bool)', 'sigPrjTitleChanged()']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.sigLoadStreamAssign = self._sigLoadStreamAssign
                self.sigPrjTitleChanged = self._sigPrjTitleChanged

                # Slots.
                self._slots = ['AddGlobalEntryToNode(PPDBSNode*,PPDBSNode*)', 'AddGlobalEntryToNode(PPDBSNode*,PPDBSNode*,bool)', 'CreateClassificationManager()', 'CreateClassificationManager(QString)', 'DBSExport(PPDBSObject*,QString)', 'DBSExport(QObjectList,QString)', 'DBSImport(PPDBSObject*,QString)', 'DBSImportPDI(QString,bool)', 'DBSImportUserDBS(QString,bool)', 'DBSLoad(QString,bool)', 'DBSNew(QString)', 'deleteLater()', 'EmitDbsModified()', 'EnableDBSFunctionality(bool)', 'EnableUpdates(bool)', 'ExpandAll()', 'ExpandAll(bool)', 'GetDBSDescription(QString)', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'IsHidden()', 'IsValid()', 'NewDBSObject(QObject*)', 'OnNewDbsFiles()', 'PrjCanClose()', 'PrjCanClose(bool)', 'PrjDBSIsModified()', 'PrjDBSLoadStreamAssign()', 'PrjDBSNeedsSave()', 'PrjDBSNew()', 'PrjDBSOpen()', 'PrjDBSOpen(QString)', 'PrjDBSSave()', 'PrjDBSSaveAs()', 'PrjDBSSaveAs(QString)', 'PrjDBSSetModified()', 'PrjDBSSetModified(bool)', 'PrjFileIsModified()', 'PrjGetDBSPtr()', 'PrjGetFileName()', 'PrjGetPrjFilePtr()', 'PrjGetTitle()', 'PrjSetDBS(PPDBS*)', 'PrjSetDBS(PPDBS*,bool)', 'PrjSetFileName(QString)', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)']

                self.AddGlobalEntryToNode = self._AddGlobalEntryToNode
                self.CreateClassificationManager = self._blankSignalSlot
                self.DBSExport = self._DBSExport
                self.DBSImport = self._DBSImport
                self.DBSImportPDI = self._DBSImportPDI
                self.DBSImportUserDBS = self._DBSImportUserDBS
                self.DBSLoad = self._DBSLoad
                self.DBSNew = self._DBSNew
                self.EmitDbsModified = self._EmitDbsModified
                self.EnableDBSFunctionality = self._EnableDBSFunctionality
                self.EnableUpdates = self._blankSignalSlot
                self.ExpandAll = self._ExpandAll
                self.GetDBSDescription = self._GetDBSDescription
                self.GetObjectFlags = self._GetObjectFlags
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.NewDBSObject = self._NewDBSObject
                self.OnNewDbsFiles = self._OnNewDbsFiles
                self.PrjCanClose = self._PrjCanClose
                self.PrjDBSIsModified = self._PrjDBSIsModified
                self.PrjDBSLoadStreamAssign = self._PrjDBSLoadStreamAssign
                self.PrjDBSNeedsSave = self._PrjDBSNeedsSave
                self.PrjDBSNew = self._PrjDBSNew
                self.PrjDBSOpen = self._PrjDBSOpen
                self.PrjDBSSave = self._PrjDBSSave
                self.PrjDBSSaveAs = self._PrjDBSSaveAs
                self.PrjDBSSetModified = self._PrjDBSSetModified
                self.PrjFileIsModified = self._PrjFileIsModified
                self.PrjGetDBSPtr = self._PrjGetDBSPtr
                self.PrjGetFileName = self._PrjGetFileName
                self.PrjGetPrjFilePtr = self._PrjGetPrjFilePtr
                self.PrjGetTitle = self._PrjGetTitle
                self.PrjSetDBS = self._PrjSetDBS
                self.PrjSetFileName = self._PrjSetFileName
                self.SetObjectFlag = self._SetObjectFlag

            #--------------------------------#
            #            PPDBSFile           #
            #--------------------------------#
            elif className == "PPDBSFile":

                # Children / Parents.
                self._parent = PbaProObject("DBSManager")
                if not PbaProObject("DBSPrjFile") in PbaProObject("DBSManager")._children:
                    PbaProObject("DBSManager")._children.append(PbaProObject("DBSPrjFile"))

                # Properties.
                self._properties = ['objectName']

                self.objectName = "DBSPrjFile"

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'sigFileNameChanged()', 'sigModify(int,QObject*)', 'sigNewFiles()']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.sigFileNameChanged = self._blankSignalSlot
                self.sigModify = self._blankSignalSlot
                self.sigNewFiles = self._blankSignalSlot

                # Slots.
                self._slots = ['AddFile(QString)', 'AddFile(QString,int)', 'AddFile(QString,int,QString)', 'DBSUse(PPDBS*)', 'DBSUse(PPDBS*,bool)', 'deleteLater()', 'EmitModificationSignal(Modification,QObject*)', 'EmitModificationSignalInt(int,QObject*)', 'EnableUpdates(bool)', 'GetId()', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'HasValidDBSFile()', 'Init()', 'InitFull()', 'IsHidden()', 'IsValid()', 'LoadAll()', 'NewFile()', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'SetSourceHashDirty()']

                self.AddFile = self._AddFile
                self.DBSUse = self._DBSUse
                self.EmitModificationSignal = self._EmitModificationSignal
                self.EmitModificationSignalInt = self._EmitModificationSignalInt
                self.EnableUpdates = self._blankSignalSlot
                self.GetId = self._GetId
                self.GetObjectFlags = self._GetObjectFlags
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.HasValidDBSFile = self._HasValidDBSFile
                self.Init = self._InitDBSPrj
                self.InitFull = self._InitFull
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.LoadAll = self._LoadAll
                self.NewFile = self._blankSignalSlot
                self.SetObjectFlag = self._SetObjectFlag
                self.SetSourceHashDirty = self._SetSourceHashDirty

            #--------------------------------#
            #         PPDBSAssignRoot        #
            #--------------------------------#
            elif className == "PPDBSAssignRoot":

                # Children / Parents.
                self._parent = PbaProObject("DBSManager")
                if not PbaProObject("AssignRoot") in PbaProObject("DBSManager")._children:
                    PbaProObject("DBSManager")._children.append(PbaProObject("AssignRoot"))

                # Properties.
                self._properties = ['objectName', 'Comment', 'Active', 'AutoStart', 'AutoSetup', 'AssignFlags', 'OfflineReplayActive', 'LastFile']

                self.objectName = "AssignRoot"
                self.Comment = ""
                self.Active = False
                self.AutoStart = True
                self.AutoSetup = True
                self.AssignFlags = "FullControl"
                self.OfflineReplayActive = False
                self.LastFile = ""

                # Signals.
                self._signals = ['AboutToChangeState(bool)', 'Activated(bool)', 'AssignFilterChanged()', 'AssignOptionsChanged()', 'ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'ClassificationChanged()', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'OfflineReplayActivated(bool)', 'SearchReplayFinished(bool)']

                self.AboutToChangeState = self._AboutToChangeState
                self.Activated = self._Activated
                self.AssignFilterChanged = self._AssignFilterChanged
                self.AssignOptionsChanged = self._AssignOptionsChanged
                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.ClassificationChanged = self._ClassificationChanged
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.OfflineReplayActivated = self._OfflineReplayActivated
                self.SearchReplayFinished = self._SearchReplayFinished

                # Slots.
                self._slots = ['AssignObject(QObject*)', 'AssignObject(QObject*,int)', 'ConnectReferences()', 'ConnectRequired()', 'CreateAssignOption(QString)', 'CreateAssignOption(QString,bool)', 'deleteLater()', 'DisableAlarmPopup(bool)', 'EnableUpdates(bool)', 'GetAvailableAssignOptions()', 'GetEntryAt(int)', 'GetEntryCount()', 'GetFolders(bool)', 'GetId()', 'GetObjectFlags()', 'GetParameters(bool)', 'GetParamRefs(bool)', 'HasUpdatesEnabled()', 'Init()', 'IsEmpty()', 'IsHidden()', 'IsValid()', 'MayBeTab()', 'NewAssignEntry(QObject*)', 'NewAssignEntry(QObject*,const char*)', 'NewAssignEntry(QObject*,const char*,int)', 'NewComment(QString)', 'NewComment(QString,int)', 'NewDummyAssignEntry()', 'NewDummyAssignEntry(QString)', 'NewDummyAssignEntry(QString,int)', 'NewFolder(QString)', 'NewFolder(QString,int)', 'NewState()', 'NewState(QString)', 'NewState(QString,int)', 'NewTab(QString)', 'NewTab(QString,int)', 'OneConnectTry()', 'OneConnectTry(int)', 'ReplaySearch()', 'ReplaySearchOn(PPDBSParamAssignEntry*)', 'Reset()', 'Run(bool)', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'ShowSignaledParameterDisplay()', 'ShowSignaledParameterDisplay(QObject*)', 'SwitchTab(PPDBSAssignFolder*)', 'Update()', 'Update(bool)']

                self.AssignObject = self._AssignObject
                self.ConnectReferences = self._ConnectReferences
                self.ConnectRequired = self._ConnectRequired
                self.CreateAssignOption = self._blankSignalSlot
                self.DisableAlarmPopup = self._DisableAlarmPopup
                self.EnableUpdates = self._blankSignalSlot
                self.GetAvailableAssignOptions = self._blankSignalSlot
                self.GetEntryAt = self._GetEntryAt
                self.GetEntryCount = self._GetEntryCount
                self.GetFolders = self._GetFolders
                self.GetId = self._GetId
                self.GetObjectFlags = self._GetObjectFlags
                self.GetParamRefs = self._GetParamRefs
                self.GetParameters = self._GetParameters
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.Init = self._InitAssign
                self.IsEmpty = self._IsEmpty
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.MayBeTab = self._blankSignalSlot
                self.NewAssignEntry = self._NewAssignEntry
                self.NewComment = self._NewComment
                self.NewDummyAssignEntry = self._NewDummyAssignEntry
                self.NewFolder = self._NewFolder
                self.NewState = self._NewState
                self.NewTab = self._NewTab
                self.OneConnectTry = self._OneConnectTry
                self.ReplaySearch = self._ReplaySearch
                self.ReplaySearchOn = self._ReplaySearchOn
                self.Reset = self._blankSignalSlot
                self.Run = self._RunAssign
                self.SetObjectFlag = self._SetObjectFlag
                self.ShowSignaledParameterDisplay = self._ShowSignaledParameterDisplay
                self.SwitchTab = self._SwitchTab
                self.Update = self._Update

            #--------------------------------#
            #      PPDBSParamAssignEntry     #
            #--------------------------------#
            elif className == "PPDBSParamAssignEntry":

                # Properties.
                self._properties = ['objectName', 'Comment', 'Value', 'ValueStr', 'ValueDbl', 'ValueRaw', 'Unit']

                self.objectName = None
                self.Comment = ""
                self.Value = 0
                self.ValueStr = "0"
                self.ValueDbl = 0.0
                self.ValueRaw = 0
                self.Unit = ""

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'Updated(QObject*)']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.Updated = self._Updated

                # Slots.
                self._slots = ['CreateAssignOption(QString)', 'CreateAssignOption(QString,bool)', 'deleteLater()', 'EnableUpdates(bool)', 'GetAvailableAssignOptions()', 'GetEntryAt(int)', 'GetEntryCount()', 'GetId()', 'GetInstance()', 'GetInstances()', 'GetInstancesAsObject()', 'GetObjectFlags()', 'GetParamRefObject()', 'GetPossibleOnlineInstances()', 'GetRefObject()', 'GetSourcePosDiff()', 'GetValue()', 'GetValueDbl()', 'GetValueStr()', 'HasUpdatesEnabled()', 'IsHidden()', 'IsValid()', 'IsWritable()', 'Reset()', 'SelectInstance(QString)', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'SetValue(QVariant)', 'SetValueDbl(double)', 'SetValueStr(QString)', 'Update()', 'Update(bool)']

                self.CreateAssignOption = self._CreateAssignOption
                self.EnableUpdates = self._blankSignalSlot
                self.GetAvailableAssignOptions = self._GetAvailableAssignOptions
                self.GetEntryAt = self._GetEntryAt # TODO Implement
                self.GetEntryCount = self._GetEntryCount # TODO Implement
                self.GetId = self._GetId
                self.GetInstance = self._GetInstance # TODO Implement
                self.GetInstances = self._GetInstances # TODO Implement
                self.GetInstancesAsObject = self._GetInstancesAsObject # TODO Implement
                self.GetObjectFlags = self._GetObjectFlags
                self.GetParamRefObject = self._GetParamRefObject # TODO Implement
                self.GetPossibleOnlineInstances = self._blankSignalSlot
                self.GetRefObject = self._GetRefObject # TODO Implement
                self.GetSourcePosDiff = self._GetSourcePosDiff
                self.GetValue = self._GetValue # TODO Implement
                self.GetValueDbl = self._GetValueDbl # TODO Implement
                self.GetValueStr = self._GetValueStr # TODO Implement
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.IsWritable = self._IsWritable
                self.Reset = self._blankSignalSlot
                self.SelectInstance = self._blankSignalSlot
                self.SetObjectFlag = self._SetObjectFlag
                self.SetValue = self._SetValue # TODO Implement
                self.SetValueDbl = self._SetValueDbl # TODO Implement
                self.SetValueStr = self._SetValueStr
                self.Update = self._Update

            #----------------------------------------------------------------#
            #                             PProApp                            #
            #----------------------------------------------------------------#
            elif className == "PProApp":

                # Properties
                self._properties = ['objectName', 'applicationName', 'applicationVersion', 'organizationName', 'organizationDomain', 'layoutDirection', 'windowIcon', 'cursorFlashTime', 'doubleClickInterval', 'keyboardInputInterval', 'wheelScrollLines', 'globalStrut', 'startDragTime', 'startDragDistance', 'quitOnLastWindowClosed', 'styleSheet', 'autoSipEnabled', 'globalStrut_width', 'globalStrut_height']

                self.objectName = "PBApro"
                self.applicationName = "PBA.pro"
                self.applicationVersion = ""
                self.organizationName = ""
                self.organizationDomain = ""
                self.layoutDirection = "LeftToRight"
                self.windowIcon = '0 0 0 69 0 0 0 0 34 0 81 0 80 0 105 0 120 0 109 0 97 0 112 0 73 0 99 0 111 0 110 0 69 0 110 0 103 0 105 0 110 0 101 0 0 0 7 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 16 0 0 0 16 8 2 0 0 0 -112 -111 104 54 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 1 82 73 68 65 84 40 -111 99 -20 -101 119 -111 -127 20 -64 -14 -18 -37 -81 -69 111 62 63 -3 -12 -3 -39 -57 -17 -17 -66 -3 124 -9 -19 23 -102 10 33 46 54 33 46 118 41 126 78 105 62 78 101 17 94 70 6 -1 -7 36 -39 -64 68 -110 106 114 52 48 48 -8 -49 -65 -1 -14 -13 -1 -1 -1 -1 -1 -1 127 -1 -27 103 -125 -126 -115 -1 97 -32 -2 -53 -49 10 -87 -85 25 -4 -25 -17 -65 -4 28 34 -62 -32 63 -97 -119 -127 -127 65 65 -116 -25 -62 -3 119 19 54 95 83 16 -29 -23 79 54 99 96 96 -40 112 -14 -47 -127 43 47 20 -60 120 18 -100 84 20 -60 120 28 116 36 32 -122 27 40 10 49 65 56 2 -36 108 112 6 68 -62 64 81 -24 -61 -41 95 27 78 62 -86 -113 48 96 96 96 -72 112 -1 29 68 -106 73 65 -116 7 -94 -5 -61 -41 95 11 -10 -35 -127 72 28 -72 -14 -126 -127 -127 -31 -63 -85 47 31 -66 -2 74 112 82 -127 24 -63 -64 -64 -32 -96 35 1 -43 -112 56 -23 -120 99 -51 -114 -60 73 71 32 -36 -125 87 94 64 20 -27 -5 106 -63 101 25 24 24 -8 -71 -39 88 -20 117 36 -32 54 -62 77 -102 -97 103 3 -15 73 -126 -109 -54 -125 87 95 22 -20 -69 3 119 -22 32 -116 56 -106 62 127 -93 -69 111 -66 -36 121 -5 -7 -23 -57 -17 63 126 -1 125 -6 -15 -37 -9 -33 127 -31 -46 -100 -84 -52 -46 -4 92 28 -84 -52 -46 -4 -100 42 -62 -68 -54 34 60 44 12 12 12 -54 34 60 -54 34 60 68 -38 0 0 86 21 -110 105 44 105 72 -76 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 16 0 0 0 16 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 24 0 0 0 24 8 2 0 0 0 111 21 -86 -81 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 2 33 73 68 65 84 56 -115 -35 84 65 104 -45 96 20 -2 -70 102 -59 -48 -60 -122 26 66 -91 82 90 18 16 -92 96 79 -21 69 -22 -20 -55 -117 -92 -57 -79 83 101 120 85 -26 89 -104 -126 103 -121 -34 103 -73 -61 96 -80 -53 64 4 79 93 5 47 -18 98 -118 -59 83 106 -118 80 -42 -107 46 -92 -90 33 -110 89 -12 -16 -22 111 9 56 -79 -12 -28 35 -121 -57 -9 -65 -9 -67 -17 -1 30 -7 35 -49 94 54 49 -113 -32 -50 63 -18 14 -3 111 103 99 0 23 22 -93 -23 4 -1 119 34 -1 108 -36 30 -72 -35 -81 62 117 -102 3 -9 -100 30 77 22 -119 55 125 -111 87 101 -111 95 -116 2 -120 -108 30 -66 110 15 -36 -18 -48 -1 -73 -101 76 69 58 -63 -85 -78 24 -127 94 -101 -103 98 58 22 -26 -62 50 79 -94 -119 -39 -43 -78 -106 85 4 0 -99 -2 -88 -45 31 53 90 61 0 -123 92 82 -118 -57 88 41 -127 20 -53 -7 -44 114 62 69 -7 -29 61 3 0 -96 -41 -96 -41 -84 19 -9 -57 84 124 -8 124 42 -83 -18 -122 64 -21 -60 -51 -34 -37 -89 -6 -61 -113 -57 12 39 112 114 53 -110 -45 104 -11 -104 22 -90 -111 -127 89 69 -88 -106 -75 -112 28 -42 -69 64 7 4 61 127 -11 105 125 -21 -120 114 -67 -104 -95 -28 -55 -98 -79 83 55 41 119 -68 0 -64 -125 59 -41 -90 111 74 68 28 -53 0 108 -84 20 88 -34 -23 -113 40 57 124 122 -101 121 -76 93 55 -77 -118 80 41 102 0 -68 109 -11 -78 -118 64 -33 68 17 107 38 119 29 47 -72 -5 -30 29 13 119 -68 -128 38 59 94 -80 83 55 29 47 -40 88 41 -124 -90 94 -49 37 39 -118 110 -26 83 0 12 -53 94 -33 58 114 -68 -64 -80 108 38 -60 -80 -20 91 -113 -34 -44 -18 -33 -88 -106 -75 -51 -75 -91 70 -85 71 54 29 -68 -1 -46 -76 108 -67 -104 97 -101 -27 72 8 -11 -124 22 12 64 -118 -57 54 -41 -106 42 -65 -4 34 22 0 76 114 33 -105 -92 74 78 -118 -57 -120 -78 105 -39 -95 69 80 29 -115 -95 85 -112 -51 -37 117 -109 88 88 72 -15 88 68 90 -35 101 -118 -40 -79 20 -113 -79 126 -26 -67 -29 5 -95 74 -26 -76 97 -39 -1 -13 79 91 -55 95 49 79 71 -83 99 103 102 -118 -4 101 73 -69 36 112 37 85 41 -87 10 -128 -18 -48 111 15 92 -1 -5 -72 61 24 1 -8 -45 107 -85 -55 34 0 85 22 120 46 -86 -54 34 123 -56 127 63 -2 -23 4 63 65 -81 -50 -94 107 110 30 -3 4 -17 -85 17 -104 -26 -4 -110 70 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 24 0 0 0 24 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 32 0 0 0 32 8 2 0 0 0 -4 24 -19 -93 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 4 77 73 68 65 84 72 -119 -75 86 79 72 35 103 20 127 -87 -15 -37 78 38 54 -29 -84 -90 -95 -127 52 67 6 44 33 -117 -45 67 -51 30 22 -44 57 121 -119 70 -16 32 123 49 34 -108 -98 86 115 20 -124 93 65 -16 -74 89 61 46 100 13 45 11 30 10 102 -21 -59 83 -116 -32 -95 73 41 70 118 16 -70 40 9 -95 -106 33 -38 113 -84 -7 -77 59 -87 -48 -61 -85 -97 -77 -93 93 35 101 -65 -45 -5 -66 -17 125 -17 -9 -2 -4 -26 -51 -77 61 125 -79 11 31 115 125 -14 81 -83 3 -128 -67 21 -91 -61 -45 -58 -37 -26 -71 -27 -16 -45 -10 54 -81 -117 -71 29 64 -93 121 -2 -57 105 -29 -16 -76 126 -8 87 -29 -92 110 104 -11 119 90 -35 -72 -6 38 26 -10 -23 53 35 -85 -88 -72 -27 29 -124 119 -36 -23 116 16 -17 103 -116 -41 -27 8 116 57 -83 0 7 -57 -43 -41 -86 126 112 124 118 120 -38 104 37 -96 -84 -94 110 46 12 -107 42 -43 120 50 95 -86 84 125 -97 59 37 -127 79 101 -10 127 -71 80 -16 -70 -104 64 87 -57 61 15 23 -24 114 -38 -104 -79 -17 27 87 -62 -65 113 113 44 -39 73 12 115 44 -47 107 6 0 -60 -109 -7 116 -82 124 85 -115 105 111 -77 -33 -42 -6 76 36 -104 -50 -107 99 -78 -56 -79 -124 99 73 58 87 -98 92 -34 -2 47 -27 70 -13 -4 -42 44 -30 88 82 124 62 -42 43 -16 -93 -117 25 -67 102 -68 -70 -50 113 -13 106 -119 69 104 55 26 -10 -11 10 -4 -85 92 -71 95 81 71 23 51 0 80 40 106 -91 74 -11 -1 2 72 2 63 29 9 114 44 89 90 -33 75 101 -10 1 -96 100 -54 73 -95 -88 125 -8 -71 13 70 86 -52 123 -65 -37 -23 119 59 -87 60 29 9 -22 53 99 126 -75 96 -42 -95 4 -107 4 30 1 36 -127 -25 88 98 -71 -67 62 -126 -60 84 95 52 -20 -93 91 -67 102 12 -50 109 -108 42 -43 -109 -105 15 45 24 -109 -53 -37 104 -35 -17 118 -18 36 -122 47 93 -114 -90 -52 -102 -105 69 -26 88 50 19 9 14 -124 60 -26 107 -114 37 -101 11 67 -110 -64 91 -4 24 8 121 18 83 125 40 -57 100 -47 -14 -60 10 16 13 -5 -42 102 -27 -109 -105 15 19 83 125 120 -99 85 84 91 52 -123 14 114 44 -95 -88 -125 115 27 88 94 106 -120 99 -55 116 36 8 0 -76 -38 22 111 -20 -59 -25 99 -104 -12 -84 -94 110 41 -22 -29 113 9 -75 -93 97 31 45 -58 -105 23 -62 -124 44 82 7 -73 20 21 0 102 34 65 60 -103 95 45 -84 60 122 -128 25 123 15 -64 -17 118 102 21 117 126 -75 -112 85 84 26 108 76 22 -87 -4 108 125 -113 58 69 15 -29 -55 -4 -77 -11 61 -124 4 0 -67 102 -104 -87 -15 94 -118 6 -25 54 6 -25 54 -80 -12 -26 59 108 103 -15 100 62 -98 -52 99 -118 10 69 109 116 49 -125 -87 -64 80 98 -78 -120 79 56 -106 96 -24 0 -48 107 73 -111 -103 85 -3 23 -71 54 51 -127 -70 -97 85 -44 116 -82 60 18 -10 -59 100 81 18 120 73 -32 -47 -88 94 51 -80 48 -119 -87 62 51 95 -1 5 48 111 -48 -106 -123 -56 52 -84 104 -40 55 16 -14 80 -68 -127 -112 7 -81 -106 -42 -9 -16 9 54 62 11 15 47 1 -80 121 -127 -119 15 -106 8 -52 9 76 101 -10 105 -72 88 12 10 -128 -90 -88 124 -7 37 115 44 65 91 -91 74 -43 -116 113 53 106 84 64 79 -11 -102 65 -69 5 -19 2 -123 -94 118 13 -64 -115 -21 -55 -72 4 0 -3 33 -113 94 51 48 45 126 -73 51 38 -117 -3 33 -49 -106 -94 22 -118 26 86 30 127 68 20 -96 -43 118 -115 37 -59 -50 -79 -76 -66 -73 54 43 -5 -35 78 73 -32 39 100 113 116 49 51 33 -117 -113 -57 -91 120 50 63 56 -73 -79 91 -44 54 23 -122 -24 -61 54 -8 42 -38 10 -64 -3 -98 -18 -73 -51 -13 -39 31 126 5 -128 82 -91 -6 -82 121 126 -65 -89 -37 -45 -55 108 41 106 86 81 -97 -116 75 95 -57 127 82 -11 6 0 -4 -4 -26 -24 -69 -95 -98 -36 -101 35 -36 -34 34 -126 45 19 -69 -80 42 -67 23 -35 -76 84 -87 -46 -100 -128 -87 -38 45 1 96 -23 122 5 126 -28 -94 -53 114 44 -103 -112 -59 84 102 95 18 120 36 40 37 8 -70 -30 119 59 105 -27 -19 94 23 -13 -31 97 98 -27 -47 -125 82 -91 42 9 124 58 87 -34 73 12 99 71 -63 121 -126 122 58 -71 -68 -67 54 43 -89 115 101 -20 -116 -76 33 122 93 -116 -19 -23 -117 93 -83 110 28 28 -97 -67 86 79 15 -114 -49 -82 -50 0 -56 -68 -51 -123 33 -31 -37 31 49 26 51 11 -51 73 -61 32 114 -65 29 5 -70 58 -18 121 92 -127 -82 14 -34 65 -20 -128 -109 -109 -17 -18 55 -66 -69 0 -96 -43 -115 -109 -70 -79 -1 -25 25 10 -115 -26 -33 72 121 -102 107 -53 103 -24 117 49 76 -69 -67 -45 65 120 7 17 93 29 -99 14 50 28 -8 -62 -84 96 107 101 -8 -19 -26 -103 59 -92 -19 119 -11 -122 -1 -5 -75 -85 -91 -87 -30 72 107 105 -30 -69 118 125 -12 -23 -6 31 97 -94 10 36 73 -115 -41 44 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 32 0 0 0 32 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 48 0 0 0 48 8 2 0 0 0 -40 96 110 -48 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 6 58 73 68 65 84 88 -123 -19 -104 77 76 27 71 20 -128 -121 2 -101 -38 94 -22 -19 -126 86 75 -83 -102 -75 -68 106 36 119 37 54 -121 -58 -121 -94 98 -10 -108 -117 19 -25 -122 114 40 70 -111 122 -87 -124 -31 104 9 41 88 -118 -108 91 32 -36 9 -50 33 -110 15 -107 76 -61 -123 94 28 87 -30 98 122 -56 34 89 -100 -116 -42 -91 -94 88 22 108 -20 -30 -97 102 -45 -88 61 -68 100 50 -103 93 -57 20 -120 -110 67 -34 -55 59 63 111 -66 121 -13 -26 -51 -13 -21 -71 123 127 27 125 72 -14 -55 -5 6 -96 -27 35 80 55 -23 59 -59 -100 -35 -61 6 -2 109 -74 -98 -103 109 11 127 -14 46 -122 119 95 -64 -97 -63 33 -10 60 -127 -52 -106 -11 -76 101 -107 -114 -114 -31 -121 -39 122 102 -74 -84 -73 -116 71 8 45 76 -86 -23 92 -87 92 109 -112 -115 -68 -101 -31 -35 23 62 119 51 -68 -101 -111 7 7 -32 -57 73 -127 118 15 27 -91 -93 -29 -35 -61 -58 126 -67 -43 126 -2 -94 -37 126 104 -55 23 43 -113 111 95 121 -112 43 45 100 116 114 99 120 39 -65 -96 3 -124 -112 -85 -65 -41 -25 117 7 -121 88 121 112 -128 -78 98 -49 -35 -5 -37 102 -53 42 30 -44 74 71 -115 -30 65 -19 -1 18 -40 69 13 -16 -113 111 95 -87 53 -83 -23 -27 -51 124 -79 -62 121 -104 -72 38 95 11 -5 -25 86 -74 116 -61 116 -100 -94 12 115 -14 32 -85 12 115 -68 -101 -23 -15 125 -97 -39 -81 -73 -49 -50 65 -54 108 52 -76 120 -13 50 66 40 95 -84 -88 1 -98 -13 48 75 -21 59 115 43 91 93 39 -6 -68 -82 -66 115 -89 65 8 97 75 68 20 49 -107 -47 -19 94 -43 73 -10 -21 -19 -45 -36 50 71 -55 38 -75 109 -61 -44 13 51 17 13 69 20 -79 -42 -76 56 15 -125 16 34 -99 -23 36 114 110 64 -87 -116 -2 100 -15 42 66 72 55 -52 -23 -27 -51 116 -82 -12 -12 -31 -115 78 78 -13 110 -127 -64 109 57 15 -109 -50 -107 16 66 -45 -53 -101 -48 -82 27 -26 9 79 -22 -36 -128 34 -118 56 -91 -55 8 -95 84 70 47 87 27 -77 -47 80 -83 -7 58 80 -23 -122 89 111 118 -119 91 -25 3 36 9 108 92 -109 -89 52 57 95 -84 0 10 -76 47 -83 -17 -112 -61 -22 77 43 95 -84 -68 91 -96 88 -40 63 -91 -55 -79 -80 63 -99 43 77 -52 111 -68 -3 68 -14 -59 -54 121 -6 80 68 17 35 -118 -120 63 -67 30 38 22 -10 75 2 -101 -50 -107 2 63 -4 84 -82 54 36 -127 93 -104 84 -87 89 -70 97 -26 -117 21 56 56 -46 60 -108 54 -44 -7 -10 117 4 74 68 67 -79 -80 -33 -34 14 -127 14 33 20 -41 -28 91 54 32 -124 80 -83 105 -51 -83 108 -127 -125 99 -71 53 -87 -98 16 -56 57 -3 80 3 -68 26 -32 59 117 -83 -50 -116 33 -124 70 59 12 -32 60 -52 -22 -52 24 57 -35 110 30 104 116 -100 -2 -122 -123 56 15 19 11 -5 19 -47 16 -87 -82 92 109 60 -56 -107 70 4 54 -82 -55 36 46 57 38 -107 -47 -67 -81 46 63 -76 -60 -62 126 -20 64 -114 -122 -60 35 -99 -127 -44 0 15 103 100 31 -89 27 38 -104 -105 -124 -32 60 -116 36 -80 -10 1 -10 125 75 2 -117 27 83 25 29 -61 -87 1 126 -83 -80 -25 0 52 27 13 37 -94 33 -84 -67 -42 -76 -18 -83 -17 -44 -102 22 -68 -114 8 -95 109 -61 4 2 -110 -107 50 33 -104 -124 108 -60 30 77 -102 103 105 125 7 127 -114 8 -50 -71 91 31 94 24 80 -106 -42 119 106 77 -117 -68 62 83 -102 60 -82 -120 -40 -105 -127 -128 12 -128 -79 -80 -1 -33 -75 56 -87 116 105 125 7 -128 36 -30 -96 -45 -71 82 -83 105 -23 -122 9 -36 82 39 32 10 5 90 -57 9 -53 75 2 75 77 -98 91 -39 -22 -28 -14 -75 -90 53 49 -65 -127 -67 39 17 13 -31 -82 -120 34 62 -66 125 5 -85 -22 -92 -95 47 -107 -47 73 20 12 -31 56 26 66 115 -66 88 33 87 74 101 116 88 27 -114 117 117 102 108 98 126 3 94 123 108 30 -5 -58 58 58 -75 99 60 32 29 22 39 86 -70 97 98 110 114 127 -96 65 55 -52 108 82 -125 -82 -59 -101 -105 -89 -105 55 103 -93 33 -68 42 -98 75 98 -87 1 -34 30 -54 29 2 35 121 83 32 -14 82 3 72 7 -57 -67 36 34 44 -119 -83 8 -25 8 64 11 -109 42 -10 107 71 35 57 0 -111 -86 -73 -99 30 35 106 -19 -123 73 117 52 -64 -109 97 -67 92 109 -112 49 9 -36 25 -17 16 15 -117 40 -94 125 -73 14 64 -28 -123 116 124 29 35 111 -70 -68 61 -18 61 -56 -107 32 -102 -125 -36 35 -78 0 -46 89 29 111 126 23 11 57 2 117 10 33 -80 -34 -12 -14 38 -23 40 84 66 77 2 57 94 -99 30 116 109 -107 106 34 13 -32 -104 -48 -112 49 -119 18 24 79 5 45 42 75 -63 -6 33 44 81 26 28 44 -44 53 -85 114 52 27 64 112 30 -58 -66 12 -104 92 127 21 -15 -79 -110 -102 83 62 121 -42 -100 -6 -23 -61 27 107 -123 -67 88 -40 -113 111 53 -7 23 -20 -55 -30 85 73 96 33 121 74 101 -12 17 -127 -99 -115 -122 0 37 -94 -120 -23 92 105 110 101 -117 -62 58 19 16 -104 36 22 -10 95 -65 -109 3 -69 70 20 49 -101 -44 -22 77 11 63 -73 -23 92 105 122 121 51 -82 -55 -85 51 99 -70 97 66 114 7 -24 -39 -92 -106 77 106 19 -13 27 -92 -50 51 -107 99 -32 44 38 -26 55 -16 41 -25 -117 -107 -23 -27 77 -120 64 -32 43 -40 90 16 -115 -80 63 -107 -85 -115 -21 119 114 17 69 -92 -34 -112 51 1 69 20 113 -83 -80 71 121 -52 90 97 15 28 69 18 88 -100 -50 -114 43 -30 90 97 -113 58 -99 114 -75 -95 27 38 117 63 -50 4 52 34 -80 -10 -56 -119 119 60 74 -68 12 -110 -64 -2 -18 -12 -113 -64 126 91 -49 4 36 9 -20 -72 45 35 75 68 67 -64 -95 6 120 12 -95 27 -90 61 122 69 20 81 18 88 -54 -64 -89 1 90 -68 121 25 18 38 72 -106 -55 39 125 54 26 -118 107 50 -8 13 -7 118 -2 92 -40 -117 107 50 -7 -68 -88 1 62 -101 -44 -20 -119 70 -33 119 65 -95 120 80 -21 90 26 35 101 54 26 66 8 65 2 122 105 -18 81 54 -87 37 -94 33 -56 55 36 -127 -123 -78 -112 36 -80 -100 -121 -95 -100 61 -101 -44 -14 -59 -54 -81 -59 10 -68 125 84 -115 -122 119 51 -54 48 -41 3 117 -22 -3 122 -5 -73 63 -114 118 15 -113 79 82 -99 -119 107 50 108 -21 -42 -92 122 105 -18 17 122 -107 -65 -106 -85 13 -20 -71 -100 -121 81 3 60 21 99 33 -65 -106 4 -74 -42 -76 -42 10 123 112 -29 124 94 87 112 104 -32 -101 47 7 125 94 23 -126 10 26 57 -89 -3 -4 -59 -18 -31 -15 -2 95 -19 -82 85 61 120 -28 -81 -33 -55 -99 -52 -84 -81 5 -41 -13 124 -97 -71 -126 67 3 -82 -2 94 -78 -105 14 -116 -82 -2 94 101 -104 83 -122 57 116 -15 37 -33 -97 -11 -10 126 -67 -43 -2 -25 5 20 95 113 -23 115 52 -64 59 38 39 -92 64 -71 19 33 20 28 98 93 125 -67 62 -81 -5 11 -81 -117 34 -96 -92 75 -92 118 -11 -9 6 -121 -40 -105 117 -55 -117 111 116 105 95 -117 -11 -22 -33 63 126 -5 21 53 -27 -45 -2 94 48 -2 -23 -124 62 -78 -9 46 31 92 37 -1 35 80 55 -7 15 54 -10 62 -9 -102 36 109 -54 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 48 0 0 0 48 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 64 0 0 0 64 8 2 0 0 0 37 11 -26 -119 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 8 57 73 68 65 84 104 -127 -19 90 79 72 35 89 26 -1 92 99 -51 38 41 59 -43 -75 110 -120 29 72 -89 48 -80 32 105 -70 122 97 -52 97 101 77 -41 -55 -117 -37 105 -24 -125 -21 30 -116 8 115 27 -19 28 -123 6 21 -124 -66 -115 -58 99 -125 -93 115 112 16 102 64 -69 115 -40 62 69 5 47 122 -39 -56 -124 -100 -30 38 45 -40 29 -126 19 75 -83 36 76 -71 13 123 -8 -76 120 -3 -22 79 -94 73 70 26 -6 -121 -121 88 -11 -22 -43 -9 -5 -66 -17 125 127 94 -67 -74 -17 -66 -33 -121 -49 25 127 -72 109 1 26 -59 23 2 -73 -115 47 4 110 27 -74 6 -97 -81 94 124 124 127 90 -59 -33 -39 95 -49 -21 121 -60 110 107 -9 -70 28 -8 -69 -89 -117 109 80 -128 107 16 56 58 -83 -98 84 126 59 58 -85 -106 42 -22 73 69 45 85 126 43 85 -44 58 -97 -27 -100 -116 40 -16 91 -23 -126 -31 93 -34 -63 -16 -114 -81 -18 58 24 -34 -63 120 -17 -40 -17 58 -66 -14 -70 -20 117 -50 108 69 -32 -24 -76 122 112 124 126 116 86 125 127 90 57 -70 82 -13 -115 49 42 5 -106 39 -6 -57 22 119 -12 52 74 21 85 -81 11 -81 -53 126 -49 -27 -16 -34 -79 -9 116 117 90 -16 105 -93 18 25 10 -99 -3 85 57 56 62 -81 94 124 108 80 104 10 -53 19 -3 81 41 -80 -79 123 56 -74 -72 35 -105 -21 -75 30 0 -40 59 -38 123 -70 58 3 127 98 -11 100 46 9 -92 63 -56 -65 20 78 15 -114 -49 -21 -9 -118 -101 1 57 -56 101 117 118 45 -75 -112 -56 0 64 56 -24 25 -107 2 -111 -112 15 0 -18 -2 -21 -57 -102 51 -16 14 -90 -89 -85 -13 -127 -57 21 -20 -26 0 -96 -19 -21 111 -33 -92 63 -56 77 87 -74 5 54 -25 6 -61 65 15 0 -96 47 105 -65 99 75 123 -87 92 -87 -2 121 -20 29 -19 -63 110 -82 13 -98 44 -73 72 80 51 68 66 -66 -11 41 73 -5 119 43 93 -104 93 75 -103 -83 -17 -102 104 52 -116 -42 68 56 -24 73 -27 74 -24 -15 126 55 27 -107 2 -109 67 -67 -38 -35 -123 68 38 -74 -76 -41 -56 -4 45 39 48 42 5 -42 67 -66 120 34 3 0 -45 -61 34 0 -56 101 117 99 -9 16 -99 -2 93 81 105 112 -2 -106 19 24 91 -36 -127 -119 126 20 61 95 84 -30 -119 -52 74 50 11 0 -31 87 -49 56 39 115 45 -89 55 68 107 75 9 -65 -101 125 62 -44 -69 -99 46 0 -64 66 34 35 124 -13 -13 66 34 35 -105 85 -71 -84 -94 -24 -115 19 104 -107 5 -94 82 96 32 -24 121 87 84 80 -30 -7 -15 -66 -41 -69 -121 -28 -128 -19 116 65 20 -8 107 101 3 67 52 -103 -128 -33 -51 78 14 -11 70 66 -66 31 -110 -39 -40 -46 -98 38 -33 -58 -18 -95 62 -50 52 -82 126 104 34 -127 -88 20 24 -107 2 -94 -64 -57 19 -103 71 -79 55 -108 106 -57 22 119 -12 -113 108 -33 52 116 -110 104 -108 -128 40 -16 -88 114 0 -120 39 50 79 95 38 -21 -12 10 -71 -84 -26 27 14 65 0 112 -61 68 -58 57 -103 72 -56 55 57 -44 -117 126 28 79 100 -48 -41 27 23 -24 -70 -88 109 -127 -103 97 17 -125 -96 33 -88 -54 108 125 74 66 107 -112 -56 23 21 -4 -5 33 -103 53 -53 -72 -100 -109 57 89 29 -47 95 111 -117 -84 88 -117 87 59 -116 -34 119 91 -11 28 -111 -112 111 121 -94 -97 115 50 -8 -81 40 -16 -6 49 126 55 27 14 122 -94 82 96 115 110 112 115 110 80 27 76 -30 57 -111 -98 73 96 -91 100 -127 -38 4 12 101 34 17 9 -7 -48 68 -100 -109 -15 91 -78 69 -127 -26 -57 -5 -88 -117 -100 -109 -103 52 33 80 19 -90 4 -4 110 118 102 88 -52 -67 122 86 -109 0 0 60 31 -22 -11 -69 -39 122 70 2 64 84 10 80 70 -120 -124 124 -122 102 -127 -101 89 0 -85 -59 -36 -85 103 -45 -61 34 -91 -47 124 81 105 -117 -84 -76 69 86 -12 21 -104 -98 -64 66 34 -125 -125 -79 -18 39 65 -115 36 -41 24 -107 28 92 38 -60 12 8 -8 -35 -20 -4 120 -33 -55 -22 -120 -31 66 -92 102 95 72 100 -12 -53 -15 -31 -89 98 105 -123 26 -107 -125 41 68 -91 0 -87 -90 120 34 67 -122 -41 -102 86 -75 -63 85 14 -94 -116 -107 47 42 -77 107 41 -65 -101 37 -43 -77 127 69 -64 -48 -35 -87 43 26 -37 81 41 64 94 -105 -53 42 73 -98 -68 43 -105 -43 -107 100 118 -108 -96 84 115 81 -39 78 86 71 40 -1 67 -47 -79 102 36 59 15 -108 -119 115 50 -31 -96 71 -17 93 -87 92 -119 82 -63 -12 -80 56 13 -32 119 -77 -44 72 -46 -3 -62 65 15 -7 20 -66 -108 -52 39 -75 9 -112 -46 -109 -94 35 40 11 82 124 -56 23 -21 87 -95 126 -3 -27 -117 74 108 105 111 -125 -16 40 42 -61 96 -37 -80 -97 43 -111 62 44 10 -68 69 -43 100 51 19 29 81 83 1 0 -112 -54 -107 98 75 123 53 -61 -59 -54 -89 -27 29 92 -27 7 114 76 -18 -43 51 -3 -125 102 1 10 97 51 19 29 -22 8 97 -92 88 -108 -83 -74 -46 -123 -19 116 -63 -27 100 -76 -96 25 -107 2 -94 -64 -113 45 -18 104 -22 -76 72 -16 36 44 118 -60 0 -64 38 124 -13 -77 -39 61 125 12 -51 23 21 -71 -84 -18 95 -11 34 91 -23 -126 -90 81 42 4 -59 19 25 116 -107 -41 -69 -121 -101 115 -125 -102 40 -53 19 -3 -113 98 111 -32 -86 63 -82 -121 64 13 11 88 -36 -45 -53 -92 -113 -24 26 -12 108 -15 7 -91 60 81 -32 -3 110 54 95 84 -88 -44 -69 -112 -56 104 -47 -42 -17 102 -105 39 -6 -75 91 3 -106 -114 96 69 -128 -14 10 -21 -2 -61 108 -80 -34 15 -3 110 86 46 -85 -108 -6 103 -41 82 -28 -14 32 9 -36 -36 2 -11 19 -96 -92 -108 -53 -22 -52 -80 8 0 -9 -115 -4 36 -107 43 61 31 -22 37 -59 90 73 102 45 74 113 -21 92 102 74 -128 115 50 84 -124 -75 120 7 -27 63 -100 -109 49 91 -96 -24 81 -108 -1 -52 -82 -91 -88 97 -87 92 -119 -108 27 -67 -50 112 66 -45 98 -114 -30 109 -35 61 61 -84 -81 -116 -109 -53 106 108 105 -113 82 -1 86 -70 -96 -97 -100 82 -106 69 52 55 37 64 121 -123 117 -1 90 79 29 -70 -79 123 -8 40 -10 38 -107 43 81 -107 69 -36 60 48 -104 9 67 -62 -76 -91 -92 74 0 -116 -95 55 120 1 66 -37 93 -60 47 29 -28 45 -61 24 95 -1 -37 111 97 115 -73 -71 104 -55 -58 22 70 -98 -107 100 22 -73 -73 112 9 110 -89 11 84 -66 15 95 -35 -102 28 -22 -27 -100 -116 -106 -5 34 33 -33 -109 -112 15 45 -112 -54 -107 94 27 -19 41 105 104 -119 5 -2 51 -1 15 -72 -118 99 -72 70 -61 65 -113 40 -16 -7 -94 -14 -12 101 82 11 -57 51 -61 34 -118 -114 -75 96 36 -28 123 -6 50 57 61 44 98 -19 -128 -107 8 62 104 -15 81 -89 37 22 64 47 -89 -34 26 14 122 -42 -89 -92 -11 41 73 43 94 6 -126 30 -50 -55 60 126 -15 118 43 93 -32 -100 -116 127 110 112 125 74 74 -27 74 -72 -42 -75 -39 -94 82 96 121 -94 95 30 -17 51 -36 29 107 -2 -26 -82 -10 -59 -123 -38 -28 -62 43 100 9 -124 -86 69 -9 -64 125 46 -71 -84 62 126 -15 -106 -54 -104 43 -55 -20 -20 90 -118 106 -36 90 72 0 95 99 -88 45 116 39 -84 109 -48 -63 -56 -6 39 18 -14 -59 77 118 -57 112 -15 24 54 -70 45 33 -112 -54 -107 -52 -94 94 -66 -88 32 67 116 51 77 -39 120 113 -61 -92 123 -58 -39 12 -117 -94 -26 19 24 8 122 -84 11 27 -108 6 61 -115 -14 22 -77 114 11 69 55 -100 -74 -7 4 68 -127 -73 -40 -28 -31 -100 12 38 -11 -5 110 86 31 28 -51 18 34 58 -113 97 48 109 50 1 -12 108 81 -32 -11 -94 112 78 102 126 -68 15 63 -112 1 97 10 4 -10 70 -93 70 45 14 -106 -122 91 -23 -126 -95 125 -102 64 -64 -17 102 79 86 71 78 86 71 68 -127 71 -49 -34 74 23 -42 -89 36 -110 -125 -33 -51 110 -50 13 98 75 -119 -98 32 10 -4 -2 -89 2 -59 19 -103 -88 20 -104 -7 -76 -116 21 5 30 -73 83 -51 62 102 -38 -2 -7 -24 -2 47 -123 -45 -12 7 -71 17 2 -24 51 -102 -60 -113 95 -68 93 -98 -24 -33 -100 27 -60 26 6 109 34 -105 -43 -79 -59 29 84 -65 -31 2 -104 89 75 -71 -100 -52 -12 -80 56 42 5 -74 -46 -123 119 69 -27 73 -56 -121 -122 -46 -57 86 0 8 118 115 15 60 -82 -53 -93 6 -43 -117 -113 7 -57 -25 -56 -28 -70 95 -19 -47 55 0 32 -74 -76 55 63 -34 39 10 60 118 -67 -94 -64 71 66 -66 -121 2 -97 47 42 -17 -118 10 -39 -75 96 54 48 -4 -92 -128 -73 6 -82 24 -18 -25 74 100 1 -126 95 -25 31 120 92 61 93 -99 -10 -114 118 -48 31 -10 -128 -58 -50 123 108 -50 13 -54 101 -11 -23 -53 -28 -75 -98 -78 -122 -59 73 15 48 44 37 -68 46 -69 -41 101 -1 123 -113 27 0 74 21 -11 -3 105 -27 -24 -84 122 112 -84 28 -99 86 106 -14 9 7 61 -6 -10 -22 6 18 123 93 -114 -98 46 -42 123 -57 126 -49 -27 -32 29 55 -19 -119 -31 -14 40 18 19 -20 -26 -32 47 -105 87 14 -114 -107 -22 -59 -1 -114 -50 -86 -38 89 -83 -20 -15 -27 65 45 -83 126 -84 95 -42 64 87 39 0 -36 115 -39 -19 29 -19 -34 59 118 123 -121 -19 -70 103 -72 -82 93 -52 -31 11 -16 -88 11 -123 123 -35 78 0 -8 -21 -97 57 -17 -33 -2 104 49 3 -98 -52 -70 -18 123 -51 -48 -52 106 84 57 -65 -8 -23 -33 -1 101 -37 109 108 -61 39 -31 -22 71 51 9 -100 41 -22 -103 -14 123 127 -88 -4 -20 -113 93 126 33 112 -37 -8 -20 9 -4 31 -99 37 63 -65 104 -116 66 -4 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 64 0 0 0 64 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 0 -128 0 0 0 -128 8 2 0 0 0 76 92 -10 -100 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 16 15 73 68 65 84 120 -100 -19 93 95 76 27 71 26 31 106 -40 102 -19 37 118 -116 -49 114 66 75 108 97 -119 8 57 -86 83 41 112 39 -47 -122 88 58 -107 23 90 -94 -26 -127 -10 30 2 66 -86 -46 23 18 -98 -18 34 69 34 72 -111 -14 86 2 79 85 -92 -108 -28 -95 39 30 42 -123 -108 -121 -53 19 113 36 -92 59 -72 -121 58 -70 21 -22 85 70 118 -23 -111 88 46 113 -20 98 -29 -85 9 -70 123 -8 96 50 -39 63 -29 -35 -39 -75 -41 78 -3 123 -120 54 -34 -35 -39 -31 -5 -51 124 -13 -51 -9 125 51 -45 -12 -59 87 -113 81 3 -42 -31 13 -85 43 -16 91 71 -125 0 -117 -47 32 -64 98 52 8 -80 24 13 2 44 70 -125 0 -117 -47 32 -64 98 52 8 -80 24 13 2 44 70 -125 0 -117 -47 32 -64 98 52 8 -80 24 -51 86 87 64 43 -42 -73 -14 -70 -98 -17 -12 8 21 -86 -119 -71 -80 -110 -128 -30 -18 -34 -109 92 17 33 -76 -103 -37 41 -66 -40 67 8 109 -26 -118 -1 -35 -35 67 8 21 119 95 108 -26 -118 38 126 43 -24 105 -123 -117 67 45 -74 118 39 -113 16 -30 -101 109 -19 78 59 66 -24 -104 -109 -25 91 108 38 126 75 23 -86 65 0 8 58 -77 -13 107 -90 88 2 17 103 118 126 -51 -20 -108 -86 -16 105 -116 -8 -42 54 -66 22 -97 102 -27 15 -72 -19 -100 -37 -2 -26 17 59 -25 -74 115 110 -98 115 -37 -33 -84 14 49 -26 19 -112 -39 41 61 -33 41 -59 -97 109 -17 95 16 127 121 21 -48 31 -14 77 14 -121 -109 -23 -4 -60 -19 -43 108 65 7 -57 -103 -99 -110 98 -101 8 122 90 -127 -107 96 -37 -2 -123 121 -107 69 8 -95 38 -29 1 -103 -52 78 105 125 107 123 -13 -105 -30 -109 92 113 51 -73 83 -36 -35 51 -91 102 -52 -72 54 28 -98 28 14 103 11 -91 -87 -7 -40 -51 -59 53 115 11 -25 91 108 -19 78 -5 49 39 -33 126 -104 -17 -12 -76 26 -25 -125 -111 -128 -11 -83 124 -4 -39 -10 -6 86 -66 22 36 46 -57 72 36 56 61 -42 -29 114 112 -79 68 102 -30 -10 106 84 76 85 -24 67 -64 71 -89 71 8 -74 -75 -78 13 -5 58 8 -64 66 -81 -78 86 97 67 127 -56 -9 -16 -6 0 92 -33 92 92 -101 -102 -113 -23 -46 72 108 8 122 90 -113 57 -7 -109 62 -105 118 50 -54 16 -80 -103 43 -82 111 109 -117 -87 92 93 8 93 -126 -111 72 112 110 -68 15 -82 -77 -123 -46 -60 -19 -43 59 75 113 -6 43 46 7 23 14 -72 17 66 -79 68 -58 32 97 65 79 107 -56 -25 -20 -12 -76 -126 -47 -91 6 101 2 -60 -89 -39 -8 -77 -68 -8 52 91 101 91 -59 116 -112 28 32 -124 -94 98 106 116 118 57 -103 -106 78 41 92 14 110 36 18 -68 16 9 -126 -12 17 66 103 -81 62 48 75 113 -71 -19 92 -24 -88 43 -40 38 -124 -114 -70 -28 119 95 33 64 124 -102 -3 87 42 39 62 -51 -42 -96 90 103 -58 -27 -63 -18 -23 -79 30 -14 -105 -87 -7 -40 -75 -7 24 92 -5 -67 -62 -28 112 120 -88 -73 -61 -27 120 57 -100 -34 89 -118 -113 -50 46 -101 94 19 -66 -59 22 58 -22 58 -23 115 -110 76 52 125 -15 -43 -29 -11 -83 -4 -22 79 -49 94 51 -71 -109 -72 119 37 50 -44 -37 65 -2 18 75 100 102 22 -41 -50 -124 124 35 -111 32 -7 123 -123 108 39 9 -128 -119 -98 -73 -37 58 61 66 -109 -5 -109 -81 -21 93 -49 -108 -123 -33 43 36 110 -99 -89 63 -109 45 -108 22 86 54 -90 -26 99 114 5 85 57 -72 -19 92 -13 107 47 125 -124 80 50 -99 95 88 -39 -112 116 2 -116 108 -95 52 -77 -72 118 115 113 -83 10 102 -110 4 -103 -99 82 -35 56 -29 -116 -64 -17 21 20 -123 -85 -47 52 -86 40 94 115 2 96 -116 -107 40 122 -116 -88 -104 -78 86 -6 -24 53 32 96 122 -84 103 36 18 -108 -21 16 112 10 -11 -121 124 -108 119 31 39 50 -107 -81 96 25 -40 -48 -119 33 -85 -21 96 8 43 63 -4 60 -44 -37 49 -4 94 -32 -30 64 23 -49 -39 98 -119 -116 -17 8 127 -17 74 -28 -38 112 -40 -17 125 57 29 -51 22 74 -13 -53 9 -105 -125 35 -51 -51 -103 -59 -75 -17 55 115 86 -44 -6 37 -102 -48 71 115 -42 -42 -64 56 -4 94 -31 -69 -23 15 65 -78 -48 9 72 41 -109 99 -84 100 78 96 -30 108 -117 25 -81 3 1 8 -95 112 -64 -3 -16 -6 0 41 119 116 96 -20 -109 90 -34 -27 -32 18 -73 -50 -29 -57 -102 -122 -18 84 -77 -110 -118 -88 -5 49 0 16 75 100 -94 98 10 27 -102 -93 -77 -53 81 49 37 -73 -24 -77 -123 -46 -99 -91 -8 -27 -63 110 -124 80 53 -19 125 10 -22 -98 -128 112 -64 61 -44 -37 -111 45 -108 70 103 -105 -121 -66 -2 20 -107 -77 109 114 7 3 117 -125 0 67 112 57 -72 -95 -34 -114 11 -111 -32 35 49 -123 -19 -97 100 58 -17 -9 10 -113 -88 106 61 118 96 -7 -48 31 -85 26 -22 -113 -128 112 -64 125 105 -80 -69 63 -28 -69 -69 20 63 119 99 -119 52 61 -127 0 -6 -72 -118 -97 -113 -43 -128 13 -118 -22 -120 0 -16 24 95 26 -20 118 57 -72 -103 -59 -75 83 19 -33 -54 39 -73 -96 85 52 18 -48 80 65 90 -47 31 -14 93 -120 4 71 34 -63 -78 78 -101 31 -45 -7 -78 51 91 -36 -16 27 61 -96 12 -4 94 1 -126 36 -32 -55 1 47 49 -35 95 -122 -67 -4 101 81 35 -46 71 -75 73 0 -116 -82 96 83 106 20 -67 94 52 8 80 0 -39 -28 81 -123 -67 -60 63 -42 -58 0 -128 106 -124 0 -112 59 118 -100 37 -45 121 -104 -63 86 -56 65 -97 -44 48 84 84 13 86 -70 34 -4 94 -31 -46 96 -9 72 36 -120 125 3 -55 116 126 106 62 86 59 -46 -87 2 44 -24 1 48 -121 -70 52 -40 -115 83 16 -48 111 82 -12 0 -45 8 -96 123 -34 49 96 116 37 -67 102 116 -47 107 44 22 -61 -72 119 19 -89 6 -107 -123 -15 -36 33 100 22 1 100 26 -102 46 68 -59 -44 -39 -85 15 -44 -18 -6 -67 2 67 -79 -79 68 38 -106 -56 -36 93 -118 -77 -111 1 105 -115 90 -98 60 119 99 105 97 101 -125 -31 19 36 -52 89 33 67 -122 62 116 -95 63 -28 123 -2 -11 -89 -32 -98 -108 67 99 75 -108 -65 53 18 9 62 -68 62 -112 -72 117 94 111 7 66 8 93 82 -87 -116 -30 -121 -12 22 46 -121 -59 4 32 -124 92 14 110 122 -84 71 -18 -51 71 -122 -1 66 -24 64 -41 -122 -61 -38 95 25 57 48 -126 -75 -32 -72 -127 -65 26 -61 28 2 -50 -24 111 104 18 40 42 -79 119 -52 104 98 -109 -61 97 -75 30 38 -121 -10 -26 -113 -116 53 59 12 -21 123 0 70 56 -32 -106 -76 86 83 -6 56 66 104 122 -84 71 75 13 -5 67 62 93 95 -84 9 2 64 -37 -102 82 21 -124 16 56 59 -31 -38 -27 -32 -52 42 22 33 52 -87 65 17 105 121 -122 -124 41 -43 99 -76 -126 -28 115 40 53 96 91 77 -53 120 8 83 4 48 73 -23 -115 17 23 27 14 -72 -53 -42 65 -53 -41 -3 94 -127 97 -60 14 7 -36 6 -35 74 -6 8 80 -100 67 -47 49 58 -69 -116 -85 -88 37 87 -25 76 -56 -89 -123 0 -78 88 -105 -125 -69 60 -40 77 111 -65 101 91 43 -27 -11 -101 -117 107 106 -93 -120 22 -18 -23 -48 -86 -126 -62 1 -9 -36 120 95 -30 -42 -7 -71 -15 62 93 -118 -110 108 32 96 -11 -45 109 103 44 41 -70 -115 65 22 -101 45 -108 -82 25 -101 69 -125 31 80 -15 86 84 76 -35 87 -81 48 67 -89 -111 -96 76 15 -112 -81 92 -48 5 -59 -18 57 113 123 85 45 79 -106 4 -27 -117 -118 -59 -34 93 -118 -85 9 -79 44 40 -58 -49 -35 10 123 71 84 9 -64 113 40 -6 -5 16 -122 -91 -36 -43 -8 -93 98 5 -44 110 41 18 -64 -84 13 -96 -111 41 -34 2 -65 41 -91 100 -29 -10 -73 -108 0 -65 87 0 45 95 86 105 -126 15 39 42 -90 40 -87 -9 -118 -55 -105 90 36 69 -1 -70 -94 55 -1 35 106 -81 -94 -72 37 46 19 -90 -105 4 -48 -4 41 14 31 -29 99 -64 75 2 -56 56 20 29 -92 -5 -116 -82 4 21 -1 108 -6 -76 8 -6 7 -99 0 121 -79 35 -27 58 43 69 -109 80 -12 15 30 87 -44 58 -70 -15 -103 74 -77 36 14 69 -121 -36 115 73 39 64 -82 109 70 34 65 -70 -71 2 -23 58 -12 98 73 -109 -47 -17 21 62 -22 -19 -96 -73 -101 88 34 -93 54 68 83 44 -23 59 75 113 92 127 -118 -90 -11 123 5 35 9 22 -51 101 -41 -18 -32 26 40 58 -115 -23 -74 10 -82 25 -120 -116 12 123 -87 1 90 55 -35 9 65 46 124 44 -117 108 -95 116 -18 -58 -110 -38 93 74 107 -48 56 -4 26 37 -96 -20 19 116 127 61 -67 15 -2 111 97 68 87 109 112 -93 51 107 14 28 21 83 -110 -28 45 18 20 -41 91 50 -99 39 21 -35 35 49 -91 -42 116 -62 1 -73 -111 32 4 -115 0 45 81 42 -77 -36 53 -24 32 1 -62 -84 98 -93 98 106 102 113 -115 62 -25 -72 -96 62 108 76 105 -50 112 49 56 14 43 19 -96 49 64 104 -94 -12 17 66 19 -73 87 -95 -7 27 41 22 2 -6 11 43 27 101 -43 66 127 -56 71 -47 -121 115 -29 125 26 21 -99 65 75 84 74 -128 -82 -40 -84 -119 -50 -78 -47 -39 101 -4 81 35 4 -128 -109 10 -46 -48 -23 79 -22 117 -67 85 8 47 9 96 8 -117 -101 -46 3 -110 -23 60 -92 -13 -29 95 52 -38 -96 106 110 56 -65 87 -104 27 -17 -69 52 -40 77 -6 -117 -28 -49 24 -9 34 0 12 -106 -45 -116 12 100 36 24 -20 125 106 -33 -91 20 -101 45 -108 -56 24 -78 -33 43 76 -113 -11 40 -38 -96 -80 102 -26 -20 -43 7 -118 28 -104 -37 -4 93 14 -114 57 58 -33 76 -10 125 -67 96 80 65 -79 68 38 -103 -50 63 18 83 81 49 69 105 -98 -108 -41 -55 -1 38 -45 -7 115 55 -106 -26 -58 -5 20 103 97 46 7 -9 -16 -6 64 -32 -77 111 36 -46 -95 -72 -34 -40 96 -60 16 106 54 -24 68 84 -69 69 110 -120 -95 11 -12 56 -116 -30 -86 -118 -87 -7 -104 -102 64 -63 83 45 -87 -119 -71 -46 71 -58 -58 66 -10 -76 20 -70 -18 99 14 83 -48 -57 21 6 -17 -34 -123 72 -112 36 -64 -27 -32 -24 -66 7 -75 -7 -41 -12 88 -113 90 -35 -84 33 -128 65 82 -58 -117 101 -32 85 34 29 -118 -21 13 33 68 -39 -84 35 -103 -50 -85 -43 -51 72 -14 0 123 76 88 123 -64 -92 -46 -59 -22 -78 67 40 -109 47 -6 -20 -127 -78 -84 -34 -56 92 -116 -99 0 74 83 53 50 53 -41 27 -121 -127 -76 34 -115 -123 -45 -45 126 102 88 -73 9 50 98 -119 86 -124 0 35 -50 41 -54 31 35 41 22 2 41 -33 77 127 72 -41 90 -92 9 68 -79 62 37 -50 31 57 -24 119 -103 59 1 123 86 4 -27 -109 -52 -101 96 -48 71 51 48 -19 -111 -26 76 8 0 22 28 -67 -7 107 119 -2 -88 -43 -115 -83 -33 -77 19 64 -71 91 33 19 -56 -17 21 24 -20 13 28 82 -89 104 127 45 -82 11 122 -73 102 54 -124 24 85 -112 37 54 40 3 112 40 -122 -18 122 -45 -94 -3 107 -117 0 -118 -31 -107 76 -25 -103 -25 -27 -90 36 -125 98 -64 -2 5 112 77 -9 61 24 95 24 -62 -20 -107 97 36 64 -69 -73 64 23 -52 -115 46 96 71 16 -67 -7 -109 -95 71 58 40 127 90 -75 7 97 -118 -92 -104 71 96 19 -109 65 -17 44 -59 -55 41 21 -67 -7 107 -73 62 41 61 -101 -71 -23 -80 16 80 -77 3 0 108 90 51 -77 -72 70 -74 104 122 -13 -89 -8 4 -11 -126 45 56 -52 -78 74 -110 -66 -118 -118 121 -27 20 -101 -111 3 -56 22 74 20 -33 42 61 117 76 -69 -44 -24 -26 47 -37 31 -2 -102 -20 -104 85 -65 104 -100 -94 100 49 26 4 88 -116 -102 -40 -86 -128 25 46 7 39 89 87 4 -29 -80 94 93 76 -58 -56 96 86 44 47 1 -62 -56 126 -81 -16 78 -64 -19 114 112 16 26 -118 -118 41 -125 43 -109 -21 102 12 -64 -85 -8 32 -122 -38 31 -14 93 26 -20 86 -53 72 -124 109 -72 -23 -26 13 36 -115 -99 -102 -8 -10 66 36 40 73 87 -51 22 74 -89 38 -66 -59 -125 51 108 20 -91 102 119 -64 -82 -33 122 -49 12 -62 -88 -101 -115 91 -121 122 59 6 -34 109 71 8 77 -51 -57 -2 -4 -15 -55 47 63 -1 -61 -119 -73 -100 112 11 54 72 76 -90 -13 46 7 119 -120 -77 33 -124 78 -68 -27 -68 56 -48 -43 -92 -18 -62 -20 15 -7 96 7 -88 -2 -112 15 88 -116 37 50 -13 -53 -119 67 -100 -51 119 -124 63 -60 -39 92 14 -18 -2 -54 70 56 -32 -2 -37 -28 31 47 14 116 -7 -114 -16 8 -95 108 -95 -12 -113 31 126 -66 -69 20 127 36 -90 -78 -123 18 60 118 -120 -77 -123 3 -18 -117 3 93 -1 -34 -52 49 108 3 91 55 42 8 7 106 -90 -57 122 -64 -82 87 -52 125 -125 29 -27 64 -97 76 14 -121 -113 123 5 -59 -93 24 -64 48 5 123 58 -106 -56 -112 9 44 112 -40 0 -92 -23 -49 -115 -9 -127 -35 -87 -106 103 -121 -9 -90 118 57 -72 123 87 34 12 25 14 117 -45 3 -2 -14 -15 73 -112 26 -4 59 113 123 -11 -13 47 -1 46 111 113 -87 108 -15 -2 -54 -58 35 49 53 -44 -37 1 109 -13 113 34 35 127 -20 66 36 -8 -5 -82 -33 -95 3 -113 5 -7 -64 -81 -69 123 -61 -17 5 -4 94 97 -8 -67 0 -12 39 -75 111 -63 -21 -9 87 54 30 39 50 3 -17 -74 31 -30 108 67 -67 29 -113 -108 -10 43 -91 -96 110 -84 32 -84 -126 65 65 -45 15 -71 32 -73 -96 -64 -83 88 -79 52 -100 15 -119 -79 -80 -78 113 -28 79 127 -59 10 -3 -20 -43 7 101 15 -44 88 88 -39 -64 -3 76 87 -26 54 -86 23 2 -56 -8 -49 -60 -19 85 45 -50 -125 88 34 3 49 22 88 -39 41 -71 11 74 76 45 12 0 103 -112 -63 -73 52 26 57 11 43 27 80 -108 -34 -92 -93 -70 33 0 46 116 -19 -8 -113 91 -82 100 -11 18 46 77 -79 40 -68 100 44 42 -90 116 29 38 -125 99 106 -12 -59 82 18 -44 7 1 -40 -101 -90 43 112 -104 45 -108 -94 74 -21 109 -80 -2 81 76 -13 -62 -19 87 -17 -6 -56 100 58 -113 -67 -33 -38 -33 -86 15 2 -64 4 42 27 55 -105 3 36 34 25 3 48 1 -118 -91 -31 -48 10 67 -108 6 10 -44 21 27 -88 15 2 64 100 12 115 -50 -100 -46 -28 8 -30 110 106 -111 59 -26 111 -87 125 -114 -114 122 34 -128 97 -81 73 -59 24 103 -8 -128 0 -59 87 -4 7 -67 77 -17 -73 -40 80 7 4 96 -115 -63 -100 -105 40 -111 38 -4 72 -33 61 -99 109 99 81 -32 91 -105 79 -94 14 8 -64 70 -117 -34 -112 -103 -33 43 -32 -109 57 -15 -113 120 -124 -92 -45 -55 22 100 -121 -62 117 53 -108 58 32 0 -53 93 -17 22 97 -40 -98 33 119 -37 -64 -91 -87 41 25 -48 -2 12 -79 -71 -2 -112 15 -122 95 -54 -26 30 114 -44 1 1 -72 49 106 89 -59 -113 -127 -45 -48 -63 91 -119 127 -57 44 -86 -75 83 -8 -99 33 62 -118 67 -1 -70 -74 82 -84 3 2 -80 32 96 -75 -123 -58 -73 -80 7 98 -26 -43 -35 -89 -53 26 57 -40 -4 -41 -75 -116 -23 -14 96 55 -24 31 -19 73 46 -128 -38 34 96 36 18 -68 -10 -22 -114 78 56 87 5 -2 -86 -55 -31 -80 -106 -111 96 110 -68 15 -70 75 50 -99 -105 -52 102 -95 112 -118 -116 32 -92 3 -107 -47 -40 -25 -16 86 -93 112 54 -94 -106 87 48 106 -120 -128 -121 -41 7 -26 -58 -5 38 -121 -61 -28 94 -109 -92 -41 44 42 -90 96 -39 23 69 46 -32 22 6 -19 15 -101 20 -112 -51 31 119 38 122 -14 18 22 -94 -38 -22 51 18 -105 7 -69 -79 3 110 116 118 89 111 88 -26 -115 79 78 29 87 60 -23 -71 -54 8 7 -36 100 -61 -57 -119 -76 -28 -104 9 -46 4 17 -53 105 -16 123 -123 107 -61 -31 -60 -83 -13 -8 -32 1 -7 18 73 -115 22 45 68 8 16 66 46 7 55 55 -34 119 -17 74 68 -79 -37 65 114 60 94 -99 48 58 -69 -84 75 -5 -121 -114 -70 62 57 117 -68 -7 116 71 -37 -23 -114 -74 -52 78 73 124 -102 -3 -25 79 -49 54 115 69 -19 69 -104 8 -55 -12 29 -1 87 50 102 6 62 -5 -26 -34 -107 8 -28 90 97 101 2 -117 -121 -56 18 36 49 22 12 -19 83 10 80 -27 -9 -82 68 -64 -103 10 39 101 41 -102 -77 -108 -49 41 -94 -35 -55 -97 126 -69 -19 116 71 27 -33 98 67 56 34 -26 -74 115 -17 119 122 -33 -17 -12 2 19 98 42 23 -33 -38 -42 82 -100 89 -128 12 53 44 32 -55 -86 121 60 102 66 -69 38 -125 -76 18 115 -123 -66 -26 -7 -52 1 103 90 20 69 84 76 5 62 -5 -26 -14 96 55 108 -90 9 9 0 -110 103 -28 -121 -11 -87 1 31 43 -17 -74 -65 -46 -44 94 57 83 -98 68 113 119 79 124 -102 -115 63 -53 87 -19 -88 115 -16 3 -69 28 28 121 -64 2 -124 -50 21 15 121 -121 121 22 -87 -93 20 79 -49 51 5 -112 123 33 -39 -12 -67 -20 -25 -32 -24 114 -112 59 -76 119 57 84 9 32 -79 -103 43 -118 -87 -20 -6 86 -66 -54 -35 2 31 69 -50 -68 -22 -40 18 4 61 -83 33 -97 -77 -45 -45 -38 -18 -28 -53 62 -84 41 40 -33 -18 -28 -37 -99 60 -22 66 8 -95 -11 -83 124 -4 -39 -10 -6 86 126 51 -73 83 -23 -98 65 -58 97 42 -6 33 -125 -32 91 108 -19 78 123 -89 71 8 -74 -75 118 122 -12 77 -33 116 103 69 116 122 -124 78 -113 0 100 108 -26 -118 -21 91 -37 -101 -65 20 -97 -28 118 42 49 122 -109 -89 -54 -104 94 -72 65 -76 59 -7 99 78 123 -80 77 56 -26 -76 107 105 -23 106 48 -108 -106 -78 -33 51 14 0 -35 34 83 44 61 -55 21 77 -23 31 -17 -108 -13 -37 84 13 -48 -58 -113 57 121 55 -49 65 99 55 -85 100 51 -13 -126 -10 59 -57 1 -118 -69 123 -5 76 -68 -40 91 -33 -54 23 119 95 -24 -19 37 -96 -126 -86 -81 127 -38 -99 60 -33 -46 -36 -23 17 -8 -26 125 -71 -85 13 -95 -58 81 -63 -60 44 -66 -59 -10 -110 -110 -82 -3 31 -127 -107 -30 -18 -117 -51 95 -118 8 -95 -11 -83 60 66 72 -115 27 -71 51 -39 68 -72 -19 -100 -37 -2 38 66 8 106 -40 126 -104 -25 91 -102 -113 -40 57 -119 -103 88 105 84 59 51 14 88 65 8 -19 79 -65 -69 94 -71 11 -12 -64 -75 112 -72 5 46 90 109 -51 31 -100 56 -118 14 -40 -46 2 -119 -118 -128 -122 12 -41 -43 23 49 29 -75 -107 -102 -120 -23 65 8 117 7 -113 -64 -59 -31 -90 -26 15 -70 -114 34 36 101 -21 -11 64 109 17 32 -63 127 82 5 -124 -48 -49 25 107 -68 35 -43 65 -19 18 -80 22 127 -66 22 127 110 117 45 42 -114 26 114 71 -1 54 -47 32 -64 98 52 8 -80 24 13 2 44 70 -125 0 -117 -47 32 -64 98 52 8 -80 24 13 2 44 70 -125 0 -117 -47 32 -64 98 52 8 -80 24 -1 7 100 -91 -99 93 56 127 126 94 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 0 -128 0 0 0 -128 0 0 0 0 0 0 0 1 0 0 0 1 -119 80 78 71 13 10 26 10 0 0 0 13 73 72 68 82 0 0 1 0 0 0 1 0 8 2 0 0 0 -45 16 63 49 0 0 0 3 115 66 73 84 8 8 8 -37 -31 79 -32 0 0 0 9 112 72 89 115 0 0 14 -60 0 0 14 -60 1 -107 43 14 27 0 0 32 0 73 68 65 84 120 -100 -19 -99 95 108 27 71 126 -57 -57 39 -101 57 -118 -108 73 83 10 65 89 -119 66 86 68 19 8 60 -124 46 96 -21 -118 -6 106 -102 47 117 31 100 43 -128 31 116 119 15 -106 96 32 47 5 108 -23 -87 48 106 64 82 97 32 -24 67 79 127 -34 -50 -128 78 50 -118 28 84 32 -88 -107 8 5 28 28 64 -53 -128 30 78 10 10 -45 8 33 -32 -82 20 -88 83 32 -101 -43 -55 52 105 -109 98 66 -57 109 31 -58 -38 -84 103 -106 -53 -35 -39 -39 -99 37 -9 -9 121 -94 105 114 57 -38 -3 125 103 126 -13 -101 -33 -4 -26 -56 -81 126 -13 8 1 -128 83 -7 -111 -24 6 0 -128 72 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 6 4 0 56 26 16 0 -32 104 64 0 -128 -93 1 1 0 -114 -26 -88 -24 6 52 55 -43 -105 -81 30 -105 -86 111 -66 -13 -3 -18 -13 106 -67 -49 -41 -5 22 66 -88 -81 -53 -37 -16 -25 -94 -99 29 12 -33 2 84 0 1 -112 -56 -83 51 -5 -12 5 126 -79 91 -86 126 -5 -14 -43 -31 -21 -125 -22 -31 107 -114 100 -9 95 52 -4 -52 -105 -24 -119 -54 -1 6 -38 93 -127 -10 -73 -16 -21 19 -19 -82 64 -69 11 -65 -106 100 3 106 -95 113 -94 0 10 7 -75 103 7 53 116 104 -33 -110 113 107 49 65 59 83 56 -88 21 14 106 -12 -5 -76 108 -94 93 29 72 38 18 -84 -112 -109 62 -73 -5 88 -101 -7 -51 -76 23 -83 44 0 108 -39 -69 -91 -125 -22 -9 -81 126 120 109 66 -25 -35 116 16 82 -105 43 4 15 35 63 62 -42 -42 -29 115 -69 -113 -74 -11 -8 -38 -15 107 -53 -37 104 17 45 34 0 108 -33 -39 -89 47 112 -17 94 56 -8 78 -79 47 4 26 34 13 35 -103 39 69 -7 -5 88 24 120 -108 -120 118 118 -76 -116 42 -102 82 0 91 -5 -27 -62 -63 119 -123 106 -19 -11 -117 -106 -74 -11 -79 -63 -2 75 3 -67 8 -95 116 -82 48 -75 -108 46 86 -60 -4 -79 88 24 120 -24 -112 70 12 -84 -118 -66 46 111 -64 -3 -6 -123 -112 -74 25 -95 9 4 -80 91 -86 62 46 29 56 -60 -36 105 -118 -107 90 34 22 66 8 37 98 -95 -111 100 116 124 126 99 49 -107 21 -35 -88 -41 -56 85 -127 -111 36 -47 115 -36 125 -94 -3 45 -5 -113 18 71 108 120 68 -46 -42 126 121 -73 116 -80 -5 -68 -6 -20 -51 -101 -21 88 -30 -111 -64 -3 91 23 -4 -98 -41 81 -99 -43 76 126 124 126 35 -99 43 -120 109 -107 70 -94 93 29 39 -38 93 61 -57 -35 61 -66 118 27 14 17 -74 16 -64 110 -87 -70 -75 -1 98 -9 121 -11 113 -23 96 -105 10 -112 3 8 33 -65 -57 117 -1 -42 -123 120 36 32 -67 51 -75 -108 -98 89 -39 20 -27 17 49 -45 -29 115 -97 -12 -75 -9 28 119 -9 117 117 -40 97 124 16 35 -128 -22 -53 87 -40 -30 -73 -10 -53 -48 -57 107 -60 -17 113 77 95 61 51 -110 -116 74 -17 108 -17 -107 -57 -25 55 -106 -41 119 4 -74 -54 32 -47 -82 14 -20 47 -11 117 117 8 9 -62 90 39 -128 -62 65 109 107 -1 69 -10 105 121 107 -1 -123 -45 -4 120 -114 76 95 61 51 54 -40 47 127 103 53 -109 31 -99 91 -37 -34 43 -117 106 18 47 2 -19 -82 -66 -82 -114 104 -89 -73 -81 -85 67 90 -59 51 27 115 5 80 56 -88 101 -98 20 -79 -47 67 0 -98 23 11 -41 -50 -54 -57 1 -52 -44 82 122 114 41 45 -92 61 102 -32 62 -42 38 -119 -63 84 79 -119 -65 0 -96 -89 -73 0 69 13 108 -17 -107 71 -25 -42 86 51 121 33 77 50 15 83 71 6 110 2 -112 122 122 -104 -59 90 -61 -35 27 -55 -95 -127 94 -6 -3 -27 -11 -99 -15 -7 -115 22 -16 -120 20 9 -76 -69 98 -35 -2 104 -89 55 -42 -19 -25 114 65 67 2 -112 60 28 98 -43 16 -80 0 58 46 36 81 -84 -44 102 87 54 13 122 68 -31 -96 55 30 9 -60 35 -127 115 -79 16 126 39 -99 43 -116 -49 111 24 -71 38 95 36 37 24 25 22 88 4 -80 91 -86 126 -11 -51 -45 -52 -109 34 120 56 98 81 -47 0 58 -76 87 -67 30 -111 -33 -29 26 73 70 -81 36 -93 -118 -105 61 50 -76 -56 -48 78 -77 -63 -61 -62 79 66 126 -122 117 6 29 2 -56 60 41 126 -99 47 101 -98 20 97 58 107 31 -44 53 -128 16 -102 89 -39 -44 -104 64 17 14 122 39 -122 -29 -12 -44 66 -62 -2 -13 108 -9 -79 -74 88 -73 -1 39 33 -97 118 7 -87 -79 0 -64 -18 109 14 -79 78 76 -45 112 114 -100 -120 -123 38 -122 -29 -119 67 87 71 -111 -59 84 118 116 110 -51 80 67 45 68 82 66 -61 -27 -123 -70 2 0 -69 111 34 26 106 0 33 -76 -104 -54 -114 -49 111 16 67 -63 72 50 58 49 28 15 7 27 120 14 -51 101 -3 4 -89 123 59 85 -58 4 82 0 96 -9 77 74 34 22 -70 127 -21 -126 -6 103 -118 -107 26 -50 -91 -13 123 92 99 -125 -3 87 -110 -47 -122 -90 95 -84 -44 70 -25 -42 -102 122 -79 25 83 -49 59 122 45 0 -104 -41 -74 0 -71 -37 -105 27 26 52 66 40 -99 43 -124 -125 94 -11 -31 2 -93 56 104 52 59 120 -58 124 -6 -35 78 -68 -66 118 100 -24 -97 126 -9 -43 55 79 33 120 -33 2 -116 36 -93 11 -41 -50 114 -71 -44 98 42 59 -75 -108 110 -43 -59 4 76 -113 -49 125 -6 -35 -50 35 -24 -46 -126 -24 -106 0 -36 -48 56 8 -44 -93 88 -87 45 -90 -78 -77 43 -101 -83 109 -6 114 -102 96 67 12 -96 -99 59 -87 -20 -60 112 -100 -31 -117 -37 123 -27 -39 -107 -51 -59 84 -74 -59 28 -98 -122 -64 8 -48 82 -8 61 -82 -36 -19 -53 90 -4 123 -119 116 -82 -128 77 -33 -68 86 -39 25 24 1 90 10 -65 -57 -75 -67 87 86 89 23 -109 -77 -102 -55 79 45 -91 91 47 121 78 23 32 -128 22 65 -53 98 22 -63 -7 -101 -9 -52 107 79 -77 0 2 104 122 70 -110 -47 -21 -125 -3 26 123 125 9 -25 76 115 -43 1 1 -120 -57 -17 113 13 13 -12 46 -81 -17 -24 -102 -128 106 95 -52 82 4 4 -128 1 1 8 38 28 -12 62 -100 -66 -24 -9 -72 -90 43 -75 -39 -107 77 45 -5 -36 -61 65 -17 -11 -63 -2 -111 100 84 -41 100 -105 -32 -127 -77 93 127 9 40 -113 46 -104 -19 -67 50 78 52 -16 123 92 19 -61 -15 -36 -19 -53 -109 -11 -29 -104 126 -113 107 -31 -38 -39 -36 -19 -53 99 -125 -3 70 -84 31 33 -28 -76 112 103 61 64 0 -30 25 -99 91 -109 -94 -112 -110 12 -24 -76 -28 -55 58 -17 -45 44 -90 -78 -89 -58 -65 80 119 114 -102 -91 -84 -112 -39 -64 58 -128 93 -72 127 -21 2 17 -61 -39 -34 43 79 45 -91 23 83 -39 112 -48 123 -9 70 -78 -31 52 -105 88 -57 85 -49 -116 56 -15 -53 -33 -62 32 -128 64 0 -10 -95 -34 -42 -106 -19 -67 114 -61 105 -18 -10 94 -7 78 42 75 -49 31 -98 125 -6 -117 122 -98 -110 61 -9 118 89 15 -72 64 118 -95 88 -87 -99 -65 121 -113 -10 76 -44 -83 63 -99 43 -116 -50 -83 69 62 -2 108 82 105 -37 -41 -20 -54 102 -67 111 25 105 106 43 1 2 -80 17 56 -7 94 -93 103 -78 -68 -66 115 -2 -26 -67 83 -29 95 -88 100 49 -52 -128 0 26 1 97 80 123 -111 -50 21 -50 -33 -68 -89 -78 -67 107 53 -109 -1 124 125 71 99 -42 26 -98 21 -48 -13 -26 63 -63 34 -64 33 32 -128 -26 -128 -71 12 -24 29 37 1 56 60 -1 71 14 -72 64 54 34 28 -12 78 14 -57 -81 36 -93 -76 -17 62 -69 -78 -55 -74 47 81 113 -96 -128 101 96 9 24 1 108 -63 -48 64 -17 -107 100 -76 88 -87 73 -5 -80 -82 -65 -71 -44 -59 -36 103 -45 -18 126 -79 82 3 1 72 -128 0 68 -126 -109 26 18 -79 16 46 98 37 -73 -53 116 -82 32 45 11 20 43 53 -114 -45 86 -104 1 -53 1 1 -120 65 -86 -66 54 -69 -78 121 -2 -26 61 -38 81 -111 -65 99 -48 101 95 -51 -28 -27 75 108 32 0 57 32 0 75 -119 71 2 87 -110 81 60 43 -99 93 -39 -4 -24 -109 84 -67 96 -50 -93 92 65 -86 125 -53 55 113 13 66 64 114 64 0 86 -128 19 -98 113 -42 126 81 91 -42 39 -57 17 -128 -16 -8 97 4 -112 3 2 48 -105 120 36 112 125 -80 127 104 -96 -41 -17 113 -31 57 -82 -58 -125 -67 36 51 53 62 1 32 -70 124 -120 -127 -54 1 1 -104 2 -82 -79 124 125 -80 31 39 50 -24 50 125 2 -29 -10 42 -1 81 -120 -1 16 -128 0 56 -109 -120 -123 36 47 31 29 -106 -22 103 48 125 -55 -18 31 25 -10 88 -28 3 8 8 -128 0 4 -64 -121 112 -48 -117 3 59 82 -18 26 -77 -23 -53 41 86 106 124 -21 114 -62 70 48 2 16 -128 81 -16 26 -106 -4 -76 34 46 -90 -113 16 58 53 -2 5 -105 9 -85 -4 34 48 3 38 0 1 48 66 119 -7 -120 -97 -23 99 120 25 43 -52 1 84 0 1 -24 6 -37 61 -79 123 -117 -81 -23 -101 7 -116 0 4 32 0 -83 -44 -85 -59 -48 68 85 53 -63 -6 105 64 0 13 -112 -81 97 17 -1 37 -19 -39 21 -46 48 -19 72 78 26 -8 63 52 32 -128 -70 -56 -41 -80 -120 -1 106 22 -45 -57 72 2 48 30 81 109 61 64 0 36 -22 -25 -124 54 -105 -23 19 -76 -64 73 71 -36 1 1 -4 0 -79 -122 69 -48 -44 -90 -113 79 7 -125 57 0 13 -108 69 65 -31 -96 23 123 -7 -11 -22 47 52 -75 -23 35 -124 -80 11 103 -1 57 -70 16 28 61 2 -48 107 88 4 -51 110 -6 24 48 125 21 -100 40 0 -59 53 44 -126 -42 48 125 -96 33 -50 18 -64 72 50 122 105 -96 87 -91 -53 71 96 -6 14 -61 17 2 -48 88 79 28 76 -33 -127 -40 78 0 -31 -96 -41 -56 65 -97 -12 -43 -24 -76 5 26 102 -45 -113 71 2 6 -53 -108 43 98 -73 61 43 124 31 10 -33 61 -2 6 -79 -99 0 70 -110 81 -74 -125 62 -39 48 120 80 -36 -12 -43 51 -70 -114 -27 -46 -59 -10 94 121 123 -81 -4 32 -109 79 -25 10 -23 92 65 -32 58 -82 -106 -38 -44 -38 73 -25 10 -89 -58 -65 -32 117 53 -125 -40 78 0 31 -14 -69 -47 13 89 -51 -28 13 70 -57 -51 -77 126 116 -40 -17 74 63 -127 -113 -46 -72 -109 -54 90 -36 125 -58 35 1 -114 -42 -113 47 -56 -15 106 6 -79 93 101 56 -114 67 109 67 18 -79 -48 -61 -23 -117 15 -89 47 106 57 117 -126 -58 -30 7 25 14 122 -57 6 -5 -115 52 -104 -115 -21 -125 -3 -36 -81 105 -122 -33 -56 -122 -19 4 96 125 -9 16 -113 4 22 -82 -99 125 56 125 81 111 119 46 -86 39 -61 13 -50 -35 -66 108 -22 -8 -125 -63 33 99 -18 -105 -75 -49 32 96 47 1 8 -68 47 -15 72 -32 -2 -83 11 -45 87 -49 104 -1 -118 -107 -125 -107 -30 -81 -21 109 48 3 102 116 -1 72 -12 -83 -109 99 47 1 8 -65 47 -40 -57 -48 56 64 -97 51 -65 3 110 -120 -82 6 -21 5 -25 5 -102 113 101 -31 15 90 -62 94 2 -80 -61 -56 -120 -121 2 45 38 101 -121 -42 34 61 13 -42 -117 -15 -77 40 -21 -15 30 8 64 17 59 -12 -87 -24 -48 -92 -44 63 19 14 122 -19 51 -109 -61 -77 2 -18 -105 53 -55 -1 65 48 2 -44 -61 62 -9 37 30 9 -88 -69 -41 -10 105 42 102 104 -96 119 -116 -85 -67 26 60 -120 91 29 -5 -36 61 16 64 93 -58 6 -5 85 -62 44 22 68 96 -12 50 49 28 -25 104 -78 -90 46 71 -38 -25 65 -37 69 0 126 -113 75 -27 -124 116 81 -88 24 -127 -107 11 118 26 -15 123 92 -68 6 -127 -95 -127 94 -77 109 -44 38 51 40 -15 2 72 -60 66 56 -86 109 101 6 -124 70 18 -79 80 -67 -98 -34 62 125 -104 -100 43 -100 -126 54 -26 121 -1 18 54 -103 65 9 75 -123 32 -54 -57 -38 -106 43 -55 -88 98 -90 -112 77 58 48 -126 112 -48 27 -113 4 12 -26 74 -88 -56 -98 35 -15 72 -64 14 57 127 2 4 -48 112 31 -106 94 -24 -5 -56 -15 -7 13 13 -12 -114 82 111 50 95 31 -25 -73 17 111 -14 -51 -75 -60 7 46 25 -71 2 -61 48 -110 -50 21 -12 -10 8 -114 27 1 -76 -20 -61 98 0 31 -84 75 -65 31 -113 4 -16 78 95 -125 55 -38 -17 113 -47 125 42 -13 -97 80 -17 -88 83 -65 -57 -107 -120 -123 -82 -85 78 -69 53 98 112 114 -62 -112 -5 -128 119 -36 55 12 28 19 -40 36 -28 109 -123 0 -76 -20 -61 98 -90 94 -110 48 78 33 -98 89 -39 28 27 -20 55 56 -69 -96 -5 84 102 35 -85 -41 90 92 5 122 121 125 103 104 -96 119 -31 -38 89 35 -94 53 -40 -65 48 -36 43 -6 80 87 45 -76 -2 8 -96 113 31 -106 65 -44 -117 61 21 43 -75 -55 -91 -12 -10 94 -39 -56 58 17 -35 126 -26 9 64 67 -25 100 121 125 39 -68 -108 54 59 -61 -89 30 108 -71 15 -117 -87 44 -61 94 5 -101 76 -94 -8 11 0 -41 18 -44 -78 15 -117 11 90 38 82 -117 -87 108 56 -24 101 30 7 -24 -63 -102 -19 -31 105 116 -51 103 86 54 69 -59 6 24 -94 -88 -53 -21 59 -52 59 117 -62 65 -81 -16 106 -115 60 -61 -96 82 -102 -18 -62 -75 -77 -106 -83 19 105 -68 -125 28 -21 54 -5 61 46 -74 49 77 -5 -61 22 82 -62 -51 -17 113 49 68 63 37 -1 -121 97 -26 109 -121 0 32 -121 17 64 -91 124 -84 -39 104 63 -12 28 59 -39 92 114 27 -103 -1 76 -19 -91 57 75 34 42 -7 48 56 -85 -37 123 101 105 4 102 -24 95 -102 94 0 -22 -75 4 45 64 87 -81 -61 -85 52 44 -13 -32 102 -121 -80 -73 10 70 -70 127 -28 40 1 -16 93 -61 90 76 101 63 95 -33 -71 123 35 -55 -16 93 93 2 -32 -75 -107 -106 57 -107 87 -69 11 100 36 91 -104 -19 20 -80 17 -3 -31 -23 98 -91 38 -81 -93 33 63 -39 91 35 118 72 39 -47 39 0 -66 107 88 -117 -87 -20 -44 82 122 123 -81 -52 124 65 93 -121 -98 -13 -102 -106 48 -53 94 -69 0 -116 52 -107 77 -25 12 17 -126 -27 -11 29 -125 -45 42 59 68 66 53 9 -128 -5 26 -106 100 -6 -8 -97 -26 69 21 -27 48 -9 55 68 -97 -54 102 -99 -38 -3 -97 68 44 100 -28 62 51 56 90 108 -65 72 -124 -1 87 51 -7 9 -3 -65 -85 -9 71 -71 -45 64 0 -36 -41 -80 8 -45 -57 48 -101 -90 -10 -121 -115 103 -22 108 -65 34 -17 -25 -52 -42 -86 -33 -29 50 -78 8 -64 118 82 19 67 -9 -65 -102 -55 115 113 41 -3 30 -105 -40 -38 -67 -54 2 48 99 13 75 -47 -12 49 108 86 -91 43 -124 108 100 33 76 -2 -92 -103 -5 102 45 -34 -102 -33 -29 90 -72 118 -42 72 48 -19 -114 -2 -30 118 108 -87 111 -12 15 -79 -23 65 120 74 -36 27 2 48 105 13 75 -59 -12 49 108 86 -91 93 0 35 -58 -26 45 -14 39 100 -34 8 -128 75 -30 25 113 126 22 83 89 6 99 98 72 125 35 -90 -65 -46 -101 122 -81 -125 108 16 8 122 45 0 -107 -13 -80 -116 -48 -48 -12 -111 1 71 80 99 -72 99 108 -80 -33 -120 83 -63 43 11 -120 22 0 -2 -61 -29 -111 -64 -121 -111 -128 -15 59 -65 -67 87 30 -97 -33 -48 -5 45 -74 -78 63 -11 -110 127 -118 -107 -102 -34 -65 66 -68 0 112 64 -109 -5 26 -106 22 -45 -57 48 -33 -126 -122 125 106 34 22 -102 24 -114 27 28 -51 -120 -79 -98 -7 70 61 -5 -12 23 70 -102 -95 78 -79 82 -5 -24 -109 -108 53 -34 63 66 -88 94 21 -31 116 -82 -96 -9 110 11 -113 -124 30 -27 94 77 64 -69 -23 99 -72 71 21 19 -79 80 60 18 -88 119 -54 -99 94 -120 -84 4 -31 61 22 77 -79 82 59 127 -13 30 -125 11 -50 -106 -6 102 36 -7 71 -79 13 -68 46 -59 6 -49 100 56 -67 -90 -113 97 -50 11 127 56 125 -111 -19 -117 -38 33 -14 28 -19 16 -74 35 72 -25 10 -93 115 107 108 19 80 -74 13 -60 42 -55 -49 15 50 -7 102 41 47 41 -63 71 0 108 -90 -113 17 126 11 84 32 -4 31 -69 117 -1 51 43 -101 83 75 105 -74 -39 39 91 -22 -101 60 -7 -121 11 77 63 2 24 49 125 100 32 -77 -46 2 -24 -96 -118 125 4 96 -16 -74 35 -42 -78 63 -22 123 95 -40 6 -94 68 44 36 48 18 -54 46 0 -29 -49 0 -39 -72 -5 -57 -37 -4 -120 55 -123 -17 -30 -61 71 4 -52 -82 108 26 -9 -62 25 -70 127 -59 -24 39 -15 1 -122 -106 -120 -19 1 89 4 -64 -59 -12 49 -74 21 -128 98 80 69 84 107 -45 -71 -62 106 38 -49 -15 104 12 -122 -44 55 -116 122 -50 34 -101 41 -57 35 1 -127 71 -40 -21 19 0 71 -45 -57 8 -113 -126 41 50 58 -73 70 15 -54 66 -68 53 35 115 92 21 -40 -94 -97 120 -25 62 -33 -106 32 -47 -123 114 -75 10 -128 -69 -23 99 -20 -29 85 75 -116 -50 -83 41 14 -12 66 -70 -1 120 36 -16 112 -6 34 -18 -2 121 29 95 105 48 -39 -114 59 98 27 -45 88 0 38 -103 62 -58 110 -127 -59 122 -42 -113 -124 122 107 56 93 103 98 56 94 -81 -86 -118 46 -20 86 -127 79 -84 27 -84 38 0 83 77 31 -119 -106 62 65 67 103 67 -72 -73 22 14 122 -17 -34 72 -82 102 -14 -93 115 107 -52 15 -59 -102 -86 111 -70 -80 -29 36 -40 108 -45 -57 -40 100 6 92 -84 -44 102 87 54 39 -105 -46 -22 31 99 -106 -21 20 117 101 -97 -57 -123 -113 94 100 120 -10 -8 96 -65 -47 -71 53 -74 -95 -128 87 -15 80 -66 24 47 -25 -56 12 41 0 107 76 31 35 92 0 120 -89 -68 -58 -65 -105 -83 -29 76 -25 10 42 -46 -62 -59 4 -12 94 -39 -17 113 -35 -67 -111 84 -15 -42 -22 97 -46 -119 119 -58 17 56 8 -4 32 0 43 77 31 35 -48 -87 72 -25 10 120 90 -87 49 116 109 82 -58 30 -82 6 55 -110 -116 50 100 100 -31 -81 -24 -46 -128 -35 -68 127 9 -127 107 97 71 -111 8 -45 -57 88 60 7 40 86 106 -85 -103 -4 -125 76 -98 33 -99 -117 121 -80 -46 -78 15 6 27 49 -101 6 -16 32 -90 -27 -61 -26 -99 120 103 28 -97 -64 17 32 -14 -15 103 -94 -86 115 -103 -25 2 73 69 -104 -45 -71 66 -87 82 91 -51 -28 21 -53 50 107 -121 -71 -87 26 59 -74 -59 84 -10 92 44 -60 96 -96 11 -41 -50 -82 126 -4 -103 -106 113 -116 -17 1 74 124 17 -24 12 31 21 101 -3 -52 -79 -120 -87 -91 116 -61 9 43 119 -72 87 -61 -91 -103 93 -39 100 16 0 62 21 -90 -31 13 97 75 125 -77 12 -127 -15 64 97 39 -60 -104 -73 15 -58 12 -40 90 -85 -67 112 29 66 40 -99 43 -80 -27 -46 104 -79 108 -77 75 20 27 68 -96 0 -124 -99 16 -45 92 2 48 -75 26 -82 -4 -13 12 3 35 -34 -55 -83 62 19 96 -21 -2 -45 -71 -62 -25 -6 -125 -83 108 83 109 81 -111 80 97 2 96 -50 -84 -76 -34 103 99 -10 -42 44 123 -94 -25 98 33 21 1 48 -89 -66 -115 -49 111 -80 -19 -78 103 -8 57 81 3 -108 48 23 -120 -83 79 21 18 44 99 30 -84 120 85 35 109 -120 -6 -51 100 -21 -110 -103 -9 -66 52 -41 -66 40 49 2 96 -50 -84 108 -94 9 0 -46 111 10 102 24 1 115 -22 27 -67 -128 -83 -111 -26 -38 21 32 70 0 -90 -122 -43 -71 -61 -20 -83 -23 -22 65 -61 65 -81 25 70 -64 -42 -3 107 95 94 -96 97 27 -9 68 109 54 106 50 1 52 -47 12 88 111 -9 111 70 -104 -110 57 -11 -115 -83 -60 -94 17 -100 53 2 48 -17 -127 -80 94 0 -42 120 107 -15 72 -64 -116 -123 42 -26 -44 55 -74 115 -17 48 108 51 7 103 -51 1 -104 -5 84 -21 11 -87 90 112 30 76 60 18 -48 123 -58 -88 22 -104 83 -33 -8 86 -2 -47 -114 -112 -43 0 49 2 96 27 -105 -123 60 21 -77 -67 -75 -79 -63 -2 -5 -73 46 24 116 0 20 127 -117 57 -11 -51 72 -9 -113 12 60 38 33 2 16 -80 14 -64 -4 119 -78 -99 125 98 16 -114 -59 64 37 -16 -26 -38 115 -79 -48 -48 64 47 -105 -89 78 -113 54 -52 -87 111 -58 43 -1 48 11 64 72 -91 104 1 2 104 -82 25 48 -77 -127 -42 -53 -18 52 99 67 22 109 55 -52 51 10 -26 -24 -89 28 -122 42 -71 72 -48 60 -72 -103 4 32 -60 5 98 -74 87 43 15 -118 37 -18 12 115 -22 91 -61 -54 63 26 97 -53 -23 16 18 9 21 48 7 48 -61 -87 48 9 -31 123 -42 -76 64 -97 85 49 54 -40 -49 -42 -101 26 -12 -2 13 -30 -108 73 -80 19 -110 32 44 -93 88 -87 -51 -68 105 -75 70 50 -97 121 85 94 97 -21 -86 -100 34 0 -74 -65 -77 -119 -106 -64 -84 100 118 101 -109 8 13 51 103 62 19 -91 -80 -115 -64 124 -48 -73 -11 55 -36 106 1 48 123 -58 -106 37 -106 -55 17 94 12 84 -99 116 -82 48 67 57 45 -52 -35 -65 88 -1 7 99 -3 32 96 -75 0 -102 107 6 108 -25 17 -96 88 -87 -115 -50 -83 -47 -35 63 -101 13 -15 58 -11 81 -70 26 -37 23 91 127 4 -80 -32 68 84 94 -40 -71 116 59 66 104 124 126 -125 54 89 81 -117 95 -68 -80 -66 78 -88 -43 97 80 -104 0 24 7 -105 110 -89 39 -84 -52 -35 63 -82 -70 -50 -93 105 63 92 -112 -19 -117 -42 -69 64 86 11 -128 -71 -68 20 -9 -106 52 -60 110 37 4 49 -37 123 -27 -113 62 73 -15 -51 125 -32 -78 -8 37 -57 -56 98 48 -33 -106 52 -60 82 1 52 -41 54 0 -31 -59 64 105 84 -50 68 98 -18 -2 -115 -92 -2 115 -57 122 -97 -77 57 4 32 100 17 -64 86 46 80 -61 -30 101 -52 -35 -65 73 -87 -1 108 -39 16 -56 -14 42 113 -106 10 -64 -78 -67 -123 -58 9 7 -67 118 88 5 -45 88 -62 -47 72 -55 127 -109 -90 -65 108 -39 16 -56 -14 65 -64 82 1 -80 -123 -43 117 85 -41 -31 -123 -88 -18 31 39 -10 60 -56 -28 -15 -79 72 26 -5 102 -26 -18 31 -41 -52 99 -5 -82 73 88 124 98 -46 17 116 105 -63 -78 31 99 43 8 94 -84 -44 -84 -97 4 91 63 2 48 23 -58 66 6 -26 -21 6 43 70 -86 -64 -10 -84 -111 -103 77 82 -60 82 1 0 -128 -35 16 86 23 8 0 -20 0 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 13 8 0 112 52 -62 -54 -93 3 4 116 44 95 72 2 -120 -33 -29 -62 33 124 92 -80 31 47 -62 -80 45 80 72 -41 -111 47 8 24 -68 38 119 64 0 -90 48 41 91 -102 -35 -34 43 43 -18 -75 13 7 -67 67 3 -67 -25 98 -95 120 36 80 111 -47 13 31 -20 -9 -7 -6 14 -57 37 91 121 -37 -92 -77 -107 112 29 -95 43 -55 -88 -30 18 -72 -10 99 20 -29 -111 64 34 22 -70 52 -48 -37 112 109 110 123 -81 -116 15 -32 88 94 -33 17 40 6 88 8 -29 79 56 -24 -51 -35 -66 44 -3 115 53 -109 63 127 -13 -98 -4 3 -119 88 104 98 56 -82 119 -7 118 121 125 103 118 101 -45 -32 -80 -112 -120 -123 -92 50 -116 -23 92 -31 -44 -8 23 8 -95 -95 -127 -34 -23 -85 103 -44 87 -66 -117 -107 -38 -7 -101 -9 84 -106 -28 71 -110 -47 -21 -125 -3 108 41 36 -117 -87 -20 -99 84 86 -56 -120 7 35 0 127 8 35 -112 23 -76 99 51 125 -52 -48 64 -17 -48 64 -17 106 38 63 58 -73 -58 101 -57 9 -74 -26 -79 -63 -2 -23 -85 103 26 126 -47 -17 113 -35 -65 117 33 -94 116 34 -27 72 50 58 49 28 55 -110 57 50 -110 -116 -114 36 -93 -53 -21 59 -29 -13 27 22 -25 38 -127 0 -8 67 8 0 119 108 126 -113 107 98 56 110 -68 4 116 34 22 122 56 125 81 113 71 -104 22 -28 102 -6 32 -109 -97 28 -114 -45 -119 116 -110 -125 78 8 -107 62 -111 50 30 9 44 92 59 -85 -46 -21 -45 121 92 120 86 -96 -8 -31 -95 -127 -34 68 44 52 -75 -108 -90 119 -6 -101 7 8 -128 63 -60 78 -102 116 -82 16 14 122 -17 -34 72 -46 15 30 -17 69 -60 -71 -97 68 -49 -105 -120 -123 -30 -111 0 -82 31 74 124 -53 -17 113 45 92 59 123 46 22 26 -99 91 -45 -37 54 121 66 110 56 -24 -99 120 115 -82 50 -75 -108 -106 123 -28 -40 -30 -27 -97 -71 -110 -116 74 2 24 73 70 -89 -81 -98 81 -52 120 91 76 101 31 100 -14 42 -13 -106 120 36 112 37 25 -91 75 -93 -6 61 -82 -23 -85 103 62 -116 4 24 -2 52 54 96 14 -64 -97 -36 -19 -53 -46 115 77 -25 10 -93 115 107 116 -3 -25 -43 76 126 106 41 -83 -59 -21 -59 86 120 93 -87 -40 -37 98 42 -85 -41 80 -98 125 -6 11 -23 58 -14 61 43 42 -105 -70 123 35 41 23 -31 -111 -95 69 -124 -48 -62 -75 -77 116 -15 -35 98 -91 54 -69 -78 57 67 -107 42 82 33 17 11 77 95 61 67 119 13 -53 -21 59 31 125 -110 -46 120 17 35 -76 -95 15 -122 44 -8 25 71 49 35 115 -87 -13 -59 42 81 -88 16 111 -22 -43 24 84 65 8 125 -5 -14 -43 106 38 -1 -21 47 -1 -16 -63 59 -66 15 -34 -15 -55 -1 43 30 9 28 -47 19 45 -11 123 92 -14 16 -48 -113 93 109 -8 -59 -8 -4 -58 -115 127 -5 -81 122 -33 -6 -97 98 85 110 -21 15 50 -7 -119 -31 56 109 -3 83 75 -23 -97 -1 -21 -125 123 15 119 -65 125 -7 74 99 123 16 66 -37 123 -27 95 127 -7 -121 82 -91 -10 -45 -9 -33 -106 -38 -125 16 -6 -32 29 95 56 -24 101 56 -92 85 47 32 0 -50 36 98 33 -71 113 -124 78 -72 -27 -49 117 102 101 -13 -17 -1 -7 119 12 -13 -68 111 95 -66 -6 -9 -75 -36 -97 -10 -54 -124 71 -108 -120 -123 30 104 -114 -112 -2 -12 -3 -73 105 -61 93 76 101 85 -84 31 33 -76 -67 87 -106 -53 38 30 9 92 -8 -85 30 -30 3 -25 111 -34 91 90 -53 -23 50 125 57 -65 -1 -29 -97 -65 124 -72 59 -4 -77 -120 -4 94 -23 -107 55 27 32 0 -50 12 13 -12 18 -10 33 49 58 -73 -10 47 -1 -15 -75 -111 -117 -89 115 -123 71 -71 -62 -16 -49 34 -14 55 19 -79 -48 -99 84 86 -117 -15 -115 36 -93 -60 -68 22 15 71 13 -65 91 -86 -44 -42 -1 -8 -25 7 -103 60 61 -123 77 -25 10 127 -3 -113 -1 105 60 116 -109 47 86 105 13 36 98 -95 -49 -41 119 -14 -59 -86 -63 -117 -85 0 -87 16 -100 -87 87 -38 105 116 110 -115 75 -23 -39 -27 -11 29 -62 89 15 7 -67 26 -125 75 116 -37 -22 -43 -104 32 -104 89 -39 -100 92 74 47 -81 -17 16 115 -42 116 -82 112 -2 -26 61 94 -53 88 -118 87 -45 18 -94 53 2 8 -128 51 -118 49 62 -26 -88 -91 34 -117 -87 44 -79 107 86 113 -118 -36 -80 109 -11 -106 -88 -21 65 -60 124 -80 -25 -61 119 17 55 -99 43 16 69 -118 -104 15 -70 -44 8 8 -128 51 -118 1 13 -18 -127 109 -94 42 -88 -33 -29 -94 -93 -91 13 -37 -90 -85 30 22 -19 62 125 -12 73 -54 -116 20 -122 25 106 -75 -101 121 -53 -65 22 64 0 60 -95 15 -69 -58 37 108 -71 -1 16 14 56 -54 -33 -71 -44 72 0 -118 -54 -44 -2 -117 -124 21 78 45 -91 -51 -85 84 64 15 2 -26 21 40 0 1 -16 -124 126 78 -29 -13 27 38 101 122 17 -34 -53 -48 64 -81 -70 23 68 8 64 87 10 26 81 118 -114 62 -107 -125 47 116 -87 106 45 -29 27 27 32 0 -98 -48 49 22 -114 -82 63 1 -50 -90 -108 -65 -93 -98 -120 70 -120 83 87 -120 -99 56 112 -101 62 -107 -125 59 -60 -71 79 -26 29 -44 0 2 -32 9 17 102 -31 94 116 -106 -128 48 98 -11 -55 34 97 67 -38 -29 -21 -31 -96 -105 -72 -78 5 -71 58 68 -13 -52 -101 7 -125 0 120 34 -17 -125 45 40 58 75 -116 0 -22 -59 -11 -119 -74 105 -113 -36 19 -58 103 77 -6 62 -99 66 103 -46 15 -127 0 120 34 55 50 -19 -123 13 -103 33 -82 -81 50 83 36 102 -25 -70 -106 87 -119 -95 -61 -126 -12 4 -116 53 -125 0 8 -128 27 -124 11 110 -103 -95 104 -127 -48 -122 -82 3 -41 18 -84 -66 83 83 0 2 -32 6 -67 74 42 -86 37 52 -124 17 -21 106 27 17 -1 -79 108 -61 -118 53 63 4 2 -32 6 -99 36 35 -86 37 52 -12 22 5 -115 95 -76 -77 -86 -71 0 2 -32 -122 -36 87 -74 -58 80 -76 79 13 9 59 -42 -34 -71 10 60 36 -63 -102 -97 6 1 112 -125 112 21 44 -8 69 -19 99 14 49 59 103 -2 69 -127 35 -128 73 115 15 16 0 31 -4 30 -105 -11 -99 37 -31 -40 -44 59 -97 -35 -56 4 -128 -128 -7 8 120 6 -84 57 -93 4 4 -64 7 33 39 -54 104 -116 -49 16 -54 52 114 -30 -96 121 43 -78 4 70 -30 -74 -70 0 1 -16 -63 122 1 -48 71 -80 -44 -77 18 -26 25 48 18 113 58 27 -122 -29 -88 -91 14 8 -128 15 -60 42 -84 5 103 12 95 127 115 19 -116 74 31 -87 88 -90 69 35 -124 0 44 -45 57 -111 -36 -6 0 70 0 -101 67 91 -122 -87 -74 66 111 0 80 89 119 -109 -73 -124 -95 71 -105 127 -59 -102 -87 14 46 26 41 127 7 92 32 -69 67 119 -7 -90 14 2 99 -44 22 -80 122 105 -89 -124 51 -51 -32 75 88 -106 -105 38 65 -20 -36 55 -23 36 99 12 8 -128 3 -118 -99 -30 21 -86 -2 2 47 -4 30 23 -31 -1 -88 -104 -120 -111 36 8 12 -31 126 52 -36 121 99 -112 112 -48 75 -4 117 119 76 75 41 71 32 0 46 40 10 0 -41 73 54 -29 -25 22 -82 -99 37 -70 127 -107 -68 107 -29 -77 73 34 -89 -107 46 -25 -58 23 122 -25 -79 -87 -39 71 32 0 14 -44 51 116 51 54 -77 -114 36 -93 -124 127 -68 -104 -54 -86 120 -10 70 66 64 24 58 -81 -37 -68 77 -70 -72 0 -80 -4 29 -77 107 36 -126 0 56 -16 33 85 109 1 -65 72 -60 66 -58 -85 -31 -54 -119 71 2 68 -103 -112 98 -91 54 62 -65 -95 -14 21 -26 36 8 57 -60 -2 99 122 -125 60 23 112 -87 93 -7 59 -85 -103 -68 -39 -55 -89 32 0 53 -122 6 122 39 -121 -29 -109 -115 10 -102 -121 -21 111 4 83 44 124 -55 70 60 18 -96 107 -116 54 44 -20 -61 37 9 -126 54 68 -38 13 51 8 -3 -41 -103 84 79 -128 0 4 -96 76 60 18 -56 -35 -66 124 -9 70 114 98 56 62 49 28 -65 127 -21 66 -18 -10 -27 122 -90 76 24 -39 98 42 43 -9 52 -18 -33 -70 96 92 3 -118 -42 -65 -104 -54 -86 -17 78 -28 -72 -100 68 -116 51 -31 -96 -105 110 15 51 -118 127 -99 53 103 5 -128 0 20 -64 -49 -125 -24 -41 -21 61 114 -70 -38 20 122 -45 115 -59 71 75 -48 69 57 -75 51 54 -40 -1 112 -6 34 -15 -45 -23 92 65 -35 -7 65 92 -109 32 -24 -110 85 -118 86 -53 -64 72 50 74 95 103 102 101 -45 -68 122 2 114 126 -12 -13 83 -17 69 -69 58 44 -8 -91 38 98 98 56 -82 -8 92 113 -11 122 -30 77 66 0 56 -50 72 88 39 -82 -24 127 -9 70 82 111 -4 4 27 25 -3 -93 26 107 18 26 -97 1 -53 -103 92 74 19 70 -119 -57 73 -26 -102 37 -8 -40 4 -38 -101 90 76 101 27 106 -37 56 -47 -82 -114 -97 -97 122 -17 -24 -23 -34 -50 -45 -67 -99 -123 -125 -38 87 -33 60 -3 106 -25 105 -31 -64 22 103 -9 -119 69 -27 -119 -46 -109 -127 122 91 70 102 86 54 63 -116 4 -28 29 63 14 113 44 -90 -78 -77 43 -101 13 109 49 17 11 93 31 -20 87 108 -119 -10 -118 -100 70 -110 32 20 25 -97 -33 -120 71 2 -14 -53 -6 61 -82 -69 55 -110 -38 -113 59 -64 -32 -77 57 20 71 -59 -103 -107 77 83 -83 63 -48 -18 -6 -37 -65 8 -58 -70 -3 -127 118 23 66 -24 -56 -81 126 -13 72 -2 -33 -69 -91 42 86 66 -107 -75 -44 117 11 -16 127 -53 35 42 -1 -117 79 -120 -112 -72 127 -21 -126 92 21 39 126 -7 91 -71 105 42 -98 65 -124 14 -61 -37 -113 114 5 -70 -74 -49 -121 -111 -128 74 45 52 92 28 87 -29 -54 -88 -4 56 -116 -19 -67 114 -28 -29 -49 -76 124 75 29 60 12 42 -38 -82 116 -32 77 -67 -126 0 -72 -48 -25 -91 -127 94 -59 73 17 -114 104 -103 -28 -7 4 -38 93 -79 110 -1 -23 119 59 123 124 110 -7 -5 -28 17 73 61 62 119 -113 -17 -99 -95 -40 59 -103 39 -59 -81 -13 -91 -52 -109 -94 -109 -107 64 67 79 -53 -120 125 48 -60 -125 -97 92 74 -89 115 5 122 -108 15 7 -67 122 103 5 -59 74 77 -41 -7 89 -58 -109 32 -22 53 99 116 110 -19 81 -82 64 59 102 -72 78 -75 20 -7 -107 15 8 116 -18 42 -63 106 38 63 62 -65 -63 61 -21 -45 125 -84 45 -42 -19 -1 73 -56 23 -21 -10 43 126 -96 -18 25 97 -79 110 127 -84 -37 -113 78 -67 -25 64 37 44 -81 -17 -44 -13 -126 -120 81 -98 72 14 83 124 126 -53 -21 59 -85 31 127 86 -81 -41 -44 -34 36 -67 81 17 -59 -55 9 47 102 86 54 -105 -41 119 22 -82 -99 85 9 16 107 92 43 -64 103 -109 -15 -19 -8 27 -38 -67 68 -29 67 -14 36 37 108 -19 -105 -65 -50 23 51 79 -118 45 63 79 -104 90 74 39 98 33 -70 -57 -94 87 -99 52 110 74 -60 -67 -26 -44 82 122 98 56 -34 -80 -120 39 -127 -58 57 3 13 -9 9 0 1 46 -113 -98 -120 -123 -82 36 -93 108 -38 94 -51 -28 -17 -92 -78 28 77 -65 -98 -97 -93 2 57 7 -48 -62 110 -87 -102 -55 23 51 79 -118 -69 37 19 -113 -18 16 75 60 18 32 -126 54 -8 -72 59 -62 16 -119 67 118 -57 -25 55 -76 -72 40 -8 -128 120 124 14 -92 -30 7 -46 -71 2 62 69 -35 72 117 45 -62 -21 -112 14 63 53 3 -100 -98 -115 -99 -5 -122 7 110 -81 102 -14 15 50 -7 -27 -11 29 94 97 -2 30 -97 -5 -12 -69 -99 125 93 29 -38 -19 94 -126 69 0 18 -123 -125 -38 -42 -2 -117 -81 -13 -91 -83 -3 23 45 -23 32 -31 73 27 126 102 -118 125 48 113 88 -30 -7 -101 -9 -12 118 -76 -31 -96 87 110 49 -37 123 101 81 -101 -80 120 33 29 -93 36 87 32 -66 45 28 69 -120 -99 -100 104 -89 55 -42 -19 119 31 107 107 -4 -123 58 24 18 -128 -100 -83 -3 114 -10 -23 -117 -42 30 22 104 -120 16 16 17 32 2 -72 -45 -29 115 -57 -70 -3 -79 -112 -97 -95 -77 87 -124 -37 65 -39 125 93 -34 -66 46 -17 -33 -67 -33 93 125 -7 106 107 -1 69 -10 105 -39 9 -77 5 -71 -11 55 123 -49 109 91 122 124 -18 -66 -82 -114 104 -89 -73 -81 -85 -61 72 103 -81 8 -1 -109 -30 -15 -40 20 -21 -10 15 -59 -34 -63 62 82 -10 105 121 107 -1 69 -21 -119 -127 75 -94 37 -96 72 -96 -35 37 25 61 94 -79 50 9 -2 2 -112 19 104 119 5 122 59 79 -9 118 34 -124 10 7 -75 -57 -91 3 44 -122 -42 112 -109 -120 41 -84 121 27 -73 29 -126 -87 61 125 61 -52 21 -128 -100 64 -69 11 71 -87 -16 63 -15 -100 97 107 -65 -68 91 58 104 -46 9 -76 98 26 28 -96 29 -9 -79 54 28 -70 -119 118 118 -12 117 -119 -87 -63 104 -99 0 8 -16 -100 1 -67 -113 -48 97 52 105 -9 121 -11 113 -87 -102 -35 127 33 -86 73 122 -31 -101 106 -26 16 -94 93 29 39 125 -18 104 -89 -9 -92 -81 -35 84 -33 70 35 -62 4 32 -25 -75 -89 116 -8 -49 -35 82 -11 113 -23 -96 80 -83 -39 124 124 104 -7 -54 -55 -58 113 31 107 -21 -15 -75 -97 -12 -71 123 -114 -69 79 -6 -38 121 -123 110 56 98 11 1 16 -12 -8 -36 -81 -17 -44 -31 -8 -16 -20 -96 -106 125 -6 98 -73 84 125 118 -16 -99 125 -26 15 114 23 8 -84 31 -45 -29 115 -97 104 127 11 123 53 39 -38 93 118 -24 -29 -43 -79 -93 0 8 -16 -28 65 -18 35 -66 86 -62 -13 -22 110 -87 -6 -19 -53 87 66 -68 38 -6 64 72 -21 -37 32 -100 104 87 -57 -113 -113 -75 -11 -8 -36 61 -57 95 -37 -67 -24 22 -23 -90 9 4 64 -125 -121 8 121 -98 19 30 37 118 75 7 -43 -17 95 109 -19 -105 17 66 102 -85 -62 120 -67 -99 -26 -94 -57 -25 118 31 59 -38 -41 -27 117 31 109 -21 -15 -75 55 69 -17 -82 -123 -90 20 0 -51 27 -93 -60 -5 -81 -33 -84 -66 124 -11 -72 84 -83 -66 -4 126 -9 121 21 -65 70 -4 -124 -47 -86 19 0 108 -24 39 125 110 -9 -79 -74 -98 -29 63 -68 22 -35 46 -77 104 17 1 40 -30 62 -42 -122 37 65 -25 -60 98 -33 -87 112 -16 93 -95 90 67 8 -31 65 -93 -6 -14 123 -19 19 -116 115 77 -21 2 5 -38 93 -127 -10 -73 16 66 -8 -26 4 -36 111 -4 -45 105 -76 -78 0 84 -64 -34 106 31 58 124 -28 -17 -65 -15 -65 -40 -95 66 88 18 -49 95 75 2 107 -26 -16 -11 -127 -35 78 4 -61 -15 22 -4 26 -5 -27 -8 53 -18 -59 17 66 45 -29 -76 -16 -59 -95 2 80 39 32 -77 21 -59 29 21 111 -71 -38 -28 -103 -58 -1 -3 77 -23 31 -2 -26 47 -27 31 -112 43 -121 79 -109 14 -5 105 57 -50 -20 -77 -7 2 2 96 -31 -19 -64 27 -31 -114 -105 -33 -3 47 109 -117 13 -9 34 1 118 0 -22 2 -79 -16 110 -73 71 -2 -49 -25 -27 86 -53 -13 115 14 32 0 22 -114 123 -33 112 -90 -65 121 82 17 -43 18 -64 32 -32 2 -79 -16 -51 -109 -78 -68 -41 -121 17 -96 121 1 1 -80 -80 -103 125 38 -70 9 0 31 -64 5 2 28 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 -86 60 121 -62 0 0 0 70 73 68 65 84 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 3 2 0 28 13 8 0 112 52 32 0 -64 -47 -128 0 0 71 -13 -1 79 2 84 -27 -50 70 39 -97 0 0 0 0 73 69 78 68 -82 66 96 -126 -1 -1 -1 -1 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1'
                self.cursorFlashTime = 1060
                self.doubleClickInterval = 500
                self.keyboardInputInterval = 400
                self.wheelScrollLines = 3
                self.globalStrut = "0 0"
                self.startDragTime = 500
                self.startDragDistance = 5
                self.quitOnLastWindowClosed = True
                self.styleSheet = ""
                self.autoSipEnabled = True
                self.globalStrut_width = None
                self.globalStrut_height = None

                # Signals.
                self._signals = ['AboutToClose()', 'AboutToCloseResources()', 'aboutToQuit()', 'AllComponentsInitialized()', 'AllComponentsLoaded()', 'AllResourcesLoaded()', 'commitDataRequest(QSessionManager&)', 'destroyed()', 'destroyed(QObject*)', 'focusChanged(QWidget*,QWidget*)', 'fontDatabaseChanged()', 'lastWindowClosed()', 'MessageReceived(QString)', 'saveStateRequest(QSessionManager&)', 'StartupFinished()', 'unixSignal(int)']

                self.AboutToClose = self._AboutToClose
                self.AboutToCloseResources = self._AboutToCloseResources
                self.AllComponentsInitialized = self._AllComponentsInitialized
                self.AllComponentsLoaded = self._AllComponentsLoaded
                self.AllResourcesLoaded = self._AllResourcesLoaded
                self.MessageReceived = self._MessageRecieved
                self.StartupFinished = self._StartupFinished
                self.commitDataRequest = self._blankSignalSlot
                self.focusChanged = self._blankSignalSlot
                self.fontDatabaseChanged = self._blankSignalSlot
                self.lastWindowClosed = self._blankSignalSlot
                self.saveStateRequest = self._blankSignalSlot

                # Slots.
                self._slots = ['aboutQt()', 'AllWidgets()', 'autoSipEnabled()', 'Beep()', 'closeAllWindows()', 'deleteLater()', 'GetComponent(QString)', 'GetComponentNames()', 'GetComponentVersion(QString)', 'GetFrameworkVersion()', 'IsRuntimeMode()', 'LicServerLost()', 'LoadSelectedResources()', 'quit()', 'quit()', 'QuitCheck()', 'QuitWithoutWarning()', 'QuitWithoutWarning(quint8)', 'Restart()', 'Restart(QStringList)', 'Restart(QStringList,bool)', 'RestartWithWarning()', 'RestartWithWarning(QString)', 'setAutoSipEnabled(bool)', 'SetParanoid(bool)', 'setStyleSheet(QString)', 'ShowMessage(QString,QString)', 'ShowMessage(QString,QString,QString)', 'ShowRuntimeNotification()', 'StartApplication(QString)', 'StartApplication(QString,QStringList)', 'StartExternalApplication(QString)', 'StartExternalApplication(QString,QString)', 'StartExternalApplication(QString,QString,QString)', 'StartExternalApplication(QString,QString,QString,QString)', 'StartExternalApplication(QString,QString,QString,QString,QString)', 'StartExternalApplication(QString,QString,QString,QString,QString,QString)', 'StartExternalApplication(QString,QString,QString,QString,QString,QString,QString)']

                self.AllWidgets = self._AllWidgets
                self.Beep = self._Beep
                self.GetComponent = self._GetComponent
                self.GetComponentNames = self._GetComponentNames
                self.GetComponentVersion = self._GetComponentVersion
                self.GetFrameworkVersion = self._GetFrameworkVersion
                self.IsRuntimeMode = self._IsRuntimeMode
                self.LicServerLost = self._LicServerLost
                self.LoadSelectedResources = self._LoadSelectedResources
                self.QuitCheck = self._blankSignalSlot
                self.QuitWithoutWarning = self._QuitWithoutWarning
                self.Restart = self._Restart
                self.RestartWithWarning = self._RestartWithWarning
                self.SetParanoid = self._SetParanoid
                self.ShowMessage = self._ShowMessage
                self.ShowRuntimeNotification = self._ShowRuntimeNotification
                self.StartApplication = self._StartApplication
                self.StartExternalApplication = self._StartExternalApplication
                self.aboutQt = self._blankSignalSlot
                self.autoSipEnabled = self._blankSignalSlot
                self.closeAllWindows = self._blankSignalSlot
                self.quit = self._blankSignalSlot
                self.setAutoSipEnabled = self._blankSignalSlot
                self.setStyleSheet = self._setStyleSheet

            #--------------------------------#
            #          PPResourceList        #
            #--------------------------------#
            elif className == "PPResourceList":

                # Children / Parents.
                self._parent = PbaProObject("PBApro")
                if not PbaProObject("ResourceList") in PbaProObject("PBApro")._children:
                    PbaProObject("PBApro")._children.append(PbaProObject("ResourceList"))

                # Properties.
                self._properties = ['objectName']

                self.objectName = "ResourceList"

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'ResourceAdded(PPResource*)']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.ResourceAdded = self._blankSignalSlot

                # Slots.
                self._slots = ['CreateVirtualResource(QString)', 'deleteLater()', 'EnableUpdates(bool)', 'FindResourceByIndex(int)', 'FindResourceBySn(int,int)', 'FindResourceByType(int,int)', 'GetObjectFlags()', 'GetResourceCount()', 'GetResourceCountByType(PPResource::ResType)', 'GetResourceObjectsByType(PPResource::ResType)', 'HasUpdatesEnabled()', 'IsHidden()', 'IsValid()', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)']

                self.CreateVirtualResource = self._CreateVirtualResource
                self.EnableUpdates = self._blankSignalSlot
                self.FindResourceByIndex = self._FindResourceByIndex
                self.FindResourceBySn = self._FindResourceBySn
                self.FindResourceByType = self._FindResourceByType
                self.GetObjectFlags = self._GetObjectFlags
                self.GetResourceCount = self._GetResourceCount
                self.GetResourceCountByType = self._GetResourceCountByType
                self.GetResourceObjectsByType = self._GetResourceObjectsByType
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.SetObjectFlag = self._SetObjectFlag

            #--------------------------------#
            #           MilResource          #
            #--------------------------------#
            elif className == "MilResource":

                self.objectName = objectPath[13 :]

                # Children / Parents.
                self._setChildParent(objectPath, self.objectName)

                # Properties.
                self._properties = ['objectName', 'Type', 'DefaultName', 'Description', 'Server', 'Sn', 'Module', 'IsOpen', 'DbsStreamId', 'BoardType', 'Coupling', 'CoupledBus', 'Amplitude', 'AmplitudeVoltage', 'IrigTimeSource', 'HSCoupling', 'HSFrameMode', 'NTGFast']

                self.Type = "Type3910"
                self.DefaultName = objectPath[13 :]
                self.Description = objectPath[13 :]
                self.Server = "local"
                self.Sn = 9999
                self.Module = 1
                self.IsOpen = True
                self.DbsStreamId = "MIL1"
                self.BoardType = "BTNtg"
                self.Coupling = 0
                self.CoupledBus = "BothBusses"
                self.Amplitude = 255
                self.AmplitudeVoltage = "0.0"
                self.IrigTimeSource = "Internal"
                self.HSCoupling = 0
                self.HSFrameMode = "Standard 3910"
                self.NTGFast = False

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot

                # Slots.
                self._slots = ['BusTest(BusTestType,bool)', 'CloseResource()', 'DBSSync()', 'DBSSync(bool)', 'deleteLater()', 'EnableUpdates(bool)', 'ExecuteBIT()', 'FindBuddies()', 'FindBuddies(uint)', 'FindBuddies(uint,QObject*)', 'GetBITResult()', 'GetBoardFeatures(BoardInfoType)', 'GetBoardStreams()', 'GetDBSStreamType()', 'GetHwInfoEntry(QString)', 'GetHwInfoList()', 'GetIrigTime()', 'GetIrigTime(PPIrigTime::IrigTimeFields)', 'GetIrigTimeDirect()', 'GetMC17SyncCounter()', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'Init()', 'Init(bool)', 'Install()', 'IsClientResource()', 'IsHidden()', 'IsNtgResource()', 'IsValid()', 'OpenResource()', 'ReadBoardMemory(uint)', 'ResetBoard()', 'SenseEfaEfex()', 'SenseEfaEfex(bool)', 'SetIrigTime(int,int,int,int)', 'SetMC17SyncCounter(quint16)', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'SetSavable(bool)', 'SetSingleLaneCoupling(TyCoupling,bool)', 'ShowMem()', 'SwitchBoardType(ResType)', 'SwitchBoardType(ResType,bool)', 'ToggleEfaEfex()', 'ToggleOpen()', 'WriteBoardMemory(uint,uint)']

                self.BusTest = self._blankSignalSlot
                self.CloseResource = self._CloseResource
                self.DBSSync = self._DBSSync
                self.EnableUpdates = self._blankSignalSlot
                self.ExecuteBIT = self._ExecuteBIT
                self.FindBuddies = self._FindBuddies
                self.GetBITResult = self._GetBITResult
                self.GetBoardFeatures = self._GetBoardFeatures
                self.GetBoardStreams = self._GetBoardStreams
                self.GetDBSStreamType = self._GetDBSStreamType
                self.GetHwInfoEntry = self._GetHwInfoEntry
                self.GetHwInfoList = self._GetHwInfoList
                self.GetIrigTime = self._GetIrigTime
                self.GetIrigTimeDirect = self._GetIrigTimeDirect
                self.GetMC17SyncCounter = self._GetMC17SyncCounter
                self.GetObjectFlags = self._GetObjectFlags
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.Init = self._InitMb
                self.Install = self._InstallMb
                self.IsClientResource = self._IsClientResource
                self.IsHidden = self._IsHidden
                self.IsNtgResource = self._IsNtgResource
                self.IsValid = self._IsValid
                self.OpenResource = self._OpenResource
                self.ReadBoardMemory = self._ReadBoardMemory
                self.ResetBoard = self._ResetBoard
                self.SenseEfaEfex = self._blankSignalSlot
                self.SetIrigTime = self._SetIrigTime
                self.SetMC17SyncCounter = self._SetMC17SyncCounter
                self.SetObjectFlag = self._SetObjectFlag
                self.SetSavable = self._SetSavable
                self.SetSingleLaneCoupling = self._SetSingleLaneCoupling
                self.ShowMem = self._ShowMem
                self.SwitchBoardType = self._blankSignalSlot
                self.ToggleEfaEfex = self._blankSignalSlot
                self.ToggleOpen = self._ToggleOpen
                self.WriteBoardMemory = self._WriteBoardMemory
#BookMark Bookmark Class
            #--------------------------------#
            #        MilResourceStatus       #
            #--------------------------------#
            elif className == "MilResourceStatus":

                self.objectName = "Status"

                # Children / Parents.
                self._setChildParent(objectPath, self.objectName)

                # Properties.
                self._properties = ['objectName', 'IrigTime', 'IrigTimeStatus', 'BCStatus', 'RTStatus', 'BMStatus', 'RPLStatus']

                self.IrigTime = "0d:0h:0m:0s:0ms"
                self.IrigTimeStatus = "Internal"
                self.BCStatus = "Off" # TODO Implement Me "Off", "Run"
                self.RTStatus = "Off" # TODO Implement Me "Off", "Run"
                self.BMStatus = "Off" # TODO Implement Me "Off", "Run"
                self.RPLStatus = "Off" # TODO Implement Me "Off", "Run"

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'IrigTimeStatusChanged()', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'Updated(QObject*)']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.IrigTimeStatusChanged = self._IrigTimeStatusChanged
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.Updated = self._Updated

                # Slots.
                self._slots = ['deleteLater()', 'EnableUpdates(bool)', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'IsHidden()', 'IsValid()', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'Update()']

                self.EnableUpdates = self._blankSignalSlot
                self.GetObjectFlags = self._blankSignalSlot
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.SetObjectFlag = self._SetObjectFlag
                self.Update = self._Update

            #--------------------------------#
            #           MilBCSetup           #
            #--------------------------------#
            elif className == "MilBCSetup":

                self.objectName = "BC"

                # Children / Parents.
                self._setChildParent(objectPath, self.objectName)

                # Properties.
                self._properties = ['objectName', 'Active', 'Enabled', 'Phases', 'RetryMode', 'MCSa']

                self.Active = False
                self.Enabled = True
                self.Phases = ["ALL", "NONE"]
                self.RetryMode = "OneAlt"
                self.MCSa = "MCSa0"

                # Signals.
                self._signals = ['AboutToChangeState(bool)', 'Activated(bool)', 'ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'Halted()', 'Halted(MilTransfer*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'PhasesChanged()', 'Started()']

                self.AboutToChangeState = self._blankSignalSlot
                self.Activated = self._blankSignalSlot
                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.Halted = self._Halted
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.PhasesChanged = self._PhasesChanged
                self.Started = self._Started

                # Slots.
                self._slots = ['AddPhase(QString)', 'AutoDbsSync()', 'Continue()', 'CreateTransferFromMessage(QObject*)', 'deleteLater()', 'DeletePhase(QString)', 'EnableUpdates(bool)', 'FastCheck(QStringList,QStringList)', 'FastTest(QStringList,QStringList)', 'FindBuddies()', 'FindBuddies(uint)', 'FindBuddies(uint,QObject*)', 'GetHaltXfer()', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'Init()', 'Install()', 'IsHidden()', 'IsValid()', 'ReadStatus()', 'ReplayActivated(bool)', 'Run(bool)', 'RunFast(bool)', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'WriteDBSInitValues()']

                self.AddPhase = self._blankSignalSlot
                self.AutoDbsSync = self._AutoDbsSync
                self.Continue = self._blankSignalSlot
                self.CreateTransferFromMessage = self._CreateTransferFromMessage
                self.DeletePhase = self._blankSignalSlot
                self.EnableUpdates = self._blankSignalSlot
                self.FastCheck = self._FastCheck
                self.FastTest = self._blankSignalSlot
                self.FindBuddies = self._FindBuddies
                self.GetHaltXfer = self._GetHaltXfer
                self.GetObjectFlags = self._blankSignalSlot
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.Init = self._InitBc
                self.Install = self._InstallBc
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.ReadStatus = self._ReadStatus
                self.ReplayActivated = self._ReplayActivated
                self.Run = self._RunBc
                self.RunFast = self._blankSignalSlot
                self.SetObjectFlag = self._SetObjectFlag
                self.WriteDBSInitValues = self._WriteDBSInitValues

            #--------------------------------#
            #           MilBCStatus          #
            #--------------------------------#
            elif className == "MilHSBCStatus" or className == "MilBCStatus":

                self.objectName = "Status"

                # Children / Parents.
                self._setChildParent(objectPath, self.objectName)

                # Properties.
                if className == "MilHSBCStatus":
                    self._properties = ['objectName', 'Status', 'MajorCycles', 'XferCount', 'ErrorCount', 'HSXferCount', 'HSErrorCount']
                else:
                    self._properties = ['objectName', 'Status', 'MajorCycles', 'XferCount', 'ErrorCount']

                self.objectName = "Status"
                self.Status = "Halted"
                self.MajorCycles = 0
                self.XferCount = 0
                self.ErrorCount = 0
                if className == "MilHSBCStatus":
                    self.HSXferCount = 0
                    self.HSErrorCount = 0

                # Signals.
                self._signals = ['ChildAdded(QObject*)', 'ChildRemoved(QObject*)', 'DataChanged(QObject*,int)', 'destroyed()', 'destroyed(QObject*)', 'LayoutChanged(QObject*)', 'NameChanged(QObject*)', 'Updated(QObject*)']

                self.ChildAdded = self._ChildAdded
                self.ChildRemoved = self._ChildRemoved
                self.DataChanged = self._blankSignalSlot
                self.LayoutChanged = self._blankSignalSlot
                self.NameChanged = self._blankSignalSlot
                self.Updated = self._blankSignalSlot

                # Slots.
                self._slots = ['deleteLater()', 'EnableUpdates(bool)', 'GetObjectFlags()', 'HasUpdatesEnabled()', 'IsHidden()', 'IsValid()', 'SetObjectFlag(quint32)', 'SetObjectFlag(quint32,bool)', 'Update()']

                self.EnableUpdates = self._blankSignalSlot
                self.GetObjectFlags = self._GetObjectFlags
                self.HasUpdatesEnabled = self._HasUpdatesEnabled
                self.IsHidden = self._IsHidden
                self.IsValid = self._IsValid
                self.SetObjectFlag = self._SetObjectFlag
                self.Update = self._Update

            #--------------------------------#
            #           BLANK.ITEM           #
            #--------------------------------#
            elif className == "BLANK.ITEM":

                # Properties.
                self._properties = []

                self.props = None

                # Signals.
                self._signals = []

                self.sig = None

                # Slots.
                self._slots = []

                self.slo = None
            #----------------------------------------------------------------------------------------------------------------------------------------#


        class MemberCaller(object):
            '''This helper class is used to call a slot / signal of a PBA.pro Object'''


            def __init__(self, arg1=None, arg2=None, arg3=None):
                ''''''

                pass
                #------------------------------------------------------------------------------------------------------------------------------------#


            def __call__(self):
                '''This member allows to call this object.'''

                pass
                #------------------------------------------------------------------------------------------------------------------------------------#
            #----------------------------------------------------------------------------------------------------------------------------------------#


        class MetaObjectInfo(object):
            '''MetaObject Descriptor'''


            def __init__(self, arg1=None, arg2=None, arg3=None, arg4=None):
                ''''''

                pass
                #------------------------------------------------------------------------------------------------------------------------------------#
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def AddProperty(self, Property=None, Type=None, Description=None):
            '''This Member allows to add a New Dynamic Property to an PBA.pro Object
        The Properties may be seen on the user Interface, and may be used
        to Add Script Information to any PBA.pro Objects.

        Property: The Name of the New Property. Must consist of Letters only (and Numbers which are not at the start)
        Type:     The Property Type is one of the following Strings
                  "QString" : String Type
                  "int"     : Signed Integer
                  "uint"    : Unsigned Integer
                  "double"  : Double

        Description: Property Description string separated by comma with one or more of the following items

        MIN=
        MAX=
        STEP=    The Range for uint,int and double Properties

        FMT=  The integer base for uint and int Properties either 2 (Binary),8(Octal),10 (Decimal/Default) or 16 (Hex)
        PREC= The Precision for double properties (0..18)

        DESC=Any Description for the Property, which appears e.g. as tool-tip

        e.g. AddProperty("IntProperty","int","MIN=0,MAX=100,STEP=2,FMT=16,DESC=This is a Integer Property added by Script")
        e.g. AddProperty("DoubleProperty","double","MIN=0,MAX=100,PREC=0")

        Property Flags, which allow to modify the state of the Dynamic Property
        FLAGS=   The Following Flag character are supported
                        r   : The Property is Read-only
                        w   : The Property is Write-able (default)
                        i   : The Property is Invalid
                        v   : The Property is Valid (default)
                        h   : The Property is Hidden
                        d   : The Property is Visible (default)
                        s   : The Property is Savable in the Project
                        n   : The Property is Not Savable in the Project (default)

        e.g.
        a Read-only Property
        AddProperty("IntProperty","int","FLAGS=r")
        Note: a Read-only Dynamic Property can still be changed by Script, but not via the User Interface

        ENUM=
        BITFIELD=
                       "uint" and "int" Properties may be defined as enum or bitfield properties.
                       The Enum List has the following format
                       :: separated by semicolon

        e.g. AddProperty("EnumProperty","uint","ENUM=0:Off;1:State1;2:State2;3:State3;4:State4")
        Bitfield Property must have only one bit set per state
        e.g. AddProperty("EnumProperty","uint","BITFIELD=0:None;0x01:Flag1;0x02:Flag2;0x04:Flag3;0x08:Flag4")

        The Return value is the new Property Index or -1 on an error'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def children(self, Type=None, Depth=1, bInherits=False):
            '''Returns a list of children
        Type: class name to search
        Depth: depth of the child hierarchy to search (1 = direct children, -1 all children recursive)
        bInherits: list contains objects which inherits from Type if True'''

            children = []
            for object in self._children:
                children.append(hex(id(object)))
            return children
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def childrenNames(self, Type=None, Depth=1, bInherits=False):
            '''Returns a list  of children object names
        Type:  class name to search
        Depth: depth of the child hierarchy to search (1 = direct children, -1 all children recursive)
        bInherits: list contains objects which inherits from Type if True'''

            childrenNames = []
            for object in self._children:
                childrenNames.append(object.objectName)
            return childrenNames
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def childrenp(self, Type=None, Depth=1, bInherits=False):
            '''Returns a list with children (as _PbaProObject)
        Type: class name to search
        Depth: depth of the child hierarchy to search (1 = direct children, -1 all children recursive)
        bInherits: list contains objects which inherits from Type if True'''

            return self._children
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def classname(self):
            '''Returns the classname of the PBA.pro object'''

            return self._className
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def DelProperty(self, Property):
            '''This Function deletes a previous added dynamic property.
            See: AddProperty above'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def FindParent(self, sClassName):
            '''Returns the parent object, search performed by class name'''

            currentClassName = ""
            objUnderSearch = self

            while currentClassName != sClassName:
                objUnderSearch = objUnderSearch.parent()
                currentClassName = objUnderSearch.classname()

            return objUnderSearch
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def firstChildOfType(self, Type=None, Depth=1, bInherits=False):
            '''Returns the first child of the specified object type as _PbaProObject.
        The Depth parameter lets you define how deep the search should be within the child hierarchy.'''

            return None
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def GetChild(self, sChildName):
            '''Returns the child object with the given name.
        This must be used as workaround, when you deal with children containing
        invalid characters (for python) in the name.
        e.g. MIL-Board1 contains a minus

        Furthermore you have to use this if there is a child with the same name
        as a property of the object
        e.g. F = MyDbsParam.GetChild("Format")'''

            for object in self._children:
                if object.objectName == sChildName:
                    return object
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def GetObjectPtr(self):
            '''get the internal object pointer'''

            return id(self)
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def help(self):
            '''Opens the scripting help'''

            print help(self)
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def inherits(self, classname):
            '''Returns True, if the class of the object matches the given classname'''

            if self.classname() == classname:
                return True
            else:
                return False
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def isA(self, classname):
            '''Returns True, if the class of the object matches the given classname'''

            if self.classname() == classname:
                return True
            else:
                return False
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def IsValid(self, classname): # pylint: disable=method-hidden
            '''Returns True if the object exists (is any alive object) and is Valid'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def IsValidObject(self, classname):
            '''Returns True if the object exists (is any alive object)
        The PPObject::IsValid slot says if the (existing) object is valid at the Moment'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def objectPath(self):
            '''Returns the classname of the PBA.pro object'''

            return self._objectPath
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def parent(self):
            '''Returns the parent object'''

            return self._parent
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def properties(self):
            '''Returns a list, containing the signals of the object'''

            return self._properties
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def root(self):
            '''Returns the root object'''

            nextClassName = self.parent().classname()
            objUnderSearch = self

            while nextClassName != "PProApp":
                objUnderSearch = objUnderSearch.parent()
                nextClassName = objUnderSearch.parent().classname()

            return objUnderSearch
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def signals(self):
            '''Returns a list, containing the signals of the object'''

            return self._signals
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def slots(self):
            '''Returns a list, containing the signals of the object'''

            return self._slots
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _setChildParent(self, objectPath, objectName):
            '''Hidden function that sets a _PbaProObject's parent and sets itself as a child of that parent.'''

            parentObjectPath = objectPath.replace("." + objectName, "")

                # Add self as an attribute of the parent.
            setattr(PbaProObject(parentObjectPath), objectName, self)

                # Set this object's parent.
            self._parent = PbaProObject(parentObjectPath)

                # Set self as a child of my parent.
            if not PbaProObject(objectPath) in PbaProObject(parentObjectPath)._children:
                PbaProObject(parentObjectPath)._children.append(PbaProObject(objectPath))
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def __str__(self):
            ''''''

            return "{0} [{1}]".format(self.objectName, self.classname())
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _blankSignalSlot(self, *args, **kwargs):
            '''Not implemented in the PBApro module.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AboutToClose(self, *args, **kwargs):
            '''Shows that the PBA.pro will be closed.'''
            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AboutToCloseResources(self, *args, **kwargs):
            '''Notification that the resources will be closed in a moment.'''
            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AllComponentsInitialized(self, *args, **kwargs):
            '''Is emitted, after all components are initialized. '''
            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AllComponentsLoaded(self, *args, **kwargs):
            '''Is emitted, after all components are loaded. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AllResourcesLoaded(self, *args, **kwargs):
            '''Is emitted, after all components are Resources are created.'''
            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _MessageRecieved(self, *args, **kwargs):
            '''Message from an other PBA.pro Instance received.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _StartupFinished(self, *args, **kwargs):
            '''Is emitted, when the PBA.pro is completely start up.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AllWidgets(self, *args, **kwargs):
            '''Returns all toplevel Widgets. '''

            return []
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _Beep(self, *args, **kwargs):
            '''Beeps. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _GetComponent(self, *args, **kwargs):
            '''Returns component defined by name. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _GetComponentNames(self, *args, **kwargs):
            '''Returns all component names. '''

            return [u'CompActiveX', u'CompAnaWdg', u'CompParameterDBS', u'CompDesigner', u'CompExamples', u'CompLastGenerationImportTool', u'CompKDC', u'CompLGPL', u'CompMIL', u'CompQWT', u'CompSave', u'CompEFAEXPORT', u'CompCompPythonStarter', u'CompQML', u'CompRecConv', u'CompPython']
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _GetComponentVersion(self, *args, **kwargs):
            '''Returns the current version of the specified component. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _GetFrameworkVersion(self, *args, **kwargs):
            '''Returns the current framework version. '''

            return PbaProObject._frameworkVersion.split(".")[0] + "." + \
                   PbaProObject._frameworkVersion.split(".")[1] + \
                   " Build " + PbaProObject._frameworkVersion.split(".")[-1]
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _IsRuntimeMode(self, *args, **kwargs):
            '''Shows if the PBA.pro is in Runtime Mode or not. '''

            return False
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _LicServerLost(self, *args, **kwargs):
            '''Internal. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _LoadSelectedResources(self, *args, **kwargs):
            '''Internal. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _QuitWithoutWarning(self, *args, **kwargs):
            '''Shutdown PBA.pro without any warning. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _Restart(self, *args, **kwargs):
            '''Restarts the PBA.pro without any warning. The optional command line is passed to the new PBA.pro instance. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _RestartWithWarning(self, *args, **kwargs):
            '''Restarts the PBA.pro but showing a messagebox with a optional question. Without argument "Restart PBA.pro?" is shown. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _SetParanoid(self, *args, **kwargs):
            '''Internal. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _ShowMessage(self, *args, **kwargs):
            '''Shows a Message. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _ShowRuntimeNotification(self, *args, **kwargs):
            '''Internal. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _StartApplication(self, *args, **kwargs):
            '''Allows to start an external Application. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _StartExternalApplication(self, *args, **kwargs):
            '''Allows to start an external Application. '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ChildAdded(self, *args, **kwargs):
            '''Automatically emitted if a child was added.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _ChildRemoved(self, *args, **kwargs):
            '''Automatically emoted if a child was removed.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _setStyleSheet(self, sheet):
            '''Automatically emoted if a child was removed.'''

            self.styleSheet = sheet
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _CreateVirtualResource(self, *args, **kwargs):
            '''Create a dummy virtual resource.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _FindResourceByIndex(self, *args, **kwargs):
            '''Returns the resource at the given index.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _FindResourceBySn(self, *args, **kwargs):
            '''Returns the resource with the given serial Number.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _FindResourceByType(self, *args, **kwargs):
            '''Returns the resource with the given type.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetResourceCount(self, *args, **kwargs):
            '''Returns the count of all resources.'''

            return 6
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetResourceCountByType(self, *args, **kwargs):
            '''Returns the amount of resources by type.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetResourceObjectsByType(self, *args, **kwargs):
            '''Returns a list of resources of a given type.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _HasUpdatesEnabled(self, *args, **kwargs):
            '''Returns true if the object is already read from Hardware (if applicable).'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsHidden(self, *args, **kwargs):
            '''Returns true, if the Object is Hidden.'''

            return False
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetObjectFlag(self, objectFlag):
            '''Allows to modify the Object Flags - For the Flags.'''

            self._objectFlag = objectFlag
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _CloseResource(self, *args, **kwargs):
            '''Closes the Resource.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSSync(self, *args, **kwargs):
            '''Synchronizes the complete resource with the Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ExecuteBIT(self, *args, **kwargs):
            '''Executes the Build In test of the Board.'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _FindBuddies(self, *args, **kwargs):
            '''Find related objects.'''

            return []
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetBITResult(self, *args, **kwargs):
            '''Returns the BIT Result after ExecuteBIT was called.'''

            return "Selftest Passed (0/0)"
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetBoardFeatures(self, *args, **kwargs):
            '''Returns Dedicated Board Features.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetBoardStreams(self, *args, **kwargs):
            '''Returns a list with all streams on the same board.'''

            return []
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetDBSStreamType(self, *args, **kwargs):
            '''Returns the matching Database Root Stream Type Node.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetHwInfoEntry(self, *args, **kwargs):
            '''Allows to request dedicated About Dialog / Extended Component Information Values. Use the Keys Name as Parameter for this call.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetHwInfoList(self, *args, **kwargs):
            '''Returns a List of all available HW Info like they are displayed in the About Dialog / Extended Component Information.'''

            return ['No Target Mode', 'Settings may be changed at "mil_ntg_counts"']
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetIrigTime(self, *args, **kwargs):
            '''Returns the IRIG Time in various units, by default in nanoseconds,.'''

            return 0
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetIrigTimeDirect(self, *args, **kwargs):
            '''Returns the Uncached IRIG Time of the Board in us.'''

            return 0
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetMC17SyncCounter(self, *args, **kwargs):
            '''Returns the MC17 Sync Counter.'''

            return 46700
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InitMb(self, *args, **kwargs):
            '''Inits the Resource and all members without warning.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InstallMb(self, *args, **kwargs):
            '''Installs the Setup on the Board.'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsClientResource(self, *args, **kwargs):
            '''Returns true, if it is a Client resource.'''

            return False
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsNtgResource(self, *args, **kwargs):
            '''Check if resource/board in "No Target Mode".'''

            return False
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsValid(self, *args, **kwargs):
            '''Returns true, if the Object is Valid.'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _OpenResource(self, *args, **kwargs):
            '''Opens the Resource.'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ReadBoardMemory(self, *args, **kwargs):
            '''Direct Read from the Board Memory.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ResetBoard(self, *args, **kwargs):
            '''Resets the Board.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetIrigTime(self, *args, **kwargs):
            '''Set the IRIG Time.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetMC17SyncCounter(self, *args, **kwargs):
            '''Sets the MC17 Sync Counter to the given value.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetSavable(self, *args, **kwargs):
            '''Allows to add / remove the related resource from the setup file.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetSingleLaneCoupling(self, *args, **kwargs):
            '''DEPRECIATED: use the property CoupledBus instead.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ShowMem(self, *args, **kwargs):
            '''Creates the Board Memory Node.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ToggleOpen(self, *args, **kwargs):
            '''Opens the resource when it is closed and vice versa.'''

            return True
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _WriteBoardMemory(self, *args, **kwargs):
            '''Direct Write to the Board Memory.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AboutToChangeState(self, *args, **kwargs):
            '''Shows, that the State of the BC'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Activated(self, *args, **kwargs):
            '''Shows, that the State of the BC'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Halted(self, *args, **kwargs):
            '''Emitted after Stop or on Xfer Halt.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PhasesChanged(self, *args, **kwargs):
            '''Emitted after a change of the Phase.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Started(self, *args, **kwargs):
            '''Emitted after Start.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AddPhase(self, *args, **kwargs):
            '''Adds a Phase of Flight'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _AutoDbsSync(self, *args, **kwargs):
            '''Synchronizes all Buffers to the Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _CreateTransferFromMessage(self, *args, **kwargs):
            '''Creates a Transfer from a Bus Monitor Message.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DeletePhase(self, *args, **kwargs):
            '''Deletes the Given Phase of Flight'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _FastCheck(self, *args, **kwargs):
            '''Same as FastTest(....) without sending the transfers. It must be send before.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetHaltXfer(self, *args, **kwargs):
            '''Returns the Transfer which has caused the halt.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InitBc(self, *args, **kwargs):
            '''Inits the Bus Controller.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InstallBc(self, *args, **kwargs):
            '''Installs the BC's Data on the Target.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ReadStatus(self, *args, **kwargs):
            '''Updates the BC Status from the Hardware.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ReplayActivated(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _RunBc(self, boolRun):
            '''Starts / Stops the Bus Controller.'''

            self.Active = boolRun
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _WriteDBSInitValues(self, *args, **kwargs):
            '''Writes all Database Init Values to the Buffer.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Update(self, *args, **kwargs):
            '''Update from Hardware.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _sigLoadStreamAssign(self, *args, **kwargs):
            '''Indicates database load start and end.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _sigPrjTitleChanged(self, *args, **kwargs):
            '''Database Stream assign was changed.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#





        def _AddGlobalEntryToNode(self, *args, **kwargs):
            '''Adds the Global structure to the database node if possible.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _CreateClassificationManager(self, *args, **kwargs):
            '''Internal (used by regression scripts). '''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#

        def _DBSExport(self, *args, **kwargs):
            '''export the given node and all children to a ppdbs-file'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSImport(self, *args, **kwargs):
            '''import the given ppdbs-file to the given DBSNode'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSImportPDI(self, *args, **kwargs):
            '''parse the PDI-File and create a new PPDBS-object, caller is responsible for returned object'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSImportUserDBS(self, *args, **kwargs):
            '''parse the PDI-File and create a new PPDBS-object, caller is responsible for returned object'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSLoad(self, *args, **kwargs):
            '''Imports any of the supported databases.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSNew(self, *args, **kwargs):
            '''create a new empty PPDBS-object, caller is responsible for returned object'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _EmitDbsModified(self, *args, **kwargs):
            '''Can be used to mark the database modified after the database was setup by script, and inform the resources for synchronization.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _EnableDBSFunctionality(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ExpandAll(self, *args, **kwargs):
            '''DEPRECIATED: Use DBSTreeView ExpandAll instead.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetDBSDescription(self, *args, **kwargs):
            '''Returns the Database Description.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewDBSObject(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _OnNewDbsFiles(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjCanClose(self, *args, **kwargs):
            '''Asks the user if he wants to save the database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSIsModified(self, *args, **kwargs):
            '''Returns true, if the database is modified.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSLoadStreamAssign(self, *args, **kwargs):
            '''Loads all DBS Steam Assign files.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSNeedsSave(self, *args, **kwargs):
            '''Returns true if the database needs to be saved.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSNew(self, *args, **kwargs):
            '''Creates a new Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSOpen(self, *args, **kwargs):
            '''use this slot load a database from script!'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSSave(self, *args, **kwargs):
            '''Saves the current database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSSaveAs(self, *args, **kwargs):
            '''Saves the current database under the given name.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjDBSSetModified(self, *args, **kwargs):
            '''Allows to clear / remove the Database modification flag.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjFileIsModified(self, *args, **kwargs):
            '''Returns true, if the database stream assign is modified.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjGetDBSPtr(self, *args, **kwargs):
            '''Returns the Current Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjGetFileName(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjGetPrjFilePtr(self, *args, **kwargs):
            '''Returns the Current Database Files.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjGetTitle(self, *args, **kwargs):
            '''Returns the current database title.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjSetDBS(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _PrjSetFileName(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetObjectFlags(self, *args, **kwargs):
            ''''''

            return self._objectFlag
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AddFile(self, *args, **kwargs):
            '''Adds A database file.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DBSUse(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _EmitModificationSignal(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _EmitModificationSignalInt(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetId(self, *args, **kwargs):
            '''Returns the Unique ID in the List.'''

            return -1
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _HasValidDBSFile(self, *args, **kwargs):
            '''Returns true, if there is a valid database file.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InitDBSPrj(self, *args, **kwargs):
            '''Clears all Database File Entries.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InitFull(self, *args, **kwargs):
            '''Clears all Database File Entries and the entire Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _LoadAll(self, *args, **kwargs):
            '''Loads all Database Files to the main PBA.pro Database.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewFile(self, *args, **kwargs):
            '''Returns a new Database Stream Assign entry'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetSourceHashDirty(self, *args, **kwargs):
            '''Causes the recreation of the source hash the next time.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AssignFilterChanged(self, *args, **kwargs):
            '''Shows that something on the options was changed.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AssignOptionsChanged(self, *args, **kwargs):
            '''Shows that generic assign options have been added.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ClassificationChanged(self, *args, **kwargs):
            '''Shows a possible change of the classification settings.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _OfflineReplayActivated(self, *args, **kwargs):
            '''Shows that the Offline Replay was started / Stopped.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SearchReplayFinished(self, *args, **kwargs):
            '''Is emitted when the replay search is finished, bFound == true if found, else false.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _AssignObject(self, *args, **kwargs):
            '''Adds all DBS children recursively to the.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ConnectReferences(self, *args, **kwargs):
            '''Forces a search for the Reference objects.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ConnectRequired(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _DisableAlarmPopup(self, *args, **kwargs):
            '''Disables / Enables the Popup of the Signalled Parameter display.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetEntryAt(self, *args, **kwargs):
            '''Returns the Assign Entry at the given Position.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetEntryCount(self, *args, **kwargs):
            '''Returns the Number of Assign Entries beyond this entry.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetFolders(self, *args, **kwargs):
            '''Returns a list of all folders in the folder.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetParamRefs(self, *args, **kwargs):
            '''Returns a list of all parameter references.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetParameters(self, *args, **kwargs):
            '''All parameters within the folder.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _InitAssign(self, *args, **kwargs):
            '''Stops the Assign if active and deletes all entries without warning.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsEmpty(self, *args, **kwargs):
            '''Returns true, if no Assign Objects are in the Folder.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _MayBeTab(self, *args, **kwargs):
            '''Shows true, when this folder may become a tab'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewAssignEntry(self, *args, **kwargs):
            '''Creates a new reference assign object on this folder with the given Property.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewComment(self, *args, **kwargs):
            '''Creates a Comment Object.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewDummyAssignEntry(self, *args, **kwargs):
            '''Creates a Dummy Assign entry, which may be feed by a script.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewFolder(self, *args, **kwargs):
            '''Creates a New Folder with the given name.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewState(self, *args, **kwargs):
            '''Creates a Dummy Assign entry, which may be feed by a script.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _NewTab(self, *args, **kwargs):
            '''Creates a new Assign Tab.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _OneConnectTry(self, *args, **kwargs):
            '''Internal.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ReplaySearch(self, *args, **kwargs):
            '''Starts the Replay Search.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ReplaySearchOn(self, *args, **kwargs):
            '''Returns a signal condition, allowing to search within the replay.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Reset(self, *args, **kwargs):
            '''Resets the Options'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _RunAssign(self, boolRun):
            '''Starts / Stops the Objects which are included in the assign.'''

            self.Active = boolRun
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _ShowSignaledParameterDisplay(self, *args, **kwargs):
            '''shows the Signalled Parameter Assign display'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SwitchTab(self, *args, **kwargs):
            '''Converts a Root Folder to a Tab and Vice Versa.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _Updated(self, *args, **kwargs):
            '''Shows a Change on the Object.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#



        def _GetEntryAt(self, *args, **kwargs):
            '''Returns the Assign Entry at the given Position.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetEntryCount(self, *args, **kwargs):
            '''Returns the Number of Assign Entries beyond this entry.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetInstance(self, *args, **kwargs):
            '''Returns the Current instance.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetInstances(self, *args, **kwargs):
            '''Returns a List of available Instances for the related Parameter.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetInstancesAsObject(self, *args, **kwargs):
            '''Returns possible Parameter References instances for the current parameter.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetParamRefObject(self, *args, **kwargs):
            '''Returns the currently displayed parameter ref on the parameter data source.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetRefObject(self, *args, **kwargs):
            '''Returns the Parameter, or the object delivering the data.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetSourcePosDiff(self, *args, **kwargs):
            '''Returns the difference in the Bits, when the parameter was assigned from a different parameter source.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetValue(self, *args, **kwargs):
            '''QVariant access function.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetValueDbl(self, *args, **kwargs):
            '''Gets the Value as Double.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _GetValueStr(self, *args, **kwargs):
            '''Gets the String Value.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IsWritable(self, *args, **kwargs):
            '''Returns if the Object is writable.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetValue(self, *args, **kwargs):
            '''Sets value via the QVariant value if writable.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetValueDbl(self, *args, **kwargs):
            '''Sets value via a Double Value if writable.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _SetValueStr(self, strValue):
            '''Sets the string value if is writable.'''

            self.ValueStr = strValue
            try:
                self.Value = int(strValue)
            except:
                pass
            try:
                self.ValueDbl = float(strValue)
            except:
                pass
            try:
                self.ValueRaw = long(strValue)
            except:
                pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _CreateAssignOption(self, sOptionName, bForce = False):
            '''This slot is used to create an assign option. The currently available options may be requested with the slot: GetAvailAssignOptions Some Components may add other options. The Standard Options Names are of the DBS Component are:
        Signal:              Allows to define Alarms and Good States etc \see PPDBSAssignSignal
        Function:            Allows to control a Value according a Function \see PPDBSAssignFunction
        PresetValue:         Allows to define a set of Prepared Control Values which are written on request \see PPDBSAssignPresetValue
        Format:              Allows to display the Valuestring in an other format than the given \see PPDBSAssignDisplayFormat
        Additional Info:     Allows to add additional info \see PPDBSAssignAdditionalInfo
        Formula:             Allows to add an Assign Calc Formula \see PPDBSAssignCalcFormula
        Parameter Recording: Allows to add a Parameter Recording Option


        e.g.
        call with CreateAssignOption("Signal") to create a Signal Element
If you set bForce to true, the Assign Option is created always, although it seems not to be adequate at the Moment. e.g. Create a Option, which allows to change the parameter value, although the parameter is not writable. '''

            # If the AssignPram --> ResourceParam --> RT is set to  Mailbox.
            if self.GetParamRefObject().FindParent("MilEfaRT").Mode == "Mailbox":
                allowedOptions = {"Additional Info" : "PPDBSAssignAdditionalInfo", "Parameter Recording" : "PPDBSAssignParameterRecording",
                                  "Format" : "PPDBSAssignDisplayFormat", "Formula" : "PPDBSAssignCalcFormula", "Signal" : "PPDBSAssignSignal",
                                  "Dyntag" : "MilDBSAssignDyntag"}

            # If the AssignPram --> ResourceParam --> RT is set to  Simulation.
            elif self.GetParamRefObject().FindParent("MilEfaRT").Mode == "Simulation":
                allowedOptions = {"Additional Info" : "PPDBSAssignAdditionalInfo", "Function'" : "PPDBSAssignFunction",
                                  "PresetValue" : "PPDBSAssignPresetValue", "Parameter Recording" : "PPDBSAssignParameterRecording",
                                  "Format" : "PPDBSAssignDisplayFormat", "Formula" : "PPDBSAssignCalcFormula", "Signal" : "PPDBSAssignSignal",
                                  "Dyntag" : "MilDBSAssignDyntag"}

            if sOptionName in allowedOptions.keys():
                className = allowedOptions.get(sOptionName)
                option = _PbaProObject(self.objectPath + "." + sOptionName, className)

                # Children / Parents.
                option._parent = PbaProObject(self._objectPath)
                self._children.append(option)

                # TODO Test Me
            #----------------------------------------------------------------------------------------------------------------------------------------#


        # TODO UP & Down Requires GetParamRefObject and RT to be implemented.

        def _GetAvailableAssignOptions(self):
            '''Sets the string value if is writable.'''

             # If the AssignPram --> ResourceParam --> RT is set to  Mailbox.
            if self.GetParamRefObject().FindParent("MilEfaRT").Mode == "Mailbox":
                return ['Additional Info', 'Parameter Recording', 'Format', 'Formula', 'Signal', 'Dyntag']

            # If the AssignPram --> ResourceParam --> RT is set to  Simulation.
            elif self.GetParamRefObject().FindParent("MilEfaRT").Mode == "Simulation":
                return ['Additional Info', 'Function', 'PresetValue', 'Parameter Recording', 'Format', 'Formula', 'Signal', 'Dyntag']

            else:
                raise Exception("Unable to determine parameter options.")

            #TODO Test Me
            #----------------------------------------------------------------------------------------------------------------------------------------#


        def _IrigTimeStatusChanged(self, *args, **kwargs):
            '''Emitted if the IRIG Time status has changed.'''

            pass
            #----------------------------------------------------------------------------------------------------------------------------------------#


#BookMark Bookmark functions



        #--------------------------------------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                      Functions.                                                                    #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
    def __detectPbaFiles():
        '''Hidden function that scans the directory that this script is located in and returns a list of .ppro files and .tmpl files.

        __detectPbaFiles() --> [*.ppro, *.tmpl...]'''

        # Scan the project directory for .ppro or .tmpl files.
        pbaFiles = []

        # Determine the next folder up from this file's location.
        cwd = os.getcwd().split("\\")[ : -1]
        newCwd = ""
        for item in cwd:
            newCwd += item + "\\"

        for dirpath, dirnames, filenames in os.walk(newCwd):
            for pbaFile in filenames:
                if (".ppro" in pbaFile or ".tmpl" in pbaFile) and ".bak" not in pbaFile:
                    pbaFiles.append(dirpath + "\\" + pbaFile)

        return pbaFiles
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def __parseXMLFiles():
        '''Hidden function that takes the discovered project files and reads the XML data into a list of dictionaries.
        The function will then go on to search the dictionary data for potential _PbaProObjects() and create them with their saved properties.'''

        xmlDicts = []

        # Discover PBA.Pro related files and search for objectPath within them.
        for tgtFile in __detectPbaFiles():
            with open(tgtFile, "r") as dataFile:
                xml = dataFile.read()
                xmlDicts.append(xmltodict.parse(xml))

        # Search for potential _PbaProObjects within the XML data recursively.
        for xmlDict in xmlDicts:
            __searchForCL(xmlDict["PPU"])

        # Set the PBA.Pro FrameWork version.
        if len(xmlDicts) > 0:
            for item in xmlDicts[0]["PPU"]["GMI"]["FI"]:
                if item["@c"] == "Framework Version":
                    PbaProObject._frameworkVersion = item["@d"]


    #------------------------------------------------------------------------------------------------------------------------------------------------#
    def __searchForCL(xmlDict, parentObj=None):
        '''Hidden function that recursively searches the XML converted dictionaries for potential _PbaProObjects()'''

        # If our XML class has child classes present.
        if str(type(xmlDict.get("CL"))) == "<type 'list'>":
            for item in xmlDict.get("CL"):
                objectName = item["@n"]
                className = item["@ty"]
                # Add object properties that have been save to the XML files.
                try:
                    properties = item["PR"]["@d"]
                except KeyError:
                    properties = False
                # Add addition object information - Used to store assign window parameter additional information.
                try:
                    ssData = item["SS"]
                except:
                    ssData = None

                newObj = __createObject(className, objectName, parentObj, properties, ssData)
                __addParentInfo(parentObj, newObj)

                # Detect further child assets.
                if "CL" in item.keys():
                    __searchForCL(item, parentObj=newObj)

        # If our XML class has no child classes.
        elif str(type(xmlDict.get("CL"))) == "<class 'collections.OrderedDict'>":
            objectName = xmlDict["CL"]["@n"]
            className = xmlDict["CL"]["@ty"]
            # Add object properties that have been save to the XML files.
            try:
                properties = xmlDict["CL"]["PR"]["@d"]
            except:
                properties = False
            # Add addition object information - Used to store assign window parameter additional information.
            try:
                ssData = item["SS"]
            except:
                ssData = None
            newObj = __createObject(className, objectName, parentObj, properties, ssData)
            __addParentInfo(parentObj, newObj)

            # Detect further child assets.
            if "CL" in xmlDict["CL"].keys():
                __searchForCL(xmlDict["CL"], parentObj=newObj)
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def __addParentInfo(parentObj, newObj):
        '''Hidden function that is triggered if a parent _PbaProObject is detected.
        This function will add all parent/child data to each object.'''

        if parentObj != None:
            # Add the child as a property of the parent.
            setattr(parentObj, newObj.objectName, newObj)
            # Add the child to the parents children.
            parentObj._children.append(newObj)
            # Add the parent to the child.
            newObj._parent = parentObj
            # Correct the objectPath to include the path of it's parent'
            newObj._objectPath = parentObj._objectPath + "." + newObj._objectPath
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def __createObject(className, objectName, parentObj=None, properties=None, ssData=None):
        '''Hidden function that creates our newly discovered potential _PbaProObjects() from XML and adds their file saved properties.'''

        # Establish the objectPath.
        if className == "MilResource":
            objectPath = "ResourceList." + objectName
        else:
            objectPath = objectName

        if className != "PPLayoutContainer" and className != "PPLayout" and className != "PPStdViewInformation" and className != "PPGeniericViewInformation": # Filter out unwanted PbaProObjects here.
            newObj = _PbaProObject(objectPath, className)
            newObj.objectName = objectName

            if properties:
                # Add properties from XML to our newly made _PbaProObject().
                for prop in properties.split(";"):
                    try:
                        name, value = prop.split("=")

                        # handle boolean values and suffixes in names.
                        if ":bool" in name:
                            name = name.replace(":bool", "")
                        if value == "false":
                            value = False
                        elif value == "true":
                            value = True

                        # Add the propertie to the newly made _PbaProObject
                        setattr(newObj, name, value)

                    except ValueError: # Used for complex properties that have multiple = signs within them.
                        pass
            if ssData:
                newObj._ssData = ssData["@d"]

            return newObj
    #------------------------------------------------------------------------------------------------------------------------------------------------#


    def connect(Src, Signal, Dest, Slot, Mode=None, bForceSingleConnect=False):
        '''Connect function

    1. Use to connect 2 QObjects (Src and Dest) with a PBA.pro Internal Connection
       e.g. connect(button, "clicked()", dialog, "close()")

    2. Use to connect a signal of a QObject Src with a global python function
       e.g. connect(button, "clicked()", None, "global_def")

       where the function global_def must have at least the parameter sender,
       which is the QObject which has emitted the signal, plus the parameters of the signal
       e.g.
       def global_def(sender):
           do_something when button was clicked

    3. Use to connect a QObject Src with a method of a python class
       e.g. class test:
                def __init__(self):
                    .......
                    connect(button,"toggled(bool)",self,"memberfunc")

            def memberfunc(self,sender,bBoolParamOfSignal):
                # do_something when button was clicked

    Mode may be one of the following:
    auto:             Automatic Connection, either direct or queued depending on the thread
    queued:           Queued Connection to the Signal of the Sender.
                      The sender is not blocked.
    direct:           Direct Connection to the Signal of the Sender.
                      The sender is blocked, until all handler of the signal are executed.
                      Note: This connection type may be dangerous,
                      due to it influences the sender heavily.'''

# ----- Arguments Error checking -----

            # Confirm the Src is a defined. - Will generate a NameError if it isn't.
        type(Src)


            # Confirm the Signal is actually a Signal within Src.signals()
        if not Signal in Src.signals():
            raise SyntaxError("member not found: %s"%Signal)


            # Confirm Dest.Slot exists and that the correct arguments have been provided.

    # For connections made globally.
        if Dest == None:

            # Get all project *.py files.
            functionFound = False
            functionDefinitionLine = ""
            pyFiles = []
            cwd = os.getcwd().split("\\")[ : -1]
            newCwd = ""

            for item in cwd:
                newCwd += item + "\\"
            for dirpath, dirnames, filenames in os.walk(newCwd):
                for pyFile in filenames:
                    if ".py" in pyFile and ".pyc" not in pyFile and "PBApro.py" not in pyFile:
                        pyFiles.append(dirpath + "\\" + pyFile)

            # Ready the *.py files and l;ook for the requested functions.
            for pyFile in pyFiles:
                with open(pyFile, "r") as dataFile:
                    data = dataFile.readlines()

                # Search the python file for the correct function definition and save it's definition if found.
                for line in data:
                    if "def %s"%Slot == line[ : len("def %s"%Slot)]:
                        functionDefinitionLine = line
                        functionFound = True
                        break

            if functionFound:
                # Determine the function's arguments.
                funcArgs =  functionDefinitionLine.split("(")[1].replace("):", "").replace(" ", "").replace("\n", "").split(",")
                if funcArgs == ['']:
                    funcArgs = []
            else:
                raise NameError("name '%s' is not defined"%Slot)


    # For connections within a class.
        else:
            if not Slot in Dest.__class__.__dict__.keys():
                raise AttributeError("'%s' object has no attribute '%s'"%(str(type(Dest)).split(".")[1].replace("'>", ""), Slot))


# ----- Check for 'Sender' &/or 'Value'-----

    # For connections made globally.
        if Dest == None:
            if "()" in Signal:
                if len(funcArgs) != 1:
                    raise Exception("Connection Argument Error: Expected 1 argument - got %s."%len(funcArgs))
            else:
                if len(funcArgs) != 2:
                    raise Exception("Connection Argument Error: Expected 2 arguments - got %s."%len(funcArgs))

    # For connections within a class.
        else:
            funcArgs = inspect.getargspec(Dest.__class__.__dict__.get(Slot)).args
            if "()" in Signal:
                if len(funcArgs) != 2:
                    raise Exception("Connection Argument Error: Expected 2 arguments - got %s."%len(funcArgs))
            else:
                if len(funcArgs) != 3:
                    raise Exception("Connection Argument Error: Expected 3 arguments - got %s."%len(funcArgs))

        _connections.append((Src, Signal, Dest, Slot))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def disconnect(_Src, Signal, _Dest, Slot):
        '''Delete a previous connection.'''

        try:
            _connections.pop(_connections.index((_Src, Signal, _Dest, Slot)))
        except ValueError:
            raise Exception("cannot delete connection : %s_%s_%s_%s"%(_Src, Signal, _Dest, Slot))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def CleanPythonReceiver(object):
        '''This should be called in a Python __del__ member function to free all
    connections an instance has made.
    Note: Since PBA.pro Version 2.0 the connections of a Object are deleted
          automatically if an Python Object is deleted'''

        for connection in _connections:
            if object == connection[2]:
                _connections.pop(_connections.index(connection))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


    def PbaProObject(objectPath):
        '''This class encapsulates a PBA.pro Object.
        - Create a Object with _PbaProObject(Path)
        - Simple setting Properties by Object.Prop = Value
        - Simple reading Properties by Object.Prop
        - Calling Slots Object.Slot(Parameters)
        e.g.
        MyObject = _PbaProObject("ResourceList.MIL-Board1")
        # Get a Property
        print(MyObject.objectName)
        # Set a Property
        MyObject.objectName = "MyResource"
        # Call a Slot
        MyObject.Init()

        Restrictions:
          You cannot deal with objects which have characters in the name, which are interpreted
          as operator from python.
          e.g. ResourceList.MIL-Board1 cannot be used due to the interpreter try s to evaluate :
          ResourceList.MIL   Board1 which is not valid
          In this case you should call:
          MyRes = ResourceList.GetChild("MIL-Board1")
          and do the further operations on "MyRes".
          You may also replace invalid characters (-+/*#%&!()? ) by an underscore:
          ResourceList.MIL_Board1'''

        for instance in _PbaProObject._instances:
            if instance.objectPath() == objectPath:
                return instance
        raise TypeError("object not found: " + str(objectPath))
        #--------------------------------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                     Main Program.                                                                  #
#----------------------------------------------------------------------------------------------------------------------------------------------------#
    # Hidden global connections list.
    _connections = []

    # Create master _PbaProObjects
    # Wipe all previous instances.
    _PbaProObject._instances = []

    # Create master PBApro objects that exist within PBA.Pro but not within the XML files.
    _PbaProObject("DBSManager", "PDBSManager")
    _PbaProObject("PBApro", "PProApp")
    _PbaProObject("ResourceList", "PPResourceList")

    # Scan the *.ppro and *.tmpl files for potential XML _PbaProObjects() and create them.
    __parseXMLFiles()

    # Create other PBApro objects that exist within PBA.Pro but not within the XML files.
        # PbaProObject on all MIL-Boards.
    for i in range(1, 7):
        _PbaProObject("ResourceList.MIL-Board%s.Status"%i, "MilResourceStatus")
        _PbaProObject("ResourceList.MIL-Board%s.BC"%i, "MilBCSetup")

        # PbaProObject on only High Speed MIL-Boards.
        if i in range(1, 3):
            _PbaProObject("ResourceList.MIL-Board%s.BC.Status"%i, "MilHSBCStatus")

        # PbaProObject on only Low Speed MIL-Boards.
        if i in range(3, 7):
            _PbaProObject("ResourceList.MIL-Board%s.BC.Status"%i, "MilBCStatus")

else:
    pass # Do not create the _PbaProProject() class and PbaProObject() /function as this script has been run within PBA.Pro.
#----------------------------------------------------------------------------------------------------------------------------------------------------#
