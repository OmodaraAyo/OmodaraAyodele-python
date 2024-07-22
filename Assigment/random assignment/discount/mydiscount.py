import discount


product_price = int (input ('Enter price: #'))
discount_on_product = int (input ('Enter discount: '))
result = (discount.my_discount(product_price, discount_on_product))
print (f'New price is #{result}')