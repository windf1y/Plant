from Shop import ShopItemBase

class Item():
    def __init__(self, id:int, goods:ShopItemBase, nums:int):
        self.id = id
        self.nums = nums
        self.goods = goods

    def get_name(self):
        return self.goods.get_name()
    
    def get_id(self):
        return self.goods.get_id()
    
    def get_sale(self):
        return self.goods.get_sale()
    
    def get_buy_back(self):
        return self.goods.get_buy_back()
    
    def get_nums(self):
        return self.nums