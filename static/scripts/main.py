#!/usr/bin/env python

import time
import datetime
import json
import argparse
import uuid

class canvas(object):
	"""
	class for canvas object;
	"""

	def __init__(self, graphs=[]):
		"""
		:- graphs: type=list, info=list of graphs;
		"""
		self.graphs=graphs
		self.logger=logger()
	
	def appendGraph(self,graph):
		"""
		append graph to self.graphs;
		:- graph: type=graph;
		:- return: type=bool;
		"""
		self.graphs.append(graph)
		return True

	def loadGraph(self,path):
		"""
		loads a graph from .json file ans appends it to self.graphs;
		:- path: type=str;
		:- return: type=bool;
		"""
		self.logger.log('Loading graph from dump...'+path)
		start=time.time()
		f=open(path,'r')
		data=json.load(f)
		result=graph()
		result.author=data['author']
		result.id=data['id']
		result.name=data['name']
		for i in xrange(0, len(data['vertices'])):
			currentVertex=vertex(result)
			if not currentVertex.fillVertexFromDumpingData(data['vertices'][str(i)]):
				self.logger.log('Failed to load vertex.', logType='error')
			else:
				result.appendVertex(currentVertex)
		for i in xrange(0, len(data['edges'])):
			currentEdge=edge(result)
			if not currentEdge.fillEdgeFromDumpingData(data['edges'][str(i)]):
				self.logger.log('Failed to load edge.', logType='error')
			else:
				result.appendEdge(currentEdge)
		for i in xrange(0, len(data['routes'])):
			currentRoute=route(result)
			if not currentRoute.fillRouteFromDumpingData(data['routes'][str(i)]):
				self.logger.log('Failed to load vertex.', logType='error')
			else:
				result.appendRoute(currentRoute)
		end=time.time()
		self.logger.log('Loading graph from dump has been successfull. Processing time:'+str(end-start))
		if not self.appendGraph(result):
			self.logger.log('Failed to append graph to canvas.', logType='error')

	def plot(self,graph,scale=1.0):
		"""
		plots a graph;
		:- graph: type=graph;		
		:- return: type=bool, info=True if success;
		"""
		pass

	def fold(self,graph):
		"""
		folds a graph;
		:- graph: type=graph;
		:- return: type=bool, info=True if success;
		"""
		return True

	def unfold(self,graph):
		"""
		unfolds a graph;
		:- graph: type=graph;
		:- return: type=bool, info=True if success
		"""
		return True

class graph(object):
	"""
	class for graph object;
	"""

	def __init__(self,name='undefined',author='undefined'):
		"""
		:- name: type=str, info=name of a graph;
		:- author: type=str, info=author of a graph;
		"""
		self.name=name
		self.author=author
		self.vertices=[]
		self.edges=[]
		self.routes=[]
		self.logger=logger()
		self.id=str(uuid.uuid4())

	def merge(self,graphs):
		"""
		merges current graph with one or more graphs;
		:- graphs: type=list, info=list of graphs for merging with current one;
		:- return: graph object
		!!!NEEDS TO BE COMPLETED!!!
		"""
		name=''
		author=''
		for i in xrange(0,len(graphs)):
			if i==0:
				name=name+graph[i].name
				author=author+graph[i].author
			name=name+'+'+graph[i].name
			author=author+' and '+graph[i].author
		proto=graph(name,author)

	def dump(self,path):
		"""
		dumps a graph in json format;
		:- path: type=str;
		:- return: type=bool, info=True if success;
		"""
		self.path=path
		self.logger=logger()
		data={}
		data['name']=self.name
		data['author']=self.author
		data['id']=self.id
		data['vertices']={}
		data['edges']={}
		data['routes']={}
		self.logger.log('Forming of vertices dict for dumping...')
		start=time.time()
		for i in xrange(0,len(self.vertices)):
			data['vertices'][str(i)]=self.vertices[i].generateDumpingData()
		end=time.time()
		self.logger.log('Forming of vertices dict for dumping is completed. Processing time:'+str(end-start))
		self.logger.log('Forming of edges dict for dumping...')
		start=time.time()
		for i in xrange(0,len(self.edges)):
			data['edges'][str(i)]=self.edges[i].generateDumpingData()
		end=time.time()
		self.logger.log('Forming of edges dict for dumping is completed. Processing time:'+str(end-start))
		self.logger.log('Forming of routes dict for dumping...')
		start=time.time()
		for i in xrange(0,len(self.routes)):
			data['routes'][str(i)]=self.routes[i].generateDumpingData()
		end=time.time()
		self.logger.log('Forming of routes dict for dumping is completed. Processing time:'+str(end-start))
		self.logger.log('Starting dumping in json format to '+path+'...')
		start=time.time()
		with open(self.path,'w') as out:
			json.dump(data,out)
		end=time.time()
		self.logger.log('Dumping in json format to '+path+'.json is completed. Processing time:'+str(end-start))
		return True

	def appendVertex(self,vertex):
		"""
		appends vertex object to a graph;
		:- vertex: type=vertex;
		:- return: type=bool, info=True if success;
		"""
		self.vertices.append(vertex)
		return True

	def appendEdge(self,edge):
		"""
		appends edge object to a graph;
		:- edge: type=edge;
		:- return: type=bool, info=True if success;
		"""
		self.edges.append(edge)
		return True

	def appendRoute(self,route):
		"""
		appends route object to a graph;
		:- route: type=route;
		:- return: type=bool, info=True if success;
		"""
		self.routes.append(route)
		return True

	def findVerticesByName(self,vertexName):
		"""
		filters vertices in self.vertices by name;
		:- vertexName: type=str;
		:- return: type=list, info=list of found vertex objects;
		"""
		result=[]
		for i in xrange(0,len(self.vertices)):
			if self.vertices[i].name==vertexName:
				result.append(self.vertices[i])
		return result

class vertex(object):
	"""
	class for vertex object;
	"""

	def __init__(self,graph,name='undefined',vType='undefined',subVtype='undefined',expandable=False):
		"""
		:- graph: type=graph, info=graph to which this vertex belongs;
		:- name: type=str;
		:- vType: type=str;
		:- subVtype: type=str;
		"""
		self.graph=graph
		self.name=name
		self.id=str(uuid.uuid4())
		self.vType=vType
		self.subVtype=subVtype
		self.logger=logger()
		self.coords=[None,None]

	def generateDumpingData(self):
		"""
		generates data for dumping;
		:- return: type=dict, info=dict of vertex properties;
		"""
		self.logger.log('Collecting vertex data...')
		start=time.time()
		result={'name':self.name,'id':self.id,'vType':self.vType,'subVtype':self.subVtype}
		end=time.time()
		self.logger.log('Collecting of vertex data is completed. Processing time:'+str(end-start))
		return result

	def fillVertexFromDumpingData(self,data):
		"""
		fills vertex object with data from dump;
		:- data: type=dict;
		:- return: type=bool;
		"""
		self.logger.log('Filling vertex data from dump...')
		start=time.time()
		try:
			self.name=data['name']
			self.id=data['id']
			self.vType=data['vType']
			self.subVtype=data['subVtype']
		except:
			self.logger.log('Vertex filling has failed.', logType='error')
			return False
		end=time.time()
		self.logger.log('Vertex('+self.id+') has been filled successfully. Processing time:'+str(end-start))
		return True

class edge(object):
	"""
	class for edge object;
	"""

	def __init__(self,graph,initial=None,final=None,directed=False):
		"""
		:- initial: type=vertex;
		:- final: type=vertex;
		:- directed: type=bool, info=if value is True set direction from intial to final;
		:- graph: type=graph, info=graph to which this vertex belongs;
		"""
		self.graph=graph
		self.initial=initial
		self.final=final
		self.directed=directed
		self.id=str(uuid.uuid4())
		if self.initial==None or self.final==None:
			self.coords=[None,None]
		else:
			self.coords=[self.initial.coords,self.final.coords]
		self.logger=logger()

	def switchDirection(self):
		"""
		switches direction of an edge;
		:- return: type=bool;
		"""
		if not self.directed:
			self.logger.log('Unable to switch direction of edge('+self.id+') because it is undirected.', logType='waring') 
			return False
		if self.initial==initial:
			self.initial=final
		elif self.intial==final:
			self.intial=intial
		if self.final==final:
			self.final=initial
		elif self.final==intial:
			self.final=final
		return True

	def removeDirection(self):
		"""
		makes edge undirected
		:- return: type=bool;
		"""
		if not self.directed:
			self.logger.log('Unable to remove direction from edge('+self.id+') because it is already undirected.', logType='warning')
			return False
		self.directed=False
		return True

	def getWay(self):
		"""
		provides name of an edge;
		:- return: type=str;
		"""
		if self.directed:
			return str(self.initial.id)+" -> "+str(self.final.id)
		else:
			return str(self.initial.id)+" -- "+str(self.final.id)

	def setInitial(self,vertex):
		"""
		sets vertex intial for this edge;
		:- vertex: type=vertex;
		:- return: type=bool;
		"""	
		self.initial=vertex
		return True

	def setFinal(self,vertex):
		"""
		sets vertex final for this edge;
		:- vertex: type=vertex;
		:- return: type=bool;
		"""	
		self.final=vertex
		return True

	def generateDumpingData(self):
		"""
		generates data for dumping;
		:- return: type=dict, info=dict of edge properties;
		"""
		self.logger.log('Collecting edge data...')
		start=time.time()
		result={'way':self.getWay(),'id':self.id}
		end=time.time()
		self.logger.log('Collecting of edge data is completed. Processing time:'+str(end-start))
		return result

	def fillEdgeFromDumpingData(self,data):
		"""
		fills edge object with data from dump. works only if self.graph is filled with vertices which are reconstructed from the dump;
		:- data: type=dict;
		:- return: type=bool;
		"""
		self.logger.log('Filling edge data from dump...')
		start=time.time()
		self.id=data['id']
		try:
			for vertex in self.graph.vertices:
				if vertex.id==data['way'].split()[0]:
					if not self.setInitial(vertex):
						self.logger.log('Setting vertex('+vertex.id+') initial for edge('+self.id+') has failed', logType='error')
						return False
				if vertex.id==data['way'].split()[2]:
					if not self.setFinal(vertex):
						self.logger.log('Setting vertex('+vertex.id+') final for edge('+self.id+') has failed', logType='error')
						return False
			if data['way'].split()[1]=='--':
				self.directed=False
			else:
				self.directed=True
			self.coords=[self.initial.coords,self.final.coords]
		except:
			self.logger.log('Edge('+self.id+') filling has failed while collecting vertex information.', logType='error')
			return False
		end=time.time()
		self.logger.log('Edge('+self.id+') has been filled successfully. Processing time:'+str(end-start))
		return True

class route(object):
	"""
	class for route object;
	"""

	def __init__(self,graph,way=[],name='undefined'):
		"""
		:- graph: type=graph;
		:- way: type=list, info=ordered list of edge objects;
		:- name: type=str;
		"""
		self.graph=graph
		self.way=way
		self.name=name
		self.id=str(uuid.uuid4())
		self.logger=logger()

	def getWay(self):
		"""
		provides way of a route;
		:- return: type=str;
		"""
		result=""
		for i in xrange(0, len(self.way)):
			if i==0:
				result=result+self.way[i].getWay()
			else:
				result=result+','+self.way[i].getWay()
		return result

	def appendEdge(self,edge):
		"""
		appends edge to route's way;
		:- return: type=bool;
		"""
		self.way.append(edge)
		return True

	def generateDumpingData(self):
		"""
		generates dumping data;
		:- return: type=dict;
		"""
		self.logger.log('Collecting route data...')
		start=time.time()
		way={}
		for i in xrange(0, len(self.way)):
			way[str(i)]={}
			way[str(i)]['edgeId']=self.way[i].id
			way[str(i)]['way']=self.way[i].getWay()
		result={'name':self.name,'id':self.id,'way':way}
		end=time.time()
		self.logger.log('Collecting of route data is completed. Processing time:'+str(end-start))
		return result

	def fillRouteFromDumpingData(self,data):
		"""
		fills route object with data from dump. works only if self.graph is filled with edges which are reconstructed from the dump;
		:- data: type=dict;
		:- return: type=bool;
		"""
		self.logger.log('Filling route data from dump...')
		start=time.time()
		self.name=data['name']
		self.id=data['id']
		try:
			for i in xrange(0, len(data['way'])):
				for g in xrange(0,len(self.graph.edges)):
					if self.graph.edges[g].id==data['way'][str(i)]['edgeId']:
						self.appendEdge(self.graph.edges[g])
		except:
			self.logger.log('Route('+self.id+') filling has failed while collectring way information.', logType='error')
			return False
		end=time.time()
		self.logger.log('Route('+self.id+') has been filled successfully. Processing time:'+str(end-start))
		return True

class logger(object):
	"""
	class for logger object;
	"""

	def __init__(self,path='log.txt'):
		"""
		:- path: type=str, info=path to log file;
		"""
		self.path=path

	def log(self,message,logType='info'):
		"""
		writes message to log file;
		:- message: type=str;
		:- logType: type=sty, values='info' or 'warning' or 'error';
		"""
		date=datetime.datetime.date(datetime.datetime.now())
		time=datetime.datetime.time(datetime.datetime.now())
		logFile=open(self.path,'a')
		if logType=='info':
			mes='info('+str(date)+'_'+str(time)+'):'+message+'\n'
			logFile.write(mes)
		elif logType=='warning':
			mes='WARNING('+str(date)+'_'+str(time)+'):'+message+'\n'
			logFile=open(self.path,'a')
			logFile.write(mes)
		elif logType=='error':
			mes='ERROR('+str(date)+'_'+str(time)+'):'+message.upper()+'\n'
			logFile=open(self.path,'a')
			logFile.write(mes)
		logFile.close()
		return True

	
