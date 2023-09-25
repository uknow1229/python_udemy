import unittest

import calculation

release_name = 'lesson'

class CalTest(unittest.TestCase):

    # testが始める前にsetUpが呼ばれる
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()
    
    def test_add_num_add_double(self):
        cal = calculation.Cal()
        self.assertEqual(
            self.cal.add_num_and_double(1, 1), 4)
        # 他にもassertのメソッド色々あるのでドキュメント見て学ぶ！
    
    # テストが終わった後にtearDownが呼ばれる
    # ファイルを綺麗にしたいとかテストで作ったテンポラリーファイルを削除したいとか
    #  色々な用途でtearDownは使える
    def tearDown(self):
        print('clean up')
        del self.cal
    
    # 例外テスト
    # unittestをスキップしたい時
    # @unittest.skip('skip!')
    @unittest.skipIf(release_name=='lesson', 'skip!')
    def test_add_num_add_double_raise(self):
        cal = calculation.Cal()
        # withステートメントの中でValueErrorという例外処理が起きれば
        # このテストは大丈夫ということをテストするためのもの
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')

if __name__ == '__main__':
    unittest.main()

