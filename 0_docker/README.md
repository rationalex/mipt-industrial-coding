# Task 0: Docker, RabbitMQ; 
## How to run:

### start consumer, RabbitMQ and MongoDB

	(sudo) docker-compose up --build
	
### build producer

	(sudo) docker build ./producer -t producer

### start producer

	(sudo) docker run -it --rm --network=0docker_default producer