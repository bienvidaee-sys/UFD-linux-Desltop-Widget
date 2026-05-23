#!/usr/bin/env python3
import tkinter as tk
import subprocess  # 把這個搬到最上面，比較乾淨
import os          # 增加這個可以幫你安全檢查

class UFDInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("UFD - Your Friend Desktop")
        self.root.geometry("800x400")

        self.characters = [
            ("Catman", "gray"), ("Diskdibian", "blue"),
            ("Easyceaer", "yellow"), ("USBcowboy", "cyan"), ("Bookman", "green")
        ]

        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=40)

        for name, color in self.characters:
            self.create_character(name, color)

    def create_character(self, name, color):
        char_frame = tk.Frame(self.top_frame, padx=15)
        char_frame.pack(side=tk.LEFT)

        # 稍微放大一點，讓表情更清楚
        canvas = tk.Canvas(char_frame, width=100, height=120, highlightthickness=0)
        canvas.pack()

        # 身體 (大圓)
        canvas.create_oval(15, 45, 85, 115, fill=color, outline="black")
        # 頭部 (小圓)
        canvas.create_oval(30, 10, 70, 50, fill=color, outline="black")
        
        # --- 靈魂表情 ---
        # 眼睛 (兩個小點)
        canvas.create_oval(40, 20, 48, 28, fill="black") # 左眼
        canvas.create_oval(52, 20, 60, 28, fill="black") # 右眼
        # 嘴巴 (半圓微笑)
        canvas.create_arc(40, 25, 60, 40, start=180, extent=180, outline="red", width=2)

        # 名字標籤
        lbl = tk.Label(char_frame, text=name, font=("Arial", 12))
        lbl.pack(pady=5)
   
        # --- 【修正後的安全試驗代碼】必須跟著上面的代碼一起縮排在函式裡面 ---
        if name == "USBcowboy":
            # 定義一個安全的點擊功能
            def click_usb(event):
                # 先用 os.path.exists 檢查 /media/sa 是否存在，避免找不到路徑而出錯
                if os.path.exists("/media/sa"):
                    subprocess.run(["xdg-open", "/media/sa"])
                else:
                    print("系統內找不到 /media/sa 資料夾！")
            
            # 同時把點擊事件綁定在 畫布(小兵身體) 和 標籤(名字) 上
            canvas.bind("<Button-1>", click_usb)
            lbl.bind("<Button-1>", click_usb)

if __name__ == "__main__":
    root = tk.Tk()
    app = UFDInterface(root)
    root.mainloop()
