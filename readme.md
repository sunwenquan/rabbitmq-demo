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
