##  Using Web3
from web3 import Web3
import json

# from shared_lib import *

################################################################################
# https://web3py.readthedocs.io/en/stable/quickstart.html
## Smart contracts are simply programs that run on blockchain
# infura_url_to_mainnet = "https://mainnet.infura.io/v3/287232e219cc4e319c6cae482494059f"
# web3 = Web3(Web3.HTTPProvider(infura_url_to_mainnet))
#
# print("Connected to infura url: " +  str(web3.isConnected()))
# print("Ethereum Block Number: " + str(web3.eth.blockNumber))
#
#
# balance = web3.eth.getBalance("0x0f02a78AB1a4adaE206444F7820d20033788e558")
# print("My balance: " + str(web3.fromWei(balance, 'ether')) + "\n")
#
# abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
# xrp_contract_addr = "0x90f64cd258373c6a2bf7f0fc0034d1a95ff6954e"
# omiseGO_addr = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"
#
# # print_json(abi)
# print()
#
# contract = web3.eth.contract(address=omiseGO_addr, abi=abi)
# print(contract)
#
# ## Simply functions
# total_supply = contract.functions.totalSupply().call()
# total_supply_18 = web3.fromWei(total_supply, 'ether')
#
# print("Entire int: " + str(total_supply))
# print(web3.fromWei(total_supply, 'ether'))
# print("Total Supply of " + contract.functions.name().call() + "(" + contract.functions.symbol().call() + "): " + str(total_supply_18))
# ## More functions at https://etherscan.io/token/0xd26114cd6EE289AccF82350c8d8487fedB8A0C07#readContract
#
# biggest_balance = contract.functions.balanceOf('0xd26114cd6EE289AccF82350c8d8487fedB8A0C07').call()
# print(web3.fromWei(biggest_balance, 'ether'))


###############################################################################
# ##  Sending transactions on a local blockchain Ganache(imagine this being the Ethereum Main net)
# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
#
# account_sender = '0xf387b3256865b24a13cb416f30A2e130E47ff6FA'
# account_recipient = '0xcA7dA3795C7F5Fb15912050B01e3b3790197386d'
#
# sender_private_key = '38bda8028fb8272d65603a7fadb8fa6f51b4952877712032cc30e42e98784dd5'
# recipient_private_key = '51f67f264e7a5b57e4b9d5c3e14772cfc8a1d90668f4172e7bdb501b01d8f536'
#
#
# # get a nonce
# nonce = web3.eth.getTransactionCount(account_sender)
# amount_to_send = 1
# ## Build transaction
# tx = {
#     'nonce' : nonce,                           ## prevents sending transaction twice
#     'to'    : account_recipient,
#     'value' : web3.toWei(amount_to_send, 'ether'),
#     'gas'   : 200000,
#     'gasPrice': web3.toWei('50', 'gwei')
# }
#
# ## Sign ttransaction
# signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)
#
# ## Send transaction
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#
# ## Get transaction hash
# print(tx_hash)


################################################################################
# ## Using Remix with ganache_url
# web3.eth.defaultAccount = web3.eth.accounts[0]
#
# ## Load the abi from the smart contract at remix.ethereum
# abi = json.loads('[{"constant":false,"inputs":[],"name":"kill","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
#
# ## Validate and get the contract that was deployed
# contract_address = web3.toChecksumAddress("0x1b44105d5e8add054f8b927f1f55c1b0b9610e34")
#
# contract = web3.eth.contract(address=contract_address, abi=abi)
#
# print(contract.functions.greet().call())
#
# ## modify the contract directly
# tx_hash = contract.functions.setGreeting('We are resetting sending the message back :)').transact()
#
# print("TX HASH: ")
# print(tx_hash)
# print()
#
# ##  make sure we actually have a valid transaction that twent through
# contract_bytecode =  "608060405234801561001057600080fd5b506040516105593803806105598339810180604052602081101561003357600080fd5b81019080805164010000000081111561004b57600080fd5b8281019050602081018481111561006157600080fd5b815185600182028301116401000000008211171561007e57600080fd5b5050929190505050336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600190805190602001906100dc9291906100e3565b5050610188565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061012457805160ff1916838001178555610152565b82800160010185558215610152579182015b82811115610151578251825591602001919060010190610136565b5b50905061015f9190610163565b5090565b61018591905b80821115610181576000816000905550600101610169565b5090565b90565b6103c2806101976000396000f3fe608060405260043610610051576000357c01000000000000000000000000000000000000000000000000000000009004806341c0e1b514610056578063a41368621461006d578063cfae321714610135575b600080fd5b34801561006257600080fd5b5061006b6101c5565b005b34801561007957600080fd5b506101336004803603602081101561009057600080fd5b81019080803590602001906401000000008111156100ad57600080fd5b8201836020820111156100bf57600080fd5b803590602001918460018302840111640100000000831117156100e157600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610235565b005b34801561014157600080fd5b5061014a61024f565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561018a57808201518184015260208101905061016f565b50505050905090810190601f1680156101b75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415610233573373ffffffffffffffffffffffffffffffffffffffff16ff5b565b806001908051906020019061024b9291906102f1565b5050565b606060018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102e75780601f106102bc576101008083540402835291602001916102e7565b820191906000526020600020905b8154815290600101906020018083116102ca57829003601f168201915b5050505050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061033257805160ff1916838001178555610360565b82800160010185558215610360579182015b8281111561035f578251825591602001919060010190610344565b5b50905061036d9190610371565b5090565b61039391905b8082111561038f576000816000905550600101610377565b5090565b9056fea165627a7a72305820c78a8bda7369a77372be9bc098e7556c8b582fd2bf313815367a3504294e6c480029"
# Greeter  =  web3.eth.contract(abi=abi, bytecode=contract_bytecode)
#
# web3.eth.waitForTransactionReceipt(tx_hash)
# print("The data sent should be the data received!")
# print("Updatted greeting: {}".format(contract.functions.greet().call()) )
#
# ## Creating and deploying a contract from python
# print("Deploying contract from python")
# tx_hash_python_deployed = Greeter.constructor("Local  Python").transact()
# print(tx_hash_python_deployed)
#
# receipt_python_deployed = web3.eth.waitForTransactionReceipt(tx_hash_python_deployed)
# print(receipt_python_deployed)
#
# contract_python_deployed = web3.eth.contract(address=receipt_python_deployed.contractAddress, abi=abi)
# ## This should be specifed from above
# print(contract_python_deployed.functions.greet().call())


####################### WEB APP DEMO BELOW ###############################
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


@app.route('/success/<name>')
def success(name):

   return render_template("send_amount.html", name="name")


## For a basic, non secure login page
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      # user = request.args.get('nm')
      # return redirect(url_for('success',name = user))
      return render_template("login.html")

@app.route('/send_amount', methods=['POST'])
def send_amount():
    if request.method == 'POST':
       sender = request.form['sender']
       sender_private_key = request.form['sender_private_key']
       receiver = request.form['receiver']
       amount = request.form['amount']
       print(sender, receiver, amount)
       tx_hash = send_money(sender, sender_private_key,receiver, amount)
       return render_template("money_sent.html", sender=sender, receiver=receiver, amount=amount, tx_hash=tx_hash)


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
def send_money(sender, sender_private_key, receiver, amount):
    # get a nonce
    nonce = web3.eth.getTransactionCount(sender)

    ## Build transaction
    tx = {
        'nonce' : nonce,                           ## prevents sending transaction twice
        'to'    : receiver,
        'value' : web3.toWei(amount, 'ether'),
        'gas'   : 200000,
        'gasPrice': web3.toWei('50', 'gwei')
    }


    ## Sign ttransaction
    signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)

    ## Send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return tx_hash

if __name__ == '__main__':
   app.run(debug = True)
