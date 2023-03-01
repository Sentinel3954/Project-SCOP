// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./GlobalStorage.sol";
import "./MakeStruct0.sol";

contract MakeStruct1 {

    GlobalStorage data;
    MakeStruct0 structs0;

    enum StatusProject {Not, Completed, Sleep, Active}
    enum StatusAddress {Not, Block, ForTeacher, ForStudent, ForAdmin, Teacher, Student, Admin}

    event Action (address hero, address target, uint numProject, string text);
    
    struct Project {
        string name;
        string goal;
        address mentor;
        address creator;
        address[] members;
        uint16 statusProject;
        uint16 numLaboratory;
        uint16[] needSchoolSubjects;
    }

    string[] public keys;

    address ownerContract;
    address[] logicContracts;

    uint public startBlock;
    uint public startDate;

    modifier onlyContract() {
        bool flag = false;
        for (uint16 i = 0; i < logicContracts.length; i++){
            flag = (flag || (msg.sender == logicContracts[i]));
        }
        require(flag);
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == ownerContract);
        _;
    }
    

    constructor (address _dataContract, uint _dateStartInSeconds) {
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
        startBlock = block.number;
        startDate = _dateStartInSeconds;
    }
    

//Secure functions

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

    // view project functions
    function getProjectStruct(uint _numProject) external view returns (Project memory project)
    {
        string memory name = data.getStringDataProject(keccak256(abi.encodePacked(_numProject, keys[18])));
        string memory goal = data.getStringDataProject(keccak256(abi.encodePacked(_numProject, keys[19])));
        address mentor = data.getAddressDataProject(keccak256(abi.encodePacked(_numProject, keys[22])));
        address creator = data.getAddressDataProject(keccak256(abi.encodePacked(_numProject, keys[42])));
        address[] memory members = data.getAddressArrayDataProject(keccak256(abi.encodePacked(_numProject, keys[23])));
        uint16 statusProject = data.getUint16DataProject(keccak256(abi.encodePacked(_numProject, keys[25])));
        uint16 numLaboratory = data.getUint16DataProject(keccak256(abi.encodePacked(_numProject, keys[24])));
        uint16[] memory needSchoolSubjects = data.getUint16ArrayDataProject(keccak256(abi.encodePacked(_numProject, keys[26])));

        project = Project(name, goal, mentor, creator, members, statusProject, numLaboratory, needSchoolSubjects);
    }

    function getRole(address _student, uint _numProject) external view returns (string memory role) {
        role = data.getStringDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[20])));
    }

    function getQuantityProjects() public view returns (uint quantityProjects) {
        quantityProjects = data.getUintDataProject(keccak256(abi.encodePacked(keys[27])));
    }

    // Задачи и дедлайны
    // Функция возвращает даты (в секундах), когда задачи были выполнены
    function getQuantityTasks(address _student, uint _numProject) external view returns (uint16 quantityTask) {
        return data.getUint16DataProject(keccak256(abi.encodePacked(_numProject, _student, keys[38])));
    }

    function getTasks(address _student, uint _numProject) external view returns (string[] memory tasks) {
        tasks = data.getStringArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[21])));
    }

    function getNumCompletionTasks(address _student, uint _numProject) view external returns (uint16[] memory readyTasksProject) {
        readyTasksProject = data.getUint16ArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[41])));
    }

    function getDeadLineTask(address _student, uint8 _numTask, uint _numProject) view external returns (uint deadlineTask) {
        deadlineTask = data.getUintArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[37])))[_numTask];
    }

    // Функция возвращает дату (в секундах), к которой должна быть выполнена задача
    function getDeadLinesStudent(address _student, uint _numProject) view external returns (uint[] memory deadlineTask) {
        deadlineTask = data.getUintArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[37])));
    }

    // functions for teacher and student
    function addInvitation(address _recipient, uint _inProject) external {
        data.addUintArrayDataUser(keccak256(abi.encodePacked(_recipient, keys[43])), _inProject);
    }

    function setAllInvitations(address _recipient, uint[] memory _allInvitations) external {
        data.setFullUintArrayDataUser(keccak256(abi.encodePacked(_recipient, keys[43])), _allInvitations);
    }

    // student functions with project
    function setActiveProjectStudent(address _student, uint _numProject) external {
        data.setUintDataUser(keccak256(abi.encodePacked(_student, keys[40])), _numProject); // участвует в проекте
    }

    // teacher functions with project
    function addActiveProjectTeacher(address _teacher, uint _numProject) external {
        data.addUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[13])), _numProject); // руководит проектом
    }

    function setActiveProjectTeacher(address _teacher, uint16 _num, uint _numProject) external {
        data.setUintArrayDataUser(keccak256(abi.encodePacked(_teacher, keys[13])), _num, _numProject); // участвует в проекте
    }

    function tryCompleteProject(address _mentor, uint _numActiveProject) external {
        data.addUintArrayDataUser(keccak256(abi.encodePacked(_mentor, keys[10])), _numActiveProject);
    }

    // function completeProject(uint _numProject) external {
    //     completedProjects = data.addUintArrayDataUser(keccak256(abi.encodePacked(_student, keys[5])));
    // }

    // change projects functions
    function increaseQuantityProjects() external {
        data.setUintDataProject(keccak256(abi.encodePacked(keys[27])), getQuantityProjects() + 1);
    }

    function setNameProject(string memory _name, uint _numProject) external {
        data.setStringDataProject(keccak256(abi.encodePacked(_numProject, keys[18])), _name);
    }

    function setMentorProject(address _mentor, uint _numProject) external {
        data.setAddressDataProject(keccak256(abi.encodePacked(_numProject, keys[22])), _mentor);
    }

    function addMemberInProject(address _newMember, uint _numProject) external {
        data.addAddressArrayDataProject(keccak256(abi.encodePacked(_numProject, keys[23])), _newMember);
    }

    function setAllMemberProject(address[] memory _members, uint _numProject) external {
        data.setFullAddressArrayDataProject(keccak256(abi.encodePacked(_numProject, keys[23])), _members);
    }

    function setSchoolSubjectsProject(uint16[] memory _numSchoolSubjects, uint _numProject) external {
        data.setFullUint16ArrayDataProject(keccak256(abi.encodePacked(_numProject, keys[26])), _numSchoolSubjects);    
    }

    function setLaboratoryProject(uint16 _numLaboratory, uint _numProject) external {
        data.setUint16DataProject(keccak256(abi.encodePacked(_numProject, keys[24])), _numLaboratory);
    }

    function setGoalInProject(string memory _goal, uint _numProject) external  onlyContract() {
        data.setStringDataProject(keccak256(abi.encodePacked(_numProject, keys[19])), _goal);
    }

    function setStatusProject(StatusProject _status, uint _numProject) external {
        data.setUint16DataProject(keccak256(abi.encodePacked(_numProject, keys[25])), uint16(_status));
    }

    function setRoleMember(string memory _roleMember, address _student, uint _numProject) external {
        data.setStringDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[20])), _roleMember);
    }

    function setCreatorProject(address _creator, uint _numProject) external {
        data.setAddressDataProject(keccak256(abi.encodePacked(_numProject, keys[42])), _creator);
    }

    // Задачи и дедлайны
    function increaceQuantityTask(address _student, uint _numProject) external {
        data.setUint16DataProject(keccak256(abi.encodePacked(_numProject, _student, keys[38])), this.getQuantityTasks(_student, _numProject) + 1);
    }

    function addTask(string memory _text, address _student, uint _numProject) external {
        data.addStringArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[21])), _text);
    }

    function changeTextTask(string memory _text, address _student, uint16 _numTask, uint _numProject) external {
        data.setStringArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[21])), _numTask, _text);
    }

    function addDeadline(address _student, uint _numProject, uint _date) external {
        data.addUintArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[37])), _date);
    }

    function setDeadline(address _student, uint16 _numTask, uint _numProject, uint _date) external {
        data.setUintArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[37])), _numTask, _date);
    }

    function setTaskComplete(address _student, uint _numProject, uint16 _numTask) external {
        data.addUint16ArrayDataProject(keccak256(abi.encodePacked(_numProject, _student, keys[41])), _numTask);
    }







    // Help functions
    // View
    function getQuantityLaboratories() external view returns (uint quantityLaboratories) {
        quantityLaboratories = data.getUint16DataUser(keccak256(abi.encodePacked(keys[29])));
    }

    // Change function
    function setLaboratories(string[] memory laboratories) external {
        data.setFullStringArrayDataUser(keccak256(abi.encodePacked(keys[4])), laboratories);
        data.setUint16DataUser(keccak256(abi.encodePacked(keys[29])), uint16(laboratories.length));
    }

    function setSchoolSubjects(string[] memory schoolSubjects) external {
        data.setFullStringArrayDataUser(keccak256(abi.encodePacked(keys[21])), schoolSubjects);
        data.setUint16DataUser(keccak256(abi.encodePacked(keys[30])), uint16(schoolSubjects.length));
    }

    


















    // Dop function
    function getTeachersInLaboratory(uint _numLaboratory) view external returns(address[] memory _teachers, address _headTeacher) {
        _teachers = data.getAddressArrayDataProject(keccak256(abi.encodePacked(_numLaboratory, keys[45])));
        _headTeacher = data.getAddressDataUser(keccak256(abi.encodePacked(_numLaboratory, keys[44])));
    }

    function setLaboratoryStruct(uint _numLaboratory, address[] memory _teachers, address _headTeacher) external {
        data.setAddressDataUser(keccak256(abi.encodePacked(_numLaboratory, keys[44])), _headTeacher);
        data.setFullAddressArrayDataProject(keccak256(abi.encodePacked(_numLaboratory, keys[45])), _teachers);
    }

    function addLaboratoryTeacher(uint _numLaboratory, address _teacher) external {
        data.addAddressArrayDataProject(keccak256(abi.encodePacked(_numLaboratory, keys[45])), _teacher);
    }

    function setFullLaboratoryTeachers(uint _numLaboratory, address[] memory _teachers) external {
        data.setFullAddressArrayDataProject(keccak256(abi.encodePacked(_numLaboratory, keys[45])), _teachers);
    }

    function setLaboratoryHeadlTeacher(uint _numLaboratory, address _headTeacher) external {
        data.setAddressDataUser(keccak256(abi.encodePacked(_numLaboratory, keys[44])), _headTeacher);
    }

    function addTeacherNumLaboratories(address _addr, uint16 _lab) external {
        data.addUint16ArrayDataUser(keccak256(abi.encodePacked(_addr, keys[8])), _lab);
    }

    function setFullTeacherNumLaboratories(address _address, uint16[] memory _labs) external {
        data.setFullUint16ArrayDataProject(keccak256(abi.encodePacked(_address, keys[45])), _labs);
    }
}