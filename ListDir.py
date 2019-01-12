from os import listdir
from os.path import isfile, join
filepath=r'F:\Games\Team Fortress 2\steamapps\common\PUBG\TslGame\Binaries\Win64'
print('WHENVER SQLERROR EXIT FAILURE')
files=[f for f in listdir(filepath) if isfile(join(filepath,f))]
for i in files:
    print('@ \''+filepath+'\\'+i+'\'')
