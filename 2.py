"""
Shopping Cart Price Calculator

This program takes a list of item prices, removes the lowest-priced
item, applies a 10% discount to all remaining items, and prints the
final total formatted to two decimal places.
"""

# Item prices in the shopping cart
prices = [12.50, 45.00, 8.99, 120.00]

# Remove the lowest-priced item
prices.remove(min(prices))

# Apply a 10% discount to each remaining item
discounted_prices = [price * 0.90 for price in prices]

# Calculate the final total
final_total = sum(discounted_prices)

# Print the final total
print(f"Final total: ${final_total:.2f}")
