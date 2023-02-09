# Use Ethereum Blockchain with Python

from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/bbe015b6dfb64d11befb9ff1695c6d56"
w3 = Web3(Web3.HTTPProvider(infura_url))

# get all information from last block created shows on Etherscan
latest = w3.eth.blockNumber
print(latest)
print(w3.eth.getBlock(latest))

# count latest 10 blocks using python
for i in range(0, 10):
    print(w3.eth.getBlock(latest - i))
    
    
# to get data from specific transaction using Etherscan
hash = '0xd6fa1274f3bffe3528b5abacbea97c3930b60edd7716727f904ac298a9745299'
print(w3.eth.getTransactionByBlock(hash, 2))