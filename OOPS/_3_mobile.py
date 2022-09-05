class Product:
    def __init__(self, pro_id, pro_name, pro_brand, pro_color, pro_price, pro_ram):
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.pro_brand = pro_brand
        self.pro_color = pro_color
        self.pro_price = pro_price
        self.pro_ram = pro_ram

    def get_disp_info(self):
        print(self.pro_id, self.pro_name, self.pro_brand, self.pro_color, self.pro_price, self.pro_ram)


hp_pro = Product(101, 'hp laptop', 'hp', 'red', 5000, 5)
hp_pro.get_disp_info()
dell_pro = Product(201, 'dell laptop', 'dell', 'Blue', 17000, 10)
dell_pro.get_disp_info()
lenovo_pro = Product(301, 'lenovo laptop', 'lenovo', 'Black', 13000, 12)
lenovo_pro.get_disp_info()
if hp_pro.pro_price > dell_pro.pro_price and hp_pro.pro_price > lenovo_pro.pro_price:
    print("Price of hp mobile is higher than other.")
elif dell_pro.pro_price > hp_pro.pro_price and dell_pro.pro_price > lenovo_pro.pro_price:
    print("Price of dell mobile is higher than other.")
else:
    print("Price of lenovo mobile is higher than other.")
if hp_pro.pro_ram > dell_pro.pro_ram and hp_pro.pro_ram>lenovo_pro.pro_ram:
    print("RAM of hp mobile is higher than other.")
elif dell_pro.pro_ram > hp_pro.pro_ram and dell_pro.pro_ram > lenovo_pro.pro_ram:
    print("RAM of dell mobile is higher than other.")
else:
    print("RAM of lenovo mobile is higher than other.")
