// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./Support.sol";

contract Teacher is Support {

    modifier onlyTeacher() {
        MakeStruct0.StatusAddress status = structs0.getStatusAddress(msg.sender);
        if (status != MakeStruct0.StatusAddress.Teacher) {
            emit Action(msg.sender, address(0), 0, "ERROR: only teacher");
            return;
        }
        _;
    }


    constructor (address _dataContract, address _structs0, address _structs1) Support(_dataContract, _structs0, _structs1) {}


    // view functions
    function checkTeacher(address _teacher) public view returns (MakeStruct0.Teacher memory) {
        return structs0.getTeacherStruct(_teacher);
    }

    // private functions
    function _checkTeacherProject(uint _numProject, bool _mustHave) private returns (bool) {
        bool flag = false;
        MakeStruct0.Teacher memory teacher = structs0.getTeacherStruct(msg.sender);

        for (uint16 i = 0; i < teacher.numActiveProjects.length; i++){
            if (_numProject == teacher.numActiveProjects[i]) {
                flag = true;
                break;
            }
        }

        if (_mustHave && !flag){
            emit Action(msg.sender, address(0), _numProject, "ERROR: not have this project");
            return false;
        }
        if (!_mustHave && flag){
            emit Action(msg.sender, address(0), _numProject, "ERROR: already have this project");
            return false;
        }
        return true;
    }

    function registration(
        string memory _login, 
        string memory _pass, 
        string memory _FIO,
        uint16[] memory _leadsSchoolSubjects,
        uint16[] memory _numLaboratories)
        public 
    {
        if (_checksForRegistration(_login, _pass)) {
            MakeStruct0.StatusAddress status = structs0.getStatusAddress(msg.sender);
            if (status == MakeStruct0.StatusAddress.ForTeacher) {
                structs0.setLogin(_login, msg.sender);
                structs0.setFIO(_FIO, msg.sender);
                structs0.setPass(_login, _pass, msg.sender);
                structs0.setTeacherSchoolSubjects(msg.sender, _leadsSchoolSubjects);
                structs0.setTeacherLaboratories(msg.sender, _numLaboratories);
                
                structs0.addSubjectTeacher(_login, _leadsSchoolSubjects);
                structs0.setStatusAddress(msg.sender, uint8(MakeStruct0.StatusAddress.Teacher));            

                emit Action(msg.sender, address(0), 0, "Teacher successfully registered");
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: wrong address");
            }
        }
    }

    function generateAddressForStudent(
        string memory _login,
        string memory _pass,
        address _newStudent)
        public userRegistered(_login, _pass, msg.sender) onlyTeacher()
    {
        MakeStruct0.StatusAddress status = structs0.getStatusAddress(_newStudent);
        if (status == MakeStruct0.StatusAddress.Not) {
            structs0.setStatusAddress(_newStudent, uint8(MakeStruct0.StatusAddress.ForStudent));
            structs0.setAddedUsers(msg.sender, _newStudent);

            emit Action(msg.sender, address(0), 0, "Address generated");
        }
        else {
            emit Action(msg.sender, address(0), 0, "ERROR: address already using");
        }
    }

    function createProject(
        string memory _login, 
        string memory _pass, 
        string memory _nameProject,
        uint16 _numLaboratory)
        public userRegistered(_login, _pass, msg.sender) onlyTeacher()
    {
        if (_normalText(_nameProject)) {
            bool flag = false;
            MakeStruct0.Teacher memory teacher = structs0.getTeacherStruct(msg.sender);
            for (uint8 i = 0; i < teacher.numLaboratories.length; i++) {
                if (teacher.numLaboratories[i] == _numLaboratory) {
                    flag = true;
                }
            }

            if (flag) {
                uint numNewProject = structs1.getQuantityProjects() + 1;
                structs1.increaseQuantityProjects();

                structs1.setNameProject(_nameProject, numNewProject);
                structs1.setMentorProject(msg.sender, numNewProject);
                structs1.setSchoolSubjectsProject(teacher.numSchoolSubjects, numNewProject);
                structs1.setLaboratoryProject(_numLaboratory, numNewProject);
                structs1.setCreatorProject(msg.sender, numNewProject);

                structs1.setStatusProject(MakeStruct1.StatusProject.Active, numNewProject);
                structs1.addActiveProjectTeacher(msg.sender, numNewProject);
                emit Action(msg.sender, address(0), 0, "Create project");
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: you not have this laboratory");
            }
        }
    }

    function joinInProject(
        string memory _login,
        string memory _pass,
        uint _numProject)
        public userRegistered(_login, _pass, msg.sender) onlyTeacher()
    {
        if (_checkTeacherProject(_numProject, false)) {
            MakeStruct0.Teacher memory teacher = structs0.getTeacherStruct(msg.sender);
            uint[] memory invitationsToProject = teacher.invitationsToProject;
            uint8 i = 0;
            for (; i < invitationsToProject.length; i++) {
                if (invitationsToProject[i] == _numProject) {
                    break;
                }
            }

            if (i != 0) {
                structs1.setMentorProject(msg.sender, _numProject);
                structs1.addActiveProjectTeacher(msg.sender, _numProject);
                emit Action(msg.sender, address(0), _numProject, "You successfully join to project");
                delete invitationsToProject[i];

                structs1.setAllInvitations(msg.sender, invitationsToProject);
            }
            else {
                emit Action(msg.sender, address(0), _numProject, "ERROR: you not invite in this project");
            }
        }
    }

    function addStudentInProject(
        string memory _loginTeacher,
        string memory _pass,
        string memory _loginStudent,
        uint _numProject)
        public userRegistered(_loginTeacher, _pass, msg.sender) onlyTeacher()
    {
        address student = structs0.getAddress(_loginStudent);
        if (_checkTeacherProject(_numProject, true) && _checkStudent(student)) {
            (,,,,, uint activeProjectStudent,,) = structs0.getStudentStruct(student);
            if (activeProjectStudent == 0) {
                MakeStruct1.Project memory project = structs1.getProjectStruct(_numProject);
                for (uint16 i = 0; i < project.members.length; i++) {
                    if (project.members[i] == student){
                        emit Action(msg.sender, student, _numProject, "ERROR: already in this project");
                        return;
                    }
                }
            }
            else {
                emit Action(msg.sender, student, 0, "ERROR: student is already participating in the project");
            }

            structs1.addMemberInProject(student, _numProject);
            structs1.setActiveProjectStudent(student, _numProject);

            emit Action(msg.sender, student, _numProject, "Succesfully add in project");
        }
    }

    function deleteStudentOutProject(
        string memory _loginTeacher,
        string memory _pass,
        string memory _loginStudent)
        public userRegistered(_loginTeacher, _pass, msg.sender) onlyTeacher()
    {
        address student = structs0.getAddress(_loginStudent);
        (,,,,, uint activeProjectStudent,,) = structs0.getStudentStruct(student);
        if (_checkStudent(student) && _checkProjectStudent(student, activeProjectStudent, true) && _checkTeacherProject(activeProjectStudent, true)) {
            MakeStruct1.Project memory project = structs1.getProjectStruct(activeProjectStudent);
            address[] memory members = project.members;
            for (uint16 i = 0; i < members.length; i++) {
                if (members[i] == student) {
                    delete members[i];
                    structs1.setAllMemberProject(members, activeProjectStudent);

                    emit Action(msg.sender, student, activeProjectStudent, "Student delete out project");
                    return;
                }
            }            
        }
    }

    function changeTaskStudent(
        string memory _loginTeacher, 
        string memory _pass,
        string memory _loginStudent,
        string memory _text,
        uint8 _numTask,
        uint _deadline)
        public userRegistered(_loginTeacher, _pass, msg.sender) onlyTeacher()
    {
        address student = structs0.getAddress(_loginStudent);
        (,,,,, uint activeProjectStudent,,) = structs0.getStudentStruct(student);

        if (_checkStudent(student) && _checkProjectStudent(student, activeProjectStudent, true)
        && _checkTeacherProject(activeProjectStudent, true) && _checkNumTask(student, _numTask, activeProjectStudent, false)
        && _checkDeadline(_deadline) && _normalText(_text)) {

            structs1.changeTextTask(_text, msg.sender, _numTask, activeProjectStudent);
            structs1.setDeadline(msg.sender, _numTask, activeProjectStudent, _deadline);

            emit Action(msg.sender, student, activeProjectStudent, "Successfully change task");
        }
    }

    function completeTask(
        string memory _loginTeacher,
        string memory _pass,
        string memory _loginStudent,
        uint8 _numTask)
        public userRegistered(_loginTeacher, _pass, msg.sender) onlyTeacher()
    {
        address student = structs0.getAddress(_loginStudent);
        (,,,,, uint activeProjectStudent,,) = structs0.getStudentStruct(student);
        if (_checkStudent(student) && _checkProjectStudent(student, activeProjectStudent, true) && _checkNumTask(student, _numTask, activeProjectStudent, false)) {
            structs1.setTaskComplete(student, activeProjectStudent, _numTask);
            emit Action(msg.sender, student, activeProjectStudent, "Status change");
        }
    } 
}