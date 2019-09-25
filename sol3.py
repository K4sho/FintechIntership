import re

test = str(input())

result = re.findall("[:;]-*(\(+|\)+|\]+|\[+)", test)
if result == None:
    print(0)
else:
    print(len(result))