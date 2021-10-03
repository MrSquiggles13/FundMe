from brownie import MockV3Aggregator, network, config, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-forked', 'mainnet-fork-dev']
CUSTOM_LOCAL_ENVIRONMENTS = ['development', 'ganache-local']

DECIMALS = 8
STARTING_VALUE = 200000000000

def get_account():
    if network.show_active() in CUSTOM_LOCAL_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    print(f"Active Network: {network.show_active()}")
    print("***Deploying Mocks***")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_VALUE, {'from': get_account()})
    print("***Mocks Deployed***")