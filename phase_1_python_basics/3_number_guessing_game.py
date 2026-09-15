import random

def get_difficulty():
    """选择难度，返回最大值和允许的猜测次数"""
    print("\n请选择难度：")
    print("1. 简单（1-50，10次机会）")
    print("2. 中等（1-100，7次机会）")
    print("3. 困难（1-500，5次机会）")
    while True:
        choice = input("输入选项（1/2/3）：").strip()
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 5
        else:
            print("❌ 无效选项，请重新输入。")

def play_game():
    """进行一局游戏"""
    max_num, max_attempts = get_difficulty()
    target = random.randint(1, max_num)
    attempts = 0

    print(f"\n我已经想好了一个 1 到 {max_num} 之间的数字。")
    print(f"你有 {max_attempts} 次机会猜中它。")

    while attempts < max_attempts:
        try:
            guess = int(input(f"第 {attempts + 1} 次猜测，请输入数字："))
        except ValueError:
            print("❌ 请输入有效的整数！")
            continue

        if guess < 1 or guess > max_num:
            print(f"⚠️ 请输入 1 到 {max_num} 之间的数字。")
            continue

        attempts += 1

        if guess < target:
            print("📉 太小了！")
        elif guess > target:
            print("📈 太大了！")
        else:
            print(f"🎉 恭喜你！在第 {attempts} 次猜中了数字 {target}！")
            return True

    print(f"😢 很遗憾，机会用完了。正确答案是 {target}。")
    return False

def main():
    print("=" * 40)
    print("       欢迎来到猜数字游戏")
    print("=" * 40)

    while True:
        play_game()
        again = input("\n是否再玩一局？（y/n）：").strip().lower()
        if again != "y":
            print("👋 感谢游玩，再见！")
            break

if __name__ == "__main__":
    main()