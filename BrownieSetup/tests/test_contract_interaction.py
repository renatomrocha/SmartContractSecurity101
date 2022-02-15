from brownie import accounts, SavingsAccount


def test_should_allow_deposit():
    # Arrange
    account = accounts[0]
    # Act
    savings_account_contract = SavingsAccount.deploy({"from": account})

    balance = savings_account_contract.balanceOf(account)
    assert balance == 0

    savings_account_contract.deposit({'value': 100})

    new_balance = savings_account_contract.balanceOf(account)
    assert new_balance == 100


def test_should_allow_withdraw():
    # Arrange
    account = accounts[0]
    # Act
    savings_account_contract = SavingsAccount.deploy({"from": account})

    balance = savings_account_contract.balanceOf(account)
    assert balance == 0

    savings_account_contract.deposit({'value': 100})

    new_balance = savings_account_contract.balanceOf(account)
    assert new_balance == 100

    savings_account_contract.withdraw()

    balance_after_withdraw = savings_account_contract.balanceOf(account)
    assert balance_after_withdraw == 0

