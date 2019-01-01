import os
PreStr = "![food](/images/Food2018/"
EndStr = ")"

for file in os.listdir('.'):
    if file[-2: ] == 'py':
        continue
    Str = PreStr + file + EndStr
    print(Str)
    print("")

