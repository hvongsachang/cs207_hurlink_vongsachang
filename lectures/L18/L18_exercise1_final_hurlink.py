import reprlib
class Sentence(object):
	def __init__(self, text):
		self.text = text
		self.words = text.split()

	def __iter__(self):
		for word in self.words:
			yield word

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
	x = Sentence('This is a sentence')
	for word in x:
		print (word)