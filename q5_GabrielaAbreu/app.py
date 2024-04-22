from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from flask import Flask, render_template, request
app = Flask(__name__)

key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
decipher = AES.new(key, AES.MODE_CBC, iv)

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
    "abc" : cipher.encrypt(pad(b'123', 16)),
    "def" : cipher.encrypt(pad(b'1234', 16)),
    "ghi" : cipher.encrypt(pad(b'12345', 16))
}

clients_balance = {
    "abc" : "1000",
    "def" : "500",
    "ghi" : "0"
}

#--------------------------------------------------------------------------
updateStoreBalance = lambda store, amount : stores_balance.update({store : int(stores_balance[store]) + int(amount)})
updateClientsBalance = lambda code, amount : clients_balance.update({code : int(clients_balance[code]) - int(amount)})
printReceipt  = lambda : "Cash payment received"
completeTransaction = lambda : "Transaction completed"

def execCash(store, amount):
    updateStoreBalance(store, amount)
    return printReceipt(), completeTransaction()

#--------------------------------------------------------------------------
def transactionApproved(store, code, amount):
    updateStoreBalance(store, amount), updateClientsBalance(code, amount)
    return completeTransaction(), closeTransaction()

closeTransaction = lambda : "Transaction closed"

paymentAnalysis = lambda user, code, password: unpad(decipher.decrypt(clients_bank_details[code]), 16).decode() == password if user in bank_clients.keys() else False

action = lambda store, amount, user, code, password : transactionApproved(store, code, amount) if paymentAnalysis(user, code, password) else "Invalid deposit details or not enough balance. Transaction canceled."

user = lambda : request.form.get("username")
code = lambda : request.form.get("usercode")
password = lambda : request.form.get("userpassword")

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

gettingFundTransfer = lambda : [e for e in start("Fund Transfer", "Store 1", "5")] if request.method == "POST" else render_template("info.html")

gettingCredit = lambda : [e for e in start("Credit", "Store 1", "50")] if request.method == "POST" else render_template("info.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cash")
def cash():
    res = lambda : [e for e in start("Cash", "Store 1", "50")]
    return res()

@app.route("/fundtransfer/", methods = ["POST", "GET"])
def fundtransfer():
    return gettingFundTransfer()
    

@app.route("/credit/", methods = ["POST", "GET"])
def credit():
    return gettingCredit()
    


    