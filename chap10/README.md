# Serving Clothing model 

## Pre-req
Run and Follow steps in c10_k.ipynb

## Test locally

```bash
python gateway_v01.py
```
>   {'dress': -1.8798637390136719, 'hat': -4.756310939788818, 'longsleeve': -2.3595337867736816, 'outwear': -1.0892633199691772, 'pants': 9.903782844543457, 'shirt': -2.8261797428131104, 'shoes': -3.648311138153076, 'shorts': 3.2411556243896484, 'skirt': -2.612095594406128, 't-shirt': -4.852035999298096}

Wrap gateway.py to include within Flask application. 


```bash
python test.py
```
>  [model OUTPUT]: {'dress': -1.8798637390136719, 'hat': -4.756310939788818, 'longsleeve': -2.3595337867736816, 'outwear': -1.0892633199691772, 'pants': 9.903782844543457, 'shirt': -2.8261797428131104, 'shoes': -3.648311138153076, 'shorts': 3.2411556243896484, 'skirt': -2.612095594406128, 't-shirt': -4.852035999298096}


## Pipenv

```
deactivate
cd c10env
pipenv install "grpcio>=1.50,<2.0" flask gunicorn keras-image-helper
pipenv install tensorflow-protobuf==2.7.0 protobuf==3.19

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

docker run -it --rm \
-p 9696:9696 \
zc-10-gateway:001 
```

### Ph 3 : With docker-compose
Create a docker compose file to run services within the same network.

```
# stop previous running instances of docker

docker build -t zc-10-gateway:002 -f image-gateway.dockerfile .
docker-compose up -d

python test.py
```
>   MODEL_OUTPUT

```
docker-compose down
```
