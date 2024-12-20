## Kube with Kind 

### Prep CMDS

```
docker build -t ping:001 . 

docker run -it --rm -p 9696:9696 ping:001

curl localhost:9696/ping
```


### Deployment

```
kind create cluster 

kubectl cluster-info --context kind-kind
kubectl get nodes

# Create a deployment.yaml

kubectl apply -f deployment.yaml
kubectl get deployment

kubectl get pods
> NAME                               READY   STATUS             RESTARTS   AGE
> ping-deployment-76d899fbcf-k58gf   0/1     ImagePullBackOff   0          26s

kubectl describe pod ping-deployment-76d899fbcf-k58gf   

kind load docker-image ping:001                      
> Image: "ping:001" with ID "sha256:2f0655a2f608a36f21c7bff176b6f068aff79d06fc83ef79c9b9ebed2cb8d529" not yet present on node "kind-control-plane", loading...

k  get pod

> NAME                               READY   STATUS    RESTARTS   AGE
> ping-deployment-76d899fbcf-k58gf   1/1     Running   0          7m40s


kubectl port-forward ping-deployment-76d899fbcf-k58gf 9696:9696

> Forwarding from 127.0.0.1:9696 -> 9696
> Forwarding from [::1]:9696 -> 9696

# From a separate terminal
curl localhost:9696/ping
> PONG%   

```


### Service

```
# Create a service.yaml and mention the respective ports and configuration.

k apply -f service.yaml
k get service  # or # k get svc

> 
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP   9h
ping         ClusterIP   10.96.188.80   <none>        80/TCP    4s

# change ping service to external ( LoadBalancer. type)
k apply -f service.yaml
k get svc

>
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        9h
ping         LoadBalancer   10.96.188.80   <pending>     80:32661/TCP   4m37s

k port-forward service/ping 8080:80
> Forwarding from 127.0.0.1:8080 -> 9696
> Forwarding from [::1]:8080 -> 9696

curl localhost:8080/ping
PONG%    

```
