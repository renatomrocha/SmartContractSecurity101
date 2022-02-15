// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

import "@openzeppelin/contracts/access/Ownable.sol";

interface ISavingsAccount {

    function deposit() external payable;

    function withdraw() external;

}


contract Investor is Ownable{

    ISavingsAccount public immutable savingsAccount;

    // savingsAccountAddress ---> Original Smart contract Address
    constructor (address savingsAccountAddress) {
        savingsAccount = ISavingsAccount(savingsAccountAddress);
    }

    function depositIntoSavingsAccount() external payable onlyOwner {
        savingsAccount.deposit{value: msg.value}();
    }

    function withdrawFromSavingsAccount() external onlyOwner {

        savingsAccount.withdraw();
    }

    receive() external payable {} // Default solidity function to enable contract to receive funds retrieved by withdraw function

}
