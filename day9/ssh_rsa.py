# @Time     :2018/7/14 下午6:05
# @Author   :Jennings
# @Email    :zjn@wiwi.ink

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.1', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()
print(result.decode())

# 关闭连接
ssh.close()
