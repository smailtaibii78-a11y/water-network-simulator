class Network:
    """
    Represents the full water distribution network.
    """

    def __init__(self):
        self.nodes = {}
        self.pipes = {}

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_pipe(self, pipe):
        self.pipes[pipe.id] = pipe

    def __repr__(self):
        return (
            f"Network(Nodes={len(self.nodes)}, "
            f"Pipes={len(self.pipes)})"
        )
