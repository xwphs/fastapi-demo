# 说明
## 如何使用
举例说明：
1. 我有一个脚本目录/opt/scripts,然后我想要调用/opt/scripts/shell/machine_info.sh这个脚本，没有参数
> curl -X POST http://ip:8088/scripts/shell/machine_info.sh -H 'Content-Type: application/json'

&emsp;

2. 我有一个脚本目录/opt/scripts,然后我想调用/opt/scripts/shell/nginx_check.sh这个脚本，参数为'-c check'
> curl -X POST http://ip:8088/scripts/shell/nginx_check.sh -H 'Content-Type: application/json' -d '{"para": "-c check"}'

