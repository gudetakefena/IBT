class Account:
    def __init__(self, balance):
        self.balance = balance

# Create branches
root_branch = Branch("Root Branch")
sub_branch1 = Branch("Sub Branch 1")
sub_branch2 = Branch("Sub Branch 2")

# Create accounts
account1 = Account(100)
account2 = Account(200)
account3 = Account(300)

# Add accounts to branches
root_branch.add_account(account1)
sub_branch1.add_account(account2)
sub_branch2.add_account(account3)

# Add sub-branches to root branch
root_branch.add_child(sub_branch1)
root_branch.add_child(sub_branch2)

# Calculate total balance
print(root_branch.total_balance())  # Output: 600