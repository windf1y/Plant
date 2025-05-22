from Storage import Item

class User():
    def __init__(self, name:str, password:str):
        self.name = name
        self.pwd = password

        # 玩家的资金
        self.fund = 0
        # 玩家的仓库
        self.storage = {}
    
    def get_fund(self):
        return self.fund

    def show_storagehouse(self):
        print(f"{'id':^5}|{'name':^10}|{'nums':^7}")
        for id, item in self.storage.items():
            print(f"{id:^5}|{item.get_name():^10}|{item.get_nums():^7}")
        print()
    
    def get_name(self):
        return self.name

    def get_pwd(self):
        return self.pwd
    
    def set_fund(self, fund):
        self.fund = fund
    
    def add_item2storage(self, id:str, item:Item):
        if self.is_in_storage(id):
            self.storage[id].nums += item.get_nums()
        else:
            self.storage[id] = item
    
    def del_item_in_storage(self, id:str):
        if not self.is_in_storage(id):
            print(f"{id:^5}已经不在仓库中")
        else:
            del self.storage[id]

    
    def get_storage_item(self, id:str):
        if not self.is_in_storage(id):
            print(f"{id:^5}不在仓库中")
        else:
            return self.storage.get(id)
        
    def is_in_storage(self, id:str) -> bool:
        if id not in self.storage.keys():
            return False
        else:
            return True
    