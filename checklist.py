# programma die de som berekent van 2 input cijfers (en alles ertussen), bijv: 2 & 5 -> 2 + 3 + 4 + 5

# Step 1: Get input in the format "a & b"
print("Benodigde format -> a & b -> bijv: 6 & 10")
user_input = input("Geef twee integers in de bovenstaande format\n")

# Step 2: Split input by '&' and convert to integers
a, b = map(int, user_input.split("&"))

# Step 3: Clean up whitespace if user types spaces around '&'
a, b = int(str(a).strip()), int(str(b).strip())

# Step 4: Determine start and end
start = min(a, b)
end = max(a, b)

# Step 5: Calculate the sum
totaal = sum(range(start, end + 1))

# Step 6: Display result
print(f"Het totaal van {start} tot {end} is {totaal}")

