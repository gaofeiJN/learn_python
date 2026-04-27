import tkinter as tk
from tkinter import ttk


# 定义一个APP类，继承自tk.Frame
class APP(tk.Frame):
    # 初始化方法，创建窗口和标签
    # master参数是父窗口，调用父类的初始化方法
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Hello World")
        self.master.geometry("800x300")
        self.pack()

        self.entry1 = ttk.Entry(self)
        self.entry1.pack(pady=20)

        # 创建一个变量，用于存储entry的内容
        self.var = tk.StringVar()
        self.var.set("Hello World")  # 设置变量的初始值

        # 将entry1的内容绑定到变量上（双向绑定）
        self.entry1.config(textvariable=self.var)

        # 将entry1与回车键绑定，按下回车键时调用on_enter方法
        self.entry1.bind("<Return>", self.on_enter)

        # 创建一个按钮
        self.button1 = ttk.Button(self, text="change entry", command=self.on_click)
        self.button1.pack(pady=20)

    # 定义一个方法，当按下回车键时调用
    def on_enter(self, event):
        # 获取entry1的内容，并打印出来
        content = self.entry1.get()
        print(content)
        print(self.var.get())  # 也可以通过变量获取内容

    # 定义一个方法，当点击按钮时调用
    def on_click(self):
        # 改变变量的值
        self.var.set("Changed!")


def main():
    root = tk.Tk()  # 创建一个Tk对象，作为主窗口
    app = APP(root)  # 创建一个APP对象，传入主窗口
    app.mainloop()  # 进入主循环，等待事件发生


if __name__ == "__main__":
    main()  # 调用main函数，启动程序
