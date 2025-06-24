def calculateTotalCost(cart,discounts):
    totalCost=0;
    for item in cart:
        itemCost=item['price']*item['quantity']
        if item['item_id'] in discounts:
            itemDisCount=itemCost*discounts[item['item_id']]
            itemCost-=itemDisCount;
        totalCost+=itemCost
    return totalCost

def main():
    cart=[
        {'item_id': 1,'productName': 'Some prduct', 'price': 1000, 'quantity':1},
        {'item_id': 2,'productName': 'Some prduct 1', 'price': 500, 'quantity':2},
        {'item_id': 3, 'productName': 'Some prduct 2', 'price': 200, 'quantity': 5}
    ]
    discounts={1:0.2}
    itemCost=calculateTotalCost(cart,discounts)
    print(itemCost)

main()