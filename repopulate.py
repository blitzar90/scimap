# -*- coding: UTF-8 -*-
"""
This script is designed to automatically delete old db objects and fill db with new example objects.

ATTENTION!: this script sould be run in shell mode of manage.py
>>>> python manage.py shell
>>>> %run ./repopulate.py
"""

from scimap import models as scimapModels


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
		4: u'Математический анализ',
		5: u'Функциональный анализ'
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
#for key in areas:
#	curArea = scimapModels.Area(title = areas[key])
	#for subKey in subArea:
	#	if areas[key] == subKey:
	#		for subSubKey in subKey:
	#			subArea = scimapModels.SubArea(title = subKey[subSubKey], mother = curArea)
#	curArea.save()
	#subArea.save()
