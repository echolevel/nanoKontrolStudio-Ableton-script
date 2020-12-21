from __future__ import absolute_import, print_function, unicode_literals
from nanokontrolstudio_echolevel import nanokontrolstudio_echolevel

def create_instance(c_instance):
	return nanokontrolstudio_echolevel(c_instance)
