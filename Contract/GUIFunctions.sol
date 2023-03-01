// SPDX-License-Identifier: GPL-3.0
pragma solidity > 0.8.0 < 0.9.0;

import "./Support.sol";

contract GUIFunctions is Support {


    constructor (address _dataContract, address _structs0, address _structs1) Support(_dataContract, _structs0, _structs1) {}

    // ПРЕ: логин, пароль (обращается к функции userRegistered)
    // ПРО: успех (пользователь авторизован)

    function myTransfer(address _recipient) external payable {
        if (msg.sender.balance >= msg.value) {
            payable(_recipient).transfer(msg.value);
        }
    }
}