class Crops():
    def __init__(self, name, mature, ):
        self.name = name
        # 成长天数
        self.growing_day = 0
        # 成熟天数
        self.mature = mature

    def show_info(self):
        print(f"==={self.name} 作物信息===")
        print(f"成长天数: {self.growing_day}")
        print(f"成熟天数: {self.mature}")

    def pass_day(self):
        if self.growing_day < self.mature:
            self.growing_day+=1
        else:
            print(f"{self.name} 已经成熟，停止生长")