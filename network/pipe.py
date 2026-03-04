class Pipe:
    """
    Represents a pipe connecting two nodes in the network.
    """

    def __init__(self, pipe_id, start_node, end_node,
                 length, diameter, roughness):
        self.id = pipe_id
        self.start_node = start_node
        self.end_node = end_node
        self.length = length
        self.diameter = diameter
        self.roughness = roughness

        # Register this pipe in connected nodes
        self.start_node.add_pipe(self)
        self.end_node.add_pipe(self)

    def __repr__(self):
        return (
            f"Pipe(id={self.id}, "
            f"start={self.start_node.id}, "
            f"end={self.end_node.id})"
        )
