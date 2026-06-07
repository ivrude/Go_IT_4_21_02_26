import uuid
import datetime


my_trabsactions = {}
curency_rate = {"USD":43,"UAH":1,"EUR":52}


def add_transaction(category, amount, currency):
    date = str(datetime.datetime.now())
    id_trans = str(uuid.uuid4())
    id_trans = id_trans[:8]
    my_trabsactions[id_trans] ={"category":category,"amount":amount,"currency":currency, "date":date}

add_transaction("Product",100,"USD")
add_transaction("Films",100,"USD")
add_transaction("Films",100,"USD")

print(my_trabsactions)

def edit_transaction(id_trans, **kwargs):
    transaction = my_trabsactions[id_trans]
    for key, value in kwargs.items():
        if key in transaction:
            transaction[key] = value
        else:
            print("Такого поля неіснує")

my_id = input("ID: ")
edit_transaction(my_id, category = "Education")
print(my_trabsactions)

def delete_transaction(id_trans):
    if id_trans not in my_trabsactions:
        print("Друже, нема таої транзакції")
    else:
        del my_trabsactions[id_trans]

delete_transaction(my_id)
print(my_trabsactions)

def curensy_translate_uah(curency,amount):
    if curency not in curency_rate:
        print("З такою валютою не працюємо")
        return None
    else:
        final_amount_uah = amount * curency_rate[curency]
        return final_amount_uah

print(curensy_translate_uah("USD",100))

