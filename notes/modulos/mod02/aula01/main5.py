from merkly.mtree import MerkleTree

leaves = ["tx0", "tx1", "tx2", "tx3"]

# Construindo uma MerkleTree
mtree = MerkleTree(leaves)
for leaf in mtree.leaves:
    print("LEAF: ", leaf.hex())

# Criando um MerkleRoot
root = mtree.root
print("ROOT: ", root.hex())