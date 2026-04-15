# Makefile

problem: test build push


NAME = linehaul-problem # modify here

test:
	echo Testing $(NAME)...
	pytest tests/

build:
	echo Building $(NAME)...
	docker build -t opthub/problem-$(NAME) .

push:
	echo Pushing $(NAME)...
	docker push opthub/problem-$(NAME)

