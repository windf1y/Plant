class NumsIsZeroInBuy(Exception):
    def __init__(self, nums):
        super().__init__(f"购买数量错误:{nums}")

class LackMoney(Exception):
    def __init__(self, money, pay):
        super().__init__(f"当前仅剩{money}，共需{pay}，购买失败")

class IdIsNull(Exception):
    def __init__(self, id):
        super().__init__(f"id:{id:^3}不存在")