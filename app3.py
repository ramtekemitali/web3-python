# how to deploy smartContract to the blockchain with python
# Create ethereum smartContract with Python

import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# print(w3.isConnected())
# print( w3.eth.blockNumber)

w3.eth.defaultAccount = w3.eth.accounts[0]


abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]');
bytecode = '608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610410806101166000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100c5578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100c3600480360381019080803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091929192905050506101e5565b005b3480156100d157600080fd5b506100da6101ff565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561011a5780820151818401526020810190506100ff565b50505050905090810190601f1680156101475780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101fb92919061033f565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102975780601f1061026c57610100808354040283529160200191610297565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a72305820257d97cbee6293347b6c7fbe579b72f44d0c3778072507abd88eb70cfbf07b930029'
	
Greeter = w3.eth.contract(bytecode=bytecode, abi=abi) 

tx_hash = Greeter.constructor().transact()
# print(tx_hash)

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# print(tx_receipt)
contract = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

print(contract.functions.greet().call())
tx_hash = contract.functions.setGreeting('HELLOOOOOOO!').transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(contract.functions.greet().call())