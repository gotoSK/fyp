import networkx as nx
import json

class TransactionGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_transaction(self, buyer, seller, qty):
        """Add transactions to the graph, summing up if an edge already exists."""
        if self.graph.has_edge(buyer, seller):
            self.graph[buyer][seller]['qty'] += qty
        else:
            self.graph.add_edge(buyer, seller, qty=qty)
    
    def normalize(self):
        """Normalize the graph by removing reciprocal transactions."""
        to_remove = []
        to_add = []

        # Normalize edges: calculate net transaction for reciprocal transactions
        for u, v in list(self.graph.edges()):
            if self.graph.has_edge(v, u):
                qty_uv = self.graph[u][v]['qty']
                qty_vu = self.graph[v][u]['qty']
                net_qty = qty_uv - qty_vu

                if net_qty > 0:
                    to_add.append((u, v, net_qty))
                elif net_qty < 0:
                    to_add.append((v, u, -net_qty))

                to_remove.append((u, v))
                to_remove.append((v, u))

        # Remove reciprocal edges
        for u, v in to_remove:
            if self.graph.has_edge(u, v):
                self.graph.remove_edge(u, v)

        # Add normalized edges
        for u, v, qty in to_add:
            self.graph.add_edge(u, v, qty=qty)

    def get_normalized_graph(self):
        """Return the normalized graph as a list of edges with source, target, and qty."""
        edges = []
        for u, v, data in self.graph.edges(data=True):
            edges.append({"source": u, "target": v, "qty": data['qty']})
        return edges
    
