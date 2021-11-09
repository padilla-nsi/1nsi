import unittest
from unittest import mock
import for_sandbox as exo 
from io import StringIO

class validator(unittest.TestCase):
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_quitting(self):
        with unittest.mock.patch('builtins.input', return_value='yes'):

            self.assertEqual(exo, second)