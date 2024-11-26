from clematis.model_generator import ModelGenerator
import networkx as nx
import matplotlib.pyplot as plt

def plot_dag(layers_dict, edges):
    # Create a directed graph
    G = nx.DiGraph()
    
    G.add_edges_from(edges)
    
    # Define the desired distances between nodes
    dist = {}
    node_distance = 0.1
    for step, machines in layers_dict.items():
        print(step, machines)
        for m1 in machines:
            dist[m1] = dict()
            for m2 in machines:
                if m1 != m2:
                    print(f"Setting distance for {m1} {m2} to {node_distance}")
                    dist[m1][m2] = node_distance

    pos = nx.kamada_kawai_layout(G, dist=dist)
    
    # Draw the graph
    nx.draw(G, pos=pos, with_labels=True, arrows=True, node_size=1000, node_color='red', font_size=10, font_color='black', font_weight='bold')
    
    # Display the graph
    plt.title("Directed Acyclic Graph from Layers")
    plt.show()

# creatinga demo model with 10 nodes and 50% seriality
model1 = ModelGenerator(n=12, s=0.5)

# generating the graph from the model
work_stations, production_edges, edge_attr, vertex_attr = model1.generate_graph()

# turn production edges to tuples
production_edges_tuples = [(edge[0], edge[1]) for edge in production_edges]

# printing the rest of the generated data
print(production_edges)
print(edge_attr)
print(vertex_attr)
print(work_stations)

# using the plot_dag function to plot the graph
plot_dag(work_stations, production_edges_tuples)