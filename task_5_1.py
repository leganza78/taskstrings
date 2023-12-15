# -*- coding: utf-8 -*-
"""
Задание 5.1

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:

Введите имя устройства: r1
Введите имя параметра: ios
15.4

Ограничение: нельзя изменять словарь london_co.

Эту задачу можно решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computer[device][parameter])
