import re

symbols = ['AAPL', 'HP', 'IBM', 'AMZN', 'MSFT', 'GOOGL', 'INTC', 'CSCO', 'ORCL', 'QCOM']

# example input
# (34 AAPL shares buy at max 780, 24 IBM shares sell at min 228, 12 AAPL shares buy at max   27) for account Hokie123
s = raw_input()

# trades = 34 AAPL shares buy at max 780, 24 IBM shares sell at min 228, 12 AAPL shares buy at max   27
trades = s[s.find("(")+1:s.find(")")]

# trade = ['34 AAPL shares buy at max 780', '24 IBM shares sell at min 228', '12 AAPL shares buy at max   27']
trade = trades.split(",")

#extraString = for account Hokie123
extraString = s.split(")")[1]

# checking trade syntax
for t in trade:
    if len(t.split()) != 7:
        print("syntax error")
        exit()

# processing trade requests
for t in trade:
    string = t
    num1 = string.split()[0]
    symbol = string.split()[1]
    action = string.split()[3]
    action2 = string.split()[4]
    action3 = string.split()[5]
    num2 = string.split()[6]

    # check number syntax
    p = re.compile('^[1-9]+[0-9]*$')
    m1 = p.match(num1)
    m2 = p.match(num2)

    # No error in num1 and num2
    if m1 and m2:
        if action2 == "at":
            if action == "buy":
                if action3 == "max":
                    action = "BuyRequests "
                else:
                    errorPosition = string.find(action3)
                    formerString = string.split(action3)
                    print(formerString[0] + action3)
                    print(" " * int(errorPosition) + "^")
                    exit()
            elif action == "sell":
                if action3 == "min":
                    action = "SellRequests "
                else:
                    errorPosition = string.find(action3)
                    formerString = string.split(action3)
                    print(formerString[0] + action3)
                    print(" " * int(errorPosition) + "^")
                    exit()
            else:
                errorPosition = string.find(action)
                formerString = string.split(action)
                print(formerString[0] + action)
                print(" " * int(errorPosition) + "^")
                exit()
    # first number syntax error
    elif not m1:
        errorPosition = s.find(num1)
        formerString = s.split(num1)
        print(formerString[0] + num1)
        print(" " * int(errorPosition) + "^")
        exit()
    # second number syntax error
    else:

        errorPosition = s.find(num2)
        formerString = s.split(num2)
        print(formerString[0] + num2)
        print(" " * int(errorPosition) + "^")
        exit()

    # check for shares grammar
    if t.split()[2] != "shares":
        errorPosition = s.find(t.split()[2])
        formerString = s.split(t.split()[2])
        print(formerString[0] + t.split()[2])
        print(" " * int(errorPosition) + "^")
        exit()

    # when symbol is not in the given list of symbol
    if symbol not in symbols:
        errorPosition = s.find(symbol)
        formerString = s.split(symbol)
        print(formerString[0] + symbol)
        print(" " * int(errorPosition) + "^")
        exit()
    
    
    # for account syntax checking
    if extraString.split(" ", 3)[1] != "for":
        errorPosition = s.find(extraString.split(" ", 3)[1])
        formerString = s.split(extraString.split(" ", 3)[1])
        print(formerString[0] + extraString.split(" ", 3)[1])
        print(" " * int(errorPosition) + "^")
        exit()
    elif extraString.split(" ", 3)[2] != "account":
        errorPosition = s.find(extraString.split(" ", 3)[2])
        formerString = s.split(extraString.split(" ", 3)[2])
        print(formerString[0] + extraString.split(" ", 3)[2])
        print(" " * int(errorPosition) + "^")
        exit()
    else:
        account = extraString.split(" ", 3)[3:]


    # account syntax error
    p = re.compile('[a-zA-Z]+[0-9]+$')
    m = p.match(account[0])
    if not m:
        errorPosition = s.find(account[0])
        formerString = s.split(account[0])
        print(formerString[0] + account[0])
        print(" " * int(errorPosition) + "^")
        exit()


    # no syntax error, print result
    print("INSERT INTO " + action + "(NumShares, Symbol, MaxPrice, AccountID) VALUES ('{}', '{}', '{}', '{}')").format(num1, symbol, num2, account)