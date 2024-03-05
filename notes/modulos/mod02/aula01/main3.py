from eth_account import Account

seed = "jump skull butter topic bronze member feed wait flee oven deer rabbit"

Account.enable_unaudited_hdwallet_features()
account = Account().from_mnemonic(mnemonic=seed)

print(account.key.hex())
print(account.address)
