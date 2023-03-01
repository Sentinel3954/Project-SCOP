// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./GlobalStorage.sol";

contract MakeStruct0 {

    GlobalStorage data;

    enum StatusAddress {Not, Block, ForTeacher, ForStudent, ForAdmin, Teacher, Student, Admin}

    event Action (address hero, address target, uint numProject, string text);

    struct Teacher {
        string login;
        string FIO;
        uint16[] numSchoolSubjects;
        uint16[] numLaboratories;
        uint[] numActiveProjects;
        uint[] invitationsToProject;
        uint[] completedProjects;
        uint[] applicationsForCompletionProject;
        bool scientistManager;
    }

    string[] public keys;

    address ownerContract;
    address[] logicContracts;

    modifier onlyContract() {
        bool flag = false;
        for (uint16 i = 0; i < logicContracts.length; i++){
            if (msg.sender == logicContracts[i]) {
                flag = true;
                break;
            }
        }
        require(flag);
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == ownerContract);
        _;
    }

    constructor (address _dataContract) {
        data = GlobalStorage(_dataContract);
        keys = ["0 - FIO (user)", "1 - login (user)", "2 - class letter (student)", "3 - school subjects (general)", "4 - laboratories (general)", "5 - completed projects (teacher, student)",
            "6 - strong sides (student)", "7 - using logins (general)", "8 - class number (student)", "9 - status address (user)", "10 - applications for completion of the project",
            "11 - numbers school subject (teacher)", "12 - numbers laboratory (teacher)", "13 - belong active projects (teacher)", "14 - password (user)", "15",
            "16 - scientist manager (teacher)", "17 - main (admin)", "18 - name (project)", "19 - goal (project)", "20 - role student (project)",
            "21 - tasks student (project)", "22 - mentor (project)", "23 - members (project)", "24 - number laboratory (project)", "25 - status (project)",
            "26 - numbers school subjects (project)", "27 - quantity projects (general)", "28 - added users (user)", "29 - quantity laboratories (general)", "30 - quantity school subjects (general)",
            "31", "32", "33 - teachers in laboratory (general)", "34 - teachers, leads school subject (general)", "35 - belong archive project (user)",
            "36", "37 - deadline for task (project)", "38 - quantity tasks student (project)", "39 - quantity strong sides (student)", "40 - belong active project (student)",
            "41 - number complete task (project)", "42 - creator (project)", "43 - invitation to project (student, teacher)"];

        ownerContract = msg.sender;
        logicContracts.push(msg.sender);
    }

//Secure function

    function getAddressesContract() public view returns (address[] memory) {
        return logicContracts;
    }

    function getOwnerContract() public view returns (address) {
        return ownerContract;
    }

    function addAddressContract(address _newContract) public onlyOwner() {
        logicContracts.push(_newContract);

        emit Action(msg.sender, _newContract, 0, "New logic contract add");
    }

    function deleteAddressContract(address _oldContract) public onlyOwner() {
        for (uint i = 0; i < logicContracts.length; i++) {
            if (logicContracts[i] == _oldContract) {
                uint lastElement = uint(logicContracts.length) - 1;
                logicContracts[i] = logicContracts[lastElement];
                logicContracts.pop();

                emit Action(msg.sender, _oldContract, 0, "Contract deleted");
            }
        }
    }

    function changeOwnerContract(address _newOwner) public onlyOwner() {
        ownerContract = _newOwner;
    }

    // View functions
    // help functions
    function getSchoolSubjects() external view returns (string[] memory schoolSubjects) {
        schoolSubjects = data.getStringArrayDataUser(keccak256(abi.encodePacked(keys[3])));
    }

    function getLaboratories() external view returns (string[] memory laboratories) {
        laboratories = data.getStringArrayDataUser(keccak256(abi.encodePacked(keys[4])));
    }
    
    // functions for teacher and student
    function getPassword(address _user) external view returns (bytes32 pass) {
        pass = data.getBytes32DataUser(keccak256(abi.encodePacked(_user, keys[14])));
    }

    function getAddress(string memory _loginUser) public view returns (address user) {
        user = data.getAddressDataUser(keccak256(abi.encodePacked(_loginUser, keys[7])));
    }

    function getLogin(address _user) external view returns (string memory login) {
        login = data.getStringDataUser(keccak256(abi.encodePacked(_user, keys[1])));
    }

    function getStatusAddress(address _user) external view returns (StatusAddress status) {
        status = StatusAddress(data.getUint8DataUser(keccak256(abi.encodePacked(_user, keys[9]))));
    }

    // student's functions
    function getStudentStruct(address _student) external view 
        returns (
        string memory login,
        string memory FIO,
        string memory classLetter, 
        string[] memory strongSides,
        uint8 class,
        uint numActiveProject,
        uint[] memory invitationsToProject,
        uint[] memory completedProjects)
    {
        login = data.getStringDataUser(keccak256(abi.encodePacked(_student, keys[1])));
        FIO = data.getStringDataUser(keccak256(abi.encodePacked(_student, keys[0])));
        classLetter = data.getStringDataUser(keccak256(abi.encodePacked(_student, keys[2])));
        strongSides = data.getStringArrayDataUser(keccak256(abi.encodePacked(_student, keys[6])));
        class = data.getUint8DataUser(keccak256(abi.encodePacked(_student, keys[8])));
        numActiveProject = data.getUintDataUser(keccak256(abi.encodePacked(_student, keys[40])));
        invitationsToProject = data.getUintArrayDataUser(keccak256(abi.encodePacked(_student, keys[43])));
        completedProjects = data.getUintArrayDataUser(keccak256(abi.encodePacked(_student, keys[5])));
    }

    function getQuantityStrongSides(address _student) external view returns (uint8 quantityStrongSides) {
        return data.getUint8DataUser(keccak256(abi.encodePacked(_student, keys[39])));
    }

    // teacher's functions
    function getTeacherStruct(address _teacher) external view returns (Teacher memory)
    {
        string memory login = data.getStringDataUser(keccak256(abi.encodePacked(_teacher, keys[1])));
        string memory FIO = data.getStringDataUser(keccak256(abi.encodePacked(_teacher, keys[0])));
        uint16[] memory numSchoolSubjects = data.getUint16ArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[11])));
        uint16[] memory numLaboratories = data.getUint16ArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[12])));
        bool scientistManager = data.getBoolDataUser(keccak256(abi.encodePacked(_teacher, keys[16])));
        uint[] memory numActiveProjects = data.getUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[13])));
        uint[] memory invitationsToProject = data.getUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[43])));
        uint[] memory completedProjects = data.getUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[5])));
        uint[] memory applicationsForCompletionProject = data.getUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[10])));

        return ((Teacher(login, FIO, numSchoolSubjects, numLaboratories, numActiveProjects, invitationsToProject, completedProjects, applicationsForCompletionProject, scientistManager)));
    }

    function getAddedUsers(address _sender) view external returns (address[] memory addedUsers) {
        addedUsers = data.getAddressArrayDataUser(keccak256(abi.encodePacked(_sender, keys[28])));
    }

    // help functions
    function addSubjectTeacher(string memory _login, uint16[] memory _schoolSubjects) external {
        for (uint16 i = 0; i < _schoolSubjects.length; i++) {
            data.addStringArrayDataUser(keccak256(abi.encodePacked(_schoolSubjects[i], keys[34])), _login);
        }
    }

    // Change functions
    // General functions for teacher and student
    function setLogin(string memory _login, address _user) external {
        data.setStringDataUser(keccak256(abi.encodePacked(_user, keys[1])), _login);
        data.setAddressDataUser(keccak256(abi.encodePacked(_login, keys[7])), _user); // логин закрепляется за адресом ученика
    }

    function setFIO(string memory _FIO, address _user) external {
        data.setStringDataUser(keccak256(abi.encodePacked(_user, keys[0])), _FIO);
    }

    function setStatusAddress(address _user, uint8 _statusAddress) external {
        data.setUint8DataUser(keccak256(abi.encodePacked(_user, keys[9])), _statusAddress); // изменение статуса адреса
    }

    function setPass(string memory _login, string memory _pass, address _student) external {
        data.setBytes32DataUser(keccak256(abi.encodePacked(_student, keys[14])), keccak256(abi.encodePacked(_login, _pass)));
    }

    function increaceQuantityStrongSides(address _student) external {
        data.setUint8DataUser(keccak256(abi.encodePacked(_student, keys[39])), this.getQuantityStrongSides(_student) + 1);
    }

    // Student functions
    function setStudentClassLetter(string memory _classLetter, address _student) external {
        data.setStringDataUser(keccak256(abi.encodePacked(_student, keys[2])), _classLetter);
    }

    function setStudentClass(address _student, uint8 _class) external {
        data.setUint8DataUser(keccak256(abi.encodePacked(_student, keys[8])), _class);
    }

    function setFullStrongSides(string[] memory _strongSides, address _student) external {
        data.setFullStringArrayDataUser(keccak256(abi.encodePacked(_student, keys[6])), _strongSides);
    }

    function addStudentStrongSide(string memory _text, address _student) external {
        data.addStringArrayDataUser(keccak256(abi.encodePacked(_student, keys[6])), _text);
    }

    function changeStudentStrongSide(string memory _text, address _student, uint16 _numStrongSide) external {
        data.setStringArrayDataUser(keccak256(abi.encodePacked(_student, keys[6])), _numStrongSide, _text);
    }

    // Teachers functions
    function setTeacherSchoolSubjects(address _teacher, uint16[] memory _numSchoolSubjects) external {
        data.setFullUint16ArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[11])), _numSchoolSubjects);
    }

    function setTeacherLaboratories(address _teacher, uint16[] memory _numLaboratories) external {
        data.setFullUint16ArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[12])), _numLaboratories);
    }

    function setHeadTeacher(address _teacher, bool _headTeacher) external {
        data.setBoolDataUser(keccak256(abi.encodePacked(_teacher, keys[15])), _headTeacher);
    }

    function setScientistManager(address _teacher, bool _scientistManager) external {
        data.setBoolDataUser(keccak256(abi.encodePacked(_teacher, keys[16])), _scientistManager);
    }

    function setAddedUsers(address _sender, address _user) external {
        data.addAddressArrayDataUser(keccak256(abi.encodePacked(_sender, keys[28])), _user);
    }

    function setFullAddedUsers(address _sender, address[] memory _addedUsers) external  onlyContract() {
        data.setFullAddressArrayDataUser(keccak256(abi.encodePacked(_sender, keys[28])), _addedUsers);
    }
}