build:
	pipenv lock -r > requirements.txt
	docker build --rm=false -t user-microservice .

run:
	docker run --name=userserv -d -p 3000:3000 -ti user-microservice
