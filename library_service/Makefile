build:
	pipenv lock -r > requirements.txt
	docker build --rm=false -t library-microservice .

run:
	docker run --name=libserv -d -p 5000:5000 -ti library-microservice