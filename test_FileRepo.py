import unittest
import filecmp
from fileRepo import FileRepo
from points import Point

class TestFileRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.listePoints = [Point(2,8),Point(6,7)]
        self.listeTemps = [2,3]            
        self.h = FileRepo()
        self.chaine = self.h.exportDataString(self.listeTemps,self.listePoints,",")
        
        self.fichier = self.h.exportDataToCsv("test",self.listeTemps,self.listePoints,",")
    
    def tearDown(self):
        pass
    
    def test_isString(self):
        self.assertTrue(self.chaine,"zfezrezre")


if __name__ == '__main__':
    unittest.main(verbosity=2)
