# Step 1: Store bill total (in ETB) and list of friends
bill_total = 1200.00  # Total bill in ETB
friends = ["Abebe", "Kebede", "Tigist", "Marta"]
num_people = len(friends)

# Step 2 & 3: Define function to calculate per-person share including tip
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total * (1 + tip_rate)
    per_person = total_with_tip / people
    return per_person

# Calculate the share using the function
share_per_person = split_bill(bill_total, num_people)

# Step 4: Loop over the list of names and print each person's share
print(f"Total Bill: {bill_total} ETB (Tip: 10%)\n")
for person in friends:
    print(f"{person} owes: {share_per_person:.2f} ETB")