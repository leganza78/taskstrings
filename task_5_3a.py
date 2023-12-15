access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
interface = {
    'Fa0/1' : "Sector-1 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/2" : "Sector-2 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/3" : "Sector-3 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/4" : "notconnect 1 auto auto 10/100BaseTX",
    "Fa0/5" : "port connected 100 a-full a-100 10/100BaseTX",
    "Fa0/6" : "connected trunk full 100 10/100BaseTX",
    "Fa0/7" : "disabled 100 auto auto 10/100BaseTX",
}
template = {"access": access_template, "trunk": trunk_template}

mode = input("Введите режим работы интерфейса (access/trunk): ")
it = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(interface[it])
print("\n".join(template[mode]).format(vlans))