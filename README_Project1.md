Project1 README
===
written by Sam Heo and Eunoh Cho
---
Specification of input for part 2
> Part2 A
    
    (16 AAPL shares buy at max 600, 26 IBM shares sell at max 228) for account Hokie123

    (16 AAPL shares buy at max 604, 27 GOOGL shares sell at min 228) for account Ho-kie123

    (17 AAPL shares buy at                      max 780,1 IBM shares sell at min 228) for account Hokie123

    (181 AAPL shares buy at min 602, 29 IBM shares sell at min 228) for account Hokie123


> Part2 B
    
    (19 AAPL shares cancel at request 19, 20 IBM shares cancel at request 10) for account Hokie123

    (34 AAPL shares buy at max 780, 10 GOOGL shares buy at max 780, 10 AAPL shares cancel at request 10) for account Hokie123


>grammar for the part2 B

    <stock_trade_requests> →  ‘(' <trade> {‘,’ <trade>} ‘) for account' <acct_ident>
    <trade> → <number> <stock_symbol> ‘shares’ (‘buy at max' | ‘sell at min' | 'cancel at request') <number>
    <number> →  [1-9] {[0-9]}
    <stock_symbol> →
    'AAPL'|'HP'|'IBM'|'AMZN'|'MSFT'|'GOOGL'|'INTC'|'CSCO'|'ORCL'|'QCOM'
    <acct_ident> →  ‘“‘alpha_char { alpha_char | digit | ’_’} ‘“‘
