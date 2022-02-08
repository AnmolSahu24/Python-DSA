
def MaxProfit(prices):
    Cost = prices[0]
    # Profit = 0
    Profit = prices[1]-prices[0]

    for sellPrice in prices:
        print("Sell",sellPrice)
        Cost = min(Cost,sellPrice)
        Profit = max(Profit,sellPrice-Cost)

        print("C",Cost)
        print("P",Cost)

    return Profit


pr = [7,1,5,3,6,4]
print(MaxProfit(pr))