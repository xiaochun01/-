import paramunittest
import unittest
@paramunittest.parametrized(
    {'numa':10,'numb':30},
    {'numa': 10, 'numb': 50},
)

class ApiTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self,numa,numb):
        self.a = numa
        self.b = numb
    def test_add(self):
        print( '%d+%d?=%d'%(self.a,self.b,40) )
        self.assertEqual(  self.a+ self.b,60 )



if __name__ == '__main__':
    unittest.main(verbosity=2)