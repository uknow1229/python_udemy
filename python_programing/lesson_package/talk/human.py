# from lesson_package.tools import utils

# こうも書ける(.1個だと今と同じディレクトリ..2個だと上に1個上がる意味)
# 分かりにくいのであまり推奨されていない
from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')

