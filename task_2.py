
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random
def dfs_recursive(graph, vertex, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(vertex)
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path)
    return path

def bfs_recursive(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_vertex, path = queue.popleft()
        if current_vertex not in visited:
            visited.add(current_vertex)

            if current_vertex == end:
                return path

            neighbors = set(graph[current_vertex]) - visited
            for neighbor in neighbors:
                queue.append((neighbor, path + [neighbor]))

def main():
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

    print("Алгоритм | Початковий вузол | Кінцевий вузол | Маршрут")
    print("-" * 45)
    for i in range(len(station_names)):
        start_node = random.choice(station_names)
        end_node = random.choice(station_names)
        if start_node != end_node:


            dfs_path = dfs_recursive(G_berlin_metro, start_node, set())
            bfs_path = bfs_recursive(G_berlin_metro, start_node, end_node)


            # print("DFS шлях:", dfs_path)
            # print("BFS шлях:", bfs_path)
            print(
                f"DFS      | {start_node:^16} | {end_node:^15} | {dfs_path}")
            print(
                f"BFS      | {start_node:^16} | {end_node:^15} | {bfs_path}")


    pos = nx.circular_layout(G_berlin_metro)
    nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
            font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')

    edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
    nx.draw_networkx_edge_labels(
        G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')

    plt.show()

if __name__ == "__main__":
    main()



























# import networkx as nx
# import matplotlib.pyplot as plt
# from collections import deque
# import random
# import pandas as pd
#
#
# def dfs_recursive(graph, vertex, visited=None, path=None):
#     if visited is None:
#         visited = set()
#     if path is None:
#         path = []
#     visited.add(vertex)
#     path.append(vertex)
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited, path)
#     return path[:-1]
#
#
# def bfs_recursive(graph, start, end):
#     queue = deque([(start, [start])])
#     visited = set()
#
#     while queue:
#         current_vertex, path = queue.popleft()
#         if current_vertex not in visited:
#             visited.add(current_vertex)
#
#             if current_vertex == end:
#                 return path
#
#             neighbors = set(graph[current_vertex]) - visited
#             for neighbor in neighbors:
#                 queue.append((neighbor, path + [neighbor]))
#
#
# def random_start_end_nodes(graph):
#     nodes = list(graph.nodes())
#     start = random.choice(nodes)
#     end = random.choice(nodes)
#     while start == end:
#         end = random.choice(nodes)
#     return start, end
#
#
# def main():
#     G_berlin_metro = nx.DiGraph()
#
#     station_names = [
#         "Alexanderplatz", "Brandenburger Tor", "Zoologischer Garten", "Potsdamer Platz",
#         "Spittelmarkt", "Friedrichstraße", "Hackescher Markt", "Kurfürstendamm",
#         "Wittenbergplatz", "Schönhauser Allee", "Schlesisches Tor", "Tierpark",
#         "Frankfurter Allee", "Hermannplatz", "Märkisches Museum"
#     ]
#
#     G_berlin_metro.add_nodes_from(station_names)
#
#     edges_with_distances = [
#         ("Alexanderplatz", "Brandenburger Tor", {'вага': 3}),
#         ("Brandenburger Tor", "Zoologischer Garten", {'вага': 4}),
#         ("Zoologischer Garten", "Potsdamer Platz", {'вага': 5}),
#         ("Potsdamer Platz", "Spittelmarkt", {'вага': 5}),
#         ("Spittelmarkt", "Friedrichstraße", {'вага': 3}),
#         ("Friedrichstraße", "Hackescher Markt", {'вага': 2}),
#         ("Hackescher Markt", "Kurfürstendamm", {'вага': 6}),
#         ("Kurfürstendamm", "Wittenbergplatz", {'вага': 4}),
#         ("Wittenbergplatz", "Schönhauser Allee", {'вага': 7}),
#         ("Schönhauser Allee", "Schlesisches Tor", {'вага': 8}),
#         ("Schlesisches Tor", "Tierpark", {'вага': 5}),
#         ("Tierpark", "Frankfurter Allee", {'вага': 3}),
#         ("Frankfurter Allee", "Hermannplatz", {'вага': 6}),
#         ("Hermannplatz", "Märkisches Museum", {'вага': 4}),
#         ("Kurfürstendamm", "Alexanderplatz", {'вага': 24}),
#         ("Potsdamer Platz", "Schönhauser Allee", {'вага': 37}),
#         ("Friedrichstraße", "Schlesisches Tor", {'вага': 18}),
#         ("Spittelmarkt", "Tierpark", {'вага': 35}),
#         ("Kurfürstendamm", "Frankfurter Allee", {'вага': 23}),
#         ("Frankfurter Allee", "Zoologischer Garten", {'вага': 16}),
#         ("Hackescher Markt", "Märkisches Museum", {'вага': 44}),
#     ]
#
#     G_berlin_metro.add_edges_from(edges_with_distances)
#
#     nodes = list(G_berlin_metro.nodes())
#
#     # Виведення результатів у вигляді таблиці
#     print("Алгоритм | Початковий вузол | Кінцевий вузол | Маршрут")
#     print("-" * 45)
#
#     for start_node in nodes:
#         for end_node in nodes:
#             if start_node != end_node:
#                 # Виклик алгоритмів для кожної пари
#                 dfs_path = dfs_recursive(G_berlin_metro, start_node, set())
#                 bfs_path = bfs_recursive(G_berlin_metro, start_node, end_node)
#
#                 print(
#                     f"DFS      | {start_node:^16} | {end_node:^15} | {dfs_path}")
#                 print(
#                     f"BFS      | {start_node:^16} | {end_node:^15} | {bfs_path}")
#
#     # Візуалізація графа
#     pos = nx.circular_layout(G_berlin_metro)
#     nx.draw(G_berlin_metro, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8,
#             font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')
#
#     edge_labels = nx.get_edge_attributes(G_berlin_metro, 'вага')
#     nx.draw_networkx_edge_labels(
#         G_berlin_metro, pos, edge_labels=edge_labels, font_color='red')
#
#     plt.show()
#
#
# if __name__ == "__main__":
#     main()
#

