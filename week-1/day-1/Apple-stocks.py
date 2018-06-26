def get_max_profit(stock_prices_oda):

    
    
    buy_price = stock_prices_oda[0]
    sell_price = stock_prices_oda[1]
    best_profit = sell_price - buy_price
    i = 0

    for price in stock_prices_oda:

		
		if i < 1:
			i += 1
			pass


		elif price - buy_price > best_profit:
 			best_profit = price - buy_price
 			sell_price=price

		elif price <= buy_price:
			buy_price = price



    return best_profit
