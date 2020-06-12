## Instruções para Setup e Configuração em Python

### Pyenv

Instalação de libs:
```
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
```

Instalação do pyenv e pyenv-virtualenv:
```
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

Editar no .bashrc:
vim .bashrc
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

Instalação de versão do python:
pyenv install <versao>

Setando python global:
pyenv versions
pyenv global <versao>
exemplo: pyenv global 3.8.2 2.7.17 (a versão 3.8 é a padrão porque é a primeira da lista)

Tutorial:
https://www.vicentemarcal.com/2017/08/09/organizando-nosso-trabalho/
https://medium.com/welcome-to-the-django/guia-definitivo-para-organizar-meu-ambiente-python-a16e2479b753

Virtualenv

No Terminal Linux:
python3 -m venv .venv
source .venv/bin/activate
deactivate
python2 -m pip install virtualenv
python2 -m virtualenv .venv

Git

ssh-keygen -t rsa
cat /home/marcus/.ssh/id_rsa.pub
No github: settings > SSH Key

Pipenv

pyenv which python
pip install pipenv
pipenv
vim .bashrc
source .bashrc

Linha adicionado ao .bashrc
export PIPENV_VENV_IN_PROJECT=1

echo $PIPENV_VENV_IN_PROJECT

mkdir pipenv-proj
cd pipenv-proj/
pipenv install

Para verificar que os arquivos Pipfile, Pipfile.lock e .venv foram criados:
ls -l -a

Build determinístico:
rm -rf .ven/
pipenv sync -d

Ativar o virtualenv do pipenv:
pipenv shell
flake8 .
exit
Ou simplesmente:
pipenv run flake8 .

Django

Setup de projeto e arquivo Manage
django-admin
django-admin startproject pypro .
python manage.py --help
python manage.py runserver

Alias para o manage.py
echo $VIRTUAL_ENV
vim ~/.bashrc
alias mng='python $VIRTUAL_ENV/../manage.py'
Ativar o ambiente virtual e executar o comando
source .venv/bin/activate ou pipenv shell
mng runserver
Publicação no Heroku
sudo snap install --classic heroku
pipenv install gunicorn
heroku apps:create <sua_app>
git remote -v
git push heroku <branch_local>:master -f
heroku config:set DISABLE_COLLECTSTATIC=1
heroku open

Criação do app:
mng startapp <nome_do_app>

Cobertura de Testes:
pipenv install --dev 'pytest-cov' codecov
pipenv run pytest --cov=pypro

Lib Python Decouple
pipenv install 'python-decouple'
cp contrib/env-sample .env
heroku config:set DEBUG=False
heroku config
 
Secret Key
Documentação Secret Key:
https://docs.djangoproject.com/en/latest/ref/settings/#secret-key
Geração de chave:
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
Setando no Heroku:
heroku config:set SECRET_KEY=<sua_chave_secreta>

Domínio e ALLOWED_HOSTS
heroku domains:add <seu_dominio.com.br>
heroku config:set ALLOWED_HOSTS='<seu_dominio.com.br>, <seu_outro_dominio.com.br>

Backup do Postgresql
Para agendar os backups no heroku:
heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Sao_Paulo'
Para visualizar os backups disponíveis:
heroku pg:backups

The Twelve-Factor App
https://12factor.net/pt_br/

Instalação e configuração do Docker
instalação: https://docs.docker.com/engine/install/ubuntu/#install-from-a-package
Docker-compose:
https://docs.docker.com/compose/install/
pós instalação:
https://docs.docker.com/engine/install/linux-postinstall/
Docker e Pycharm
https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html
