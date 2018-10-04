build:
	docker build --rm=false -t user-microservice .
run:
	docker run --name=userserv --net=isolated_network -d -p 3000:3000 user-microservice
