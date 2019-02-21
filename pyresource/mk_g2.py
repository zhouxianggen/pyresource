# coding: utf8
from . import VPS_ALL

content = '''#!/bin/bash

machines=()
'''

for idx,v in enumerate(VPS_ALL):
    v.desc = '%-10s' % v.desc
    v.ip = '%-19s' % v.ip
    content += "machines[%d]='%s\\t%s\\t%d\\t%s\\t%s'\n" % (
            idx, v.desc, v.ip, v.port, 'root', v.pswd)

content += r'''
echo "################# 机器列表 ################"
echo -e "index\t云主机\tIP\t端口\t用户\t密码"
for idx in "${!machines[@]}"
do
    echo -e "$idx\t${machines[idx]}"
done

echo "输入要跳转到的机器序号: "
read idx

IFS='|' read -ra t <<< "${machines[idx]//\\t/|}"

ip=${t[1]}
port=${t[2]}
user=${t[3]}
pswd=${t[4]}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
./_g2 $ip $port $user $pswd

'''

path = '/usr/local/bin/g2'
open(path, 'wb').write(content)
os.system('chmod a+x %s' % path)
print 'finished'

