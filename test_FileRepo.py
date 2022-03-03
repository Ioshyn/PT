import unittest
import filecmp
import sys
sys.path.append("../")
from src.models.FileRepo import FileRepo
from src.models.points import Point

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
        self.assertTrue(type(self.chaine) is str)
    
    def test_sameLength(self):
        self.assertTrue(len(self.listePoints) is len(self.listeTemps))
    
    def test_convert_str(self):
        v = FileRepo()
        chaine1 = v.exportDataString(self.listeTemps,self.listePoints,",")
        self.assertTrue(chaine1 == self.chaine)
    
    def test_convert_csv(self):
        v = FileRepo()
        v.exportDataToCsv("test1",self.listeTemps,self.listePoints,",")
        result = filecmp.cmp("test.csv", "test1.csv")
        self.assertTrue(result)
    
    
        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
