import osmnx as ox
import networkx as nx
from graphs import *
def main():
	#Cargar el mapa de lima, desde la PUCP, 1.5 kilómetros a la redonda

	G = ox.graph_from_address(address='PUCP Peru, Avenida Universitaria, Virgen de Fatima, San Miguel, Lima, L32, Peru',
							   distance = 1500, distance_type='network',network_type='drive',simplify=True)

	G_projected=ox.project_graph(G)

	#Se almacena el grafo para ser procesado con networkx

	ox.save_graphml(G_projected, filename='PUCP.graphml') 

	roads,distances,keys,nodes=Floyd_Warshall()

	print('Mapa cargado')
	print('Algoritmo completado')
	#calculamos las rutas para los 3 integrantes
	for i in ['Manuel','Mario','Stev']:
		#cambiamos los colores de los nodos de las rutas
		distancia,ruta=get_route(i,roads,distances,keys,nodes)
		nc = ['r' if node in ruta else 'b' for node in G_projected.nodes()]
		print('La distancia mínima que debe recorrer ',i,' es:',distancia)
		print('Observe el ploteo para ver la ruta')
		fig,ax=ox.plot_graph(G_projected,node_color=nc)

if __name__=="__main__":
	main()