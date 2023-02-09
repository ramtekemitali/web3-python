# Ethereum smartContract with python
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

print(w3.isConnected())
print(w3.eth.blockNumber)

# to send CRyptocurrency
# acc_1,acc_2-ganache's address 1,2 and privatekey=address1's key
account_1 = "0x52bCC0116d39e55733F19BbBA143460e85cac307"
account_2 = "0x91cdc210DcdA0e308AEeEcE4B42e463048A7D20f"

private_key = "32875e9f4eb0b85f97e6fef1f7bc32e51a18db044cd49820f9060281a70e39d2"


# get the nonce
nonce = w3.eth.getTransactionCount(account_1) 

# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(tx_hash)
'''check ganache transaction'''
print(w3.toHex(tx_hash))

# send transaction
# get transaction hash