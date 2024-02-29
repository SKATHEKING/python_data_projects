import datetime

import pymongo
import pprint

client = pymongo.MongoClient('mongodb+srv://interview:6gzt7LHFWZZRnxuA@cetoaioperational.cuo5rlo.mongodb.net/demo')

db = client['demo']
collection = db['missions']

missions = []

#cursor = collection.find({})
#for mission in cursor:
    # print(mission)
 #   missions.append(mission)

# date 2020
# pprint.pprint(missions)

#missions_2020 = []
#year = 2020
#success = 'Success'
#for mission in missions:
    # print(mission['net'])
    # print(type(mission['net']))
 #   mission_date = mission['net'].year
  #  status = mission['status']['abbrev']
    # print(mission_date)
   # if mission_date == year:
    #    if status != success:
            # pprint.pprint(mission)
     #       missions_2020.append(mission)

docu = collection.find_one({'net': '2008-08-03T03:34:00.000+00:00'})
island = collection.find_one({'pad': 'Omelek Island'})

pprint.pprint((docu))
pprint.pprint(island)
