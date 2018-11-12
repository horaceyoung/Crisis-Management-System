from callcentre.models import Incident

# incident 0
incident = Incident()
incident.caller_name = 'JENNIFER CHOW'
incident.mobile_number = '83425921'
incident.incident_location = 'Jurong East'
incident.incident_region = 'North West'
incident.incident_category = 'Fire Fighting'
incident.incident_type ='Fire'
incident.incident_description = "There is a big fire"

if incident.incident_category=='Emergency Ambulance':
	incident.incident_department = 'Singapore Civil Defence Force'
if incident.incident_category=='Rescue and Evacuation':
	incident.incident_department = 'Singapore Civil Defence Force'
if incident.incident_category=='Fire Fighting':
	incident.incident_department = 'Singapore Civil Defence Force'
if incident.incident_category=='Gas Leak Control':
	incident.incident_department = 'Singapore Power'

incident.save()

# incident 1
incident1 = Incident()
incident1.caller_name = 'JACK LEE'
incident1.mobile_number = '83029342'
incident1.incident_location = 'Bukit Panjang'
incident1.incident_region = 'Central Singapore'
incident1.incident_category = 'Rescue and Evacuation'
incident1.incident_type ='Haze'
incident1.incident_description = "low visibility on the road"

if incident1.incident_category=='Emergency Ambulance':
	incident1.incident_department = 'Singapore Civil Defence Force'
if incident1.incident_category=='Rescue and Evacuation':
	incident1.incident_department = 'Singapore Civil Defence Force'
if incident1.incident_category=='Fire Fighting':
	incident1.incident_department = 'Singapore Civil Defence Force'
if incident1.incident_category=='Gas Leak Control':
	incident1.incident_department = 'Singapore Power'

incident1.save()
# incident 2
incident2 = Incident()
incident2.caller_name = 'LIM YONG XIAO'
incident2.mobile_number = '83924892'
incident2.incident_location = 'Yishun'
incident2.incident_region = 'North East'
incident2.incident_category = 'Emergency Ambulance'
incident2.incident_type ='Single Car Accident'
incident2.incident_description = "Two people injured"

if incident2.incident_category=='Emergency Ambulance':
	incident2.incident_department = 'Singapore Civil Defence Force'
if incident2.incident_category=='Rescue and Evacuation':
	incident2.incident_department = 'Singapore Civil Defence Force'
if incident2.incident_category=='Fire Fighting':
	incident2.incident_department = 'Singapore Civil Defence Force'
if incident2.incident_category=='Gas Leak Control':
	incident2.incident_department = 'Singapore Power'

incident2.save()
# incident 3
incident3 = Incident()
incident3.caller_name = 'CHAN WEE LEE'
incident3.mobile_number = '02940393'
incident3.incident_location = 'Boon Lay'
incident3.incident_region = 'North East'
incident3.incident_category = 'Fire Fighting'
incident3.incident_type ='Fire'
incident3.incident_description = "There is a big fire"

if incident3.incident_category=='Rescue and Evacuation':
	incident3.incident_department = 'Singapore Civil Defence Force'
if incident3.incident_category=='Rescue and Evacuation':
	incident3.incident_department = 'Singapore Civil Defence Force'
if incident3.incident_category=='Fire Fighting':
	incident3.incident_department = 'Singapore Civil Defence Force'
if incident3.incident_category=='Gas Leak Control':
	incident3.incident_department = 'Singapore Power'

incident3.save()
# incident 4
incident4 = Incident()
incident4.caller_name = 'LAM CHOW XIONG'
incident4.mobile_number = '90239232'
incident4.incident_location = 'Boon Lay'
incident4.incident_region = 'North West'
incident4.incident_category = 'Rescue and Evacuation'
incident4.incident_type ='Two Car Collisions'
incident4.incident_description = "At least four persons were injured and one person died. "

if incident4.incident_category=='Emergency Ambulance':
	incident4.incident_department = 'Singapore Civil Defence Force'
if incident4.incident_category=='Rescue and Evacuation':
	incident4.incident_department = 'Singapore Civil Defence Force'
if incident4.incident_category=='Fire Fighting':
	incident4.incident_department = 'Singapore Civil Defence Force'
if incident4.incident_category=='Gas Leak Control':
	incident4.incident_department = 'Singapore Power'

incident4.save()
# incident 5
incident5 = Incident()
incident5.caller_name = 'CHENG LONG'
incident5.mobile_number = '39201567'
incident5.incident_location = 'Sengkang'
incident5.incident_region = 'North East'
incident5.incident_category = 'Rescue and Evacuation'
incident5.incident_type ='Fire'
incident5.incident_description = "Big fire"

if incident5.incident_category=='Emergency Ambulance':
	incident5.incident_department = 'Singapore Civil Defence Force'
if incident5.incident_category=='Rescue and Evacuation':
	incident5.incident_department = 'Singapore Civil Defence Force'
if incident5.incident_category=='Fire Fighting':
	incident5.incident_department = 'Singapore Civil Defence Force'
if incident5.incident_category=='Gas Leak Control':
	incident5.incident_department = 'Singapore Power'

incident5.save()

# incident 6
incident6 = Incident()
incident6.caller_name = 'EMILY SONG'
incident6.mobile_number = '20931024'
incident6.incident_location = 'Pasir Ris'
incident6.incident_region = 'North East'
incident6.incident_category = 'Gas Leak Control'
incident6.incident_type ='Typhoon'
incident6.incident_description = "low visibility on the road"

if incident6.incident_category=='Emergency Ambulance':
	incident6.incident_department = 'Singapore Civil Defence Force'
if incident6.incident_category=='Rescue and Evacuation':
	incident6.incident_department = 'Singapore Civil Defence Force'
if incident6.incident_category=='Fire Fighting':
	incident6.incident_department = 'Singapore Civil Defence Force'
if incident6.incident_category=='Gas Leak Control':
	incident6.incident_department = 'Singapore Power'

incident6.save()

# incident 7
incident7 = Incident()
incident7.caller_name = 'CHOW JIEMING'
incident7.mobile_number = '83924892'
incident7.incident_location = 'Redhill'
incident7.incident_region = 'Central Singapore'
incident7.incident_category = 'Emergency Ambulance'
incident7.incident_type ='Single Car Accident'
incident7.incident_description = "Four people seriously injured"

if incident7.incident_category=='Emergency Ambulance':
	incident7.incident_department = 'Singapore Civil Defence Force'
if incident7.incident_category=='Rescue and Evacuation':
	incident7.incident_department = 'Singapore Civil Defence Force'
if incident7.incident_category=='Fire Fighting':
	incident7.incident_department = 'Singapore Civil Defence Force'
if incident7.incident_category=='Gas Leak Control':
	incident7.incident_department = 'Singapore Power'

incident7.save()

# incident 8
incident8 = Incident()
incident8.caller_name = 'Jackie Underwood'
incident8.mobile_number = '39098432'
incident8.incident_location = 'Clementi'
incident8.incident_region = 'Central Singapore'
incident8.incident_category = 'Emergency Ambulance'
incident8.incident_type ='Dengue'
incident8.incident_description = "One person fainted"

if incident8.incident_category=='Emergency Ambulance':
	incident8.incident_department = 'Singapore Civil Defence Force'
if incident8.incident_category=='Rescue and Evacuation':
	incident8.incident_department = 'Singapore Civil Defence Force'
if incident8.incident_category=='Fire Fighting':
	incident8.incident_department = 'Singapore Civil Defence Force'
if incident8.incident_category=='Gas Leak Control':
	incident8.incident_department = 'Singapore Power'

incident8.save()

# incident 9
incident9 = Incident()
incident9.caller_name = 'Ellen Koller'
incident9.mobile_number = '89204212'
incident9.incident_location = 'Novena'
incident9.incident_region = 'Central Singapore'
incident9.incident_category = 'Emergency Ambulance'
incident9.incident_type ='Zika'
incident9.incident_description = "A person fainted"

if incident9.incident_category=='Emergency Ambulance':
	incident9.incident_department = 'Singapore Civil Defence Force'
if incident9.incident_category=='Rescue and Evacuation':
	incident9.incident_department = 'Singapore Civil Defence Force'
if incident9.incident_category=='Fire Fighting':
	incident9.incident_department = 'Singapore Civil Defence Force'
if incident9.incident_category=='Gas Leak Control':
	incident9.incident_department = 'Singapore Power'

incident9.save()
