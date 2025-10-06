import os
import json
import subprocess

EXT_JSON = ".json"
EXT_TXT = ".txt"
FILENAME = "Enonce_03_install_list"
INSTALL_LST_FILENAME = f"{FILENAME}{EXT_JSON}"
REPORT_FILENAME = f"{FILENAME}_result{EXT_TXT}"
POWERSHELL_EXEC_FILENAME = "Executor.ps1"
FIELD_PC = "machine"
FIELD_SOFTWARE = "logiciels"
SEP = "------"
SEP_SUCCESS = f"{SEP}Success{SEP}-"
SEP_FAILURE = f"{SEP}Failure{SEP}-"

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
	installed: list[str] = []
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
			installed.append( res.stdout )
	return installed

def generate_report( installed: str, report_filename: str ):
	# out[0] -> Success output ; out[1] -> Failure output.
	out = ["",""]
	out[0] += f"{SEP_SUCCESS}\n"
	out[1] += f"{SEP_FAILURE}\n"
	state = "succeed","failed"
	for element in installed:
		parsed = json.loads( element )
		i = bool( int( parsed["Result"] ) )
		out[i] += (
			f"Machine {parsed["Machine"]} install {parsed["Logiciel"]} "
			f"{state[i]} in {parsed["Duration"]:.3f} secondes\n"
		)
	out[0] += f"--------------------\n\n"
	out[1] += f"--------------------"
	with open( report_filename, 'w' ) as r:
		r.write( out[0] )
		r.write( out[1] )

def main():
	to_install = MyJson( INSTALL_LST_FILENAME )
	installed = installation_sub_processes( to_install )
	generate_report( installed, REPORT_FILENAME )

if __name__ == "__main__":
	main()
