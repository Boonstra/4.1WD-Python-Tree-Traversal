from node import Node

# Nodes
theropodiaNode = Node("Theropodia")

ceratosauriaNode = Node("Ceratosauria")
tetanuraeNode = Node("Tetanurae")

coelophysoiNode = Node("Coelophysoi")
abelisauroiNode = Node("Abelisauroi")

coelurosauriaNode = Node("Coelurosauria")

tRexNode = Node("T-Rex")
eendNode = Node("Eend")

# Build tree
theropodiaNode.add_child(ceratosauriaNode)
theropodiaNode.add_child(tetanuraeNode)

ceratosauriaNode.add_child(coelophysoiNode)
ceratosauriaNode.add_child(abelisauroiNode)

tetanuraeNode.add_child(coelurosauriaNode)

coelurosauriaNode.add_child(tRexNode)
coelurosauriaNode.add_child(eendNode)

# Perform action
theropodiaNode.perform_action()