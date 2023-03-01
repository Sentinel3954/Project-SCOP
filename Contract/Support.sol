// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./GlobalStorage.sol";
import "./MakeStruct0.sol";
import "./MakeStruct1.sol";

contract Support {

    GlobalStorage data;
    MakeStruct0 structs0;
    MakeStruct1 structs1;

    event Action (address hero, address target, uint numProject, string text);

    modifier userRegistered(string memory _login, string memory _pass, address _user) {
        if (structs0.getPassword(_user) != keccak256(abi.encodePacked(_login, _pass))) {
            emit Action(msg.sender, address(0), 0, "ERROR: wrong data");
            return;
        }
        _;
    }

    function auth (string memory _login, string memory _pass, address _sender) external userRegistered(_login, _pass, _sender) returns (bool a) {
        return true;
    }
    
    constructor (address _data, address _struct0, address _struct1) {
        data = GlobalStorage(_data);
        structs0 = MakeStruct0(_struct0);
        structs1 = MakeStruct1(_struct1);
        constructHelpData();
    }


    // view functions
    function checkProject(uint _numProject) public view returns (MakeStruct1.Project memory project) {
        return structs1.getProjectStruct(_numProject);
    }

    // functions for testing 
    function constructHelpData() private {
        string[] memory schoolSubjects = new string[](5);
        schoolSubjects[0] = "Math";
        schoolSubjects[1] = "Physics";
        schoolSubjects[2] = "Informatics";
        schoolSubjects[3] = "Russian";

        string[] memory laboratories = new string[](11);
        laboratories[0] = "Not";
        laboratories[1] = "Electricity and magnetism";
        laboratories[2] = "Prototyping";
        laboratories[3] = "Mechanics and strength";
        laboratories[4] = "Thermal phenomena and molecular structures";
        laboratories[5] = "Microelectronics and circuit engineering";
        laboratories[6] = "Autonomous avionics";
        laboratories[7] = "Robotics";
        laboratories[8] = "Programming";
        laboratories[9] = "Mathematical modeling and analysis";
        laboratories[10] = "Astronomy and Aerospace Systems";
        
        structs1.setLaboratories(laboratories);
        structs1.setSchoolSubjects(schoolSubjects);
    }

    function constructData() public {
        // local testing
        // Teacher
        // structs0.setLogin("Denis", 0x583031D1113aD414F02576BD6afaBfb302140225);
        // structs0.setFIO("Sheptalin Denis Sergeevich", 0x583031D1113aD414F02576BD6afaBfb302140225);
        // structs0.setPass("Denis", "1", 0x583031D1113aD414F02576BD6afaBfb302140225);
        // uint16[] memory needSchoolSubjects = new uint16[](1);
        // needSchoolSubjects[0] = 1;
        // structs0.setTeacherSchoolSubjects(0x583031D1113aD414F02576BD6afaBfb302140225, needSchoolSubjects);
        // uint16[] memory laboratoriesProject = new uint16[](1);
        // laboratoriesProject[0] = 1;
        // structs0.setTeacherLaboratories(0x583031D1113aD414F02576BD6afaBfb302140225, laboratoriesProject);
        // structs0.setScientistManager(0x583031D1113aD414F02576BD6afaBfb302140225, true);

        // structs0.setStatusAddress(0x583031D1113aD414F02576BD6afaBfb302140225, uint8(MakeStruct0.StatusAddress.Teacher));

        // Student
        // structs0.setLogin("Artem", 0xdD870fA1b7C4700F2BD7f44238821C26f7392148);
        // structs0.setFIO("Artemov Artem Artemovich", 0xdD870fA1b7C4700F2BD7f44238821C26f7392148);
        // structs0.setStudentClassLetter("\xD0\x98", 0xdD870fA1b7C4700F2BD7f44238821C26f7392148);
        // structs0.setStudentClass(0xdD870fA1b7C4700F2BD7f44238821C26f7392148, 10);
        // structs0.setPass("Artem", "1", 0xdD870fA1b7C4700F2BD7f44238821C26f7392148);
        // string[] memory strongSides = new string[](2);
        // strongSides[0] = "I can fly";
        // structs0.setFullStrongSides(strongSides, 0xdD870fA1b7C4700F2BD7f44238821C26f7392148);

        // structs0.setStatusAddress(0xdD870fA1b7C4700F2BD7f44238821C26f7392148, uint8(MakeStruct0.StatusAddress.Student));

        // // addresses
        // structs0.setStatusAddress(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x617F2E2fD72FD9D5503197092aC168c91465E7f2, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x17F6AD8Ef982297579C203069C1DbfFE4348c372, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x5c6B0f7Bf3E7ce046039Bd8FABdfD3f9F5021678, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x03C6FcED478cBbC9a4FAB34eF9f40767739D1Ff7, uint8(MakeStruct0.StatusAddress.ForStudent));
        // structs0.setStatusAddress(0x1aE0EA34a72D944a8C7603FfB3eC30a6669E454C, uint8(MakeStruct0.StatusAddress.ForStudent));
        // // structs0.setStatusAddress(0x0A098Eda01Ce92ff4A4CCb7A4fFFb5A43EBC70DC, uint8(MakeStruct0.StatusAddress.ForStudent));

        // structs0.setStatusAddress(0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c, uint8(MakeStruct0.StatusAddress.ForTeacher));
        // structs0.setStatusAddress(0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C, uint8(MakeStruct0.StatusAddress.ForTeacher));
        // structs0.setStatusAddress(0x4B0897b0513fdC7C541B6d9D7E929C4e5364D2dB, uint8(MakeStruct0.StatusAddress.ForTeacher));

        // // GUI
        // // ----------------- Teacher
        structs0.setLogin("Denis", 0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7);
        structs0.setFIO("Sheptalin Denis Sergeevich", 0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7);
        structs0.setPass("Denis", "1", 0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7);
        uint16[] memory needSchoolSubjects = new uint16[](1);
        needSchoolSubjects[0] = 1;
        structs0.setTeacherSchoolSubjects(0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7, needSchoolSubjects);
        uint16[] memory laboratoriesProject = new uint16[](1);
        laboratoriesProject[0] = 1;
        structs0.setTeacherLaboratories(0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7, laboratoriesProject);
        structs0.setHeadTeacher(0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7, true);
        structs0.setScientistManager(0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7, true);

        structs0.setStatusAddress(0x486516Ce05a158cBD488F219Ca64Fea674b4b8f7, uint8(MakeStruct0.StatusAddress.Teacher));

        // // ---------------------- Student
        structs0.setLogin("Artem", 0xD08270D7cFd9b50A6E94b40c95175acD9A62c234);
        structs0.setFIO("Artemov Artem Artemovich", 0xD08270D7cFd9b50A6E94b40c95175acD9A62c234);
        structs0.setStudentClassLetter("\xD0\x98", 0xD08270D7cFd9b50A6E94b40c95175acD9A62c234);
        structs0.setStudentClass(0xD08270D7cFd9b50A6E94b40c95175acD9A62c234, 10);
        structs0.setPass("Artem", "1", 0xD08270D7cFd9b50A6E94b40c95175acD9A62c234);
        string[] memory strongSides = new string[](2);
        strongSides[0] = "I can fly";
        structs0.setFullStrongSides(strongSides, 0xD08270D7cFd9b50A6E94b40c95175acD9A62c234);

        structs0.setStatusAddress(0xD08270D7cFd9b50A6E94b40c95175acD9A62c234, uint8(MakeStruct0.StatusAddress.Student));

        // // ---------------- Adresses
        structs0.setStatusAddress(0xA8368d91ce67D60b9e1288eB2ba2555C0e09EE94, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0x16496CAA734bA101cA1D931c648F9FA12856B69e, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0x52a0024cB03CCB7B787eba15A6f7FF7EF2fCE3f9, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0xF18919Fa57FBa4c75c4bE86762B485f1b4A5D954, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0xE2449a03bFa5A89dA6295EB6547e91A15c63Ac8B, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0xa796B7739989cDcA7c861BEd94F4aE01d23B18CE, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0xa3e508192eeD1CB8151D6F2dB5Bd0ba45dC49535, uint8(MakeStruct0.StatusAddress.ForTeacher));
        structs0.setStatusAddress(0x19acaE5Ab26022D4e0249899cD6d780BD1a31DD0, uint8(MakeStruct0.StatusAddress.ForTeacher));

        structs0.setStatusAddress(0x6D7Bd28346ceDB712Fa6811C4e16332A8fD38f26, uint8(MakeStruct0.StatusAddress.ForStudent));
        structs0.setStatusAddress(0x234D8945797EE0995A9748DAd31E3629bB0dD888, uint8(MakeStruct0.StatusAddress.ForStudent));
        structs0.setStatusAddress(0x2180768fE112ff886b74436bF0E46954E87B7882, uint8(MakeStruct0.StatusAddress.ForStudent));
        structs0.setStatusAddress(0xF375A7eEDe5f1d2420e17e5eAaBa5FEf17098bdd, uint8(MakeStruct0.StatusAddress.ForStudent));
        structs0.setStatusAddress(0x1b4e31DE080A09083f92b64626cE1487B1f6bC00, uint8(MakeStruct0.StatusAddress.ForStudent));
        structs0.setStatusAddress(0xAE05dd8c2a3A791ac26dD8124CBE8dB4aA96C2ca, uint8(MakeStruct0.StatusAddress.ForStudent));
    }

    // private functions
    function _checkStudent(address _student) internal returns (bool) {
        if (structs0.getStatusAddress(_student) != MakeStruct0.StatusAddress.Student) {
            emit Action(msg.sender, address(0), 0, "ERROR: this address not belong student");
            return false;
        }
        return true;
    }

    function _checkProjectStudent(address _student, uint _numActiveProject, bool _mustHave) internal returns (bool) {
        if (_mustHave) {
            if (_numActiveProject == 0) {
                emit Action(_student, address(0), 0, "ERROR: student not have active project");
                return false;
            }
        }
        else {
            if (_numActiveProject != 0) {
                emit Action(_student, address(0), 0, "ERROR: student already have active project");
                return false;
            }
        }
        return true;
    }

    function _normalText(string memory _text) internal returns (bool) {
        if (bytes(_text).length > 20) {
            if (bytes(_text).length < 340) {
                return true;
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: long text");
            }     
        }
        else {
            emit Action(msg.sender, address(0), 0, "ERROR: short text");
        }
        return false;
    }

    function _checkDeadline(uint _deadline) internal returns (bool) {
        uint startDate = structs1.startDate();
        uint startBlock = structs1.startBlock();
        if (_deadline > (startDate + (block.number - startBlock) * 5)) {
            return true;
        }
        else {
            emit Action(msg.sender, address(0), 0, "ERROR: wrong new deadline");
        }
        return false;
    }

    function _checkNumTask(address _student, uint8 _numTask, uint _numProject, bool _addTask) internal returns (bool) {
        uint16[] memory numCompletionTask = structs1.getNumCompletionTasks(_student, _numProject);
        for (uint8 i = 0; i < numCompletionTask.length; i++) {
            if (_numTask == numCompletionTask[i]) {
                return false;
            }
        }

        uint16 quantityTasks = structs1.getQuantityTasks(_student, _numProject);
        if (_addTask) {
            if (quantityTasks < 20) {
                return true;
            }
            else {
                emit Action(msg.sender, _student, _numProject, "ERROR: too many tasks");
            }
        }
        else {
            if (quantityTasks > _numTask) {
                return true;
            }
            else {
                emit Action(msg.sender, _student, _numProject, "ERROR: too big number task");
            }
        }
        return false;
    }

    function _checksForRegistration(string memory _login, string memory _pass) internal returns (bool) {
        if (bytes(_pass).length != 0 && bytes(_login).length != 0) {
            if (structs0.getAddress(_login) == address(0)) {
                MakeStruct0.StatusAddress status = structs0.getStatusAddress(msg.sender);
                if (status == MakeStruct0.StatusAddress.ForStudent ||
                    status == MakeStruct0.StatusAddress.ForTeacher ||
                    status == MakeStruct0.StatusAddress.ForAdmin) {

                    return true;
                }
                else {
                    emit Action(msg.sender, address(0), 0, "ERROR: address occupied");
                }
            }
            else {
                emit Action(msg.sender, address(0), 0, "ERROR: login occupied");
            }
        }
        else {
            emit Action(msg.sender, address(0), 0, "ERROR: empty password or login");
        }
        return false;
    }
}