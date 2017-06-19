# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 06:37:35 2013
 
@author: Sukhbinder Singh
 
Reads a Binary file and 
Returns Header,Points,Normals,Vertex1,Vertex2,Vertex3
 
"""
import numpy as np
from struct import unpack

import mpl_toolkits.mplot3d as a3d
import matplotlib.colors as colors
import matplotlib.pyplot as plt


def ShowCooordsTopology(coords,topo):
    '''Plots the STL if coords and topology is given.  '''
    ax = a3d.Axes3D(plt.figure())
 
    xm,ym,zm=coords.max(axis=0)
    xmi,ymi,zmi =coords.min(axis=0)
 
    for nodes in topo:
        tri = a3d.art3d.Poly3DCollection([coords[nodes,:3]])
        tri.set_color(colors.rgb2hex([0.9,0.6,0.]))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
 
    ax.set_xlim3d([xmi,xm])
    ax.set_ylim3d([ymi,ym])
    ax.set_zlim3d([zmi,zm])
 
    plt.show()



def ShowSTLFile(v1,v2,v3):
    '''Plots the STL files, give vertices v1,v2,v3'''
    ax = a3d.Axes3D(plt.figure())  
    
    xm,ym,zm=v1.max(axis=0)
    xmi,ymi,zmi =v2.min(axis=0)
 
    for i in range(v1.shape[0]):
        vtx=np.vstack((v1[i],v2[i],v3[i]))
        tri = a3d.art3d.Poly3DCollection([vtx])
        tri.set_color(colors.rgb2hex([0.9,0.6,0.]))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
 
    ax.set_xlim3d([xmi,xm])
    ax.set_ylim3d([ymi,ym])
    ax.set_zlim3d([zmi,zm])
 
    plt.show()




def BinarySTL(fname):
    '''Reads a binary STL file '''
    fp = open(fname, 'rb')
    Header = fp.read(80)
    nn = fp.read(4)
    Numtri = unpack('i', nn)[0]
    #print 'Number of triangles in the STL file: ',nn
    record_dtype = np.dtype([
                   ('normals', np.float32,(3,)),  
                   ('Vertex1', np.float32,(3,)),
                   ('Vertex2', np.float32,(3,)),
                   ('Vertex3', np.float32,(3,)) ,              
                   ('atttr', '<i2',(1,) )
    ])
    data = np.fromfile(fp , dtype = record_dtype , count =Numtri)
    fp.close()
 
    Normals = data['normals']
    Vertex1= data['Vertex1']
    Vertex2= data['Vertex2']
    Vertex3= data['Vertex3']
 
    p = np.append(Vertex1,Vertex2,axis=0)
    p = np.append(p,Vertex3,axis=0) #list(v1)
    Points =np.array(list(set(tuple(p1) for p1 in p)))
     
    return Header,Points,Normals,Vertex1,Vertex2,Vertex3
  
if __name__ == '__main__':
    fname = "bent_plate.stl" #"engine.stl" # "porsche.stl"
    head,p,n,v1,v2,v3 = BinarySTL(fname)
    print head
    print p.shape
    
