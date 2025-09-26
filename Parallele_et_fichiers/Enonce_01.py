# ------------------------------------------------------------------[ MODULE.S ]
import threading

# Ne peut pas fonctionner puisque les fonctions de Tester ne sont pas async.
#import asyncio

import time
import os

from Enonce_01_Tester import Tester

# -----------------------------------------------------------------------[ DOC ]

# https://stackoverflow.com/questions/40581649/passing-multiple-arguments-in-python-thread

# ----------------------------------------------------------------[ CONSTANT.S ]

EXT = ".txt"
PREFIX = "secret_"
NAMES = [ "un", "deux", "trois" ]
SECRET_1 = f"{PREFIX}{NAMES[0]}{EXT}"
SECRET_2 = f"{PREFIX}{NAMES[1]}{EXT}"
SECRET_3 = f"{PREFIX}{NAMES[2]}{EXT}"
SECRET_FILES = [ SECRET_1, SECRET_2, SECRET_3 ]

# ----------------------------------------------------------------[ FUNCTION.S ]

def launch_all( threads_lst: list[ threading.Thread ] ):
	for t in threads_lst:
		t.start()

def join_all( threads_lst: list[ threading.Thread ] ):
	for t in threads_lst:
		res = t.join()

def import_secrets( secret_files: list[str] ):
	secrets_content: list[str] = []
	for file in secret_files:
		with open( file, ) as f:
			content = f.read()
			secrets_content.append( content )
	return secrets_content

def prepare_secrets(
	funcs: list,
	secrets: list[str]
):
	threads_lst: list[threading.Thread] = []
	i = 0
	for func in funcs:
		t = threading.Thread( None, func, args=(secrets[i],) )
		i += 1
		threads_lst.append( t )
	return threads_lst

def start_tester(
	testeur: Tester,
	funcs: list,
	secrets_path: list[str]
):
	threads_lst = prepare_secrets( funcs, secrets_path )
	launch_all( threads_lst )
	join_all( threads_lst )
	secrets = import_secrets( secrets_path )
	testeur.check_secrets( secrets[0], secrets[1], secrets[2] )

def main():
	curdir = os.path.dirname( __file__ )+'\\'

	testeur = Tester()
	testeur_funcs = [
		testeur.prepare_secret_1,
		testeur.prepare_secret_2,
		testeur.prepare_secret_3
	]
	secrets_path = [
		f"{curdir}{SECRET_1}",
		f"{curdir}{SECRET_2}",
		f"{curdir}{SECRET_3}"
	]
	start_tester( testeur, testeur_funcs, secrets_path )
	
if __name__ == "__main__":
	main()
