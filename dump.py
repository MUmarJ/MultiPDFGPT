import json
from solcx import compile_standard, install_solc

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

with open("./compiled_code.json", "w+") as f:
    json.dump(compiled_sol, f)
