# Creando un clúster de ElasticSearch en local con Docker

## Requisitos

WSL 2 backend
Docker Compose

## Instalación 

### Aumentar memoria
```
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

### Ejecutar docker compose
Ejecutar el archivo `docker-compose.yml` desde la terminal.
* `cd <LOCATION>`
* `docker-compose up -d` (La flag `-d` crea el clúster en modo `detached`, por lo que no veremos logs de ejecución) 

### Recoger credenciales
`docker container cp <CID>:/usr/share/elasticsearch/config/certs .`
Situarlos en la carpeta certs correspondiente

### Parar el servicio
To stop the cluster, run docker-compose down. The data in the Docker volumes is preserved and loaded when you restart the cluster with docker-compose up.
`docker-compose down`

## Referencias
[Install Docker](https://docs.docker.com/get-docker/)
[Install multi-node Elasticsearch cluster with Docker Compose](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file)






[Kibana home](http://localhost:5601/app/home#/)






## docker-compose commands



Attach yourself to the logs of all running services, whereas -f means you follow the log output and the -t option gives you timestamps.
`docker-compose logs -f -t`


To delete the network, containers, and volumes when you stop the cluster, specify the -v option:
`docker-compose down -v`

List containers
`docker ps`