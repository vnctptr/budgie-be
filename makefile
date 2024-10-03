CONFIG := ./testdata/config.toml

run:
	python -m budgie $(CONFIG)

test:
	py.test

.PHONY: run test
