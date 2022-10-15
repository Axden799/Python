def maxProfit(prices) -> int:
        max_diff = 0
        for x in range(len(prices)):
            for y in prices[x:]:
                diff = y - prices[x]
                if diff > max_diff:
                    max_diff = diff
        if max_diff < 1:
            return 0
        else:
            return max_diff

def maxProfitBetter(prices) -> int:
    min_price = math.inf
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price) > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

tests = {
    'test1': {
        'prices': [7, 6, 4, 3, 1],
        'expected': 0
    }
}

for test in tests.values():
    response = maxProfit(test['prices'])
    result = True if test['expected'] == response else False
    print(f"response: {response}, result: {result}")