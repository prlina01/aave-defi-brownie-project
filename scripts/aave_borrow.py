from brownie import network, config, interface

from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account
from web3 import Web3

amount = Web3.toWei(0.1, 'ether')

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]['weth_token']
    if network.show_active() in ['mainnet-fork']:
        get_weth()
    lending_pool = get_lending_pool()
    approve_erc20(amount, lending_pool.address, erc20_address, account)

def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config['networks'][network.show_active()]['lending_pool_addresses_provider']
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()

    lending_pool = interface.IlendingPool(lending_pool_address)
    return lending_pool

def approve_erc20(amount, spender, erc20_address, account):
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    return tx
