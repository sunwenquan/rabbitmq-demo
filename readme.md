## 参考资料
https://www.rabbitmq.com/tutorials/tutorial-one-python.html

## Hello
1. 启动rabbit-server
2. 运行receive.py
3. 运行send.py
4. 再次运行send.py

预期结果：
1. 每次运行send.py将发送hello到mq队列
2. 运行receive.py后，将从mq队列中取数据，如果队列中无数据将进入等待状态。

## rabbit基本命令

### 创建rabbit用户
``rabbitmqctl add_user gavin 123456``

### 创建vhost
``localhost:~ gavinsun$ rabbitmqctl add_vhost vhost_one``

### 授权rabbit用户访问vhost的权限
``localhost:~ gavinsun$ rabbitmqctl set_permissions -p vhost_one gavin ".*" ".*" ".*"`
后边三个.*分别代表：配置权限、写权限、读权限

### 为用户分配角色权限 
rabbitmqctl set_user_tags username administrator
user_tags 可以是：administrator, monitoring, management

如果设置权限为management，则该用户可用于登陆http://localhost:15672/
http://localhost:15672/是rabbitmq管理后台地址。

### 查看所有vhost
rabbitmqctl list_vhosts

## celery使用rabbitmq作为broker，使用redis作为backend
1. 创建tasks.py
2. 创建run_celery_server.py,运行该文件，此时将启动一个celery server
3. 创建calling_the_task.py，运行该文件，celery server将收到任务并执行任务
4. 创建check_result_from_redis.py，运行该文件，将看到任务运行的结果



