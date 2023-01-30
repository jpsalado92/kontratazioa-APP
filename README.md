# kontratazioa-APP

## Set up a Elasticsearch cluster locally

### First run

```bash
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

### Run docker-compose

Ejecutar el archivo `docker-compose.yml` desde la terminal.

```shell
cd elasticsearch
docker-compose up -d # -d means detached
```

Now we can access [Kibana home (localhost:5601)](http://localhost:5601/app/home#/). The password for the `elastic` user can be found under the [.env](elasticsearch/.env) file at the `ELASTIC_PASSWORD` entry.

### Retrieve the certs

```shell
docker ps
'18231d91e26f   docker.elastic.co/elasticsearch/elasticsearch:8.1.0   "/bin/tini -- /usr/l…"   About an hour ago   Up About an hour (healthy)   9200/tcp, 9300/tcp                   elasticsearch-es03-1'
# Grab the Container ID, in this example 18231d91e26f
```

```shell
# Then apply it in the following command
docker container cp 18231d91e26f:/usr/share/elasticsearch/config/certs/ca/ca.crt ./../secrets/
# That will get the /cert directory to the current folder
```

## 2. Otros comandos Docker

### Parar el servicio

Parar la ejecución de los contenedores. Los datos en los "Docker Volumes" se mantienen para futuras ejecuciones del
cluster.

```shell
docker-compose down
```

### Acceder a los logs del clúster

```shell
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

