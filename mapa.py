# %pip install osmnx
import osmnx as ox
import matplotlib.pyplot as plt

# 1. Definice oblasti (Blatiny, Řepy) a nový poloměr
stred = (50.0687, 14.3051)
polomer = 1000  # Zvětšeno na 1000 metrů

# 2. Stažení sítě
G = ox.graph_from_point(stred, dist=polomer, network_type='drive')

# --- PRÁCE S KONKRÉTNÍM UZLEM ---

# Najdeme uzel, který je geograficky nejblíže našemu zadanému středu
# X je zeměpisná délka (lon), Y je zeměpisná šířka (lat)
vybrany_uzel_id = ox.distance.nearest_nodes(G, X=stred[1], Y=stred[0])

# Vytáhneme si slovník s daty o tomto konkrétním uzlu
data_uzlu = G.nodes[vybrany_uzel_id]
lat = data_uzlu['y']
lon = data_uzlu['x']

# Vytvoření odkazů
osm_odkaz = f"https://www.openstreetmap.org/node/{vybrany_uzel_id}"
google_odkaz = f"https://www.google.com/maps?q={lat},{lon}"

# Výpis informací do konzole
print("-" * 40)
print(f"Informace o vybraném uzlu (OSM ID: {vybrany_uzel_id}):")
print(f"Zeměpisná šířka (Lat): {lat}")
print(f"Zeměpisná délka (Lon): {lon}")
print(f"Odkaz na OpenStreetMap: {osm_odkaz}")
print(f"Odkaz na Google Maps:     {google_odkaz}")
print("-" * 40)

# --- VYKRESLENÍ GRAFU ---
pozadi = "#1A0B2E"
barva_cest = "#00F0FF"
barva_uzlu = "#FF003C"

# Vykreslení celé sítě
fig, ax = ox.plot_graph(
    G,
    bgcolor=pozadi,
    node_color=barva_uzlu,
    node_size=10,             # Trochu jsem zmenšil uzly, protože při 1000m jich bude víc
    edge_color=barva_cest,
    edge_linewidth=1.2,       
    edge_alpha=0.8,           
    show=True                 
)
