import functools
from flask import Flask, render_template, request
app = Flask(__name__)

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
printReceipt  = lambda : "Cash payment received"
completeTransaction = lambda : "Transaction completed"

def execCash(store, amount):
    updateStoresBalance(store, amount)
    return printReceipt(), completeTransaction()

#--------------------------------------------------------------------------
def transactionApproved(store, code, amount):
    updateStoresBalance(store, amount), updateClientsBalance(code, amount)
    return completeTransaction(), closeTransaction()

closeTransaction = lambda : "Transaction closed"

paymentAnalysis = lambda user, code, password: clients_bank_details[code] == password if user in bank_clients.keys() else False

action = lambda store, amount, user, code, password : transactionApproved(store, code, amount) if paymentAnalysis(user, code, password) else "Invalid deposit details or not enough balance. Transaction canceled."

user = lambda : str(request.form["username"])
code = lambda : str(request.form["usercode"])
password = lambda : str(request.form["userpassword"])

def execFundTransfer(store, amount):
    return action(store, amount, user(), code(), password())

#--------------------------------------------------------------------------
def execCredit(store, amount):
    return action(store, amount, user(), code(), password())

#--------------------------------------------------------------------------
def chooseTransaction(transactionType, store, amount):
    return createTransaction(), selectTransaction(transactionType, store, amount)

selectTransaction = lambda transactionType, store, amount : execCredit(store, amount) if transactionType == "Credit" else execCash(store, amount) if transactionType == "Cash" else execFundTransfer(store, amount) if transactionType == "Fund Transfer" else "Invalid transaction type"

createTransaction = lambda : "Starting transaction"

start = chooseTransaction

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cash")
def cash():
    res = lambda : [e for e in start("Cash", "Store 1", "50")]
    return res()

@app.route("/fundtransfer/", methods = ["POST", "GET"])
def fundtransfer():
    if request.method == "POST":
        res = lambda : [e for e in start("Fund Transfer", "Store 1", "5")]
        return res()
    else:
        return render_template("info.html")
    

@app.route("/credit/", methods = ["POST", "GET"])
def credit():
    if request.method == "POST":
        res = lambda : [e for e in start("Credit", "Store 1", "50")]
        return res()
    else:
        return render_template("info.html")


    