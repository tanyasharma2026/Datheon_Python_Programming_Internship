import csv
import os

PORTFOLIO_FILE = "portfolio.csv"

def load_portfolio():
    portfolio = {}
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                symbol = row["Symbol"].upper()
                portfolio[symbol] = {
                    "shares": int(row["Shares"]),
                    "buy_price": float(row["Buy Price"])
                }
    return portfolio

def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, mode='w', newline='') as file:
        fieldnames = ["Symbol", "Shares", "Buy Price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for symbol, data in portfolio.items():
            writer.writerow({
                "Symbol": symbol,
                "Shares": data["shares"],
                "Buy Price": data["buy_price"]
            })

def display_portfolio(portfolio):
    print("\n================ Current Portfolio ================")
    if not portfolio:
        print("Your portfolio is empty.")
        print("===================================================")
        return

    print(f"{'Stock':<10}{'Shares':<10}{'Buy Price':<12}{'Total Cost':<12}")
    print("-" * 46)
    
    total_portfolio_value = 0
    for symbol, data in portfolio.items():
        total_cost = data["shares"] * data["buy_price"]
        total_portfolio_value += total_cost
        print(f"{symbol:<10}{data['shares']:<10}${data['buy_price']:<11.2f}${total_cost:<11.2f}")
        
    print("-" * 46)
    print(f"Total Invested Amount: ${total_portfolio_value:.2f}")
    print("===================================================")

def add_stock(portfolio):
    symbol = input("Enter stock symbol (e.g., AAPL, GOOG): ").strip().upper()
    if not symbol:
        print("❌ Invalid symbol!")
        return
        
    try:
        shares = int(input(f"Enter number of shares for {symbol}: "))
        price = float(input(f"Enter purchase price per share ($): "))
        if shares <= 0 or price <= 0:
            print("❌ Shares and price must be greater than zero!")
            return
    except ValueError:
        print("❌ Invalid numeric input!")
        return

    if symbol in portfolio:
        total_shares = portfolio[symbol]["shares"] + shares
        total_cost = (portfolio[symbol]["shares"] * portfolio[symbol]["buy_price"]) + (shares * price)
        portfolio[symbol]["buy_price"] = total_cost / total_shares
        portfolio[symbol]["shares"] = total_shares
    else:
        portfolio[symbol] = {"shares": shares, "buy_price": price}

    save_portfolio(portfolio)
    print(f"✅ Successfully added {shares} shares of {symbol} to your portfolio.")

def remove_stock(portfolio):
    symbol = input("Enter stock symbol to remove: ").strip().upper()
    if symbol not in portfolio:
        print(f"❌ Stock {symbol} not found in your portfolio.")
        return

    try:
        shares_to_remove = int(input(f"You have {portfolio[symbol]['shares']} shares. How many to remove? "))
        if shares_to_remove <= 0:
            print("❌ Number of shares must be greater than zero!")
            return
        if shares_to_remove > portfolio[symbol]["shares"]:
            print("❌ You cannot remove more shares than you own!")
            return
    except ValueError:
        print("❌ Invalid numeric input!")
        return

    if shares_to_remove == portfolio[symbol]["shares"]:
        del portfolio[symbol]
    else:
        portfolio[symbol]["shares"] -= shares_to_remove

    save_portfolio(portfolio)
    print(f"✅ Successfully removed {shares_to_remove} shares of {symbol}.")

def main():
    portfolio = load_portfolio()
    while True:
        print("\n*** Stock Portfolio Tracker Menu ***")
        print("1. View Current Portfolio")
        print("2. Add / Update Stock")
        print("3. Remove Stock")
        print("4. Exit Tracker")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            display_portfolio(portfolio)
        elif choice == '2':
            add_stock(portfolio)
        elif choice == '3':
            remove_stock(portfolio)
        elif choice == '4':
            print("Exiting Portfolio Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid selection! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
    
