import tkinter as tk
from tkinter import messagebox

class MainPage:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('表白')
        self.root.geometry('400x300')

        self.left = 0
        self.right = 2  # 记录按钮左右位置


        self.root.overrideredirect(True)
        self.show_button()

    def show_button(self):
        self.frame = tk.Frame()
        tk.Label(self.frame).grid(row=0)
        tk.Label(self.frame, text='你喜欢我吗', height=3, font=18, justify='center', fg='blue').grid(row=1, column=1)
        tk.Label(self.frame).grid(row=2)

        tk.Button(self.frame, text='喜欢', height=2, font=10, command=self.like, fg='red').grid(row=3, column=self.left)
        tk.Button(self.frame, text='不喜欢', height=2, font=10, command=self.dislike, fg='red').grid(row=3, column=self.right)
        self.frame.pack()

    def like(self):
        messagebox.showinfo(message='讨厌，死鬼！')
        root.quit()

    def dislike(self):
        self.frame.destroy()
        tmp = self.left
        self.left = self.right
        self.right = tmp
        self.show_button()

if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()