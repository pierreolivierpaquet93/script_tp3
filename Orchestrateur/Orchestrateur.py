import sys
import os
import json
import subprocess

INSTALL_LST_FILENAME = "Enonce_03_install_list.json"
FIELD_PC = "machine"
FIELD_SOFTWARE = "logiciels"

class MyJson():
	def __init__(
		self,
		filepath: str
	):
		self._filepath = filepath;
		self._raw_content = ""
		self._parsed = None
		install_lst_file = f"{os.path.dirname(__file__)}\\{INSTALL_LST_FILENAME}"
		if os.path.exists( install_lst_file ):
			with open( install_lst_file ) as f:
				self._raw_content = f.read()
				self._parsed = json.loads( self._raw_content )

def main():
	MyJson( INSTALL_LST_FILENAME )

if __name__ == "__main__":
	main()
