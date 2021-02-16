import unittest
import calculation

class MyTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        pass

    # 退出清理
    def tearDown(self):
        pass

    # 定义测试方法，以test开头
    def testSum(self):
        self.assertEqual(calculation.sum(1,2),3,'test sum pass!')

    def testSub(self):
        self.assertEqual(calculation.sub(4, 2), 2, 'test sub pass!')

if __name__ == "__main__":
    unittest.main()