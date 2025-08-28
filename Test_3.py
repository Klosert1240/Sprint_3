import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


    @property
    def get_name_items(self):
        return self.__name_items

    @property
    def get_number_items(self):
        return self.__number_items


    def add_item_to_cheque(self, name):

        if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items.append(int(1))


    def delete_item_from_check(self, name):
        if name not in name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            index = self.__name_items.index(name)
            del self.__name_items[index]
            del self.__number_items[index]
    
    def check_amount(self):
        total = []
        for name in self.__name_items:
            price = self.__item_price.get(name, 0)
            total.append(price)
        return sum(total)

        if sum(self.__number_items) > 10:
            total_sum *= 0.9
        return total_sum
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for name in self.__name_items:
            if self.__tax_rate.get(name) == 0.2:
                twenty_percent_tax.append(name)

        for name in twenty_percent_tax:
            price = self.__item_price.get(name, 0)
            total.append(price)

    total_sum = sum(total)
    total_nds = total_sum * 0.2

    total_quantity = sum(self.__number_items)
    if total_quantity > 10:
        total_nds *= 0.9  # применяем скидку к налогам

    return total_nds


    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for name in self.__name_items:
            if self.__tax_rate.get(name) == 0.1:
                ten_percent_tax.append(name)

        for name in ten_percent_tax:
            price = self.__item_price.get(name, 0)
            total.append(price)

        total_sum = sum(total)
        total_nds = total_sum * 0.1

        total_quantity = sum(self.__number_items)
        if total_quantity > 10:
            total_nds *= 0.9
        return total_nds
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
    
        tel_str = str(telephone_number)

        if len(tel_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f"+7{tel_str}"
