# Кonstantin Filippov 22.01.2021
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

from random import randrange

class Device:
    manufacturer : str
    weight_kg  : float
    box_height : float
    box_width  : float
    box_length : float

    def __init__(self, model_name, weight_kg, is_color):
        self.manufacturer = model_name
        self.weight_kg  = weight_kg
        self.is_color  = is_color


class Printer(Device):
    dock_pages : int
    cartridge  : str

    def __init__(self, model_name, weight_kg, is_color, dock_pages, cartridge):
        self.model_name = model_name
        self.weight_kg = weight_kg
        self.is_color = is_color

        self.dock_pages = dock_pages
        self.cartridge = cartridge

    def __str__(self):
        rv = "Принтер компании \""  + str(self.model_name) + "\" вес " + str(self.weight_kg) + "кг "
        rv += "цветной " if self.is_color else "ч/б "
        rv += "лоток " + str(self.dock_pages) + " страниц " + "картридж \"" + str(self.cartridge) + "\"."
        return rv

class Scaner(Device):
    scan_dpi : int

    def __init__(self, model_name, weight_kg, is_color, scan_dpi):
        self.model_name = model_name
        self.weight_kg = weight_kg
        self.is_color = is_color

        self.scan_dpi = scan_dpi

    def __str__(self):
        rv = "Сканер компании \""  + str(self.model_name) + "\" вес " + str(self.weight_kg) + "кг "
        rv += "цветной " if self.is_color else "ч/б "
        rv += "разрешеие " + str(self.scan_dpi) + "dpi."
        return rv

class Kopir(Device):
    pages_per_minute: int

    def __init__(self, model_name, weight_kg, is_color, pages_per_minute):
        self.model_name = model_name
        self.weight_kg = weight_kg
        self.is_color = is_color

        self.pages_per_minute = pages_per_minute

    def __str__(self):
        rv = "Копир компании \""  + str(self.model_name) + "\" вес " + str(self.weight_kg) + "кг "
        rv += "цветной " if self.is_color else "ч/б "
        rv += "скорость " + str(self.pages_per_minute) + " стр/мин."
        return rv

class Storage:
    name    : str
    address : str
    capacity_pallets : int  # max_stock
    available_pallets : int # stock

    def __init__(self, name, address, available_pallets, capacity_pallets):
        self.name = name
        self.address = address
        self.capacity_pallets = capacity_pallets
        self.available_pallets = available_pallets
        print(f"Создан склад с загрузкой: {available_pallets}/", end='')
        print(f"{capacity_pallets} [паллет]. \"{name}\"  \t\t| Адрес: \"{address}\"")

    def __str__(self):
        rv = str()
        rv = "Склад с загрузкой: "+ str(self.available_pallets)+"/"+str(self.capacity_pallets)+"[паллет]"
        rv = rv + str(self.name)+ "\t\t| Адрес: \""+str(self.address)+"\""
        return rv

    """ Наивная приёмка материала """
    def naive_gr(self, device : Device, qty_pal):
        if self.capacity_pallets < qty_pal or self.capacity_pallets - self.available_pallets < qty_pal:
            print(f"! Приёмка {qty_pal} [паллет] невозможна, доступно ", self.capacity_pallets - self.available_pallets)
        else:
            self.available_pallets += qty_pal
            print(f"<- Товар принят на склад \"{self.name}\" в количестве: ", qty_pal)

    """ Наивный отпуск материала """
    def naive_gi(self, device : Device, qty_pal, target_storage):
        if self.available_pallets < qty_pal:
            print(f"! Отпуск {qty_pal} [паллет] со склада \"{self.name}\"  невозможен, доступны ", self.available_pallets)
        else:
            self.available_pallets -= qty_pal
            target_storage.naive_gr(device, qty_pal)
            print(f"-> Товар отпущен со склада \"{self.name}\" на склад \"{target_storage.name}\"", end='')
            print(f" в количестве: ", qty_pal)

class Company:
    company_name : str

    def __init__(self, company_name):
        self.company_name = company_name

    def __str__(self):
        return self.company_name

class StoringDepartment(Storage):
        company_o : Company

        def __init__(self, company_o, name, address, available_pallets, capacity_pallets):
            self.company_o = company_o
            super().__init__(name, address, available_pallets, capacity_pallets)


def d8u5():
    p = Printer("Sanon",5.5, False, 200, "SA-1203")
    s = Scaner("KP", 2, True, 2400)
    k = Kopir("Zerox N7", 12, True, 600)

    print(p)
    print(s)
    print(k)

    sl1 = Storage("GN Logistic Четырежды не Парк", "Поумолчанская область, пгт Подкапотнино", 10, 20)
    sl2 = Storage("СМТП", "Краснонеподарский край, г.Старороссийск, ул. Постовая, д. 20", 2, 4)
    sl3 = Storage("Актор", "Вторая область, Сапожный район, поселок Усть-Лужа, квартал Судоверфь", 2, 3)
    sl4 = Storage("Еловые Линии", "г.Старостоличный, ул. Прибалтийских Стелков, дом 31", 1, 3)

    print("--")
    print(sl1)
    sl1.naive_gr(p, randrange(1,10))
    print(sl1)
    sl1.naive_gr(p, randrange(1,10))
    print(sl1)

    print("--")
    c1 = Company("ЗАО \"Золотое копытце\"")
    c2 = Company("ООО \"Рожки на Банковском\"")
    c3 = Company("ПАО \"Сказки Пушкина\"")

    print("--")
    sd1 = StoringDepartment(c1, "Главный склад", "Магнитогорск, Кузнецова, д.1", 0, 10)
    print(sd1)
    sl1.naive_gi(s, 3, sd1)
    print(sd1)

    print("--")
    print(sl2)
    sd1.naive_gi(s, 1, sl2)

d8u5()


