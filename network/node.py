class Node:
    """
    Represents a junction node in the water distribution network.
    """

    def __init__(self, node_id, elevation=0.0, demand=0.0):
        self.id = node_id
        self.elevation = elevation
        self.demand = demand
        self.connected_pipes = []

    def add_pipe(self, pipe):
        """Attach a pipe to this node."""
        self.connected_pipes.append(pipe)

    def __repr__(self):
        return (
            f"Node(id={self.id}, "
            f"elevation={self.elevation}, "
            f"demand={self.demand})"
        )
