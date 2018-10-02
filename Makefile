build:
	(cd library_service; make build)
	(cd user_service; make build)

run:
	(cd library_service; make run)
	(cd user_service; make run)

lets_go:
	(cd library_service; make build)
	(cd user_service; make build)
	(cd library_service; make run)
	(cd user_service; make run)
