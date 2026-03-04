from network.node import Node
from network.pipe import Pipe
from network.network import Network


# Create network
net = Network()

# Create nodes
n1 = Node(1, elevation=100)
n2 = Node(2, elevation=95)

# Create pipe
p1 = Pipe(1, start_node=1, end_node=2, length=500, diameter=0.3)

# Add to network
net.add_node(n1)
net.add_node(n2)
net.add_pipe(p1)

print(net)
