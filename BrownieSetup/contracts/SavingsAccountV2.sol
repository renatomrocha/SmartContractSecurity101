pragma solidity 0.8.9;

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SavingsAccountV2 is ReentrancyGuard{

    using Address for address payable;

    mapping(address => uint256) public balanceOf;

    function deposit() external payable {
        balanceOf[msg.sender] += msg.value;
    }

    function withdraw() external nonReentrant {

        uint256 amountDeposited = balanceOf[msg.sender];

        payable(msg.sender).sendValue(amountDeposited);

        balanceOf[msg.sender] = 0;
    }



}
