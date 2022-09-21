from datetime import datetime

import os
print(datetime.now().strftime('현재시간은 %Y-%m-%d %H:%M:%S입니다'))
print('현재 위치는', str(os.getcwd()))

with open('./log', 'a') as f:
    f.write(datetime.now().strftime('현재시간은 %Y-%m-%d %H:%M:%S입니다.\n'))
    f.write('현재 위치는 ' + str(os.getcwd()) + '\n')