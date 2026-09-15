import tkinter as tk
from tkinter import ttk, messagebox
import random


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("猜数字游戏")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        # 游戏状态变量
        self.target = 0
        self.max_num = 100
        self.max_attempts = 7
        self.attempts = 0
        self.game_active = False

        # ---------- 难度选择区域 ----------
        tk.Label(root, text="选择难度：", font=("微软雅黑", 12)).pack(pady=5)
        self.difficulty_var = tk.StringVar()
        self.difficulty_combo = ttk.Combobox(
            root,
            textvariable=self.difficulty_var,
            state="readonly",
            font=("微软雅黑", 11)
        )
        self.difficulty_combo['values'] = (
            "简单 (1-50, 10次机会)",
            "中等 (1-100, 7次机会)",
            "困难 (1-500, 5次机会)"
        )
        self.difficulty_combo.current(1)  # 默认选中等
        self.difficulty_combo.pack(pady=5)

        # ---------- 开始按钮 ----------
        self.start_button = tk.Button(
            root, text="开始游戏", font=("微软雅黑", 12),
            command=self.start_game, bg="#4CAF50", fg="white", width=12
        )
        self.start_button.pack(pady=8)

        # ---------- 提示信息 ----------
        self.info_label = tk.Label(
            root, text="请点击「开始游戏」", font=("微软雅黑", 12),
            fg="blue", wraplength=380
        )
        self.info_label.pack(pady=10)

        # ---------- 输入区域 ----------
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="输入数字：", font=("微软雅黑", 12)).pack(side=tk.LEFT)
        self.guess_entry = tk.Entry(input_frame, font=("微软雅黑", 12), width=10)
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())  # 回车键也能提交

        self.guess_button = tk.Button(
            input_frame, text="猜！", font=("微软雅黑", 12),
            command=self.check_guess, state=tk.DISABLED, width=6
        )
        self.guess_button.pack(side=tk.LEFT)

        # ---------- 剩余次数 ----------
        self.attempts_label = tk.Label(root, text="", font=("微软雅黑", 12))
        self.attempts_label.pack(pady=8)

        # ---------- 重新开始按钮 ----------
        self.restart_button = tk.Button(
            root, text="重新开始", font=("微软雅黑", 12),
            command=self.start_game, state=tk.DISABLED, width=12
        )
        self.restart_button.pack(pady=8)

    def start_game(self):
        """根据难度初始化游戏"""
        choice = self.difficulty_var.get()
        if "简单" in choice:
            self.max_num, self.max_attempts = 50, 10
        elif "中等" in choice:
            self.max_num, self.max_attempts = 100, 7
        else:
            self.max_num, self.max_attempts = 500, 5

        self.target = random.randint(1, self.max_num)
        self.attempts = 0
        self.game_active = True

        # 更新界面
        self.info_label.config(
            text=f"已生成 1 到 {self.max_num} 之间的数字，开始猜吧！",
            fg="blue"
        )
        self.attempts_label.config(text=f"剩余次数：{self.max_attempts - self.attempts}")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.difficulty_combo.config(state=tk.DISABLED)
        self.guess_entry.focus()  # 自动聚焦到输入框

    def check_guess(self):
        """检查用户猜测"""
        if not self.game_active:
            return

        # 读取并验证输入
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("输入错误", "请输入有效的整数！")
            self.guess_entry.delete(0, tk.END)
            return

        if guess < 1 or guess > self.max_num:
            messagebox.showwarning("范围错误", f"请输入 1 到 {self.max_num} 之间的数字！")
            self.guess_entry.delete(0, tk.END)
            return

        self.attempts += 1

        # 判断大小
        if guess < self.target:
            self.info_label.config(text="📉 太小了！", fg="orange")
        elif guess > self.target:
            self.info_label.config(text="📈 太大了！", fg="orange")
        else:
            self.info_label.config(
                text=f"🎉 恭喜！在第 {self.attempts} 次猜中了数字 {self.target}！",
                fg="green"
            )
            self.end_game()
            return

        # 更新剩余次数
        remaining = self.max_attempts - self.attempts
        if remaining <= 0:
            self.info_label.config(
                text=f"😢 机会用完了！正确答案是 {self.target}。",
                fg="red"
            )
            self.end_game()
        else:
            self.attempts_label.config(text=f"剩余次数：{remaining}")
            self.guess_entry.delete(0, tk.END)

    def end_game(self):
        """结束游戏，禁用输入"""
        self.game_active = False
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.difficulty_combo.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()