import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI 计算器")
        self.root.geometry("380x320")
        self.root.resizable(False, False)

        # ---------- 标题 ----------
        tk.Label(
            root, text="BMI 计算器", font=("微软雅黑", 16, "bold")
        ).pack(pady=10)

        # ---------- 身高输入 ----------
        height_frame = tk.Frame(root)
        height_frame.pack(pady=5)
        tk.Label(height_frame, text="身高 (cm)：", font=("微软雅黑", 12)).pack(side=tk.LEFT)
        self.height_entry = tk.Entry(height_frame, font=("微软雅黑", 12), width=10)
        self.height_entry.pack(side=tk.LEFT, padx=5)

        # ---------- 体重输入 ----------
        weight_frame = tk.Frame(root)
        weight_frame.pack(pady=5)
        tk.Label(weight_frame, text="体重 (kg)：", font=("微软雅黑", 12)).pack(side=tk.LEFT)
        self.weight_entry = tk.Entry(weight_frame, font=("微软雅黑", 12), width=10)
        self.weight_entry.pack(side=tk.LEFT, padx=5)

        # ---------- 计算按钮 ----------
        tk.Button(
            root, text="计算 BMI", font=("微软雅黑", 12),
            command=self.calculate, bg="#4CAF50", fg="white", width=12
        ).pack(pady=12)

        # ---------- 结果显示 ----------
        self.result_label = tk.Label(
            root, text="请输入身高和体重", font=("微软雅黑", 12),
            fg="blue", wraplength=340
        )
        self.result_label.pack(pady=5)

        self.category_label = tk.Label(
            root, text="", font=("微软雅黑", 13, "bold"), fg="black"
        )
        self.category_label.pack(pady=5)

        # ---------- 重置按钮 ----------
        tk.Button(
            root, text="重置", font=("微软雅黑", 11),
            command=self.reset, width=8
        ).pack(pady=8)

    def calculate(self):
        """读取输入，计算 BMI，并显示结果"""
        try:
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())
        except ValueError:
            messagebox.showwarning("输入错误", "请输入有效的数字！")
            return

        if height_cm <= 0 or weight_kg <= 0:
            messagebox.showwarning("输入错误", "身高和体重必须大于 0！")
            return

        # 厘米转米
        height_m = height_cm / 100

        # BMI 公式
        bmi = weight_kg / (height_m ** 2)

        # 保留一位小数
        bmi_rounded = round(bmi, 1)

        # 分类（WHO 标准）
        if bmi < 18.5:
            category = "偏瘦"
            color = "orange"
        elif 18.5 <= bmi < 24:
            category = "正常"
            color = "green"
        elif 24 <= bmi < 28:
            category = "超重"
            color = "orange"
        else:
            category = "肥胖"
            color = "red"

        # 更新界面
        self.result_label.config(text=f"你的 BMI 是：{bmi_rounded}", fg="black")
        self.category_label.config(text=f"分类：{category}", fg=color)

    def reset(self):
        """清空输入和结果"""
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.result_label.config(text="请输入身高和体重", fg="blue")
        self.category_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()