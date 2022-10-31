## Avaliação Técnica DSIN - Teste Prático

## Tecnologias utilizadas:
Python 3
Django 
Vscode
Sqlite

## Esse projeto consiste em:
- Criar uma agenda para disponibilizar os serviços do salão
- Permitir o usuário escolher um serviço em dia e horário de acordo com agenda do salão
- Permitir alterações nos agendamentos

## Configurando o ambiente
Faça o download do zip e extraia o arquivo
Crie um máquina virtual e instale a bibliotecas disponíveis no 
arquivo requirementes.txt:

## Entre na pasta criada e inicie um ambiente virtual:

- $ cd teste-dsin
- $ python3 -m venv venv

## Depois você deve ativá-lo com o seguinte comando:

- $ source ./venv/bin/activate

## Após ativado, instale as bibliotecas necessárias para executar o projeto:

 - $ pip install -r requirements.txt

## Para poder ter o primeiro acesso e pode configurar a aplicação vamos executar o comando  'migrate' para gerar o banco de dados padrão do Django(SQLite). 

- $ ./manage.py migrate

## E depois criar o superusuario:

- $ ./manage.py createsuperuser

Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):


## Para iniciar o servidor depois deste passo você deve:

- $ ./manage.py runserver

## Para visualizar se tudo esta executando

http://localhost:8000/

