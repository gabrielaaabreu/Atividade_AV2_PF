stores_balance = {
    "Store 1" : "1500",
    "Store 2" : "1000", 
    "Store 3" : "500"
}

bank_clients = {
    "Mary" : "abc",
    "John" : "def",
    "James" : "ghi"
}

clients_bank_details = {
    "abc" : "123",
    "def" : "1234",
    "ghi" : "12345"
}

updateBalance = lambda store, amount : stores_balance.update({store : int(stores_balance[store]) + int(amount)})
printReceipt  = lambda : print("Cash payment received")
completeTransaction = lambda : print("Transaction completed")

def transactionApproved(store, amount):
    updateBalance(store, amount)
    completeTransaction()

checkBankApproval = lambda code, password : clients_bank_details[code] == password if code in clients_bank_details.keys() else False
checkBankDetails = lambda code, password : True if checkBankApproval(code, password) else False
paymentAnalysis = lambda user, code, password : checkBankDetails(code, password) if user in bank_clients.keys() else False
action = lambda store, amount, user, code, password : transactionApproved(store, amount) if paymentAnalysis(user, code, password) else print("Invalid bank deposit details. Transaction canceled.")

def execCash(store, amount):
    updateBalance(store, amount)
    printReceipt()
    completeTransaction()

def execFundTransfer(store, amount):
    user = "Mary"
    code = "abc"
    password = "123"
    action(store, amount, user, code, password)

def execCredit(store, amount):
    user = "Mary"
    code = "abc"
    password = "123"
    action(store, amount, user, code, password)

def chooseTransaction(transactionType, store, amount):
    createTransaction()
    selectTransaction(transactionType, store, amount)

selectTransaction = lambda transactionType, store, amount : execCredit(store, amount) if transactionType == "Credit" else execCash(store, amount) if transactionType == "Cash" else execFundTransfer(store, amount) if transactionType == "Fund Transfer" else "Invalid transaction type"

createTransaction = lambda : print("Starting transaction")

start = chooseTransaction

print(start("Cash", "Store 1", "30"))
print("---------------------")
print(stores_balance["Store 2"])
print(start("Fund Transfer", "Store 2", "100"))
print(stores_balance["Store 2"])





