# import geopandas as gpd
# import networkx as nx
# from shapely.geometry import LineString
# from docx import Document
# import osmnx as ox
#
# # Загрузка shp файла
# gdf = gpd.read_file('gis_osm_railways_free_1.shp')
#
# # Создание графа
# G = nx.Graph()
#
# # Добавление узлов в граф
# for i, row in gdf.iterrows():
#     G.add_node(i, geometry=row['geometry'])
#
# # Добавление ребер в граф
# for i, row in gdf.iterrows():
#     for j, row2 in gdf.iterrows():
#         if i != j:
#             G.add_edge(i, j, weight=row['geometry'].distance(row2['geometry']))
#
# # Построение маршрута
# path = nx.shortest_path(G, source=0, target=3, weight='weight')
#
# # Создание линии маршрута
# line = LineString([G.nodes[i]['geometry'] for i in path])
#
# # Создание документа Word
# doc = Document()
#
# # Добавление информации о графах и маршрутах в документ
# doc.add_paragraph('Граф:')
# doc.add_paragraph(str(G.nodes))
# doc.add_paragraph(str(G.edges))
# doc.add_paragraph('Маршрут:')
# doc.add_paragraph(str(path))
# doc.add_paragraph('Протяженность маршрута: ' + str(line.length))
#
# # Сохранение документа
# doc.save('output.docx')
#
# # Сохранение линии маршрута в shp файл
# gdf_route = gpd.GeoDataFrame(geometry=[line])
# gdf_route.to_file('route.shp')
#
# # Сохранение графа в shp файл
# gdf_graph = gpd.GeoDataFrame(geometry=[LineString(data['geometry']) for node, data in G.nodes(data=True)])
# gdf_graph.to_file('graph.shp')
