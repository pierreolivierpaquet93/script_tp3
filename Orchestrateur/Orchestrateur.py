import sys
import os
import json
import subprocess

INSTALL_LST_FILENAME = "Enonce_03_install_list.json"
POWERSHELL_EXEC_FILENAME = "Executor.ps1"
FIELD_PC = "machine"
FIELD_SOFTWARE = "logiciels"

class MyJson():
	def __init__(
		self,
		filepath: str
	):
		self._filepath = f"{os.path.dirname(__file__)}\\{filepath}"
		self._raw_content = ""
		self._parsed = None
		if os.path.exists( self._filepath ):
			with open( self._filepath ) as f:
				self._raw_content = f.read()
				self._parsed = json.loads( self._raw_content )

	def getParsed( self ):
		return self._parsed

def installation_sub_processes( to_install: MyJson ):
	for item in to_install.getParsed():
		for program in item[FIELD_SOFTWARE]:
			powershell_exec = (
				f"{os.path.dirname(__file__)}"
				f"\\{POWERSHELL_EXEC_FILENAME}"
			)
			arguments = [
				"powershell",
				"-File",
				powershell_exec,
				"-machine",
				item[FIELD_PC],
				"-logiciel",
				program
			]
			res = subprocess.run(
				arguments,
				capture_output=True,
				text=True
			)
			print( res.stdout )

def main():
	to_install = MyJson( INSTALL_LST_FILENAME )
	installation_sub_processes( to_install )

if __name__ == "__main__":
	main()
