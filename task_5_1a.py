computer = {
    'pc1': {
        'os':'Windows 10',
        'Processor':'ADM Phenom II',
        'ram':'8 Gb',
        'motherboard':'GA-970A-D3 (rev. 1.0)',
        'hdd':'wd cavial blue',
        'bp' : 'HIPER HPT-400',
        'videokarta' : 'gtx 960ti',
    },
    'pc2': {
        'os':'Windows 10',
        'Processor':'ADM Phenom II x4',
        'ram':'4 Gb',
        'motherboard':'GA-970A-D3 (rev. 1.0)',
        'hdd':'wd cavial blue',
        'bp' : 'HIPER HPT-400',
        'videokarta' : '-',
    },
    'pc3': {
        'os':'Windows 10',
        'Processor':'Intel Core i7-2600',
        'ram':'16 Gb',
        'motherboard':'MSI (MAG B560M MORTAR',
        'hdd':'wd cavial blue',
        'bp' : 'HIPER HPT-400',
        'videokarta' : 'rtx 3090',
    }
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")

print(computer[device][parameter])