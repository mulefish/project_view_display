import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
# G.add_edges_from(
#     [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

G.add_edges_from(
    [('src', 'index.js'), ('src', 'App.test.js'), ('src', 'routes.js'), ('src',
                                                                         'setupTests.js'), ('src', 'App.js'), ('src', 'pages'), ('src', 'redux')]
)

# ,('pages','Home'),('pages','Diagram'),('pages','FauxForce'),('pages','ABCDocuments'),('pages','SecondPass'),('pages','ForceDirectedGraph'),('redux','index.js'),('redux','reducers.js'),('Home','layout.js'),('Home','index.js'),('Diagram','memory.js'),('Diagram','Diagram.js'),('FauxForce','layout.js'),('FauxForce','logic.js'),('FauxForce','Controls.js'),('FauxForce','index.js'),('FauxForce','ReadJson.js'),('ABCDocuments','layout.js'),('ABCDocuments','index.js'),('ABCDocuments','redux'),('SecondPass','layout.js'),('SecondPass','logic.js'),('SecondPass','Controls.js'),('SecondPass','memory.js'),('SecondPass','index.js'),('ForceDirectedGraph','layout.js'),('ForceDirectedGraph','logic.js'),('ForceDirectedGraph','Controls.js'),('ForceDirectedGraph','index.js'),('redux','types.js'),('redux','actions.js'),('redux','index.js'),('redux','reducers.js'),('redux','thunks.js'),


val_map = {'src': 1.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
# red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
# black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color=values, node_size=500)


# nodePos = nx.circular_layout(G)
# print("nodePos : \n", nodePos)

nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()
