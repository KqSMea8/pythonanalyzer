#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Creature()

	result.template = "object/creature/npc/droid/crafted/shared_probe_droid.iff"
	result.attribute_template_id = 3
	result.stfName("droid_name","probe_droid_crafted")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result