## Avaliação Técnica DSIN - Teste Prático

Esse projeto consiste em:
- Criar uma agenda para disponibilizar os serviços do salão
- Permitir o usuario escolher um serviço em dia e horario de acordo com agenda do salão
- Permitir alterações nos agendamentos

## Configurando o ambiente
Faça o download deste repositorio
Crie um maquina virtual e instale a bibliotecas disponiveis no 
arquivo requirementes.txt:

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd teste-dsin
$ python3 -m venv venv
```
Depois voce deve ativa-lo com o seguinte comando:

```
$ source ./venv/bin/activate
```
Apos ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requirements.txt
```
Para poder ter o primeiro acesso e pode configurar o aplicação vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuario:
```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Para iniciar o servidor depois deste passo você deve:
```
(venv)$ ./manage.py runserver
```


Para visualizar se tudo esta executando como esperado vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)

