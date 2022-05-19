from datetime import datetime
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
path = 'output.txt'
f = open(path, 'a')
f.writelines(now)
f.writelines('\n')
f.close()
