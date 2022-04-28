
build:
	docker build . -t borjagomez/redditbot

run:
	docker-compose up -d --build

stop:
	docker-compose down

bash:
	docker run -it borjagomez/redditbot /bin/bash

logs:
	docker-compose logs -f redditbot

push:
	docker tag borjagomez/redditbot:latest public.ecr.aws/d4e8a7g0/borja-reddit-broker-bot:latest
	docker push public.ecr.aws/d4e8a7g0/borja-reddit-broker-bot:latest

auth:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 681261969843.dkr.ecr.us-east-1.amazonaws.com