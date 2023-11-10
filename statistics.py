import geopandas as gpd

# Чтение shp-файла
shapefile = gpd.read_file('gis_osm_railways_free_1.shp')

# Вывод информации о shp-файле
print(shapefile.head())

# Вывод общей информации о shp-файле
print(shapefile.info())

# Вывод описательной статистики
print(shapefile.describe())