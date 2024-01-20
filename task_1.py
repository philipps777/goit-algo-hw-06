import networkx as nx
import matplotlib.pyplot as plt

G_berlin_metro = nx.DiGraph()

station_names = [
    "Alexanderplatz", "Brandenburger Tor", "Zoologischer Garten", "Potsdamer Platz",
    "Spittelmarkt", "Friedrichstraße", "Hackescher Markt", "Kurfürstendamm",
    "Wittenbergplatz", "Schönhauser Allee", "Schlesisches Tor", "Tierpark",
    "Frankfurter Allee", "Hermannplatz", "Märkisches Museum"
]
G_berlin_metro.add_nodes_from(station_names)
edges_with_distances = [
    ("Alexanderplatz", "Brandenburger Tor", {'вага': 3}),
    ("Brandenburger Tor", "Zoologischer Garten", {'вага': 4}),
    ("Zoologischer Garten", "Potsdamer Platz", {'вага': 5}),
    ("Potsdamer Platz", "Spittelmarkt", {'вага': 5}),
    ("Spittelmarkt", "Friedrichstraße", {'вага': 3}),
    ("Friedrichstraße", "Hackescher Markt", {'вага': 2}),
    ("Hackescher Markt", "Kurfürstendamm", {'вага': 6}),
    ("Kurfürstendamm", "Wittenbergplatz", {'вага': 4}),
    ("Wittenbergplatz", "Schönhauser Allee", {'вага': 7}),
    ("Schönhauser Allee", "Schlesisches Tor", {'вага': 8}),
    ("Schlesisches Tor", "Tierpark", {'вага': 5}),
    ("Tierpark", "Frankfurter Allee", {'вага': 3}),
    ("Frankfurter Allee", "Hermannplatz", {'вага': 6}),
    ("Hermannplatz", "Märkisches Museum", {'вага': 4}),
    ("Kurfürstendamm", "Alexanderplatz", {'вага': 24}),
    ("Potsdamer Platz", "Schönhauser Allee", {'вага': 37}),
    ("Friedrichstraße", "Schlesisches Tor", {'вага': 18}),
    ("Spittelmarkt", "Tierpark", {'вага': 35}),
    ("Kurfürstendamm", "Frankfurter Allee", {'вага': 23}),
    ("Frankfurter Allee", "Zoologischer Garten", {'вага': 16}),
    ("Hackescher Markt", "Märkisches Museum", {'вага': 44}),
]


G_berlin_metro.add_edges_from(edges_with_distances)
num_nodes = G_berlin_metro.number_of_nodes()
num_edges = G_berlin_metro.number_of_edges()


degrees = dict(G_berlin_metro.degree())
degree_centrality = nx.degree_centrality(G_berlin_metro)

print("Кількість вершин у графі: ", num_nodes)
print("Кількість ребер у графі: ", num_edges)
print("Ступінь вершин: ", degrees)
print("Ступінь центральності вершин: ", degree_centrality)



pos = nx.circular_layout(G_berlin_metro)
nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
        font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')

edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
nx.draw_networkx_edge_labels(
    G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')

plt.show()
