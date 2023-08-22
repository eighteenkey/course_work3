def executed_base():
    """
    Функция примает json список, преобразует в python и фильтрует, оставляя только успешно выполненные транзакции.
    :return: Список выполненных банковских транзакций.
    """
    import json
    executed_transactions = []

    with open('operations.json', 'r', encoding="utf-8") as operations_list:
        operations_read = operations_list.read()
    transactions = json.loads(operations_read)

    for transaction in transactions:
        if transaction.get('state') == 'EXECUTED':
            executed_transactions.append(transaction)
    return executed_transactions


def recent_transactions(executed_transactions):
    """
    Сортировка по дате.
    :param list_transactions: Список тразакций.
    :return: 5 последних успешных транзакций (по дате).
    """
    from datetime import datetime

    recent_transactions = sorted(executed_transactions,
    key=lambda item: datetime.fromisoformat(item['date']),
    reverse=True)[:5]
    return recent_transactions


def transaction_output(new_transactions):
    """
    Преобразование данных в нужный формат.
    :param сортированный список данных.
    :return: Данные транзакций в необходимом формате.
    """
    from datetime import datetime
    result_string = ""

    for item in new_transactions:
        date = datetime.fromisoformat(item['date']).strftime('%d.%m.%Y')
        description = item['description']
        operation_amount = item['operationAmount']['amount']
        currency = item['operationAmount']['currency']['name']
        to_ = 'Счет **' + item['to'][-4:]
        from_ = item.get('from')
        if from_ == None:
            card_number = "Неизвестно"
        elif from_[0:4] == "Счет":
            card_number = 'Счет **' + from_[-4:]
        else:
            card_number = "{} {}{} {}".format(from_[0:-12], from_[-12:-10], '** ****', from_[-4::])

        result_string += f'{date} {description}\n{card_number} -> {to_}\n{operation_amount} {currency}\n\n'

    return result_string