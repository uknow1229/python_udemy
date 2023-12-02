# pytest
# unittestよりももう少し機能が充実している

import pytest
import calculation

is_release = True

class TestCal(object):

  # クラス全体のテストが実行される前と後に何かやりたい場合setupclassを使う
  @classmethod
  def setup_class(cls):
      print('start')
      cls.cal = calculation.Cal()

  @classmethod
  def teardown_class(cls):
      print('end')
      del cls.cal

  def setup_method(self, method):
      print('method={}.format(method.__name__)')
      # self.cal = calculation.Cal()

  def teardown_method(self, method):
      print('method={}.format(method.__name__)')
      # del self.cal
          
  def test_add_num_and_double(self, request):
      os_name = request.config.getoption('--os-name')
      print(os_name)
      os_name = 'mac'
      if os_name == 'mac':
          print('ls')
      elif os_name == 'windows':
          print('dir')
      assert self.cal.add_num_and_double(1, 1) == 4

  # 例外テスト
  # @pytest.mark.skip(reason='skip!')
  @pytest.mark.skipif(is_release==True,
                    reason='skip!')
  def test_add_num_add_double_raise(self):
      with pytest.raises(ValueError):
          self.cal.add_num_and_double('1', '1')