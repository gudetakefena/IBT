class Account:[{
	"resource": "/c:/Users/Dell/Desktop/IBT/codesops-practice/module 01/day8/main.py",
	"owner": "Pylance",
	"code": {
		"value": "reportUndefinedVariable",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pylance-release/blob/main/docs/diagnostics/reportUndefinedVariable.md",
			"scheme": "https",
			"authority": "github.com"
		}
	},
	"severity": 4,
	"message": "\"name\" is not defined",
	"source": "Pylance",
	"startLineNumber": 75,
	"startColumn": 4,
	"endLineNumber": 75,
	"endColumn": 8,
	"modelVersionId": 39,
	"origin": "extHost1"
}]
    def init(self, account_number, name, balance, transactions=None):
        self.account_number = account_number  # Integer or unique string
        self.name = name
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def repr(self):
        return f"Account({self.account_number}, '{self.name}', Balance: {self.balance})"


class AccountRegistry:
    def init(self):
        self.accounts = []

    # Step 1 & 3 requirement: Keeping data sorted automatically upon addition
    def add_account(self, account):
        """Adds an account and ensures the list remains sorted by account_number for binary search."""
        self.accounts.append(account)
        # Binary search requires the dataset to be sorted
        self.accounts.sort(key=lambda acc: acc.account_number)

    # Step 2: Add top_by_balance(n) using sorted with a key=lambda
    def top_by_balance(self, n):
        """Returns the top n accounts with the highest balances."""
        # Sorts in descending order (highest balance first) using lambda
        sorted_accounts = sorted(self.accounts, key=lambda acc: acc.balance, reverse=True)
        return sorted_accounts[:n]

    # Step 3: Write custom binary_search and find_by_number()
    def _binary_search(self, target_number):
        """Custom iterative binary search implementation."""
        low = 0
        high = len(self.accounts) - 1

        while low <= high:
            mid = (low + high) // 2
            current_num = self.accounts[mid].account_number

            if current_num == target_number:
                return mid  # Return the index where the account is found
            elif current_num < target_number:
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Target not found

    def find_by_number(self, account_number):
        """Uses custom binary search to locate an account by its number."""
        index = self._binary_search(account_number)
        if index != -1:
            return self.accounts[index]
        return None

    # Step 4: Add recursive total_transactions() for one account
    def total_transactions(self, account_number):
        """Finds the account and computes total transaction amounts recursively."""
        account = self.find_by_number(account_number)
        if not account:
            return 0
        
        # Helper function to perform the recursion safely
        def _recursive_sum(transactions, index):
            # Base case: end of the transaction list reached
            if index == len(transactions):
                return 0
            # Recursive step: current item value + sum of the remaining items
            return transactions[index] + _recursive_sum(transactions, index + 1)

        return _recursive_sum(account.transactions, 0)


# Step 5: Test all three on sample data
if name == "main":
    registry = AccountRegistry()

    # Populate Sample Data (Out of order to verify sorting/searching functions)
    registry.add_account(Account(104, "gudeta", 500, [100, -50, 200]))
    registry.add_account(Account(101, "sara", 12000, [500, 1500, -200]))
    registry.add_account(Account(103, "Chale", 1500, [50, 50, 100]))
    registry.add_account(Account(102, "girma", 8500, [1000, -300]))

    print("--- 1. Testing Leaderboard (Top 2 by Balance) ---")
    top_accounts = registry.top_by_balance(2)
    for idx, acc in enumerate(top_accounts, 1):
        print(f"Rank {idx}: {acc.name} - ${acc.balance}")

    print("\n--- 2. Testing Custom Binary Search ---")
    target_id = 103
    found_account = registry.find_by_number(target_id)
    print(f"Searching for Account #{target_id}: {found_account}")

    missing_id = 999
    print(f"Searching for Account #{missing_id}: {registry.find_by_number(missing_id)}")

    print("\n--- 3. Testing Recursive Transactions Total ---")
    bob_total = registry.total_transactions(101)
    print(f"gudeta's total transaction ledger sum: ${gudeta_total}")