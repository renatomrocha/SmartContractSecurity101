from brownie import accounts, SavingsAccountV2, InvestorV2, Wei




def test_deposit():
    # Arrange
    deployer, user, attacker = accounts[0], accounts[1], accounts[2]

    # Deploy savings account contract
    savings_account_contract = SavingsAccountV2.deploy({"from": deployer})

    # deposit funds
    savings_account_contract.deposit({"from": deployer, "value": Wei("100 ether")})

    assert savings_account_contract.balanceOf(deployer) == Wei("100 ether")

    savings_account_contract.deposit({"from": user, "value": Wei("50 ether")})

    assert savings_account_contract.balanceOf(user) == Wei("50 ether")

    # Deploy Investor with attacher address
    investor_contract = InvestorV2.deploy(savings_account_contract.address, {"from": attacker})


def test_withdraw():
    # Arrange
    deployer, user, attacker = accounts[0], accounts[1], accounts[2]

    # Deploy savings account contract
    savings_account_contract = SavingsAccountV2.deploy({"from": deployer})

    # deposit funds
    savings_account_contract.deposit({"from": deployer, "value": Wei("100 ether")})
    savings_account_contract.deposit({"from": user, "value": Wei("50 ether")})
    savings_account_contract.withdraw({"from": deployer})


    assert savings_account_contract.balanceOf(deployer) == 0
    assert savings_account_contract.balanceOf(user) == Wei("50 ether")

    # Deploy Investor with attacher address
    investor_contract = InvestorV2.deploy(savings_account_contract.address, {"from": attacker})


def test_attack():
    # Arrange
    deployer, user, attacker = accounts[0], accounts[1], accounts[2]

    # Deploy savings account contract
    savings_account_contract = SavingsAccountV2.deploy({"from": deployer})

    # deposit funds
    savings_account_contract.deposit({"from": deployer, "value": Wei("100 ether")})
    savings_account_contract.deposit({"from": user, "value": Wei("50 ether")})
    savings_account_contract.withdraw({"from": deployer})


    assert savings_account_contract.balanceOf(deployer) == 0
    assert savings_account_contract.balanceOf(user) == Wei("50 ether")

    # # Deploy Investor with attacher address
    # investor_contract = InvestorV2.deploy(savings_account_contract.address, {"from": attacker})
    #
    # investor_contract.attack({"from": attacker, "value": Wei('10 ether')})

    print("Savings account balance ", savings_account_contract.balance())

    # assert savings_account_contract.balance == Wei("50 ether")


def main():
    test_attack()