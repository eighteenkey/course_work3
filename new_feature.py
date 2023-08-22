from function import executed_base, recent_transactions, transaction_output

executed_transactions = executed_base()
new_transactions = recent_transactions(executed_transactions)
print(transaction_output(new_transactions))