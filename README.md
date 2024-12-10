# dlzc
Deep Learning Project for ML Zoomcamp

conda install scipy, keras-preprocessing, tensorflow==2.17.1



# tf-lite

> Note: works only on Docker

Docker Exec 
```
docker build --platform linux/amd64 -t clothing-model .

docker run -it --rm -p 8080:8080 --platform linux/amd64 clothing-model:latest
```

Test

```
python test.py
```

