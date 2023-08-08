<h1 align="center"> Projeto Location API </h1>

<h2 align="center">📷 Prévia <h2>

![location](https://github.com/pedro-hnrq/Proj_location_API_/assets/74242717/cdddec8a-5d4e-4fe0-8300-54018632cfe0)


<h3>🎯 Objetivo</h3>

<h5 align="justify">Este Projeto Location API, tem como objetivo atender ao um teste, utilizando o Django REST Framework - DRF com o Banco de Dados MonoDB. A API permite o gerenciamento dos registros do Endereço usando ViaCEP e o cadastro dos clientes.</h5>

<h4>Funcionalidade</h4>

<ul>
<h5 align="justify"><li>Autenticação de usuários: é possível realizar o criação de novo usuário ou gerar um token de autenticação.</li></h5>
<h5 align="justify"><li>CRUD (Criar, Editar, Listar e Excluir): os usuários autenticados têm permissão para realizar todas as operações de CRUD nos médicos e consultas.</li></h5>
<h5 align="justify"><li>Leitura de dados: usuários não autenticados têm permissão apenas para leitura de dados, sem a possibilidade de fazer alterações.</li></h5>
</ul>

<h4>Endpoints Disponíveis</h4>
<ul>
<h5><li>Versão 1 da API: http://127.0.0.1:8000/api/v1/</li></h5>
<ul>
    <h5><li>http://127.0.0.1:8000/api/v1/address/</li></h5>
    <h5><li>http://127.0.0.1:8000/api/v1/client/</li></h5>
    <h5><li>http://127.0.0.1:8000/api/v1/addres/zip/cep</li></h5>
    <h5><li>http://127.0.0.1:8000/api/v1/client/id/address/</li></h5>

</ul>

</ul>

<h4>Métodos HTTP suportados</h4>
<ul>
<h5><li>GET: Recuperar informações de endereços ou clientes e exibir.</li></h5>
<h5><li>POST: Criar um novo registro do endereço ou cliente.</li></h5>
<h5><li>PUT: Atualizar pelo ID, as informações de um endereço ou do cliente existente .</li></h5>
<h5><li>PATCH: Atualizar pelo ID, só uma parte que deseja do cadastro informado.</li></h5>
<h5><li>DELETE: pegar pelo ID e Excluir um endereço ou clientes.</li></h5>
</ul>


<h4> 🚀 Como executar </h4>

#### 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python (versão 3.10.X)
- Docker (versão 23.0.X)
- Docker Compose (versão 2.17.X)
- Mongo (versão 6.X.X)
- GIT (versão 2.X.X)

#### 🛠️ Instalação

Faça o clone do projeto:

Link ssh
```
git@github.com:pedro-hnrq/Proj_location_API_.git
```  
Após clonar o repositório acesse o diretório
```
cd Proj_location_API_
``` 

Crie uma maquina virtual  para rodar o projeto.

```python
python -m venv .venv
```

Uma vez criado seu ambiente virtual, você deve ativá-lo.

No Unix ou no MacOS, executa:

```bash
source .venv/bin/activate
```

No Windows, execute:

```bash
.venv\Scripts\activate.bat
```

Com o ambiente virtual ativo instale as dependências

Com pip
```python
pip install -r requirements.dev.txt
```

execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (Lembre-se de modificá-los)

```bash
cp env .env
```
#### Execução na máquina

Na primeira vez é necessário executar esse comando para aplicar as migrações do banco de dados
```python
python manage.py migrate
```

Criando super usuário para acessar o painel administrativo
```python
python manage.py createsuperuser
```

Executando a aplicação
```python
python manage.py runserver
```
#### Execução dos endpoints

Como o mongoDB não suporta o `Token` para Django REST Framework,uma das maneiras foi executa através do `Shell`
```python
python manage.py shell
```

Importe as LIBs, uma por vez
```python
>>> from rest_framework.authtoken.models import Token
>>> from django.contrib.auth.models import User
```
Agora pegar o super usuário cadastrado
```python
>>> admin = User.objects.get(id=1)
>>> admin
```

Gera o Token
```python
>>> token = Token.objects.create(user=admin)
>>> token.key
```


#### Execução de produção com docker

Na primeira fazemos a coleta dos arquivos estáticos da aplicação
```python
python manage.py collectstatic
```

Depois basta executar
```bash
docker-compose up -V -d
```

Agora você pode acessar [localhost](http://localhost) no seu navegador.

Para acessar o painel administrativo basta criar um super usuário com o seguinte comando

```bash
docker compose exec app python manage.py createsuperuser
```

Para poder parar a aplicação no docker basta executar
```bash
docker compose down
```


#### Realizar Teste

```python
python manage.py test
```


  
Observação: usei o IDE do Visual Studio Code, juntamente com as extensões que instalei na IDE, uma foi o MongoDB para conectar ao serviço do Banco Dados não-relacional, já outro chamado Thunder Client para realiza as requisição HTTP (GET, POST, PUT, PATCH, DELETE e Token).


## Licença
[MIT License](LICENSE)
