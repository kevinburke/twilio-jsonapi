venv:
	virtualenv venv

install: venv
	. venv/bin/activate; pip install . --use-mirrors \
		--download-cache /tmp/pipcache
	@echo "\033[95m\n\nInstalled! Be sure to add ${PWD}/venv/bin to your \$$PATH\n\033[0m"

