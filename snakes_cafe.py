

welcom='''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************'''

Appetizers = ["Wings",'Cookies','Spring Rolls']
Entrees =['Salmon','Steak', 'Meat Tornado','A Literal Garden']
Desserts= ['Ice Cream','Cake','Pie']
Drinks =['Coffee','Tea','Unicorn Tears']

make_order="""***********************************
** What would you like to order? **
***********************************"""
print(welcom)
print('')

print("Appetizers")
print("----------")
for item in Appetizers:
    print(item)

print('')
print("Entrees")
print("----------")
for item in Entrees:
    print(item)

print('')
print("Desserts")
print("----------")
for item in Desserts:
    print(item)

print('')
print("Drinks")
print("----------")
for item in Drinks:
    print(item)

print(make_order)



order=""
arr=[]
while order !='quit':
    order=input("> ")
    if order !='quit':
        if order in Appetizers or order in Entrees or order in Desserts or order in Drinks :
            arr.append(order)
            print(f"** {arr.count(order)} order of {order} has been added to your meal **")
        else: print(f"this order {order} is not available now")
        

print("you'r list orders are " ,arr)
