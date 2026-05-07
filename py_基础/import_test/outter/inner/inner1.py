import sys
import import_test

print(f"sys.path[0] = {sys.path[0]}")
print(f"import_test.outter.inner.__path__ = {import_test.outter.inner.__path__}")
print(f"import_test.outter.inner.__name__ = {import_test.outter.inner.__name__}")
print(f"import_test.outter.inner.__package__ = {import_test.outter.inner.__package__}")


# PS E:\learn_python\py_基础> python -m import_test.outter.inner.inner1
# sys.path[0] = E:\learn_python\py_基础
# import_test.outter.inner.__path__ = _NamespacePath(['E:\\learn_python\\py_基础\\import_test\\outter\\inner'])
# import_test.outter.inner.__name__ = import_test.outter.inner
# import_test.outter.inner.__package__ = import_test.outter.inner
# PS E:\learn_python\py_基础>
