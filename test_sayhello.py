import unittest
from module_foo import sayhello
class SayHelloTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_SayHello(self):
        rv=sayhello()
        self.assertEqual(rv,'hello')

    def test_SayHello_Somebody(self):
        rv=sayhello(to='zzj')
        self.assertEqual(rv,'hello,zzj')
    
if __name__=='__main__':
    unittest.main()
