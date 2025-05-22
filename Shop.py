class ShopItemBase():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
class Seed(ShopItemBase):
    def __init__(self, name, id, sale, buy_back):
        self.sale = sale
        self.buy_back = buy_back
        super().__init__(name, id)

    def get_sale(self):
        return self.sale
    
    def get_buy_back(self):
        return self.buy_back
    
class Shop():
    def __init__(self):
        # 商店
        self.list = {}
        self.goods_nums = 0
        self.id = 0
        self.id_list = []

    def sell(self):
        """
        商店出售
        """
        yumi = Seed("玉米", self.id, 80, 100)
        self.list[str(self.id)] = yumi
        self.id_list.append(self.id)
        self.id += 1
        self.goods_nums += 1
        xiaomai = Seed("小麦", self.id, 10, 30)
        self.list[str(self.id)] = xiaomai
        self.id_list.append(self.id)
        self.id += 1
        self.goods_nums += 1
        dadou = Seed("大豆", self.id, 50, 60)
        self.list[str(self.id)] = dadou
        self.id_list.append(self.id)
        self.id += 1
        self.goods_nums += 1

    def buy(self):
        """
        商店回收
        """
        pass

    def get_goods(self, id:str)->ShopItemBase:
        return self.list.get(id)
    
    def show_shop(self):
        """
        展示商店
        """
        for id in self.id_list:
            if not self.get_goods(str(id)):
                print(f" {id} 不存在")
                self.id_list.remove(id)
            else:
                gd = self.get_goods(str(id))
                print(f"{id:^3}|{gd.name:^10}| sell price = {gd.get_sale():^5}| buy price = {gd.get_buy_back():^5}")
