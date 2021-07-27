import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_installed_modules_to_add_to_installed_apps():
	"""
		Gets a list of installed module names to add to the list
		of installed apps.
		The list is retrieved from the base directory, and only includes
		items that are prefixed with module_
	"""
	return [item for item in os.listdir(BASE_DIR) if item.startswith('module_')]



