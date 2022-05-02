# MLOps-Week3

## Programming Assignment: AWS, FastAPI, and HuggingFace

This is is the containerized version of the Huggingface + FastAPI for the Reddit Robot TSLA.

You can also push the container in an AWS Public ECR for future deployment in an EC2 or in Kubernetes.

## How to us it

All the commends are implemented using Makefile. Here you have the list of available commands:

* Build the image:

```
make build
```

* Run the container associated to the image:

```
make run
```

* Stop the container associated to the image

``` 
make stop
``` 

* Access the container in the console

```
make bash
```

* Access the logs

``` 
make logs
```

* Push the image to the public ECR at AWS

```
make push 
```

* Authenticate docker in AWS

```
make auth
```
