class BankingSystem:
    def __init__(self):
        self.accounts={}

    def create_account(self,account_name,initial_balance):
        if account_name in self.accounts:
            print(f"Account with name {account_name} already exists.")
        else:
            self.accounts[account_name]={
                'balance':initial_balance,
                'transaction_history':[]
            }
            print(f"Account {account_name} created with balance {initial_balance}.")

    def delete_account(self,account_name):
        if account_name in self.accounts:
            del self.accounts[account_name]
            print(f"Account {account_name} has been deleted.")
        else:
            print(f"Account {account_name} not found.")

    def view_balance(self,account_name):
        if account_name in self.accounts:
            balance=self.accounts[account_name]['balance']
            print(f"Balance of account {account_name}: {balance}")
        else:
            print(f"Account {account_name} not found.")

    def transfer_funds(self,from_account,to_account,amount):
        if from_account not in self.accounts:
            print(f"Account {from_account} not found.")
            return
        if to_account not in self.accounts:
            print(f"Account {to_account} not found.")
            return
        if self.accounts[from_account]['balance']<amount:
            print(f"Insufficient funds in {from_account} to transfer {amount}.")
            return
        self.accounts[from_account]['balance']-=amount
        self.accounts[to_account]['balance']+=amount
        self.accounts[from_account]['transaction_history'].append(f"Transferred {amount} to {to_account}.")
        self.accounts[to_account]['transaction_history'].append(f"Received {amount} from {from_account}.")
        print(f"Transferred {amount} from {from_account} to {to_account}.")

    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        print("List of all accounts & balances.")
        for account_name,data in self.accounts.items():
            print(f"Account: {account_name},Balance: {data['balance']}")

    def view_transaction_history(self,account_name):
        if account_name in self.accounts:
            print(f"Transaction history for {account_name}:")
            if not self.accounts[account_name]['transaction_history']:
                print("No transaction found.")
            else:
                for transaction in self.accounts[account_name]['transaction_history']:
                    print(f"-{transaction}.")


bank=BankingSystem()

bank.create_account("Alice",5000)
bank.create_account("Rifat",2000)

bank.view_balance("Alice")
bank.view_balance("Rifat")

bank.transfer_funds("Alice","Rifat",1000)

bank.list_all_accounts()

bank.view_transaction_history("Rifat")
bank.view_transaction_history("Alice")

bank.delete_account("Rifat")
bank.list_all_accounts()