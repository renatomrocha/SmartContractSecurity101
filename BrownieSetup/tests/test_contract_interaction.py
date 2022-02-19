from brownie import accounts, SavingsAccount, Investor


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


def test_externally_called_deposit():
    # Arrange
    account = accounts[0]
    # Act
    savings_account_contract = SavingsAccount.deploy({"from": account})

    investor_contract = Investor.deploy(savings_account_contract.address, {"from": account})

    investor_contract.depositIntoSavingsAccount({"value": 100})

    balance_after_deposit = savings_account_contract.balanceOf(investor_contract.address)

    assert balance_after_deposit == 100


def test_externally_called_withdraw():
    # Arrange
    account = accounts[0]
    # Act
    savings_account_contract = SavingsAccount.deploy({"from": account})

    investor_contract = Investor.deploy(savings_account_contract.address, {"from": account})

    investor_contract.depositIntoSavingsAccount({"value": 100})

    balance_after_deposit = savings_account_contract.balanceOf(investor_contract.address)

    assert balance_after_deposit == 100

    investor_contract.withdrawFromSavingsAccount()

    balance_after_withdraw = savings_account_contract.balanceOf(investor_contract.address)

    assert balance_after_withdraw == 0

