build:
	docker build -t python3.5-mamba ./

shell:
	docker run -ti -v ${PWD}:/opt/python python3.5-mamba /bin/bash

test:
	mamba --enable-coverage --format documentation
