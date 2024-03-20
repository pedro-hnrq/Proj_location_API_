<h1 align="center"> Projeto Location API </h1>

<h2 align="center">📷 Prévia <h2>



![location_2](https://github.com/pedro-hnrq/Proj_location_API_/assets/74242717/33202b5b-d076-4ade-8d0f-8a7e6a78978c)



<h3>🎯 Objetivo</h3>

<h5 align="justify">O objetivo do Projeto Location API é aprimorar os conhecimentos em Django REST Framework e Swagger, capacitando-se para efetuar requisições e manipular endpoints. Além disso, visa integrar essas habilidades com um banco de dados não relacional, como o MongoDB. Através dessa API, será possível gerenciar registros de endereços utilizando o serviço ViaCEP, bem como cadastrar clientes de forma eficiente.</h5>

#### 🗂️ Funcionalidade

<ul>
<h5 align="justify"><li>Autenticação de usuários: é possível realizar o criação de novo usuário ou gerar um token de autenticação.</li></h5>
<h5 align="justify"><li>CRUD (Criar, Editar, Listar e Excluir): os usuários autenticados têm permissão para realizar todas as operações de CRUD nos médicos e consultas.</li></h5>
<h5 align="justify"><li>Leitura de dados: usuários não autenticados têm permissão apenas para leitura de dados, sem a possibilidade de fazer alterações.</li></h5>
</ul>

#### 🏁 Endpoints Disponíveis
<ul>
<h5><li>Versão 1 da API, poderá acessar pelo Swagger ou DRF:
<ul><h5> Swagger:
<li> http://127.0.0.1:8000/api/schema/swagger/</li>
<li> http://127.0.0.1:8000/api/schema/redoc/</li></h5></ul>
<ul><h5> DRF:
    <li>http://127.0.0.1:8000/api/v1/</li>
    <li>http://127.0.0.1:8000/api/v1/address/</li>
    <li>http://127.0.0.1:8000/api/v1/client/</li>
    <li>http://127.0.0.1:8000/api/v1/addres/zip/cep</li>
    <li>http://127.0.0.1:8000/api/v1/client/id/address/</li>
</h5>
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

- Python
- Django 
- Django REST Framework 
- Mongo 
- GIT

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
pip install -r requirements.txt
```

execute os comandos abaixo para criar arquivo de variáveis de ambiente a partir de exemplos. (Lembre-se de modificá-los)

```bash
mv env .env
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
<!-- #### Realizar Teste

```python
python manage.py test
``` -->


  
Observação: usei o IDE do Visual Studio Code, juntamente com as extensões que instalei na IDE, uma foi o MongoDB para conectar ao serviço do Banco Dados não-relacional, já outro chamado Thunder Client para realiza as requisição HTTP (GET, POST, PUT, PATCH, DELETE e Token).


## Licença
[MIT License](LICENSE)
