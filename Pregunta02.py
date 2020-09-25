# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f1VJ3Y0xju-2bKLV_a3PbdePS_Cl_pXZ
"""

import networkx as nx

def Lista(G):
    gx = nx.Graph()
    n = len(G)
    gx.add_nodes_from([u for u in range(n)])
    for u in range(n):
        for v in G[u]:
            gx.add_edge(u, v)
    nx.draw(gx, with_labels=True, node_color='orange', alpha = 0.75, node_size = 1000, node_shape ='p')

G = [[1, 2],
     [3, 4],
     [0, 4, 5],
     [1, 4],
     [ ],
     [0,2]]

def maximo(G):
    m = 0
    for i in range(6):
        var = len(G[i])
        if m < var:
            m = var
    print(m)

maximo(G)