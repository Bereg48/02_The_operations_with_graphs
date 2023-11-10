import geopandas as gpd

# Загрузка файла shp
gdf = gpd.read_file('gis_osm_railways_free_1.shp')

# Проверка геометрии
gdf['is_valid'] = gdf['geometry'].is_valid

# Выявление ошибок
invalid_geometries = gdf[~gdf['is_valid']]

# Вывод ошибок
for index, row in invalid_geometries.iterrows():
    print(f"Index: {index}, Error: {row['geometry'].explain_validity()}")

# Исправление ошибок
gdf['geometry'] = gdf['geometry'].buffer(0)

# Проверка исправленной геометрии
gdf['is_valid'] = gdf['geometry'].is_valid

# Выявление ошибок после исправления
invalid_geometries_after_fix = gdf[~gdf['is_valid']]

# Вывод ошибок после исправления
for index, row in invalid_geometries_after_fix.iterrows():
    print(f"Index: {index}, Error: {row['geometry'].explain_validity()}")