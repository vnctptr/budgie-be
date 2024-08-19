FLASK := python -m flask

run:
	$(FLASK) --app budgie run

.PHONY: run
