import ast
suits = input()
suits = ast.literal_eval(suits)
budget = int(input())

def findSalePrice(original_price, discount_rate):
    discount_price = original_price * (discount_rate/100)
    sale_price = original_price - discount_price
    return sale_price
def buy_expensive_suit(suits, budget):
    discounted_list = discounted_prices(suits)
    maximum_index = binary_search(discounted_list,budget)
    if maximum_index == -1 :
        return -1
    else:
        tupple = (suits[maximum_index][0],discounted_list[maximum_index])
        return tupple
def discounted_prices(suits):
    temp = []
    for i in range(len(suits)):
        temp.append(suits[i][1] * (1-(suits[i][2]/100)))
    return temp
def binary_search(lst,budget):
    before_length = 0
    found = False
    index_found = 0
    plus_index = 0
    no_of_times_break_and_larger = 0
    while found == False:
        index = int(len(lst)/2)
        if budget == lst[index]:
            index_found = index+plus_index
            found = True
        if len(lst) == 1 and found == False:
            if budget > lst[index]:
                index_found = index+plus_index
                found = True
            else:
                index_found = -1
            break
        elif budget < lst[index]:
            lst = lst[0:index]
        elif budget > lst[index]:
            if no_of_times_break_and_larger == 0 :
                before_length = len(lst)
            else:
                pass
            lst = lst[index:(len(lst))]
            plus_index = before_length - len(lst)
            plus_index = removing_minus(plus_index)
            no_of_times_break_and_larger += 1
    return index_found
def removing_minus(number):
    if number < 0 :
        number = number * -1
    return number

suit_to_buy = buy_expensive_suit(suits, budget)
print(suit_to_buy)