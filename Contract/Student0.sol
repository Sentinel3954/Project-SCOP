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
    
    
    // view functions:
    function checkStudent(address _student) public view
        returns (
        string memory login,
        string memory FIO,
        string memory classLetter,
        string[] memory strongSides,
        uint8 numClass,
        uint numActiveProject,
        uint[] memory invitationsToProject,
        uint[] memory completedProjects)
    {
        (login, FIO, classLetter, strongSides, numClass, numActiveProject, invitationsToProject, completedProjects) = structs0.getStudentStruct(_student);
    }

    // main functions
    function registration(
        string memory _login,
        string memory _FIO,
        string memory _classLetter,
        string memory _pass,
        uint8 _class)
        public 
    {  
        if (_checksForRegistration(_login, _pass)) {
            if (_class <= 11 && _class >= 1) {
                structs0.setLogin(_login, msg.sender);
                structs0.setFIO(_FIO, msg.sender);
                structs0.setStudentClassLetter(_classLetter, msg.sender);
                structs0.setStudentClass(msg.sender, _class);
                structs0.setPass(_login, _pass, msg.sender);

                structs0.setStatusAddress(msg.sender, uint8(MakeStruct0.StatusAddress.Student));

                emit Action(msg.sender, address(0), 0, "Student successfully registered");
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: wrong class");
            }
        }
    }
    
    function addStrongSide(
        string memory _login, 
        string memory _pass,
        string memory _text)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        if (_normalText(_text)) {
            uint8 quantityStrongSides = structs0.getQuantityStrongSides(msg.sender);
            if (quantityStrongSides < 10) { // проверка количества сильных сторон (максимум 10)
                structs0.addStudentStrongSide(_text, msg.sender);
                structs0.increaceQuantityStrongSides(msg.sender);

                emit Action(msg.sender, address(0), 0, "Add strong side");
            }
            else {
                emit Action(msg.sender, address(0), 0, "Too much strong sides");
            }
        }
    }

    function changeStrongSide(
        string memory _login,
        string memory _pass,
        string memory _newText,
        uint8 _numStrongSide)
        public userRegistered(_login, _pass, msg.sender) onlyStudent()
    {
        if (_normalText(_newText)) {
            uint8 quantityStrongSides = structs0.getQuantityStrongSides(msg.sender);
            if (quantityStrongSides > _numStrongSide) {
                structs0.changeStudentStrongSide(_newText, msg.sender, _numStrongSide);

                emit Action(msg.sender, address(0), 0, "Change strong side");
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: too big number strong side");
            }
        }
    }
}