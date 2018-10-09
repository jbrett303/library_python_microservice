build:
	docker build --rm=false -t library-microservice .
run:
	docker run --name=libserv --net=isolated_network -d -p 5000:5000 library-microservice