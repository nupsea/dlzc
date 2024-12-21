## CMDS

```

k apply -f model-deployment.yaml


# For any changes, can remove the deployment and re-apply 

k delete -f ../k-dum/deployment.yaml
k apply -f ../k-dum/deployment.yaml

k get pods

k port-forward tf-serving-clothing-model-5f6c96694c-lcc5m 8500:8500

#  Uncomment the gateway py changes.
cd ..
python gateway.py
> MODEL_OUTPUT

# Create service 
k apply -f model-service.yaml
k get service/tf

k port-forward service/tf-serving-clothing-model 8500:8500


# create gateway deployment
kind load docker-image zc-10-gateway:002 

# Add the env name:value similar to docker-compose
Format: <NAME>.default.svc.cluster.local:8500 
viz. tf-serving-clothing-model.default.svc.cluster.local:8500


# try

k exec -it ping-deployment-7c67498747-2dknn -- bash

root@ping-deployment-7c67498747-2dknn:/app# 
apt update
apt install curl

root@ping-deployment-6c76966889-tz2td:/app# curl localhost:9696/ping
PONG

root@ping-deployment-6c76966889-tz2td:/app# curl ping.default.svc.cluster.local/ping 
PONG

root@ping-deployment-6c76966889-tz2td:/app# curl tf-serving-clothing-model.default.svc.cluster.local:8500
curl: (1) Received HTTP/0.9 when not allowed

apt install telnet

root@ping-deployment-6c76966889-tz2td:/app# telnet tf-serving-clothing-model.default.svc.cluster.local 8500
Trying 10.96.211.117...
Connected to tf-serving-clothing-model.default.svc.cluster.local.
Escape character is '^]'.
@@ kj
Connection closed by foreign host.

k apply -f gateway-deployment.yaml

k get pods
k port-forward gateway-7c95d674d5-7lg26 9696:9696

python test.py

{'dress': -1.8798637390136719, 'hat': -4.756310939788818, 'longsleeve': -2.3595337867736816, 'outwear': -1.0892633199691772, 'pants': 9.903782844543457, 'shirt': -2.8261797428131104, 'shoes': -3.648311138153076, 'shorts': 3.2411556243896484, 'skirt': -2.612095594406128, 't-shirt': -4.852035999298096}


# Create Gateway service
k apply -f gateway-service.yaml

k get service
NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
gateway                     LoadBalancer   10.96.211.105   <pending>     80:32158/TCP   7s
kubernetes                  ClusterIP      10.96.0.1       <none>        443/TCP        35h
ping                        LoadBalancer   10.96.188.80    <pending>     80:32661/TCP   25h
tf-serving-clothing-model   ClusterIP      10.96.211.117   <none>        8500/TCP       78m

 k port-forward service/gateway 8080:80
Forwarding from 127.0.0.1:8080 -> 9696
Forwarding from [::1]:8080 -> 9696

# change test.py test2.py and the port.
python test2.py
> MODEL_OUTPUT

```