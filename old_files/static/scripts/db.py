#!/usr/bin/env python

import psycopg2 
import uuid
from main import logger

"""
FIRST CHECK IF STEPS IN 'root/scimap/db_readme.txt' ARE PERFORMED
(default base is scimap, user is blitzar)
"""

logger=logger('../../db_log.txt')


def connect():
	
	"""
	connects to the database;
	"""

	try:
		conn = psycopg2.connect("dbname=base user='blitzar' host='localhost' password='88162440'")
		conn.autocommit = True
	except:
	    logger.log("Unable to connect to the database")
	
	return conn

def addNode(nodeId,name,initial,final):
	
	"""
	adds node to the database;
	:- nodeId: type=str;
	:- name: type=str;
	:- initial: type=list;
	:- final: type=list;
	:- return: type=bool;
	"""

	logger.log('Adding node %s to the database...' % nodeId)
	objType='node'

	# init connection to the database
	conn=connect()

	# define cursor
	cur=conn.cursor()

	# change format for postgres syntax
	initial=str(initial).replace("'",'')
	initial=str(initial)[1:-1]
	final=str(final).replace("'",'')
	final=str(final)[1:-1]

	try:	
		cur.execute("insert into graph.nodes values('%s','%s','%s','{%s}','{%s}',%s)" % (nodeId,name,objType,initial,final,'default'))
		cur.close()
		conn.close()
		
		logger.log('Node %s has been successfully added to the database.' % nodeId)
		return True
	except:
		logger.log('Node %s addition to the database has failed.' % nodeId, logType = 'error')
		return False

def getObjectById(objId):
	
	"""
	gets object from the database;
	:- objId: type = str;
	:- return: type = tuple, info = (bool, result dict);
	"""

	logger.log('Searching for object %s in the database...' % objId)

	# init connection to the database
	conn=connect()

	# define cursor
	cur=conn.cursor()
	
	try:
		cur.execute("select * from graph.nodes where id = '%s'" % objId)
		dbAnswer = cur.fetchall()
		cur.close()
		conn.close()

		logger.log('Object has %s been found.' % objId)
	except:
		logger.log('Failed to find object %s' % objId, logType = 'error')
		return (False, None)

	# converting result to dict
	coulumns = ['id', 'name', 'type', 'initial', 'final', 'way']
	result = []
	for row in dbAnswer:
		result.append(dict(zip(coulumns, row)))
	
	return (True, result)

def getObjectsByName(objName):
	
	"""
	gets objects from the database with name objName;
	:- objName: type = str;
	:- return: type = tuple, info = (bool, result dict);
	"""

	logger.log('Searching for objects in the database with name =  %s.' % objName)

	# init connection to the database
	conn=connect()

	# define cursor
	cur=conn.cursor()
	
	try:
		cur.execute("select * from graph.nodes where name = '%s'" % objName)
		dbAnswer = cur.fetchall()
		cur.close()
		conn.close()

		logger.log('Object has %s been found.' % objName)
	except:
		logger.log('Failed to find object %s' % objName, logType = 'error')
		return (False, None)

	# converting result to dict
	coulumns = ['id', 'name', 'type', 'initial', 'final', 'way']
	result = []
	for row in dbAnswer:
		result.append(dict(zip(coulumns, row)))
	
	return (True, result)

