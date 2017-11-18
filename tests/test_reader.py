# -*- coding: utf-8 -*-

from mootdx.reader import Reader, ExReader
import unittest

class TestReader(unittest.TestCase):
    reader = None

    ##初始化工作
    def setUp(self):
        self.reader = Reader(tdxdir='/Volumes/BOOTCAMP/new_tdx')
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testDaily(self):
        self.assertTrue( self.reader.daily(symbol='000001') is not None)
        
        
    def testMinbar(self):
        self.assertTrue( self.reader.minbar(symbol='000001') is not None)
        
    def fzlineMinbar(self):
        self.assertTrue( self.reader.fzline(symbol='000001') is not None)


class TestExReader(unittest.TestCase):
    reader = None

    ##初始化工作
    def setUp(self):
        self.reader = ExReader(tdxdir='/Volumes/BOOTCAMP/new_tdx')
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testDaily(self):
        self.assertTrue(not self.reader.daily(symbol='000001') is None)
        
        
    def testMinbar(self):
        self.assertTrue(not self.reader.minbar(symbol='000001') is None)
          
if __name__ =='__main__':
    unittest.main()
