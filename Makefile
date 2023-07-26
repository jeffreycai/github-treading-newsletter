# include and export env vars
ifneq (,$(wildcard ./.env))
	include .env
	export
endif

init:
	python3 -m pip install -r requirements.txt
.PHONEY: init

run:
	python3 main.py
.PHONEY: init