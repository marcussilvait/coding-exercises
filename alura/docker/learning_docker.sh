''' Comandos utilizados no Docker para estudo
'''

# exibe a versão do docker.
docker version

# cria um container com a respectiva imagem passada como parâmetro.
docker run NOME_DA_IMAGEM

#  exibe todos os containers em execução no momento.
docker ps

# exibe todos os containers, independentemente de estarem em execução ou não.
docker ps -a

# conecta o terminal que estamos utilizando com o do container.
docker run -it NOME_DA_IMAGEM

# inicia o container com id em questão.
docker start ID_CONTAINER

# interrompe o container com id em questão.
docker stop ID_CONTAINER

# inicia o container com id em questão e integra os terminais, além de permitir interação entre ambos.
docker start -a -i ID_CONTAINER

# remove o container com id em questão.
docker rm ID_CONTAINER

# remove todos os containers que estão parados.
docker container prune

# remove a imagem passada como parâmetro.
docker rmi NOME_DA_IMAGEM

# ao executar, dá um nome ao container.
docker run -d -P --name NOME dockersamples/static-site

# define uma porta específica para ser atribuída à porta 80 do container, neste caso 12345.
docker run -d -p 12345:80 dockersamples/static-site

# define uma variável de ambiente AUTHOR com o valor Fulano no container criado.
docker run -d -P -e AUTHOR="Fulano" dockersamples/static-site

# cria um volume no respectivo caminho do container, caso seja especificado um caminho local monta o volume local no volume do container.
docker run -v "[CAMINHO_VOLUME_LOCAL:]CAMINHO_VOLUME_CONTAINER" NOME_DA_IMAGEM - 

# retorna diversas informações sobre o container.
docker inspect ID_CONTAINER

# para descobrir o IP dessa máquina virtual no caso do Docker Toolbox
docker-machine ip

# cria uma imagem a partir de um Dockerfile.
docker build -f Dockerfile

# constrói e nomeia uma imagem não-oficial informando o caminho para o Dockerfile.
docker build -f CAMINHO_DOCKERFILE/Dockerfile -t NOME_USUARIO/NOME_IMAGEM

# exemplo de build - deve estar no dir com Dockerfile
docker build -f Dockerfile -t marvinsilva/node .

# inicia o processo de login no Docker Hub.
docker login

# envia a imagem criada para o Docker Hub.
docker push NOME_USUARIO/NOME_IMAGEM

# baixa a imagem desejada do Docker Hub
docker pull NOME_USUARIO/NOME_IMAGEM

# mostra o ip atribuído ao container pelo docker (funciona apenas dentro do container).
hostname -i

# cria uma rede especificando o driver desejado.
docker network create --driver bridge NOME_DA_REDE

# cria um container especificando seu nome e qual rede deverá ser usada.
docker run -it --name NOME_CONTAINER --network NOME_DA_REDE NOME_IMAGEM

# pegando dados de um banco em um outro container
docker pull douglasq/alura-books:cap05
docker pull mongo
docker network create --driver bridge minha-rede
docker run -d --name meu-mongo --network minha-rede mongo
docker run --network minha-rede -d -p 8080:3000 douglasq/alura-books:cap05

''' Principais comandos utilizados durante o curso de Docker
'''
# Comandos relacionados às informações
docker version # exibe a versão do docker que está instalada.
docker inspect ID_CONTAINER # retorna diversas informações sobre o container.
docker ps # exibe todos os containers em execução no momento.
docker ps -a # exibe todos os containers, independentemente de estarem em execução ou não.

# Comandos relacionados à execução
docker run NOME_DA_IMAGEM # cria um container com a respectiva imagem passada como parâmetro.
docker run -it NOME_DA_IMAGEM # conecta o terminal que estamos utilizando com o do container.
docker run -d -P --name NOME dockersamples/static-site # ao executar, dá um nome ao container e define uma porta aleatória.
docker run -d -p 12345:80 dockersamples/static-site # define uma porta específica para ser atribuída à porta 80 do container, neste caso 12345.
docker run -v "CAMINHO_VOLUME" NOME_DA_IMAGEM # cria um volume no respectivo caminho do container.
docker run -it --name NOME_CONTAINER --network NOME_DA_REDE NOME_IMAGEM # cria um container especificando seu nome e qual rede deverá ser usada.

# Comandos relacionados à inicialização/interrupção
docker start ID_CONTAINER # inicia o container com id em questão.
docker start -a -i ID_CONTAINER # inicia o container com id em questão e integra os terminais, além de permitir interação entre ambos.
docker stop ID_CONTAINER # interrompe o container com id em questão.

# Comandos relacionados à remoção
docker rm ID_CONTAINER # remove o container com id em questão.
docker container prune # remove todos os containers que estão parados.
docker rmi NOME_DA_IMAGEM # remove a imagem passada como parâmetro.

# Comandos relacionados à construção de Dockerfile
docker build -f Dockerfile # cria uma imagem a partir de um Dockerfile.
docker build -f Dockerfile -t NOME_USUARIO/NOME_IMAGEM # constrói e nomeia uma imagem não-oficial.
docker build -f Dockerfile -t NOME_USUARIO/NOME_IMAGEM CAMINHO_DOCKERFILE # constrói e nomeia uma imagem não-oficial informando o caminho para o Dockerfile.

# Comandos relacionados ao Docker Hub
docker login # inicia o processo de login no Docker Hub.
docker push NOME_USUARIO/NOME_IMAGEM # envia a imagem criada para o Docker Hub.
docker pull NOME_USUARIO/NOME_IMAGEM # baixa a imagem desejada do Docker Hub.

#Comandos relacionados à rede
hostname -i # mostra o ip atribuído ao container pelo docker (funciona apenas dentro do container).
docker network create --driver bridge NOME_DA_REDE # cria uma rede especificando o driver desejado.

# Comandos relacionados ao docker-compose
docker-compose build # Realiza o build dos serviços relacionados ao arquivo docker-compose.yml, assim como verifica a sua sintaxe.
docker-compose up # Sobe todos os containers relacionados ao docker-compose, desde que o build já tenha sido executado.
docker-compose down # Para todos os serviços em execução que estejam relacionados ao arquivo docker-compose.yml.