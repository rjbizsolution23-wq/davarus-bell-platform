.PHONY: setup dev test build check deploy

setup:
	cd app && npm install

dev:
	python3 -m http.server 8080 --directory app/public

check:
	cd app && npx tsc --noEmit

deploy:
	cd app && npx wrangler deploy
