from clematis.model_generator_ns import ModelGeneratorNS
from clematis.dynamic_manufacturing import DynamicManufacturing
from igraph import *

production_model = ModelGeneratorNS(n=14, s=10)

work_stations, production_edges, vertex_attr = production_model.generate_graph()
print(work_stations)

manufacturing_sim = DynamicManufacturing(Graph(production_edges, directed=True, vertex_attrs=vertex_attr), seed=42)
for _ in range(10):
	total_production, zero_count, one_count, two_count, state_array = manufacturing_sim.iterate(output="output.csv", write2file=True)
