# Creando un clúster de ElasticSearch en local con Docker

## 1. Primer uso

### Aumentar memoria

```
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

### Ejecutar docker compose

Ejecutar el archivo `docker-compose.yml` desde la terminal.

``` shell
cd <LOCATION>
docker-compose up -d # (La flag `-d` crea el clúster en modo `detached`, por lo que no veremos logs de ejecución)
```

De esta manera, el cluster se crea, y podemos aceder a Kibana a través del siguiente puerto.

* [Kibana home (localhost:5601)](http://localhost:5601/app/home#/)

### Recoger credenciales

Hay que recoger los credenciales con el siguiente comando.

``` shell
docker container cp <CID>:/usr/share/elasticsearch/config/certs .
```

Después, hay que sSituarlos en la carpeta `certs` correspondiente.

## 2. Otros comandos Docker

### Parar el servicio

Parar la ejecución de los contenedores. Los datos en los "Docker Volumes" se mantienen para futuras ejecuciones del
cluster.

``` shell
docker-compose down
```

### Acceder a los logs del clúster

``` shell
docker-compose logs -f -t
```

* `-f` para ir siguiendo el output del log.
* `-t` para mostrar timestamps del log.

### Hard reset

Para parar el servicio y eliminar la red, los contenedores y los volúmenes:

```
docker-compose down -v
```

### Listar contenedores

```
docker ps
```

## Referencias

* [Install Docker](https://docs.docker.com/get-docker/)
* [Install multi-node Elasticsearch cluster with Docker Compose](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)
