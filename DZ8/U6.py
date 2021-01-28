# Кonstantin Filippov 22.01.2021
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

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
    name : str
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
            print(f"! Приёмка {qty_pal} [паллет] на склад  \"{self.name}\" невозможна, доступно ", end='')
            print(self.capacity_pallets - self.available_pallets)
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

class StoringDepartment(Storage):
        company_o : Company

        def __init__(self, company_o, name, address, available_pallets, capacity_pallets):
            self.company_o = company_o
            super().__init__(name, address, available_pallets, capacity_pallets)


def d8u6():

    printer = Printer("Sanon",5.5, False, 200, "SA-1203")
    scaner  = Scaner("KP", 2, True, 2400)
    kopir   = Kopir("Zerox N7", 12, True, 600)

    sl1 = Storage("ЖН Логистик Четырежды не Парк", "Поумолчанская область, пгт Подкапотнино", 800, 1200)
    sl2 = Storage("СМТП", "Краснонеподарский край, г.Старороссийск, ул. Постовая, д. 20", 700, 1400)
    sl3 = Storage("Актор", "47 область, Сапожный район, поселок Усть-Лужа, квартал Судоверфь", 300, 600)
    sl4 = Storage("Еловые Линии", "г.Старостоличный, ул. Прибалтийских Стелков, дом 98", 999, 1000)

    c1 = Company("ЗАО \"Золотое копытце\"")
    c2 = Company("ООО \"Бублики на Банковском\"")
    c3 = Company("ПАО \"Сказки А.С.П.\"")

    sd1 = StoringDepartment(c1, "Лукоморье", "Магнитогорск, Кузнецова, д.1",  randrange(1, 10), randrange(100, 200))
    sd2 = StoringDepartment(c2, "Тля и тов.", "Муходеровка, Муравьёвая,11", randrange(1, 10), randrange(100, 300))
    sd3 = StoringDepartment(c3, "Маски-Шоу", "Бахильная ул, 13", randrange(1, 10), randrange(100, 400))

    technics = list()
    technics.append(printer)
    technics.append(scaner)
    technics.append(kopir)

    storages = list()
    storages.append(sl1)
    storages.append(sl2)
    storages.append(sl3)
    storages.append(sl4)

    c_storages = list()
    c_storages.append(sd1)
    c_storages.append(sd2)
    c_storages.append(sd3)

    while True:
        print("-- Приёмка --")
        slx = storages[int(randrange(0, len(storages)))]
        print(slx)
        tex = technics[randrange(0, len(technics))]
        print(tex)
        slx.naive_gr(tex, randrange(100,200))
        print(slx)

        print("-- Отпуск компании --")
        csx = c_storages[randrange(0,len(c_storages))]
        print(csx.company_o.company_name)
        print(csx)
        print(slx)
        slx.naive_gi(technics[randrange(0, len(technics))], randrange(100, 1000), csx)
        print(csx)
        print(slx)

        iv = input("Продолжить Enter, exit для выхода:")
        if iv == "exit":
            break


d8u6()


