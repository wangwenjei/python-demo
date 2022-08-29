# 模块导入
"""
    # 导入模块内部流程
        import foo
            首次导入模块发生的三件事:
                1.执行foo.py
                2.产生foo.py的名称空间,将foo.py运行过程中产生的名字都丢到foo的名称空间中
                3.在当前文件中产生的一个名字foo,该名字指向2中产生的名称空间

        from foo import get
            首次导入模块发生的三件事:
                1.执行foo.py
                2.产生foo.py的名称空间,将运行过程中产生的名字都丢到foo的名称空间中
                3.在当前名称空间拿到一个名字,该名字与模块名称空间中的某一个内存地址


    # 导入顺序
        import 内置模块
        import 第三方模块
        import 自定义模块(规范命名为纯小写+下划线风格)

    # 起别名
        import foo as f   

    # 导入方式 
        import导入模块在使用时必须加前缀"模块名."
            优点: 肯定不会与当前名称空间中的名字冲突
            缺点: 加前缀显得麻烦

        from ... import ... 导入模块在使用时不用加前缀
            优点: 代码更精简
            缺点: 容易与当前名称空间混淆


        from foo import *  导入所有功能
        可以在foo.py内利用__all__定义*具体包含
        __all__=['x','get']   此时 * 中只会有 x 和 get 两个功能

"""


# __name__
"""
    1.当foo.py被运行时,__name__的值为'__main__'
    2.当foo.py被当做模块导入时,__name__的值为'foo'

    当文件运行时执行c()函数,当文件被当做模块导入时不执行c()
    if __name__ == '__main__':   # 敲个main回车,快捷生成
        c()
"""

# 自定义模块规范
"""
	"模块的文档描述注释" 
	import sys #导入模块

	x=1 #定义全局变量,如果非必须,则最好使用局部变量,
	    #这样可以提高代码的易维护性,并且可以节省内存提高性能

	class Foo: #定义类,并写好类的注释
	    '类注释'
	    pass

	def test(): #定义函数,并写好函数的注释
	    '函数功能注释'
	    pass

	if __name__ == '__main__': #主程序
	    test() #在被当做脚本执行时,执行此处的代码
"""

# 包
"""
    # 什么是包
        1.包就是一个包含有__init__.py文件的文件夹
        2.包的本质是模块的一种形式,包是用来被当做模块导入
            1.产生一个名称空间
            2.运行包下的__init__.py文件,将运行过程中产生的名字都丢到的名称空间中
            3.在当前文件的名称空间中拿到包的名字


    绝对导入,以包的文件夹为起始进行导入
        from foo.m1 import f1

    相对导入:
        仅限于包内使用,不能跨出包
        包内模块之间的导入,推荐使用相对导入
        from .m1 import f1
"""

# run.py
"""
	import os
	import sys
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	sys.path.append(BASE_DIR)


	from core import src
	if __name__ == '__main__':
	    src.run()
"""

