FLASK := python -m flask

run:
	$(FLASK) --app budgie run

test:
	py.test

.PHONY: run test
