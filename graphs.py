import networkx as nx
import numpy as np
def getAddress(name):
	return{
		'Manuel':'499774491',
		'Mario':'499841834',
		'Stev': '649998996',
	}[name]


def Floyd_Warshall():
	G1 = nx.read_graphml("PUCP.graphml")
	#Se implementará el algoritmo de floyd watshall
	#para esta matriz haciendo el uso de la librería
	#numpy para poder manejar mejor los arreglos
	N = nx.number_of_nodes(G1)
	#crearemos 2 matrices NxN,una para las distancias y otra
	#para el camino a seguir
	distances = np.zeros((N,N))
	roads = np.zeros((N,N))
	#para poder trabajar con la matriz, cada nodo deberá tener
	#un identificador que está en [0..N-1]
	#para esto se creará una lista
	nodes = list(G1.nodes)
	#ahora se creará un diccionario para saber
	#qué número de identificador tiene cada nodo
	keys = dict()
	for i in range(N):
		keys[nodes[i]]=i
	#ahora llenaremos la matriz de distancias con los datos de G
	for i in range(N):
		for j in range(N):
			try:
				distance=float(G1[nodes[i]][nodes[j]][0]['length'])
				distances[i][j]=distance
				roads[i][j]=i

			except KeyError:
				distances[i][j]=2000#un valor muy grande, para
									#representar inf en el algoritmo
				roads[i][j]=-1

	#ahora se deberá modificar ambas matrices N veces para
	#llegar a la solución final
	for k in range(N):
		for i in range(N):
			for j in range(N):
				if(distances[i][j]>distances[i][k]+distances[k][j]):
					distances[i][j]=distances[i][k]+distances[k][j]
					roads[i][j]=roads[k][j]

	return(roads,distances,keys,nodes)
	#Ahora debemos encontrar la ruta usada por nuestro algoritmo
	#Para esto definimos el Nodo PUCP y el nodo de la casa de los integrantes
	
def get_route(name,roads,distances,keys,nodes):	
	nodoPucp='1843102399'

	nodoGrupo=getAddress(name)


	distanciaMin=distances[keys[nodoPucp]][keys[nodoGrupo]]
	caminoMin=list()
	caminoMin.append(int(nodoGrupo))
	caminoMin.append(int(nodoPucp))

	inicio = keys[nodoGrupo]

	fin = keys[nodoPucp]

	while True:
		punto = int(roads[inicio][fin])
		if punto == inicio:
			break
		caminoMin.insert(1,int(nodes[punto]))
		fin = punto

	return(distanciaMin,caminoMin)



