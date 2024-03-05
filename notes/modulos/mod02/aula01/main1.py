import hashlib

data = "nearx"
data_encoded = data.encode()

output = hashlib.sha256(data_encoded)
output_decoded = output.hexdigest()
print(output_decoded)