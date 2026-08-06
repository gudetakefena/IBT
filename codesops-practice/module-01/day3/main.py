import os

input_filename = "transactions.txt"
output_filename = "report.txt"

totals = {}

# Steps 1 & 4: Try to read transactions line by line with exception handling
try:
    with open(input_filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            # Step 2: Parse line (expects "Name,Amount") and build total dict
            parts = line.split(",")
            if len(parts) == 2:
                name = parts[0].strip()
                amount = float(parts[1].strip())
                totals[name] = totals.get(name, 0.0) + amount

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found. Please create it first.")
    exit(1)
except ValueError:
    print("Error: Could not parse amount in file. Ensure format is 'Name,Amount'.")
    exit(1)

# Step 3: Sort customers by total spend (highest first)
sorted_totals = sorted(totals.items(), key=lambda item: item[1], reverse=True)

# Print to console and Step 5: Write summary to report.txt
print("--- TeleBirr Summary Report ---")
with open(output_filename, "w") as report_file:
    report_file.write("--- TeleBirr Summary Report ---\n")
    for name, total_spend in sorted_totals:
        line_str = f"{name}: {total_spend:.2f} ETB"
        print(line_str)
        report_file.write(line_str + "\n")

print(f"\nSummary successfully written to {output_filename}")