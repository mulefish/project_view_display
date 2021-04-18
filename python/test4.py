# import networkx as nx
# import matplotlib as plt
# # https://www.youtube.com/watch?v=xREnpVUbkFI

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# G.add_edges_from(
#     [('src', 'index.js'), ('src', 'App.test.js'), ('src', 'routes.js'), ('src', 'setupTests.js'), ('src', 'App.js'), ('src', 'pages'), ('src', 'redux'), ('redux', 'index.js'), ('redux', 'reducers.js'), ('pages', 'Home'), ('pages', 'Diagram'), ('pages', 'FauxForce'), ('pages', 'ABCDocuments'), ('pages', 'SecondPass'), ('pages', 'ForceDirectedGraph'), ('ABCDocuments', 'layout.js'), ('ABCDocuments', 'index.js'), ('ABCDocuments', 'redux'), ('SecondPass', 'layout.js'), ('SecondPass', 'logic.js'), ('SecondPass', 'Controls.js'), ('SecondPass', 'memory.js'),
#      ('SecondPass', 'index.js'), ('Diagram', 'memory.js'), ('Diagram', 'Diagram.js'), ('FauxForce', 'layout.js'), ('FauxForce', 'logic.js'), ('FauxForce', 'Controls.js'), ('FauxForce', 'index.js'), ('FauxForce', 'ReadJson.js'), ('ForceDirectedGraph', 'layout.js'), ('ForceDirectedGraph', 'logic.js'), ('ForceDirectedGraph', 'Controls.js'), ('ForceDirectedGraph', 'index.js'), ('Home', 'layout.js'), ('Home', 'index.js'), ('redux', 'types.js'), ('redux', 'actions.js'), ('redux', 'index.js'), ('redux', 'reducers.js'), ('redux', 'thunks.js'), ]
# )

G.add_edges_from(
    [('src', 'index.js'),
     ('src', 'App.test.js'),
     ('src', 'routes.js'),
     ('src', 'setupTests.js'),
     ('src', 'App.js'),
     ('src', 'pages'),
     ('src', 'redux'),
     ('redux', 'dinosaur'),
     ('redux', 'kittycat')
     ]
)

# G.add_edges_from(
#     [('src', 'index.js'), ('src', 'App.test.js'), ('src', 'routes.js'), ('src',
#                                                                          'setupTests.js'), ('src', 'App.js'), ('src', 'pages'), ('src', 'redux'), ('redux', 'dinosaur'), ('redux', 'kittycat')]
# )


val_map = {}
# val_map = {'A': 1.0,
#            'D': 0.9,
#            'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = []
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                       node_color=values, node_size=500)


# for n in G.nodes():
#     print(nx.node_attribute_xy(G, n))


nodePos = nx.circular_layout(G)
print("nodePos : \n", nodePos)

# print(nx.get_node_attributes(G.nodes()))

# print(dir(nx))
# print(nx.node_attribute_xy)
nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()


# import matplotlib.pyplot as plt
# import networkx as nx
# # %matplotlib inline

# # matplotlib inline

# G2 = nx.DiGraph()
# G2.add_node(900, pos=(0, 0))
# G2.add_node(901, pos=(1, 0))
# G2.add_node(902, pos=(0, 1))
# G2.add_node(903, pos=(1, 1))
# G2.add_node(904, pos=(0, -1))

# nodePos = nx.circular_layout(G2)
# print("nodePos : \n", nodePos)
# ('nodePos : \n', {904: array([1.00000000e+00, 2.38418583e-08]),
# 900: array([0.30901696, 0.95105658]), 901: array([-0.80901709,  0.58778522]),
# 902: array([-0.80901698, -0.58778535]), 903: array([ 0.30901711, -0.95105647])})

# nx.draw_networkx(G2, with_labels=True, pos=nodePos)
# plt.show()
