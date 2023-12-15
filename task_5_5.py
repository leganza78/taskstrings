import json
from pprint import pprint
with open("teplate.json") as f:
    file_content = f.read()
    template = json.loads(file_content)
# вывод всех данных
pprint(template)
print('-----------------------------------------------------------------------------------------')
# вывод по условию
for switch in template.keys():
    if template[switch]['10/100Mbps'] == "5x" and \
            template[switch]['MAC address entrles'] == "1k":
        pprint(template[switch])