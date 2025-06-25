# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

# Dictionary to store user portfolio
portfolio = {}

# Take user input
while True:
    stock = input("Enter stock symbol (e.g. AAPL), or 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty < 0:
                print("Quantity can't be negative. Try again.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    else:
        print("Stock not found in price list.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("Do you want to save the result? (yes/no): ").lower()
if save == "yes":
    try:
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                investment = price * qty
                file.write(f"{stock}: {qty} shares x ${price} = ${investment}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("✅ Portfolio saved to 'portfolio_summary.txt'")
    except Exception as e:
        print(f"⚠️ Error saving file: {e}")
