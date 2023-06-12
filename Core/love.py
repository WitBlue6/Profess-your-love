import tkinter as tk
from tkinter import messagebox
import random as rd
class MainPage:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('表白')
        width = 400
        height = 300
        swidth = root.winfo_screenwidth()
        sheight = root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d'%(width, height, swidth/2-width/2, sheight/2-height/2))

        self.left = 0
        self.right = 2  # 记录按钮左右位置
        self.flag = False # 记录是否拒绝过
        self.words = ["不要拒绝人家嘛~",  "真的不再考虑一下嘛~", "不喜欢我嘛~", "不要这样嘛~", "你就从了我吧~",
                      "来嘛来嘛~", "快说你喜欢人家啦~", "不要点这个选项了嘛~", "好不好嘛~", "哎哟~", "同意人家好不好嘛~"]

        self.root.overrideredirect(True)
        self.show_button()

    def show_button(self):
        self.frame = tk.Frame()
        tk.Label(self.frame).grid(row=0)
        if self.flag == False:
            tk.Label(self.frame, text='你喜欢我吗^_^', height=3, font=18, justify='center', fg='blue').grid(row=1, column=1)
        else:
            tk.Label(self.frame, text=self.words[rd.randint(0, len(self.words)-1)], height=3,
                     font=18, justify='center', fg='green').grid(row=1, column=1)
        tk.Label(self.frame).grid(row=2)

        tk.Button(self.frame, text='喜欢', height=2, font=10, command=self.like, fg='red').grid(row=3, column=self.left)
        tk.Button(self.frame, text='不喜欢', height=2, font=10, command=self.dislike, fg='red').grid(row=3, column=self.right)

        self.frame.pack()

    def like(self):
        messagebox.showinfo(message='哎呀真讨厌！')
        root.quit()

    def dislike(self):
        self.frame.destroy()
        tmp = self.left
        self.left = self.right
        self.right = tmp

        self.flag = True  # 记录是否不喜欢过

        self.show_button()

if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()