# User micro-service demo

## Running the service
You can run the service on it's own by running 'python run.py'  The service will run on localhost:5000.

## Testing the service
You can run all tests using 'pipenv run python -m pytest tests/'

## Overall purpose
This service was made as 1/2 of a demonstration using two very basic microservices that talk to each other in a docker environment.
When it is ran in that context it will launch in a docker container accessible at port 3000 while the other service is accessible at 5000.
The service itself is a demostration and exploration of structure, the flask framework and those components in a microservice context.