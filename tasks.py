from celery import Celery

rabbitmq_url = 'amqp://gavin:123456@localhost/vhost_one'
redis_url = 'redis://localhost:6379'

app = Celery('tasks',broker=rabbitmq_url,backend=redis_url)

@app.task
def add(x,y):
	return x + y
	
	
