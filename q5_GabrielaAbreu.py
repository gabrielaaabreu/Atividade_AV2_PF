stores_balance = { 
    "Store 1" : "1500",
    "Store 2" : "1000", 
    "Store 3" : "500"
}

stores_details = {
    "Store 1" : "jkl",
    "Store 2" : "mno", 
    "Store 3" : "pqr"
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

clients_balance = {
    "abc" : "1000",
    "def" : "500",
    "ghi" : "0"
}

#--------------------------------------------------------------------------
updateStoresBalance = lambda store, amount : stores_balance.update({store : int(stores_balance[store]) + int(amount)})
updateClientsBalance = lambda code, amount : clients_balance.update({code : int(clients_balance[code]) - int(amount)})
printReceipt  = lambda : print("Cash payment received")
completeTransaction = lambda : print("Transaction completed")

def execCash(store, amount):
    updateStoresBalance(store, amount)
    printReceipt()
    completeTransaction()

#--------------------------------------------------------------------------
def transactionApproved(store, code, amount):
    updateStoresBalance(store, amount)
    updateClientsBalance(code, amount)
    completeTransaction()
    closeTransaction()

closeTransaction = lambda : print("Transaction closed")
checkBankDetails = lambda code, password, amount : clients_bank_details[code] == password and clients_balance[code] >= amount if code in clients_bank_details.keys() else False
paymentAnalysis = lambda user, code, password, amount : checkBankDetails(code, password, amount) if user in bank_clients.keys() else False

action = lambda store, amount, user, code, password : transactionApproved(store, code, amount) if paymentAnalysis(user, code, password, amount) else print("Invalid deposit details or not enough balance. Transaction canceled.")

user = lambda : input("User: ")
code = lambda : input("Code: ")
password = lambda : input("Password: ")

def execFundTransfer(store, amount):
    action(store, amount, user(), code(), password())

#--------------------------------------------------------------------------
def execCredit(store, amount):
    action(store, amount, user(), code(), password())

#--------------------------------------------------------------------------
def chooseTransaction(transactionType, store, amount):
    createTransaction()
    selectTransaction(transactionType, store, amount)

selectTransaction = lambda transactionType, store, amount : execCredit(store, amount) if transactionType == "Credit" else execCash(store, amount) if transactionType == "Cash" else execFundTransfer(store, amount) if transactionType == "Fund Transfer" else "Invalid transaction type"

createTransaction = lambda : print("Starting transaction")

start = chooseTransaction

from flask import Flask

app = Flask('app')

@app.route('/')
def beginning () :
    return start

app.run(host='0.0.0.0', port=8080)