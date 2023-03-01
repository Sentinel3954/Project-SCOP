abi_suport = """
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_data",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_struct",
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
		"name": "CheckRegister",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
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
		"name": "HaveActiveProject",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
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
		"name": "_checksForProject",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
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
				"internalType": "address",
				"name": "_sender",
				"type": "address"
			}
		],
		"name": "_checksForRegistration",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
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
		"name": "_findActiveProject",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "activeProject",
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
				"name": "_helpContr",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_structs",
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
				"internalType": "uint256",
				"name": "_numProject",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_loginStudent",
				"type": "string"
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
				"name": "_newStudent",
				"type": "address"
			}
		],
		"name": "generateAddressForStudent",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""