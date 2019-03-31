import optparse
from check_target import check_target
from getalldirresult import getalldirresult

def call_check_target():
	target = check_target()

	f = open("tmp/tmp.txt", mode="w")
	f.write(target)
	f.close()

def call_getalldirresult():
	f = open("tmp/tmp.txt", mode="r")
	for target in f:
		target = target
	f.close()

	parser = optparse.OptionParser()
	parser.add_option('-q', '--mode',
		action="store", dest="mode",
		help="mode1: get help text of tareget, mode2: get package list from target, mode3: generate target import line", default="spam")
	options, args = parser.parse_args()
	mode = int(options.mode)

	# --- call getalldirresult
	getalldirresult(mode, target)

# functions
call_check_target()
call_getalldirresult()
