# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

print("===== Stock Portfolio Tracker =====")

total_investment = 0

# Number of different stocks
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("\nEnter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity

        print("Stock Price:", price)
        print("Investment:", investment)

        total_investment += investment
    else:
        print("Stock not available in the list.")

# Display total
print("\n-----------------------------")
print("Total Investment Value:", total_investment)
print("-----------------------------")

# Optional: Save result to a text file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("------------------------\n")
        file.write("Total Investment Value: " + str(total_investment))

    print("Result saved in portfolio.txt")
