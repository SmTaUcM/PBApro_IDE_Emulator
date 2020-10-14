template = {
# Class PPDBSParamAssignEntry
"PPDBSParamAssignEntry" : {
"completions" : [
{
"text": "ValueStr",
"rightLabel": "",
"type": "value",
"raw_type": "statement"
},

{
"text": "ValueRaw",
"rightLabel": "",
"type": "value",
"raw_type": "statement"
},

{
"text": "TestFunc",
"rightLabel": "",
"type": "function",
"raw_type": "function"
},

{
"text": "AnotherTestFunc",
"rightLabel": "",
"type": "function",
"raw_type": "function"
},
], # End of Completions

"tooltip" : {
"ValueStr" : [
{
"text": "",
"docstring": "Object Property\n\nThe Value Property interpreted as string. ",
"type": "value",
"description": "",
"signature": ""
}
],

"ValueRaw" : [
{
"text": "",
"docstring": "Object Property\n\nThe Value Property In the RAW Format from the datasource. ",
"type": "value",
"description": "",
"signature": ""
}
],

"TestFunc" : [
{
"text": "",
"docstring": "Test Func Doc String",
"type": "function",
"description": "",
"signature": "TestFunc(str: test, str: func) -> None"
},
],

"AnotherTestFunc" : [
{
"text": "",
"docstring": "Another Test Func Doc String",
"type": "function",
"description": "",
"signature": "AnotherTestFunc(str: help, str: me) -> None"
},
],

}, # End of Tooltips

"arguments" : {
"TestFunc" : [
{
"raw_docstring": "",
"name": "TestFunc",
"docstring": "TestFunc(str: test, str: func) -> None",
"params": [
{
"docstring": "",
"name": "test",
"value": None,
"description": "param test: str"
},

{
"docstring": "",
"name": "func",
"value": None,
"description": "param func: str"
}
],

"description": "def TestFunc"
}
],

"AnotherTestFunc" : [
{
"raw_docstring": "",
"name": "TestFunc",
"docstring": "AnotherTestFunc(str: help, str: me) -> None",
"params": [
{
"docstring": "",
"name": "help",
"value": None,
"description": "param help: str"
},

{
"docstring": "",
"name": "me",
"value": None,
"description": "param me: str"
}
],

"description": "def AnotherTestFunc"
}
],
},# End of Arguments
} # End of PPDBSParamAssignEntry
} # End of template.s