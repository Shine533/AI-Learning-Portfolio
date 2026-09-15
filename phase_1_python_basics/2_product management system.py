import pandas as pd
import os

# ========== 数据文件配置 ==========
DATA_FILE = "2_inventory.xlsx"  # 数据保存为Excel格式

# ========== 读取数据 ==========
def load_data():
    """启动时自动读取 Excel 文件"""
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_excel(DATA_FILE)
            print(f"✅ 已成功加载库存数据（共{len(df)}条）")
            return df.to_dict(orient="records")
        except Exception as e:
            print(f"⚠️ 读取失败，使用默认数据。错误：{e}")
    print("📭 未找到库存文件，已为您创建默认初始数据。")
    return [
        {"id": 1, "name": "纸管机", "quantity": 10, "price": 5000, "supplier": "河南机械厂"},
        {"id": 2, "name": "分切机", "quantity": 3, "price": 8000, "supplier": "广东精密机械"},
        {"id": 3, "name": "复卷机", "quantity": 8, "price": 6000, "supplier": "江苏自动化"}
    ]

# ========== 保存数据 ==========
def save_data(products):
    """每次修改后，自动保存为 Excel 文件"""
    try:
        df = pd.DataFrame(products)
        df.to_excel(DATA_FILE, index=False)
        print("💾 数据已自动保存到 inventory.xlsx")
    except Exception as e:
        print(f"❌ 保存失败：{e}")

# ========== 初始化 ==========
products = load_data()
next_id = max([p["id"] for p in products], default=0) + 1
LOW_STOCK_THRESHOLD = 5

# ========== 功能函数（与之前完全一样） ==========
def display_menu():
    print("\n" + "="*45)
    print("     外贸产品库存管理系统")
    print("="*45)
    print("1. 添加产品")
    print("2. 删除产品")
    print("3. 修改产品")
    print("4. 查询产品（按ID）")
    print("5. 显示所有产品")
    print("6. 库存预警（显示低库存产品）")
    print("7. 退出")
    print("="*45)

def add_product():
    global next_id
    print("\n--- 添加产品 ---")
    name = input("请输入产品名称: ").strip()
    if name == "":
        print("❌ 产品名称不能为空！")
        return
    try:
        quantity = int(input("请输入库存数量: "))
        if quantity < 0:
            print("❌ 数量不能为负数！")
            return
    except ValueError:
        print("❌ 请输入有效的整数！")
        return
    try:
        price = float(input("请输入产品价格（美元）: "))
        if price < 0:
            print("❌ 价格不能为负数！")
            return
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    supplier = input("请输入供应商名称: ").strip()
    if supplier == "":
        supplier = "未指定"

    new_product = {"id": next_id, "name": name, "quantity": quantity, "price": price, "supplier": supplier}
    products.append(new_product)
    next_id += 1
    save_data(products)
    print(f"✅ 产品 '{name}' 添加成功！ID: {new_product['id']}")

def delete_product():
    print("\n--- 删除产品 ---")
    try:
        pid = int(input("请输入要删除的产品ID: "))
    except ValueError:
        print("❌ 请输入有效的整数！")
        return
    for product in products:
        if product["id"] == pid:
            products.remove(product)
            save_data(products)
            print(f"✅ 产品ID {pid} 已删除！")
            return
    print(f"❌ 未找到ID为 {pid} 的产品！")

def update_product():
    print("\n--- 修改产品 ---")
    try:
        pid = int(input("请输入要修改的产品ID: "))
    except ValueError:
        print("❌ 请输入有效的整数！")
        return
    for product in products:
        if product["id"] == pid:
            print(f"当前信息: {product}")
            print("（直接按回车保留原值）")
            new_name = input(f"新名称（当前: {product['name']}）: ").strip()
            if new_name != "": product["name"] = new_name

            new_qty = input(f"新数量（当前: {product['quantity']}）: ").strip()
            if new_qty != "":
                try:
                    qty = int(new_qty)
                    if qty < 0:
                        print("❌ 数量不能为负数！")
                        return
                    product["quantity"] = qty
                except ValueError:
                    print("❌ 请输入有效的整数！")
                    return

            new_price = input(f"新价格（当前: {product['price']}）: ").strip()
            if new_price != "":
                try:
                    price = float(new_price)
                    if price < 0:
                        print("❌ 价格不能为负数！")
                        return
                    product["price"] = price
                except ValueError:
                    print("❌ 请输入有效的数字！")
                    return

            new_supplier = input(f"新供应商（当前: {product['supplier']}）: ").strip()
            if new_supplier != "": product["supplier"] = new_supplier

            save_data(products)
            print("✅ 产品信息更新成功！")
            print(f"更新后: {product}")
            return
    print(f"❌ 未找到ID为 {pid} 的产品！")

def query_product():
    print("\n--- 查询产品 ---")
    try:
        pid = int(input("请输入要查询的产品ID: "))
    except ValueError:
        print("❌ 请输入有效的整数！")
        return
    for product in products:
        if product["id"] == pid:
            print(f"🔍 查询结果: {product}")
            return
    print(f"❌ 未找到ID为 {pid} 的产品！")

def show_all_products():
    if not products:
        print("\n📭 当前库存为空！")
        return
    print("\n" + "="*80)
    print(f"{'ID':<5} {'产品名称':<12} {'库存':<6} {'价格(美元)':<12} {'供应商':<15}")
    print("-"*80)
    for p in products:
        warning = " ⚠️低库存" if p["quantity"] <= LOW_STOCK_THRESHOLD else ""
        print(f"{p['id']:<5} {p['name']:<12} {p['quantity']:<6} {p['price']:<12.2f} {p['supplier']:<15}{warning}")
    print("="*80)

def low_stock_alert():
    print(f"\n--- 库存预警（阈值: {LOW_STOCK_THRESHOLD}）---")
    low_items = [p for p in products if p["quantity"] <= LOW_STOCK_THRESHOLD]
    if not low_items:
        print("✅ 所有商品库存充足，无预警。")
        return
    print(f"⚠️ 以下 {len(low_items)} 种商品库存不足，请及时补货：")
    print("-"*60)
    for p in low_items:
        print(f"ID: {p['id']} | {p['name']} | 库存: {p['quantity']} | 供应商: {p['supplier']}")
    print("-"*60)

# ========== 主程序 ==========
def main():
    while True:
        display_menu()
        choice = input("请选择操作（1-7）: ").strip()
        if choice == "1": add_product()
        elif choice == "2": delete_product()
        elif choice == "3": update_product()
        elif choice == "4": query_product()
        elif choice == "5": show_all_products()
        elif choice == "6": low_stock_alert()
        elif choice == "7":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 无效选项，请输入1-7之间的数字！")
        input("\n按回车键继续...")

if __name__ == "__main__":
    main()