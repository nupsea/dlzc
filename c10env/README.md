## Pipenv

```
deactivate
cd c10env
pipenv install "grpcio>=1.50,<2.0" flask gunicorn keras-image-helper
pipenv install tensorflow-protobuf==2.7.0 
# protobuf==3.19

pipenv shell
# test with local python call by uncommenting in the main function
python gateway.py 
```                                                                                                                                                                                                           
##  Docker

### Ph 1

```
docker build -t zc-10-model:xception-v4-001 -f image-model.dockerfile .

docker run -it --rm \
-p 8500:8500 \
zc-10-model:xception-v4-001 

pipenv run python gateway.py
```
>   [model OUTPUT]

### Ph 2
```
docker build -t zc-10-gateway:001 -f image-gateway.dockerfile .
(or) 
docker build --no-cache --platform linux/amd64 -t zc-10-gateway:001 -f image-gateway.dockerfile .


docker run -it --rm \
-p 9696:9696 \
zc-10-gateway:001 
```

### Ph 3 : With docker-compose
Create a docker compose file to run services within the same network.

```
# stop previous running instances of docker

docker build -t zc-10-gateway:002 -f image-gateway.dockerfile .
(or)
docker build --no-cache --platform linux/amd64 -t zc-10-gateway:002 -f image-gateway.dockerfile .

docker-compose up -d

python test.py
```
>   MODEL_OUTPUT

```
docker-compose down
```
