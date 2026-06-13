import uuid
import datetime
import logging

my_trabsactions = {}
curency_rate = {"USD":43,"UAH":1,"EUR":52}

logging.basicConfig(level=logging.DEBUG)


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
    try:
        transaction = my_trabsactions[id_trans]
    except KeyError:
        print("Немає такої транзакції")
        return

    for key, value in kwargs.items():
        if key in transaction:
            transaction[key] = value
        else:
            print("Такого поля неіснує")

my_id = input("ID: ")
edit_transaction(my_id, category = "Education")
print(my_trabsactions)

def delete_transaction(id_trans):
    try:
        del my_trabsactions[id_trans]

    except KeyError:
        print("Нема такого ID")
        logging.warning("Невірне введення транзакції")


delete_transaction(my_id)
print(my_trabsactions)

def curensy_translate_uah(curency,amount):
    try:
        final_amount_uah = amount * curency_rate[curency]
        return final_amount_uah
    except KeyError:
        print("З такою валютою не працюємо")
        return 0

print(curensy_translate_uah("POL",100))

def get_transaction_in_range(date_from, date_to):
    result = {}
    for key, value in my_trabsactions.items():
        trans_date = datetime.datetime.fromisoformat(value["date"])
        if date_from <= trans_date <= date_to:
            result[key] = value
    return result

def zvit(dict_transaction):
    total = 0
    for key, value in dict_transaction.items():
        amount_in_uah = curensy_translate_uah(value["currency"], value["amount"])
        total += amount_in_uah
    print(f"Потрачено за введений період: {total}")

def month(year = None,month = None):
    now = datetime.datetime.now()
    year_data = now.year if year is None else year
    month_data = now.month if month is None else month
    if month_data  == 12:
        date_to = datetime.datetime(year_data+1, 1, 1)
    else:
        date_to = datetime.datetime(year_data, month_data + 1, 1)
    date_from = datetime.datetime(year_data,month_data,1)
    range_of_transactions = get_transaction_in_range(date_from, date_to)
    zvit(range_of_transactions)

def week():
    now = datetime.datetime.now()
    date_from = now - datetime.timedelta(weeks=1)
    range_of_transactions = get_transaction_in_range(date_from, now)
    zvit(range_of_transactions)

def year(year = None):
    now = datetime.datetime.now()
    year_data = now.year if year is None else year
    date_from = datetime.datetime(year_data, 1, 1)
    date_to = datetime.datetime(year_data + 1, 1, 1)
    range_of_transactions = get_transaction_in_range(date_from, date_to)
    zvit(range_of_transactions)

month()
week()
month(2026,6)