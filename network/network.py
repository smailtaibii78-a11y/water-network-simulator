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
       def build_incidence_matrix(self):
        """
        Builds the node-pipe incidence matrix.
        """
        import numpy as np

        num_nodes = len(self.nodes)
        num_pipes = len(self.pipes)

        A = np.zeros((num_nodes, num_pipes))

        node_ids = list(self.nodes.keys())
        pipe_ids = list(self.pipes.keys())

        for j, pipe_id in enumerate(pipe_ids):
            pipe = self.pipes[pipe_id]

            start_index = node_ids.index(pipe.start_node)
            end_index = node_ids.index(pipe.end_node)

            A[start_index, j] = -1
            A[end_index, j] = 1

        return A
