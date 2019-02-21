import optparse

"""
parser = optparse.OptionParser()

parser.add_option('-q', '--query',
    action="store", dest="query",
    help="query string", default="spam")

options, args = parser.parse_args()

print('Query string:', options.query)
"""


parser = optparse.OptionParser()

parser.add_option('-q', '--mode',
    action="store", dest="mode",
    help="mode string", default="spam")

options, args = parser.parse_args()

print(options.mode)
