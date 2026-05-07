import sys

# 绝对导入
# from outter import outter1
# from outter import outter2

# 在任意目录下运行`python /path/to/test0.py`，导入 `outter1` 和 `outter2` 模块。
# 这将触发 Python 的绝对导入机制，查找 `outter1` 和 `outter2` 模块，并执行它们的代码。

# sys.path[0] 是当test0.py脚本所在的目录路径。Python 会在 sys.path 中查找模块，找到 outter1.py 和 outter2.py 并执行它们的代码。
# __name__ 为 __main__，因为 test0.py 是作为顶级模块运行的。
# 没有__path__属性，因为 test0.py 不是包的一部分，而是作为顶级模块运行的。只有包才有 __path__ 属性。
# print(f"sys.path[0]: {sys.path[0]}")
# print(f"__path__: {__path__}") # 这行会报错，因为 test0.py 不是包的一部分，没有 __path__ 属性。
# print(f"__name__: {__name__}")

# 导入结果：
# ```bash
# PS E:\learn_python\py_基础> python "E:\learn_python\py_基础\import\test0.py"
# outter1_name: outter1
# outter2_name: outter2
# sys.path[0]: E:\learn_python\py_基础\import
# __name__: __main__
# PS E:\learn_python\py_基础>
# ```


# 相对导入
from .outter import outter1
from .outter import outter2
import import_test

# 在包含import目录的目录下运行`python -m import_test.test0`，导入 `outter1` 和 `outter2` 模块。
# 这将触发 Python 的相对导入机制，查找 `outter1` 和 `outter2` 模块，并执行它们的代码。

# sys.path[0] 是执行命令的目录，即包含 import 目录的目录路径。Python 会在 sys.path 中查找模块，找到 outter1.py 和 outter2.py 并执行它们的代码。
# package.__path__ 为包的绝对路径
# package.__name__ 为包名
# package.__package__ 为包名
# __name__ 为 __main__

# 虽然import中没有__init__.py文件，但在Python 3.3及以上版本中，包不再需要__init__.py文件来被识别为包。
# 只要目录结构正确，Python就能识别import目录为包，并允许相对导入。
print(f"sys.path[0]: {sys.path[0]}")
print(f"import_test.__path__: {import_test.__path__}")
print(f"import_test.__name__: {import_test.__name__}")
print(f"import_test.__package__: {import_test.__package__}")
print(f"__name__: {__name__}")

# 导入结果：
# ```bash
# PS E:\learn_python\py_基础> python -m import_test.test0
# outter1_name: outter1
# outter2_name: outter2
# sys.path[0]: E:\learn_python\py_基础
# import_test.__path__: _NamespacePath(['E:\\learn_python\\py_基础\\import_test'])
# import_test.__name__: import_test
# import_test.__package__: import_test
# __name__: __main__
# PS E:\learn_python\py_基础>
# ```
