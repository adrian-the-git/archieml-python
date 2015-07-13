import os
import glob
import json
import unittest


import archieml

class TestArchieML(unittest.TestCase):
	def test_loader(self):
		testdir = os.path.dirname(os.path.realpath(__file__))
		for	filename in glob.glob('{}/archieml.org/test/1.0/*.aml'.format(testdir)):
			print filename
			slug, i = os.path.basename(filename).split('.')[:2]
			with open(filename) as f:
				metadata = archieml.load(f)
				test = metadata['test']
				expected = json.loads(metadata['result'])

			with open(filename) as f:
				actual = archieml.load(f)
				del actual['test']
				del actual['result']
			self.assertEqual(json.dumps(expected), json.dumps(actual), """{slug}.{i} {test}
expected: {expected}
actual  : {actual}""".format(slug=slug, i=i, test=test, expected=expected, actual=actual))
