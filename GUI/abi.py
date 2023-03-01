abi_make_struct0 = """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_dateStartInSeconds",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_newContract",
				"type": "address"
			}
		],
		"name": "addAddressContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "addStudentStrongSide",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "uint16[]",
				"name": "_schoolSubjects",
				"type": "uint16[]"
			}
		],
		"name": "addSubjectTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_newOwner",
				"type": "address"
			}
		],
		"name": "changeOwnerContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint16",
				"name": "_numStrongSide",
				"type": "uint16"
			}
		],
		"name": "changeStudentStrongSide",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_oldContract",
				"type": "address"
			}
		],
		"name": "deleteAddressContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "getAddedUsers",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "addedUsers",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginUser",
				"type": "string"
			}
		],
		"name": "getAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAddressesContract",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLaboratories",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "laboratories",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getLogin",
		"outputs": [
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwnerContract",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getPassword",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "pass",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "getQuantityStrongSides",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "quantityStrongSides",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getSchoolSubjects",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "schoolSubjects",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "getStatusAddress",
		"outputs": [
			{
				"internalType": "enum MakeStruct0.StatusAddress",
				"name": "status",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "getStudentStruct",
		"outputs": [
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "FIO",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "classLetter",
				"type": "string"
			},
			{
				"internalType": "string[]",
				"name": "strongSides",
				"type": "string[]"
			},
			{
				"internalType": "uint8",
				"name": "class",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "numActiveProject",
				"type": "uint256"
			},
			{
				"internalType": "uint256[]",
				"name": "invitationsToProject",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			}
		],
		"name": "getTeacherStruct",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "login",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "FIO",
						"type": "string"
					},
					{
						"internalType": "uint16[]",
						"name": "numSchoolSubjects",
						"type": "uint16[]"
					},
					{
						"internalType": "uint16[]",
						"name": "numLaboratories",
						"type": "uint16[]"
					},
					{
						"internalType": "uint256[]",
						"name": "numActiveProjects",
						"type": "uint256[]"
					},
					{
						"internalType": "uint256[]",
						"name": "invitationsToProject",
						"type": "uint256[]"
					},
					{
						"internalType": "bool",
						"name": "scientistManager",
						"type": "bool"
					}
				],
				"internalType": "struct MakeStruct0.Teacher",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "increaceQuantityStrongSides",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "keys",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "setAddedUsers",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_FIO",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "setFIO",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			},
			{
				"internalType": "address[]",
				"name": "_addedUsers",
				"type": "address[]"
			}
		],
		"name": "setFullAddedUsers",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string[]",
				"name": "_strongSides",
				"type": "string[]"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "setFullStrongSides",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "_headTeacher",
				"type": "bool"
			}
		],
		"name": "setHeadTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			}
		],
		"name": "setLogin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "setPass",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "_scientistManager",
				"type": "bool"
			}
		],
		"name": "setScientistManager",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_user",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "_statusAddress",
				"type": "uint8"
			}
		],
		"name": "setStatusAddress",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "_class",
				"type": "uint8"
			}
		],
		"name": "setStudentClass",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_classLetter",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "setStudentClassLetter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "uint16[]",
				"name": "_numLaboratories",
				"type": "uint16[]"
			}
		],
		"name": "setTeacherLaboratories",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "uint16[]",
				"name": "_numSchoolSubjects",
				"type": "uint16[]"
			}
		],
		"name": "setTeacherSchoolSubjects",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "startBlock",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "startDate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
"""
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
abi_make_struct1 = """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_dateStartInSeconds",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "addActiveProjectTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_newContract",
				"type": "address"
			}
		],
		"name": "addAddressContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_date",
				"type": "uint256"
			}
		],
		"name": "addDeadline",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_recipient",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_inProject",
				"type": "uint256"
			}
		],
		"name": "addInvitation",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numLaboratory",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			}
		],
		"name": "addLaboratoryTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_newMember",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "addMemberInProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "addTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			},
			{
				"internalType": "uint16",
				"name": "_lab",
				"type": "uint16"
			}
		],
		"name": "addTeacherNumLaboratories",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_newOwner",
				"type": "address"
			}
		],
		"name": "changeOwnerContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint16",
				"name": "_numTask",
				"type": "uint16"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "changeTextTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_oldContract",
				"type": "address"
			}
		],
		"name": "deleteAddressContract",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAddressesContract",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint8",
				"name": "_numTask",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getDeadLineTask",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "deadlineTask",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getDeadLinesStudent",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "deadlineTask",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getNumCompletionTasks",
		"outputs": [
			{
				"internalType": "uint16[]",
				"name": "readyTasksProject",
				"type": "uint16[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwnerContract",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getProjectStruct",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "goal",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "mentor",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "creator",
						"type": "address"
					},
					{
						"internalType": "address[]",
						"name": "members",
						"type": "address[]"
					},
					{
						"internalType": "uint16",
						"name": "statusProject",
						"type": "uint16"
					},
					{
						"internalType": "uint16",
						"name": "numLaboratory",
						"type": "uint16"
					},
					{
						"internalType": "uint16[]",
						"name": "needSchoolSubjects",
						"type": "uint16[]"
					}
				],
				"internalType": "struct MakeStruct1.Project",
				"name": "project",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getQuantityLaboratories",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quantityLaboratories",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getQuantityProjects",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "quantityProjects",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getQuantityTasks",
		"outputs": [
			{
				"internalType": "uint16",
				"name": "quantityTask",
				"type": "uint16"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getRole",
		"outputs": [
			{
				"internalType": "string",
				"name": "role",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "getTasks",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "tasks",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numLaboratory",
				"type": "uint256"
			}
		],
		"name": "getTeachersInLaboratory",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "_teachers",
				"type": "address[]"
			},
			{
				"internalType": "address",
				"name": "_headTeacher",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "increaceQuantityTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "increaseQuantityProjects",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "keys",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setActiveProjectStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			},
			{
				"internalType": "uint16",
				"name": "_num",
				"type": "uint16"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setActiveProjectTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_recipient",
				"type": "address"
			},
			{
				"internalType": "uint256[]",
				"name": "_allInvitations",
				"type": "uint256[]"
			}
		],
		"name": "setAllInvitations",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address[]",
				"name": "_members",
				"type": "address[]"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setAllMemberProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_creator",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setCreatorProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint16",
				"name": "_numTask",
				"type": "uint16"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_date",
				"type": "uint256"
			}
		],
		"name": "setDeadline",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numLaboratory",
				"type": "uint256"
			},
			{
				"internalType": "address[]",
				"name": "_teachers",
				"type": "address[]"
			}
		],
		"name": "setFullLaboratoryTeachers",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			},
			{
				"internalType": "uint16[]",
				"name": "_labs",
				"type": "uint16[]"
			}
		],
		"name": "setFullTeacherNumLaboratories",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_goal",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setGoalInProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string[]",
				"name": "laboratories",
				"type": "string[]"
			}
		],
		"name": "setLaboratories",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numLaboratory",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_headTeacher",
				"type": "address"
			}
		],
		"name": "setLaboratoryHeadlTeacher",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16",
				"name": "_numLaboratory",
				"type": "uint16"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setLaboratoryProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numLaboratory",
				"type": "uint256"
			},
			{
				"internalType": "address[]",
				"name": "_teachers",
				"type": "address[]"
			},
			{
				"internalType": "address",
				"name": "_headTeacher",
				"type": "address"
			}
		],
		"name": "setLaboratoryStruct",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_mentor",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setMentorProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setNameProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_roleMember",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setRoleMember",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string[]",
				"name": "schoolSubjects",
				"type": "string[]"
			}
		],
		"name": "setSchoolSubjects",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint16[]",
				"name": "_numSchoolSubjects",
				"type": "uint16[]"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setSchoolSubjectsProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "enum MakeStruct1.StatusProject",
				"name": "_status",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "setStatusProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			},
			{
				"internalType": "uint16",
				"name": "_numTask",
				"type": "uint16"
			}
		],
		"name": "setTaskComplete",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "startBlock",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "startDate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
"""
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
abi_student0= """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs0",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs1",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			}
		],
		"name": "addStrongSide",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "auth",
		"outputs": [
			{
				"internalType": "bool",
				"name": "a",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_newText",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "_numStrongSide",
				"type": "uint8"
			}
		],
		"name": "changeStrongSide",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "checkStudent",
		"outputs": [
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "FIO",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "classLetter",
				"type": "string"
			},
			{
				"internalType": "string[]",
				"name": "strongSides",
				"type": "string[]"
			},
			{
				"internalType": "uint8",
				"name": "numClass",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "numActiveProject",
				"type": "uint256"
			},
			{
				"internalType": "uint256[]",
				"name": "invitationsToProject",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "constructData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_FIO",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_classLetter",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "_class",
				"type": "uint8"
			}
		],
		"name": "registration",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################



abi_student1= """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs0",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs1",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_deadline",
				"type": "uint256"
			}
		],
		"name": "addTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "auth",
		"outputs": [
			{
				"internalType": "bool",
				"name": "a",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_goal",
				"type": "string"
			}
		],
		"name": "changeGoalProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_role",
				"type": "string"
			}
		],
		"name": "changeRole",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "_numTask",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_deadline",
				"type": "uint256"
			}
		],
		"name": "changeTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_student",
				"type": "address"
			}
		],
		"name": "checkDataStudentInProject",
		"outputs": [
			{
				"internalType": "string",
				"name": "roleMember",
				"type": "string"
			},
			{
				"internalType": "string[]",
				"name": "tasksMember",
				"type": "string[]"
			},
			{
				"internalType": "uint256[]",
				"name": "deadLines",
				"type": "uint256[]"
			},
			{
				"internalType": "uint16[]",
				"name": "numReadyTask",
				"type": "uint16[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "checkProject",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "goal",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "mentor",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "creator",
						"type": "address"
					},
					{
						"internalType": "address[]",
						"name": "members",
						"type": "address[]"
					},
					{
						"internalType": "uint16",
						"name": "statusProject",
						"type": "uint16"
					},
					{
						"internalType": "uint16",
						"name": "numLaboratory",
						"type": "uint16"
					},
					{
						"internalType": "uint16[]",
						"name": "needSchoolSubjects",
						"type": "uint16[]"
					}
				],
				"internalType": "struct MakeStruct1.Project",
				"name": "project",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "constructData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_nameProject",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginMentor",
				"type": "string"
			},
			{
				"internalType": "uint16",
				"name": "_numLaboratory",
				"type": "uint16"
			},
			{
				"internalType": "uint16[]",
				"name": "_needSchoolSubjects",
				"type": "uint16[]"
			}
		],
		"name": "createProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginInvited",
				"type": "string"
			}
		],
		"name": "inviteToProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "joinInProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""


##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################


abi_teacher = """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs0",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs1",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginTeacher",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "addStudentInProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "auth",
		"outputs": [
			{
				"internalType": "bool",
				"name": "a",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginTeacher",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_text",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "_numTask",
				"type": "uint8"
			},
			{
				"internalType": "uint256",
				"name": "_deadline",
				"type": "uint256"
			}
		],
		"name": "changeTaskStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_teacher",
				"type": "address"
			}
		],
		"name": "checkTeacher",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "login",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "FIO",
						"type": "string"
					},
					{
						"internalType": "uint16[]",
						"name": "numSchoolSubjects",
						"type": "uint16[]"
					},
					{
						"internalType": "uint16[]",
						"name": "numLaboratories",
						"type": "uint16[]"
					},
					{
						"internalType": "uint256[]",
						"name": "numActiveProjects",
						"type": "uint256[]"
					},
					{
						"internalType": "uint256[]",
						"name": "invitationsToProject",
						"type": "uint256[]"
					},
					{
						"internalType": "bool",
						"name": "scientistManager",
						"type": "bool"
					}
				],
				"internalType": "struct MakeStruct0.Teacher",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginTeacher",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
			},
			{
				"internalType": "uint8",
				"name": "_numTask",
				"type": "uint8"
			}
		],
		"name": "completeTask",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "constructData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_nameProject",
				"type": "string"
			},
			{
				"internalType": "uint16",
				"name": "_numLaboratory",
				"type": "uint16"
			}
		],
		"name": "createProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_loginTeacher",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
			}
		],
		"name": "deleteStudentOutProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_newStudent",
				"type": "address"
			}
		],
		"name": "generateAddressForStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			}
		],
		"name": "joinInProject",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_FIO",
				"type": "string"
			},
			{
				"internalType": "uint16[]",
				"name": "_leadsSchoolSubjects",
				"type": "uint16[]"
			},
			{
				"internalType": "uint16[]",
				"name": "_numLaboratories",
				"type": "uint16[]"
			}
		],
		"name": "registration",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################

abi_guifunction = """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_dataContract",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs0",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs1",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "hero",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "target",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "numProject",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "text",
				"type": "string"
			}
		],
		"name": "Action",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_pass",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "auth",
		"outputs": [
			{
				"internalType": "bool",
				"name": "a",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "constructData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_recipient",
				"type": "address"
			}
		],
		"name": "myTransfer",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]
"""





