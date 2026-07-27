# ==========================================
# Exercise 1: Temperature Label
# ==========================================
temp = float(input("Enter temperature in °C: "))

if temp < 15:
    print("cold")
elif temp <= 28:
    print("warm")
else:
    print("hot")


# ==========================================
# Exercise 2: Receipt Loop
# ==========================================
for i in range(1, 11):
    print(f"Receipt #{i}")


# ==========================================
# Exercise 3: Even Numbers
# ==========================================
for num in range(1, 21):
    if num % 2 == 0:
        print(num)


# ==========================================
# Exercise 4: Discount Function
# ==========================================
def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    return price - discount_amount

# Testing with default discount (10%)
print("Original $100 with default discount:", apply_discount(100))

# Testing with explicit discount (20%)
print("Original $100 with 20% discount:", apply_discount(100, 20))


# ==========================================
# Exercise 5: Countdown
# ==========================================
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")