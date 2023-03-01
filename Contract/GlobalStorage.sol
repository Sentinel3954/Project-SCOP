// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

contract GlobalStorage {

    // Безопасность:

    address ownerContract;
    address[] logicContracts;

    // Данные пользователей:

    mapping (bytes32 => string) internal stringDataUser;
    mapping (bytes32 => string[]) internal stringArrayDataUser;

    mapping (bytes32 => address) internal addressDataUser;
    mapping (bytes32 => address[]) internal addressArrayDataUser;

    mapping (bytes32 => uint8) internal uint8DataUser;
    mapping (bytes32 => uint8[]) internal uint8ArrayDataUser;
    mapping (bytes32 => uint16) internal uint16DataUser;
    mapping (bytes32 => uint16[]) internal uint16ArrayDataUser;
    mapping (bytes32 => uint) internal uintDataUser;
    mapping (bytes32 => uint[]) internal uintArrayDataUser;

    mapping (bytes32 => bytes32) internal bytes32DataUser;
    mapping (bytes32 => bytes32[]) internal bytes32ArrayDataUser;

    mapping (bytes32 => bool) internal boolDataUser;
    mapping (bytes32 => bool[]) internal boolArrayDataUser;

    // Данные проекта:

    mapping (bytes32 => string) internal stringDataProject;
    mapping (bytes32 => string[]) internal stringArrayDataProject;

    mapping (bytes32 => address) internal addressDataProject;
    mapping (bytes32 => address[]) internal addressArrayDataProject;

    mapping (bytes32 => uint8) internal uint8DataProject;
    mapping (bytes32 => uint8[]) internal uint8ArrayDataProject;
    mapping (bytes32 => uint16) internal uint16DataProject;
    mapping (bytes32 => uint16[]) internal uint16ArrayDataProject;
    mapping (bytes32 => uint) internal uintDataProject;
    mapping (bytes32 => uint[]) internal uintArrayDataProject;

    mapping (bytes32 => bytes32) internal bytes32DataProject;
    mapping (bytes32 => bytes32[]) internal bytes32ArrayDataProject;

    mapping (bytes32 => bool) internal boolDataProject;
    mapping (bytes32 => bool[]) internal boolArrayDataProject;

    constructor() {
        ownerContract = msg.sender;
        logicContracts.push(msg.sender);
    }


    // Модификаторы доступа:

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

    // Вспомогательные функции просмотра данных:

    function getAddressesContracts() public view onlyContract() returns (address[] memory) {
        return logicContracts;
    }

    function getOwnerContract() public view onlyContract() returns(address) {
        return ownerContract;
    }

    // Вспомогательные функции:

    function addAddressContract(address _newAddressContract) public onlyOwner() {
        require(msg.sender == ownerContract);
        logicContracts.push(_newAddressContract);
    }

    function changeOwnerContract(address _newAddressContract) public onlyOwner() {
        require(msg.sender == ownerContract);
        ownerContract = _newAddressContract;
    }

    function delAddressContract(address _oldAddress) public onlyOwner() {
        require(msg.sender == ownerContract);
        for (uint16 i = 0; i < logicContracts.length; i++){
            if (logicContracts[i] == _oldAddress){
                logicContracts[i] = address(0);
                break;
            }
        }
    }


    // Просмотр данных пользователей:
    // Строки:
    function getStringDataUser(bytes32 _key) external view onlyContract() returns (string memory) {
        return stringDataUser[_key];
    }

    function getStringArrayDataUser(bytes32 _key) external view onlyContract() returns (string[] memory) {
        return stringArrayDataUser[_key];
    }
        
    // Адреса:
    function getAddressDataUser(bytes32 _key) external view onlyContract() returns (address) {
        return addressDataUser[_key];
    }

    function getAddressArrayDataUser(bytes32 _key) external view onlyContract() returns (address[] memory) {
        return addressArrayDataUser[_key];
    }

    // Числа:
    // Uint8:
    function getUint8DataUser(bytes32 _key) external view onlyContract() returns (uint8) {
        return uint8DataUser[_key];
    }

    function getUint8ArrayDataUser(bytes32 _key) external view onlyContract() returns (uint8[] memory) {
        return uint8ArrayDataUser[_key];
    }

    // Uint16:
    function getUint16DataUser(bytes32 _key) external view onlyContract() returns (uint16) {
        return uint16DataUser[_key];
    }

    function getUint16ArrayDataUser(bytes32 _key) external view onlyContract() returns (uint16[] memory) {
        return uint16ArrayDataUser[_key];
    }

    // Uint:
    function getUintDataUser(bytes32 _key) external view onlyContract() returns (uint) {
        return uintDataUser[_key];
    }

    function getUintArrayDataUser(bytes32 _key) external view onlyContract() returns (uint[] memory) {
        return uintArrayDataUser[_key];
    }

    // Байты:
    function getBytes32DataUser(bytes32 _key) external view onlyContract() returns (bytes32) {
        return bytes32DataUser[_key];
    }

    function getBytes32ArrayDataUser(bytes32 _key) external view onlyContract() returns (bytes32[] memory) {
        return bytes32ArrayDataUser[_key];
    }

    // Bool:
    function getBoolDataUser(bytes32 _key) external view onlyContract() returns (bool) {
        return boolDataUser[_key];
    }

    function getBoolArrayDataUser(bytes32 _key) external view onlyContract() returns (bool[] memory) {
        return boolArrayDataUser[_key];
    }

    // Изменение данных пользователей:
    // Строк:
    function setStringDataUser(bytes32 _key, string memory _newString) external onlyContract() {
        stringDataUser[_key] = _newString;
    }

    function setStringArrayDataUser(bytes32 _key, uint16 _num, string memory _newString) external onlyContract() {
        stringArrayDataUser[_key][_num] = _newString;
    }

    function setFullStringArrayDataUser(bytes32 _key, string[] memory _newStrings) external onlyContract() {
        stringArrayDataUser[_key] = _newStrings;
    }

    function addStringArrayDataUser(bytes32 _key, string memory _newString) external onlyContract() {
        stringArrayDataUser[_key].push(_newString);
    }

    // Адресов:
    function setAddressDataUser(bytes32 _key, address _newAddress) external onlyContract() {
        addressDataUser[_key] = _newAddress;
    }

    function setAddressArrayDataUser(bytes32 _key, uint16 _num, address _newAddress) external onlyContract() {
        addressArrayDataUser[_key][_num] = _newAddress;
    }

    function setFullAddressArrayDataUser(bytes32 _key, address[] memory _newAddresses) external onlyContract() {
        addressArrayDataUser[_key] = _newAddresses;
    }

    function addAddressArrayDataUser(bytes32 _key, address _newAddress) external onlyContract() {
        addressArrayDataUser[_key].push(_newAddress);
    }

    // Чисел:
    // Uint8:
    function setUint8DataUser(bytes32 _key, uint8 _newUint8) external onlyContract() {
        uint8DataUser[_key] = _newUint8;
    }

    function setUint8ArrayDataUser(bytes32 _key, uint16 _num, uint8 _newValue) external onlyContract() {
        uint8ArrayDataUser[_key][_num] = _newValue;
    }

    function setFullUint8ArrayDataUser(bytes32 _key, uint8[] memory _newValues) external onlyContract() {
        uint8ArrayDataUser[_key] = _newValues;
    }

    function addUint8ArrayDataUser(bytes32 _key, uint8 _newValue) external onlyContract() {
        uint8ArrayDataUser[_key].push(_newValue);
    }

    // Uint16:
    function setUint16DataUser(bytes32 _key, uint16 _newValue) external onlyContract() {
        uint16DataUser[_key] = _newValue;
    }

    function setUint16ArrayDataUser(bytes32 _key, uint16 _num, uint16 _newValue) external onlyContract() {
        uint16ArrayDataUser[_key][_num] = _newValue;
    }

    function setFullUint16ArrayDataUser(bytes32 _key, uint16[] memory _newValues) external onlyContract() {
        uint16ArrayDataUser[_key] = _newValues;
    }

    function addUint16ArrayDataUser(bytes32 _key, uint16 _newValue) external onlyContract() {
        uint16ArrayDataUser[_key].push(_newValue);
    }

    // Uint:
    function setUintDataUser(bytes32 _key, uint _newValue) external onlyContract() {
        uintDataUser[_key] = _newValue;
    }

    function setUintArrayDataUser(bytes32 _key, uint16 _num, uint _newValue) external onlyContract() {
        uintArrayDataUser[_key][_num] = _newValue;
    }

    function setFullUintArrayDataUser(bytes32 _key, uint[] memory _newValues) external onlyContract() {
        uintArrayDataUser[_key] = _newValues;
    }

    function addUintArrayDataUser(bytes32 _key, uint _newValue) external onlyContract() {
        uintArrayDataUser[_key].push(_newValue);
    }

    // Байтов:
    function setBytes32DataUser(bytes32 _key, bytes32 _newValue) external onlyContract() {
        bytes32DataUser[_key] = _newValue;
    }

    function setBytes32ArrayDataUser(bytes32 _key, uint16 _num, bytes32 _newValue) external onlyContract() {
        bytes32ArrayDataUser[_key][_num] = _newValue;
    }

    function setFullBytes32ArrayDataUser(bytes32 _key, bytes32[] memory _newValues) external onlyContract() {
        bytes32ArrayDataUser[_key] = _newValues;
    }

    function addBytes32ArrayDataUser(bytes32 _key, bytes32 _newValue) external onlyContract() {
        bytes32ArrayDataUser[_key].push(_newValue);
    }

    // Bool:
    function setBoolDataUser(bytes32 _key, bool _newValue) external onlyContract() {
        boolDataUser[_key] = _newValue;
    }

    function setBoolArrayDataUser(bytes32 _key, uint16 _num, bool _newValue) external onlyContract() {
        boolArrayDataUser[_key][_num] = _newValue;
    }

    function setFullBoolArrayDataUser(bytes32 _key, bool[] memory _newValues) external onlyContract() {
        boolArrayDataUser[_key] = _newValues;
    }

    function addBoolArrayDataUser(bytes32 _key, bool _newValue) external onlyContract() {
        boolArrayDataUser[_key].push(_newValue);
    }
    
    // Просмотр данных проекта:
    // Строки:
    function getStringDataProject(bytes32 _key) external view onlyContract() returns (string memory) {
        return stringDataProject[_key];
    }

    function getStringArrayDataProject(bytes32 _key) external view onlyContract() returns (string[] memory) {
        return stringArrayDataProject[_key];
    }

    // Адреса:
    function getAddressDataProject(bytes32 _key) external view onlyContract() returns (address) {
        return addressDataProject[_key];
    }

    function getAddressArrayDataProject(bytes32 _key) external view onlyContract() returns (address[] memory) {
        return addressArrayDataProject[_key];
    }

    // Числа:
    // Uint8:
    function getUint8DataProject(bytes32 _key) external view onlyContract() returns (uint8) {
        return uint8DataProject[_key];
    }

    function getUint8ArrayDataProject(bytes32 _key) external view onlyContract() returns (uint8[] memory) {
        return uint8ArrayDataProject[_key];
    }

    // Uint16
    function getUint16DataProject(bytes32 _key) external view onlyContract() returns (uint16) {
        return uint16DataProject[_key];
    }  

    function getUint16ArrayDataProject(bytes32 _key) external view onlyContract() returns (uint16[] memory) {
        return uint16ArrayDataProject[_key];
    }

    // Uint:
    function getUintDataProject(bytes32 _key) external view onlyContract() returns (uint) {
        return uintDataProject[_key];
    }

    function getUintArrayDataProject(bytes32 _key) external view onlyContract() returns (uint[] memory) {
        return uintArrayDataProject[_key];
    }

    // Байты:
    function getBytes32DataProject(bytes32 _key) external view onlyContract() returns (bytes32) {
        return bytes32DataProject[_key];
    }

    function getBytes32ArrayDataProject(bytes32 _key) external view onlyContract() returns (bytes32[] memory) {
        return bytes32ArrayDataProject[_key];
    }

    // Bool:
    function getBoolDataProject(bytes32 _key) external view onlyContract() returns (bool) {
        return boolDataProject[_key];
    }

    function getBoolArrayDataProject(bytes32 _key) external view onlyContract() returns (bool[] memory) {
        return boolArrayDataProject[_key];
    }

    // Изменение данных проекта:
    // Строк:
    function setStringDataProject(bytes32 _key, string memory _newString) external onlyContract() {
        stringDataProject[_key] = _newString;
    }
    
    function setStringArrayDataProject(bytes32 _key, uint16 _num, string memory _newString) external onlyContract() {
        stringArrayDataProject[_key][_num] = _newString;
    }

    function setFullStringArrayDataProject(bytes32 _key, string[] memory _newString) external onlyContract() {
        stringArrayDataProject[_key]= _newString;
    }

    function addStringArrayDataProject(bytes32 _key, string memory _newString) external onlyContract() {
        stringArrayDataProject[_key].push(_newString);
    }

    // Адресов:
    function setAddressDataProject(bytes32 _key, address _newAddress) external onlyContract() {
        addressDataProject[_key] = _newAddress;
    }

    function setAddressArrayDataProject(bytes32 _key, uint16 _num, address _newAddress) external onlyContract() {
        addressArrayDataProject[_key][_num] = _newAddress;
    }

    function setFullAddressArrayDataProject(bytes32 _key, address[] memory _newAddress) external onlyContract() {
        addressArrayDataProject[_key] = _newAddress;
    }

    function addAddressArrayDataProject(bytes32 _key, address _newAddress) external onlyContract() {
        addressArrayDataProject[_key].push(_newAddress);
    }

    // Чисел:
    // Uint8:
    function setUint8DataProject(bytes32 _key, uint8 _newUint8) external onlyContract() {
        uint8DataProject[_key] = _newUint8;
    }

    function setUint8ArrayDataProject(bytes32 _key, uint16 _num, uint8 _newValue) external onlyContract() {
        uint8ArrayDataProject[_key][_num] = _newValue;
    }

    function setFullUint8ArrayDataProject(bytes32 _key, uint8[] memory _newValues) external onlyContract() {
        uint8ArrayDataProject[_key] = _newValues;
    }

    function addUint8ArrayDataProject(bytes32 _key, uint8 _newValue) external onlyContract() {
        uint8ArrayDataProject[_key].push(_newValue);
    }

    // Uint16:
    function setUint16DataProject(bytes32 _key, uint16 _newValue) external onlyContract() {
        uint16DataProject[_key] = _newValue;
    }

    function setUint16ArrayDataProject(bytes32 _key, uint16 _num, uint16 _newValue) external onlyContract() {
        uint16ArrayDataProject[_key][_num] = _newValue;
    }

    function setFullUint16ArrayDataProject(bytes32 _key, uint16[] memory _newValues) external onlyContract() {
        uint16ArrayDataProject[_key] = _newValues;
    }

    function addUint16ArrayDataProject(bytes32 _key, uint16 _newValue) external onlyContract() {
        uint16ArrayDataProject[_key].push(_newValue);
    }

    // Uint:
    function setUintDataProject(bytes32 _key, uint _newValue) external onlyContract() {
        uintDataProject[_key] = _newValue;
    }

    function setUintArrayDataProject(bytes32 _key, uint16 _num, uint _newValue) external onlyContract() {
        uintArrayDataProject[_key][_num] = _newValue;
    }

    function setFullUintArrayDataProject(bytes32 _key, uint[] memory _newValues) external onlyContract() {
        uintArrayDataProject[_key] = _newValues;
    }

    function addUintArrayDataProject(bytes32 _key, uint _newValue) external onlyContract() {
        uintArrayDataProject[_key].push(_newValue);
    }

    // Байтов:
    function setBytes32DataProject(bytes32 _key, bytes32 _newValue) external onlyContract() {
        bytes32DataProject[_key] = _newValue;
    }

    function setBytes32ArrayDataProject(bytes32 _key, uint16 _num, bytes32 _newValue) external onlyContract() {
        bytes32ArrayDataProject[_key][_num] = _newValue;
    }

    function setFullBytes32ArrayDataProject(bytes32 _key, bytes32[] memory _newValues) external onlyContract() {
        bytes32ArrayDataProject[_key] = _newValues;
    }

    function addBytes32ArrayDataProject(bytes32 _key, bytes32 _newValue) external onlyContract() {
        bytes32ArrayDataProject[_key].push(_newValue);
    }

    // Bool:
    function setBoolDataProject(bytes32 _key, bool _newValue) external onlyContract() {
        boolDataProject[_key] = _newValue;
    }

    function setBoolArrayDataProject(bytes32 _key, uint16 _num, bool _newValue) external onlyContract() {
        boolArrayDataProject[_key][_num] = _newValue;
    }

    function setFullBoolArrayDataProject(bytes32 _key, bool[] memory _newValues) external onlyContract() {
        boolArrayDataUser[_key] = _newValues;
    }

    function addBoolArrayDataProject(bytes32 _key, bool _newValue) external onlyContract() {
        boolArrayDataUser[_key].push(_newValue);
    }
}