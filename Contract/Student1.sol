// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./Support.sol";

contract Student is Support {

    modifier onlyStudent() {
        MakeStruct0.StatusAddress status = structs0.getStatusAddress(msg.sender);
        if (status != MakeStruct0.StatusAddress.Student) { // проверка статуса пользователя
            emit Action(msg.sender, address(0), 0, "ERROR: only student");
            return;
        }
        _;
    }


    constructor (address _dataContract, address _structs0, address _structs1) Support(_dataContract, _structs0, _structs1) {}
    

    // view functions
    function checkDataStudentInProject(address _student) public view 
        returns (
        string memory roleMember,
        string[] memory tasksMember,
        uint[] memory deadLines,
        uint16[] memory numReadyTask) 
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(_student);
        roleMember = structs1.getRole(_student, numActiveProject);
        tasksMember = structs1.getTasks(_student, numActiveProject);
        deadLines = structs1.getDeadLinesStudent(_student, numActiveProject);
        numReadyTask = structs1.getNumCompletionTasks(_student, numActiveProject);
    }

    // private functions


    // Project functions
    function createProject(
        string memory _loginStudent,
        string memory _pass,
        string memory _nameProject,
        string memory _loginMentor,
        uint16 _numLaboratory,
        uint16[] memory _needSchoolSubjects)
        public userRegistered(_loginStudent, _pass, msg.sender) onlyStudent()
    {
        if (_normalText(_nameProject)) {
            address mentor = structs0.getAddress(_loginMentor);
            (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);

            if (numActiveProject == 0) {
                if (structs0.getStatusAddress(mentor) == MakeStruct0.StatusAddress.Teacher) {
                    uint numNewProject = structs1.getQuantityProjects() + 1;
                    structs1.increaseQuantityProjects();

                    structs1.setNameProject(_nameProject, numNewProject);
                    structs1.addInvitation(mentor, numNewProject); // отправляется приглашение учителю
                    structs1.addMemberInProject(msg.sender, numNewProject);
                    structs1.setLaboratoryProject(_numLaboratory, numNewProject);
                    structs1.setSchoolSubjectsProject(_needSchoolSubjects, numNewProject);
                    structs1.setStatusProject(MakeStruct1.StatusProject.Active, numNewProject);
                    structs1.setCreatorProject(msg.sender, numNewProject);

                    structs1.setActiveProjectStudent(msg.sender, numNewProject);

                    emit Action(msg.sender, address(0), numNewProject, "Project create");
                }
                else {
                    emit Action(msg.sender, address(0), 0, "ERROR: teacher not exist");
                } 
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: you already have active project");
            }
        }
    }

    function inviteToProject(
        string memory _login,
        string memory _pass,
        string memory _loginInvited)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        address invited = structs0.getAddress(_loginInvited);
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        (,,,,, uint numActiveProjectInvited,,) = structs0.getStudentStruct(invited);

        if (_checkProjectStudent(msg.sender, numActiveProject, true) && _checkStudent(invited) && _checkProjectStudent(invited, numActiveProjectInvited, false)) {
            address creatorProject = structs1.getProjectStruct(numActiveProject).creator;

            if (creatorProject == msg.sender) {
                address[] memory members = structs1.getProjectStruct(numActiveProject).members;
                for (uint8 i = 0; i < members.length; i++) {
                    if (members[i] == invited) {
                        emit Action(msg.sender, invited, numActiveProject, "ERROR: this student is already involved in the project");
                        return;
                    }
                }

                (,,,,,, uint[] memory invitationsToProject,) = structs0.getStudentStruct(invited);
                for (uint8 i = 0; i < invitationsToProject.length; i++) {
                    if (invitationsToProject[i] == numActiveProject) {
                        emit Action(msg.sender, invited, 0, "ERROR: this student is already invited in this project");
                        return;
                    }
                }

                structs1.addInvitation(invited, numActiveProject);
                emit Action(msg.sender, invited, numActiveProject, "The invitation has been sent successfully");
            }
            else {
                emit Action(msg.sender, address(0), numActiveProject, "ERROR: you cannot invite, because you are not the creator of the project");
            }
        }
    }

    function joinInProject(
        string memory _login,
        string memory _pass,
        uint _numProject)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);

        if (_checkProjectStudent(msg.sender, numActiveProject, false)) {
            (,,,,,, uint[] memory invitationsToProject,) = structs0.getStudentStruct(msg.sender);
            bool flag = false;
            for (uint8 i = 0; i < invitationsToProject.length; i++) {
                if (invitationsToProject[i] == _numProject) {
                    flag = true;
                }
            }

            if (flag) {
                structs1.addMemberInProject(msg.sender, _numProject);
                structs1.setActiveProjectStudent(msg.sender, _numProject);
                emit Action(msg.sender, address(0), _numProject, "You successfully join to project");

                address creatorProject = structs1.getProjectStruct(_numProject).creator;
                for (uint8 i = 0; i < invitationsToProject.length; i++) {
                    if (invitationsToProject[i] != _numProject) {
                        emit Action(msg.sender, creatorProject, invitationsToProject[i], "Invitation declined");
                    }
                }
                structs1.setAllInvitations(msg.sender, new uint[](0));
            }
            else {
                emit Action(msg.sender, address(0), _numProject, "ERROR: you not invite in this project");
            }
        }
    }

    function changeGoalProject(
        string memory _login, 
        string memory _pass,
        string memory _goal)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        if (_checkProjectStudent(msg.sender, numActiveProject, true) && _normalText(_goal)) {
            structs1.setGoalInProject(_goal, numActiveProject);

            emit Action(msg.sender, address(0), numActiveProject, "Change goal");
        }
    }

    function changeRole(
        string memory _login,
        string memory _pass,
        string memory _role)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        if (_checkProjectStudent(msg.sender, numActiveProject, true) && _normalText(_role)) {
            structs1.setRoleMember(_role, msg.sender, numActiveProject);

            emit Action(msg.sender, address(0), numActiveProject, "Successfully change role");
        }
    }
    
    function addTask(
        string memory _login,
        string memory _pass,
        string memory _text,
        uint _deadline)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        if (_checkProjectStudent(msg.sender, numActiveProject, true) && _normalText(_text) 
        && _checkDeadline(_deadline) && _checkNumTask(msg.sender, 0, numActiveProject, true)) {

            structs1.addTask(_text, msg.sender, numActiveProject);
            structs1.increaceQuantityTask(msg.sender, numActiveProject);
            structs1.addDeadline(msg.sender, numActiveProject, _deadline);

        emit Action(msg.sender, address(0), 0, "Add task");
        }
    }

    function changeTask(
        string memory _login,
        string memory _pass,
        string memory _text,
        uint8 _numTask,
        uint _deadline)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        if (_checkProjectStudent(msg.sender, numActiveProject, true) && 
        _normalText(_text) && _checkDeadline(_deadline) && _checkNumTask(msg.sender, 0, numActiveProject, true)) {

            structs1.changeTextTask(_text, msg.sender, _numTask, numActiveProject);
            structs1.setDeadline(msg.sender, _numTask, numActiveProject, _deadline);
            
            emit Action(msg.sender, address(0), numActiveProject, "Successfully change text task");
        }
    }

    function completeProject(string memory _login, string memory _pass) public userRegistered(_login, _pass, msg.sender) onlyStudent() {
        (,,,,, uint numActiveProject,,) = structs0.getStudentStruct(msg.sender);
        if (_checkProjectStudent(msg.sender, numActiveProject, true)) {
            uint16 quantityTasks = structs1.getQuantityTasks(msg.sender, numActiveProject);
            uint16[] memory numCompletionTasks = structs1.getNumCompletionTasks(msg.sender, numActiveProject);
            if (quantityTasks == numCompletionTasks.length) {
                address mentor = structs1.getProjectStruct(numActiveProject).mentor;
                structs1.tryCompleteProject(mentor, numActiveProject);
            }
        }
    }
}