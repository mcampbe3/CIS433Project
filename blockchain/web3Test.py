from web3 import Web3

url = "https://mainnet.infura.io/v3/e0a31e6522e54dccac113c00fe1ae0fb"

web3 = Web3(Web3.HTTPProvider(url))

web3.isConnected()


print(web3.eth.blockNumber)
