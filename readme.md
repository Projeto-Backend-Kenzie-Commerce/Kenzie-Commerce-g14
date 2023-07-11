<h1 align="center"> Kenzie Commerce </h1>

<p align="center">
Projeto desenvolvido por alunos da Kenzie Academy Brasil.
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-documentação">Documentação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>


<br>



## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- Python
- Django

## 📚  Bibliotecas

Esse projeto foi desenvolvido com as seguintes bibliotecas:

- djangorestframework
- djangorestframework-simplejwt
- drf-spectacular
- gunicorn
- psycopg2-binary
- python-dotenv
- whitenoise
- pytest

## 💻 Projeto

Apresentamos o Kenzie Commerce, um sistema para impulsionar seu e-commerce. Com nossa tecnologia avançada, você terá uma plataforma eficiente e amigável. Imagine uma ferramenta inteligente que conecta todas as partes do seu negócio, como cadastro de produtos, vendas e gerenciamento de pedidos, permitindo que trabalhem juntas harmoniosamente. Além disso, você pode definir diferentes níveis de acesso para administradores, vendedores e clientes, garantindo controle e segurança. Nossa equipe especializada cuidou de todos os detalhes técnicos, permitindo que você se concentre no crescimento do seu negócio. Estamos aqui para ajudar e responder a quaisquer perguntas que você possa ter.

## 🔖 Documentação

Você pode visualizar a documentação do projeto através desse [link](https://www.figma.com/file/gpqavL469k0pPUGOmAQEM9/Explorer-Lab-%2301/duplicate).

## :memo: Licença

Esse projeto está sob a licença da Kenzie Academy Brasil.

---

##  📱 Contatos

- https://www.linkedin.com/in/daniel-willian-260204246/
- https://www.linkedin.com/in/alysson-fernandes-cisne/
- https://www.linkedin.com/in/patrick-almeida-64b897237/
- https://www.linkedin.com/in/gustavocmasscarenhas/

<br>

## Instalação dos pacotes de teste

- Rotas Users


- Rotas Products


- Rotas Addreess


- Rotas Orders


- Rotas Cart

 
- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de orders:
```python
pytest --testdox -vvs tests/orders/
```

- Rodando testes de address:
```python
pytest --testdox -vvs tests/address/
```

- Rodando testes de shop_cart:
```python
pytest --testdox -vvs tests/cart/
```

- Rodando testes de products:
```python
pytest --testdox -vvs tests/products/
```
