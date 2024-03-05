from merkly.mtree import MerkleTree


leaves = ["tx0", "tx1", "tx2", "tx3"]

# Construindo uma MerkleTree
mtree = MerkleTree(leaves)

# Criando um MerkleRoot
root = mtree.root
print(root.hex())

# Criando uma MerkleProof
proof = mtree.proof("tx2")
print(proof)

# Verificando um MerkleProof
print(mtree.verify(proof, "tx2"))