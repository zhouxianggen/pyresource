# coding: utf8
from . import ECS_ALL

content = '''#!/bin/bash

machines=()
'''

for idx,e in enumerate(ALL_ECS):
    content += "machines[%d]='%s\\t%s\\t%s'\n" % (
            idx, e.ip, e.inner_ip, ','.join(e.groups))

content += '''
echo "################# 机器列表 ################"
echo -e "index\\t外网IP\\t\\t内网IP\\t\\t描述"
for idx in "${!machines[@]}"
do
    echo -e "$idx\\t${machines[idx]}"
done

echo "输入要跳转到的机器序号: "
read idx

IFS='\\t' read -ra t <<< "${machines[idx]}"

inner_ip=${t[2]}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
./_g admin $inner_ip 5a24996cf312

'''

path = '/usr/local/bin/g'
open(path, 'wb').write(content)
os.system('chmod a+x %s' % path)
print 'finished'

