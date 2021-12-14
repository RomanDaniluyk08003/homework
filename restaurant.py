food_1_name      = 'Pizza'
food_2_name      = 'Cola'
food_3_name      = 'French fries'
food_1_price     = 100
food_2_price     = 50
food_3_price     = 150
food_1_available = 100
food_2_available = 100
food_3_available = 100
food_delivery    = 150 
food_1_quantity  = str(input('How many ' + food_1_name + ' do you want ? '))
if int(food_1_quantity) > food_1_available :
    print("This quantity is out of stock")
food_2_quantity  = str(input('How many ' + food_2_name + ' do you want ? '))
if int(food_2_quantity) > food_2_available :
    print("This quantity is out of stock")
food_3_quantity  = str(input('How many ' + food_3_name + ' do you want ? '))
if int(food_3_quantity) > food_3_available :
    print("This quantity is out of stock")
food_1_cost = int(food_1_quantity) * food_1_price
food_2_cost = int(food_2_quantity) * food_2_price
food_3_cost = int(food_3_quantity) * food_3_price
total_1 = food_1_cost+food_2_cost+food_3_cost
total_2 = food_1_cost+food_2_cost+food_3_cost+food_delivery
delivery = input("Do you need delivery? Y/N ")
if delivery == 'Y':
    if  (food_1_cost+food_2_cost+food_3_cost)>1000:
        print('You have ordered \n',food_1_quantity,' x ',food_1_name,' = ',food_1_cost,'\n',
                                    food_2_quantity,' x ',food_2_name,' = ',food_2_cost,'\n', 
                                    food_3_quantity,' x ',food_3_name,' = ',food_3_cost,'\n',
                        'Total  - ',total_1)
    else :
        print('You have ordered \n',food_1_quantity,' x ',food_1_name,' = ',food_1_cost,'\n',
                                    food_2_quantity,' x ',food_2_name,' = ',food_2_cost,'\n', 
                                    food_3_quantity,' x ',food_3_name,' = ',food_3_cost,'\n',
                        'Delivery-',food_delivery,'\n',
                         'Total - ',total_2)                            