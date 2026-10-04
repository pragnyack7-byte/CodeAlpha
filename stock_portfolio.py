stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300
}
stock = input("Enter stock name(AAPL/TSLA/MSFT)").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity
    print("Total Investment: $", total)
else:
    print("Stock not found!")