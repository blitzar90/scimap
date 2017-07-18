# -*- coding: UTF-8 -*-
"""
This script is designed to automatically delete old db objects and fill db with new example objects.

ATTENTION!: this script sould be run in shell mode of manage.py
>>>> python manage.py shell
>>>> %run ./repopulate.py
"""

from scimap import models as scimapModels

# math imports
import numpy as np
import random

## supplimentary functions

def getProperRandom( quant, curNum = None):
	
	"""
	Gets randon int in range quant except curNum;
	"""


	curRandomNumber = np.ceil( random.random() * quant - 1)
	
	if curNum == None:

		return int(curRandomNumber)
	
	else:
		
		while int(curRandomNumber) - 1  == curNum:
			curRandomNumber = np.ceil( random.random() * quant - 1)
	
		return int(curRandomNumber)


## delete section

# delete nodes
oldNodes = scimapModels.Node.objects.all()
oldNodes.delete()

# delete routes
oldRoutes = scimapModels.Route.objects.all()
oldRoutes.delete()

# delete links
oldLinks = scimapModels.Link.objects.all()
oldLinks.delete()

# delete areas
oldAreas = scimapModels.Area.objects.all()
oldAreas.delete()

# delete subAreas
oldSubAreas = scimapModels.SubArea.objects.all()
oldSubAreas.delete()


## populate section

# area/subArea settings
areas = {
	1: u'Математика', 
	2: u'Физика', 
	3: u'Биология', 
	4: u'Компьютерные науки'
}
subArea = {
	u'Математика':{
		1: u'Геометрия',
		2: u'Алгебра',
		3: u'Математический анализ',
		4: u'Функциональный анализ'
	}, 
	u'Физика':{
		1: u'Электродинамика',
		2: u'Оптика',
		3: u'Квантовая механика'
	}, 
	u'Биология':{
		1: u'Ботаника',
		2: u'Анатомия'
	}, 
	u'Компьютерные науки':{
		1: u'DOTA',
		2: u'LOL',
		3: u'WOW'
	}
}

# populate areas

print('Adding areas and subareas')

for key in areas:

	curArea = scimapModels.Area(title = areas[key])

	for subKey in subArea:

		if areas[key] == subKey:

			for i in xrange(len(subArea[subKey])):
				curSubArea = scimapModels.SubArea(title = subArea[subKey][i+1])
				curArea.save()
				curSubArea.save()
				curSubArea.AreasField.add(curArea)

	curSubArea.save()

# populate nodes

print('Adding nodes')

n = 10 # number of nodes
depth = 1 # relevant number of links

for i in xrange(n):

	curNode = scimapModels.Node(title = u'нода %s' % str(i))
	curNode.save()

Nodes = scimapModels.Node.objects.all()
SubAreas = scimapModels.SubArea.objects.all()
Areas = scimapModels.Area.objects.all()

# filling many to many fields
for i in xrange(len(Nodes)):
	
	curNode = Nodes[i]

	curNode.subArea.add(SubAreas[getProperRandom(len(SubAreas), i )])
	curNode.area.add(Areas[getProperRandom( len(Areas), i )])

	for i in xrange(depth):
		
		if random.random()>0.5: # make different depth
	
			curNode.fromNodes.add(Nodes[getProperRandom(  len(Nodes), i )])
			curNode.toNodes.add(Nodes[getProperRandom(  len(Nodes), i)])
	
		else:
	
			curNode.fromNodes.add(Nodes[getProperRandom(  len(Nodes), i   )])
			curNode.toNodes.add(Nodes[getProperRandom(len(Nodes), i  )])

			break

	curNode.save()

# populate Routes

print('Adding routes')

n = 10 # number of routes
quant = 5 # maximum number of nodes in route

for i in xrange(n):
	curRoute = scimapModels.Route(title = 'route %s' % str(i))
	curRoute.save()

	for i in range(getProperRandom(quant)):
		curRoute.nodes.add(Nodes[getProperRandom(len(Nodes))])
