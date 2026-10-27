shopper_name_1 = "Sam Shore"
item_price_1 = 1.00
item_price_2 = 1.50
item_price_3 = 2.00
item_price_4 = 2.50
item_price_5 = 3.00

number_of_item_1 = 1
number_of_item_2 = 2
number_of_item_3 = 3
number_of_item_4 = 4
number_of_item_5 = 5

item_1_spending = number_of_item_1 * item_price_1
item_2_spending = number_of_item_2 * item_price_2
item_3_spending = number_of_item_3 * item_price_3
item_4_spending = number_of_item_4 * item_price_4
item_5_spending = number_of_item_5 * item_price_5

total_item_spending = item_1_spending + item_2_spending + item_3_spending + item_4_spending + item_5_spending
total_items_bought = number_of_item_1 + number_of_item_2 + number_of_item_3 + number_of_item_4 + number_of_item_5
average_price = total_item_spending / total_items_bought

print(f"{shopper_name_1}: Total bill ${total_item_spending}, average price per item ${round(average_price, 2)}")
