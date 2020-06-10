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