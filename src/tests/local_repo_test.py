import os.path
import unittest

from repository.local import Local

class LocalRepoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.join('test_data')
        if not os.path.exists(path):
            os.mkdir(path)
        test_file = os.path.join('test_data', 'omega')
        with open(test_file, 'w', encoding = 'utf-8') as file:
            file.write('a,b,c,d,e,f,g')

    def setUp(self):
        self.local = Local('test_data')

    def test_initialization(self):
        self.assertEqual(self.local.folder, 'test_data')

    def test_get_path(self):
        self.assertEqual(self.local.get_path('alpha'),
                         os.path.join('test_data', 'alpha'))

    def test_saving(self):
        string_list = ['alpha', 'beta', 'gamma']
        self.local.save_string_list(string_list, 'gamma')

        self.assertTrue(os.path.exists(os.path.join('test_data', 'gamma')))
        with open(os.path.join('test_data', 'gamma'), 'r', encoding = 'utf-8') as file:
            self.assertEqual(file.read(), 'alpha,beta,gamma')

    def test_loading(self):
        string_list = self.local.read_string_list('omega')
        self.assertListEqual(string_list, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
