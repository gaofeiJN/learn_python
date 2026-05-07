# 模块导入机制：
# 模块导入经历三个核心步骤：
# 1. **查找（Find）**
#   **元路径查找器（meta path finders）** 列表 `sys.meta_path` 中。导入模块时，按顺序询问这些查找器是否能找到并加载指定模块。
#   默认的 `sys.meta_path` 通常包含三个查找器：
#   1. **`BuiltinImporter`**
#       负责内置模块（用 C 写的，如 `sys`, `math`）。
#   2. **`FrozenImporter`**
#       负责冻结模块（嵌入在解释器里的 Python 模块，冷门）。
#   3. **`PathFinder`**
#       **负责绝大部分外部模块和包**。它会遍历 **`sys.path`** 中的每个目录，寻找模块文件。
#       1. 对于单文件模块，查找 `module_name.py`。
#       2. 对于包，查找 `package_name/__init__.py`。
#       `sys.path` 是一个列表，包含了 Python 解释器搜索模块的目录路径。默认情况下，它包括当前目录(sys.path[0])、标准库目录和第三方包目录。
#       当前目录：
#       - 当直接运行一个 Python 文件时`python /path/to/script.py`，
#           - 当前目录(sys.path[0])为 `/path/to`（绝对路径）
#           - `__name__` 为 `__main__`，因为脚本作为顶级模块运行。
#           - 没有`__path__`属性，因为 test0.py 不是包的一部分，而是作为顶级模块运行的。只有包才有 __path__ 属性。
#       - 当使用 `python -m package.subpackage.module_name` 运行模块时，
#           - 当前目录(sys.path[0])为执行命令的目录，即 `os.getcwd()`
#           - `package.subpackage.__path__` 为subpackage包的绝对路径
#           - `package.subpackage.__name__` 为package.subpackage
#           - `package.subpackage.__package__` 为package.subpackage
#           - `__name__` 为`__main__`
#   如果找到模块文件，`PathFinder` 会返回一个 **加载器（loader）** 对象。
#   如果所有查找器都无法找到模块，导入会失败并抛出 `ModuleNotFoundError`。
#   查找器的工作流程：
#       1. 接收模块名称和导入上下文（如父包信息）。
#       2. 根据模块名称和上下文，尝试定位模块文件。
#       3. 如果找到模块文件，返回一个加载器对象；否则返回 `None`。
#   查找器的设计允许开发者通过自定义查找器来实现特殊的导入行为（如从网络、数据库等非文件系统来源导入模块）。
#   例如，`PathFinder` 的查找流程：
#   ```python
#   import sys
#   import importlib.machinery
#   def find_spec(name, path=None, target=None):
#       for entry in sys.path:
#           # 构造模块文件路径
#           module_path = os.path.join(entry, name + '.py')
#           if os.path.isfile(module_path):
#               # 找到模块文件，返回加载器
#               return importlib.machinery.SourceFileLoader(name, module_path)
#           return None  # 没有找到模块
#   ```
#
# 2. **加载（Load）**
#    通过加载器创建模块对象，并执行模块代码来填充其命名空间。
#    加载器负责：
#    1. 创建一个新的模块对象。
#    2. 执行模块代码，初始化模块命名空间。
#    3. 将模块对象添加到 `sys.modules` 中，以便后续导入可以直接使用缓存。
#    加载器的工作流程：
#    1. 接收模块名称和模块文件路径。
#    2. 创建一个新的模块对象。
#    3. 执行模块代码，填充模块命名空间。
#    4. 将模块对象添加到 `sys.modules` 中。
#    例如，`SourceFileLoader` 的加载流程：
#    ```python
#    import sys
#    import importlib.machinery
#    def load_module(name, module_path):
#        # 创建模块对象
#        module = types.ModuleType(name)
#        # 执行模块代码
#        with open(module_path, 'r') as f:
#            code = f.read()    exec(code, module.__dict__)
#        # 将模块对象添加到 sys.modules
#        sys.modules[name] = module
#        return module
#    ```
# 3. **绑定（Bind）**
#    将模块对象（或其中的属性）绑定到当前命名空间的变量名上。
#    绑定的方式取决于导入语句的形式：
#    1. **`import module_name`**
#       将模块对象绑定到变量 `module_name` 上。
#    2. **`from module_name import name1, name2`**
#       将模块对象中的 `name1`, `name2` 等属性绑定到当前命名空间的变量 `name1`, `name2` 上。
# 导入模块的结果：
#    1. 模块对象被创建并执行，模块级代码运行一次。
#    2. 模块对象被缓存到 `sys.modules` 中，后续导入同一模块会直接使用缓存。
#
# 导入模块的方式：
# 1. **直接导入模块**
