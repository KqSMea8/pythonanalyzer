class StartingStats:
	__slots__ = ('health', 'action', 'mind')
	def __init__(self, health, action, mind):
		self.health = health
		self.action = action
		self.mind = mind

StartStats = {		
	'bothan:combat_brawler'        :	StartingStats((1000,500,400),(1100,650,450 ),(600 ,400,300 )),
	'bothan:combat_marksman'       :	StartingStats((1000,450,300),(1100,750,400 ),(700 ,400,400 )),
	'bothan:crafting_artisan'      :	StartingStats((600 ,300,300),(1100,700,400 ),(1000,500,500 )),
	'bothan:outdoors_scout'        :	StartingStats((800 ,300,350),(1100,700,500 ),(800 ,450,400 )),
	'bothan:science_medic'         :	StartingStats((600 ,300,300),(1000,600,400 ),(1100,600,500 )),
	'bothan:social_entertainer'    :	StartingStats((500 ,300,300),(1300,700,500 ),(900 ,500,400 )),
	'human:combat_brawler'         :	StartingStats((1100,600,500),(900 ,450,450 ),(600 ,400,400 )),
	'human:combat_marksman'        :	StartingStats((1100,550,400),(900 ,550,400 ),(700 ,400,400 )),
	'human:crafting_artisan'       :	StartingStats((700 ,400,400),(900 ,500,400 ),(1000,500,600 )),
	'human:outdoors_scout'         :	StartingStats((900 ,400,450),(900 ,500,500 ),(800 ,450,500 )),
	'human:science_medic'          :	StartingStats((700 ,400,400),(800 ,400,400 ),(1100,600,600 )),
	'human:social_entertainer'     :	StartingStats((600 ,400,400),(1100,500,500 ),(900 ,500,500 )),
	'ithorian:combat_brawler'      :	StartingStats((1000,500,400),(800 ,350,500 ),(800 ,600,450 )),
	'ithorian:combat_marksman'     :	StartingStats((1000,450,300),(800 ,450,450 ),(900 ,600,450 )),
	'ithorian:crafting_artisan'    :	StartingStats((600 ,300,300),(800 ,400,450 ),(1200,700,650 )),
	'ithorian:outdoors_scout'      :	StartingStats((800 ,300,350),(800 ,400,550 ),(1000,650,550 )),
	'ithorian:science_medic'       :	StartingStats((600 ,300,300),(700 ,300,450 ),(1300,800,550 )),
	'ithorian:social_entertainer'  :	StartingStats((500 ,300,300),(1000,400,550 ),(1100,700,550 )),
	'moncal:combat_brawler'        :	StartingStats((1000,500,400),(800 ,350,500 ),(800 ,600,450 )),
	'moncal:combat_marksman'       :	StartingStats((1000,450,300),(800 ,450,450 ),(900 ,600,450 )),
	'moncal:crafting_artisan'      :	StartingStats((600 ,300,300),(800 ,400,450 ),(1200,700,650 )),
	'moncal:outdoors_scout'        :	StartingStats((800 ,300,350),(800 ,400,550 ),(1000,650,550 )),
	'moncal:science_medic'         :	StartingStats((600 ,300,300),(700 ,300,450 ),(1300,800,650 )),
	'moncal:social_entertainer'    :	StartingStats((500 ,300,300),(1000,400,550 ),(1100,700,550 )),
	'rodian:combat_brawler'        :	StartingStats((1000,500,400),(1000,550,800 ),(500 ,300,350 )),
	'rodian:combat_marksman'       :	StartingStats((1000,450,300),(1000,650,750 ),(600 ,300,350 )),
	'rodian:crafting_artisan'      :	StartingStats((600 ,300,300),(1000,600,750 ),(900 ,400,550 )),
	'rodian:outdoors_scout'        :	StartingStats((800 ,300,350),(1000,600,850 ),(700 ,350,450 )),
	'rodian:science_medic'         :	StartingStats((600 ,300,300),(900 ,500,750 ),(1000,500,550 )),
	'rodian:social_entertainer'    :	StartingStats((500 ,300,300),(1200,600,850 ),(800 ,400,450 )),
	'sullustan:combat_brawler'     :	StartingStats((1200,500,400),(1100,350,350 ),(500 ,300,700 )),
	'sullustan:combat_marksman'    :	StartingStats((1200,450,300),(1100,450,300 ),(600 ,300,700 )),
	'sullustan:crafting_artisan'   :	StartingStats((800 ,300,300),(1100,400,300 ),(900 ,400,900 )),
	'sullustan:outdoors_scout'     :	StartingStats((1000,300,350),(1100,400,400 ),(700 ,350,800 )),
	'sullustan:science_medic'      :	StartingStats((800 ,300,300),(1000,300,300 ),(1000,500,800 )),
	'sullustan:social_entertainer' :	StartingStats((700 ,300,300),(1300,400,400 ),(800 ,400,800 )),
	'trandoshan:combat_brawler'    :	StartingStats((1250,800,800),(800 ,350,350 ),(500 ,300,400 )),
	'trandoshan:combat_marksman'   :	StartingStats((1250,750,700),(800 ,450,300 ),(600 ,300,400 )),
	'trandoshan:crafting_artisan'  :	StartingStats((850 ,600,700),(800 ,400,300 ),(900 ,400,600 )),
	'trandoshan:outdoors_scout'    :	StartingStats((1050,600,750),(800 ,400,400 ),(700 ,350,500 )),
	'trandoshan:science_medic'     :	StartingStats((850 ,600,700),(700 ,300,300 ),(1000,500,600 )),
	'trandoshan:social_entertainer':	StartingStats((750 ,600,700),(1000,400,400 ),(800 ,400,500 )),
	'twilek:combat_brawler'        :	StartingStats((1000,500,650),(1050,650,350 ),(600 ,300,300 )),
	'twilek:combat_marksman'       :	StartingStats((1000,450,550),(1050,750,300 ),(700 ,300,300 )),
	'twilek:crafting_artisan'      :	StartingStats((600 ,300,550),(1050,700,300 ),(1000,400,500 )),
	'twilek:outdoors_scout'        :	StartingStats((800 ,300,600),(1050,700,400 ),(800 ,350,400 )),
	'twilek:science_medic'         :	StartingStats((800 ,300,600),(1050,700,400 ),(800 ,350,400 )),
	'twilek:social_entertainer'    :	StartingStats((500 ,300,550),(1250,700,400 ),(900 ,400,400 )),
	'wookiee:combat_brawler'       :	StartingStats((1350,850,550),(1000,450,450 ),(600 ,450,400 )),
	'wookiee:combat_marksman'      :	StartingStats((1350,800,450),(1000,550,400 ),(700 ,450,400 )),
	'wookiee:crafting_artisan'     :	StartingStats((950 ,650,450),(1000,500,500 ),(1000,550,600 )),
	'wookiee:outdoors_scout'       :	StartingStats((1150,650,500),(1000,500,500 ),(800 ,500,500 )),
	'wookiee:science_medic'        :	StartingStats((950 ,650,450),(900 ,400,400 ),(1100,650,600 )),
	'wookiee:social_entertainer'   :	StartingStats((850 ,650,450),(1200,500,500 ),(900 ,550,500 )),
	'zabrak:combat_brawler'        :	StartingStats((1200,500,400),(1100,350,350 ),(500 ,300,700 )),
	'zabrak:combat_marksman'       :	StartingStats((1200,450,300),(1100,450,300 ),(600 ,300,700 )),
	'zabrak:crafting_artisan'      :	StartingStats((800 ,300,300),(1100,400,300 ),(900 ,400,900 )),
	'zabrak:outdoors_scout'        :	StartingStats((1000,300,350),(1100,400,400 ),(700 ,350,800 )),
	'zabrak:science_medic'         :	StartingStats((800 ,300,300),(1000,300,300 ),(1000,500,900 )),
	'zabrak:social_entertainer'    :	StartingStats((700 ,300,300),(1300,400,400 ),(800 ,400,800 ))
}