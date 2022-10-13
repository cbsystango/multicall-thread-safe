
import concurrent.futures
import os

from web3 import Web3

from multicall.call import Call
from multicall.multicall import Multicall

os.putenv("ASYNC_W3", "0") # Disable Async W3
w3 = Web3(provider=Web3.HTTPProvider("https://rpc.ankr.com/eth/"))

def process_data(success=None, value=None):
	if success:
		return value
	else:
		return False


calls = [
	Call(
		'0xdAC17F958D2ee523a2206206994597C13D831ec7',
		'name()(bytes)',
		[['name', process_data()]]
	),
	Call(
		'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
		'name()(bytes)',
		[['name_two', process_data()]]
	),
	Call(
		'0xdAC17F958D2ee523a2206206994597C13D831ec7',
		'symbol()(bytes)',
		[['symbol', process_data()]]
	),
	Call(
		'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
		'symbol()(bytes)',
		[['symbol_two', process_data()]]
	),
	Call(
		'0xdAC17F958D2ee523a2206206994597C13D831ec7',
		'decimals()(uint256)',
		[['decimals', process_data()]]
	),
	Call(
		'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
		'decimals()(uint256)',
		[['decimals_two', process_data()]]
	),
]

def exec_mcall():
	multi = Multicall(
		calls, _w3=w3, require_success=False
	)
	return multi()

def main():
	futures = []
	with concurrent.futures.ThreadPoolExecutor(2) as executor:
		for _ in range(2):
			future = executor.submit(exec_mcall)
			futures.append(future)
	for future in concurrent.futures.as_completed(futures):
		print("mcall result ===>", future.result())
main()