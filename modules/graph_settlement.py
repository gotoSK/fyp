from flask import jsonify
import networkx as nx


class TransactionGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_transaction(self, buyerMemberId, sellerMemberId, contract_quantity):
        """Add transactions to the graph, summing up if an edge already exists."""
        if self.graph.has_edge(buyerMemberId, sellerMemberId):
            self.graph[buyerMemberId][sellerMemberId]['contract_quantity'] += contract_quantity
        else:
            self.graph.add_edge(buyerMemberId, sellerMemberId,
                                contract_quantity=contract_quantity)

    def tarjan_scc(self):
        """Find strongly connected components (SCCs) using Tarjan's algorithm."""
        sccs = list(nx.strongly_connected_components(self.graph))
        return sccs

    def apply_netting(self):
        """Perform netting using Tarjan's SCCs to minimize transactions within cycles."""
        sccs = self.tarjan_scc()
        for scc in sccs:
            if len(scc) > 1:  # Only process cycles
                self.net_scc_transactions(scc)

    def net_scc_transactions(self, scc):
        """Net transactions within an SCC, keeping only net positive balances."""
        subgraph = self.graph.subgraph(scc).copy()
        balances = {node: 0 for node in scc}

        # Calculate net balance for each node
        for u, v, data in subgraph.edges(data=True):
            contract_quantity = data['contract_quantity']
            balances[u] -= contract_quantity
            balances[v] += contract_quantity

        # Remove all existing edges in SCC
        for u, v in list(subgraph.edges()):
            self.graph.remove_edge(u, v)

        # Add only net transactions
        for u in scc:
            for v in scc:
                if balances[u] > 0 and balances[v] < 0:
                    transfer_amount = min(balances[u], -balances[v])
                    self.graph.add_edge(
                        u, v, contract_quantity=transfer_amount)
                    balances[u] -= transfer_amount
                    balances[v] += transfer_amount

    def get_normalized_graph(self):
        """Return the netted graph as a list of edges with source, target, and contract_quantity."""
        edges = []
        for u, v, data in self.graph.edges(data=True):
            edges.append({"source": u, "target": v,
                         "contract_quantity": data['contract_quantity']})
        return edges
