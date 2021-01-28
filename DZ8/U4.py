# Кonstantin Filippov 22.01.2021
# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    name : str
    address : str
    capacity_pallets : int
    available_pallets : int

    def __init__(self, name, address, capacity_pallets, available_pallets):
        self.name = name
        self.address = address
        self.capacity_pallets = capacity_pallets
        self.available_pallets = available_pallets

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

def d8u4():
    p = Printer("Sanon",5, False, 200, "SA-1203")
    s = Scaner("KP", 2, True, 2400)
    k = Kopir("Zerox N7", 12, True, 600)

    print(p)
    print(s)
    print(k)

d8u4()


