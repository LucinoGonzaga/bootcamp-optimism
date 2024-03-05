from eth_account import Account

seed = "jump skull butter topic bronze member feed wait flee oven deer rabbit"

Account.enable_unaudited_hdwallet_features()
account = Account().from_mnemonic(mnemonic=seed)

print('Chave privada: ',  account.key.hex())
print('Chave publica: ', account.address)

tx = {
    "to": "0xF0109fC8DF283027b6285cc889F5aA624EaC1F55",
    "value": 1000000000,

    "gas": 2000000,
    "maxFeePerGas": 2000000000,
    "maxPriorityFeePerGas": 1000000000,
    "nonce": 0,
    "chainId": 1,
}

signed_tx = account.sign_transaction(tx)

print("Slipt da assinatura: ", signed_tx.r)
print("slipt da assinatura: ", signed_tx.s)
print("Slot onde pode ficar alguma informação: ", signed_tx.v)