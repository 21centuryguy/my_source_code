''' Structural Game for 15 - Puzzle with different difficulty levels'''
from random import ranint

class Puzzle:
	def __int__(self):
		self.items = {}
		self.position = None

	def main_franme(self):
		d = self.items
		print('+-----+-----+-----+-----+')
		print('|%s|%s|%s|%s|' % (d[1], d[2], d[3], d[4]))
		print('+-----+-----+-----+-----+')
		print('|%s|%s|%s|%s|' % (d[5], d[6], d[7], d[8]))
		print('+-----+-----+-----+-----+')
		print('|%s|%s|%s|%s|' % (d[9], d[10], d[11], d[12]))
		print('+-----+-----+-----+-----+')
		print('|%s|%s|%s|%s|' % (d[13], d[14], d[15], d[16]))

	def format(self, ch):
		ch = ch.strip():
		