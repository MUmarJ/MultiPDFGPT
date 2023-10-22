import json
from solcx import compile_standard, install_solc
from web3 import Web3

install_solc("0.8.17")

with open("./SimpleStorage.sol", "r") as f:
    simple_storage_file = f.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.deployedBytecode"]}
            }
        },
    },
    solc_version="0.8.17",
)

# Get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Network params
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x6c5f30bD019732Fd1C0cd033122EcC3b79ab7305"
private_key = "0xcd33556b1e617ecd95b3e4a5a79a8fa42e752fc430f0ad93f31a3e7dcbd20692"

# Create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.get_transaction_count(my_address)
# print(nonce)

# Build transaction, sign and send transaction
transaction = SimpleStorage.constructor().build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)

# Sign transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print(tx_hash.hex())


# Working with Contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(simple_storage.functions.retrieve().call())
transaction = simple_storage.functions.store(15).build_transaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(simple_storage.functions.retrieve().call())
