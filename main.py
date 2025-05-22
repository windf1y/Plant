import os

from User import User
# from Crops import Crops
from Shop import Shop
from Storage import Item
from Except import *

user = User("windfly", "1")
user.set_fund(1000)

################################## 基础设计
# 游戏时间
game_time = 1  # 游戏时间，单位为天

# 商店开门
crop_shop = Shop()
crop_shop.sell()
##################################

def buy_seeds(shop:Shop, user:User):
    print("\n可购买的种子：")
    shop.show_shop()

    try:
        id_crop = int(input("请输入要购买的种子id："))
        if id_crop not in shop.id_list:
            raise IdIsNull(id_crop)
        nums = int(input("数量:"))
        if nums <= 0:
            raise NumsIsZeroInBuy(nums)
        buy_price = shop.get_goods(str(id_crop)).get_sale()
        pay_money = nums * buy_price
        if user.get_fund() < pay_money:
            raise LackMoney(user.get_fund(), pay_money)
        user.set_fund(user.get_fund() - pay_money)
        item = Item(id_crop, goods=shop.get_goods(str(id_crop)), nums=nums)
        user.add_item2storage(str(id_crop), item)
        print(f"购买{shop.get_goods(str(id_crop)).name:^5} * {nums:^8}成功")
        print(f"本次花费共{pay_money:^7}")
    except NumsIsZeroInBuy as e:
        print(e)
    except LackMoney as e:
        print(e)
    except IdIsNull as e:
        print(e)



def plant_crops():
    print("\n可种植的作物：")
    user.show_storagehouse()

    seed_id = input("请输入要种植的作物id：")
    # 先从仓库中拿出来
    if not user.is_in_storage(seed_id):
        # 不在
        print(f"{seed_id:^5}仓库中不存在")
    else:
        quantity = int(input("请输入种植数量："))
        has_nums = user.get_storage_item(seed_id).nums
        if quantity > has_nums:
            print(f"{id:^5}库存不足")
        elif quantity == has_nums:
            user.del_item_in_storage(seed_id)
        else:
            user.get_storage_item(seed_id).nums -= quantity
    # 再放到土地里

# def harvest_crops():
#     global player_crops, player_inventory
#     print("\n可收获的作物：")
#     for crop, quantity in player_crops.items():
#         if game_time >= crops_info[crop]["growth_time"]:
#             print(f"{crop} - 种植数量：{quantity}")

#     crop_name = input("请输入要收获的作物名称：")
#     if crop_name in player_crops and game_time >= crops_info[crop_name]["growth_time"]:
#         quantity = player_crops.pop(crop_name)
#         yield_amount = quantity * crops_info[crop_name]["yield"]
#         if crop_name in player_inventory:
#             player_inventory[crop_name] += yield_amount
#         else:
#             player_inventory[crop_name] = yield_amount
#         print(f"成功收获 {yield_amount} 个 {crop_name}！")
#     else:
#         print("输入的作物名称无效或尚未成熟！")

# def sell_crops():
#     global player_money, player_inventory
#     print("\n可销售的作物：")
#     for crop, quantity in player_inventory.items():
#         print(f"{crop} - 库存：{quantity}")

#     crop_name = input("请输入要销售的作物名称：")
#     if crop_name in player_inventory and player_inventory[crop_name] > 0:
#         quantity = int(input("请输入销售数量："))
#         if quantity <= player_inventory[crop_name]:
#             total_price = quantity * crops_info[crop_name]["price"]
#             player_money += total_price
#             player_inventory[crop_name] -= quantity
#             print(f"成功销售 {quantity} 个 {crop_name}，获得 {total_price} 元！")
#         else:
#             print("库存不足，无法销售！")
#     else:
#         print("输入的作物名称无效或库存不足！")

def check_farm_status():
    print("农场状态：")
    print(f"游戏时间：第 {game_time} 天")

def show_uer_info(user:User):
    print("=" * 30)
    print(f"玩家：{user.get_name()}")
    print(f"资金：{user.get_fund()} 元")
    user.show_storagehouse()
    print("=" * 30)

if __name__ == "__main__":
    while True:
        os.system('cls')
        print("=" * 30)
        print(f"游戏时间：第 {game_time} 天")
        print("=" * 30)

        # 显示菜单
        print("\n1. 购买种子")
        print("2. 种植作物")
        print("3. 收获作物")
        print("4. 市场销售")
        print("5. 查看农场状态")
        print("6. 查看玩家状态")
        print("7. 退出游戏")

        choice = input("\n请选择操作：")

        if choice == "1":
            buy_seeds(crop_shop, user)
        elif choice == "2":
            plant_crops()
        elif choice == "3":
            harvest_crops()
        elif choice == "4":
            sell_crops()
        elif choice == "5":
            check_farm_status()
        elif choice == "6":
            show_uer_info(user)
        elif choice == "7":
            print("感谢游玩，再见！")
            break
        else:
            print("无效的选择，请重新输入！")
        
        choice = input("是否进入下一天 [y]/[n]: ")
        if choice == 'y':
            # 模拟一天过去
            game_time += 1