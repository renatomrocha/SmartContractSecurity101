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


// Old version, this way withdrawn funds would be trapped inside the smart contract
//    receive() external payable {} // Default solidity function to enable contract to receive funds retrieved by withdraw function

    // This way, receive function (which processes ETH transfers to this SC) will automatically forward the received eth to the owner's account
    receive() external payable {
        payable(owner()).transfer(address(this).balance);
    }

}
