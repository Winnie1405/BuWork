import numpy
import scipy
import matplotlib
import sklearn
import skimage
import h5py
import pandas
import keras
import tensorflow
import cv2
def dfs(graph, node, search):
    st = [[node, None]]
    visited = []
    i = 1
    while st:
        print("open",st)
        print("close",visited)
        path = st.pop(0)
        print("current",path)
        print()
        node = path[0]
        if node == search:
            parent = path[1]
            put = [node]
            while parent is not None:
                for x in visited:
                    if x[0] == parent:
                        parent = x[1]
                        put.insert(0,x[0])
            return put
        elif path not in st or path not in visited:
            visited.insert(0,path)
            root = []
            for x in graph[node]:
                root.append((x,node))
            st = root + st
if __name__ == '__main__':
    graph = {
        'A' : ['B','C','D'],
        'B' : ['E','F'],
        'E' : ['H'],
        'F' : ['H'],
        'H' : [],
        'C' : ['F','G'],
        'D' : ['G'],
        'G' : ['I','J','K'],
        'I' : [],
        'J' : [],
        'K' : []
    }
    path = dfs(graph,'A','G')
    print("Shortest Path",path)