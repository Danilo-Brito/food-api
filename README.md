<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="resources/lojinha.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Minha Biblioteca - API</h3>

  <p align="center">
   Projeto MVP - Sprint: Desenvolvimento Full Stack Básico
</div>

## Sobre o Projeto

---

[![Product Name Screen Shot][product-screenshot]](http://127.0.0.1:5000/openapi/swagger)

Este projeto tem como objetivo ajudar a listar os livros comprados cadastrando eles plataforma.

Nesta API você ira conseguir fazer as seguintes ações:

* Adicionar um alimento
* Editar a quantidade de um alimento
* Deletar um alimento
* Listar todos os alimento

## Como Executar

### Installation

1. Faça o clone do reposítorio. Este comando instala as dependências/bibliotecas, descritas no
   arquivo `requirements.txt`.
   ```sh
   git clone https://github.com/Danilo-Brito/library-api
   ```
2. Abra o terminal e execute o comando abaixo.
   ```sh
   (env)$ pip install -r requirements.txt
   ```
   
3. Abra o arquivo `database.py` altera as credências para a que você utiliza no seu SQL.

4. Execute no terminal o arquivo `database.py`
   [![Product Name Screen Shot][ex]]()

   > Caso esteja usando VS Code, o comando pode ser executado clicando com o botão direito em cima do arquivo.
   E acessando a opção da imagem.

5. Execute o arquivo `library.py` no terminal, para executar a API.
6. Abra no seu browser o link para ter acesso a doc da api
   ```
   http://127.0.0.1:5000/openapi/swagger
   ```
---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker-compose up --build
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.
---
<!-- CONTACT -->

## Contact

Danilo Brito - danilomelo.brito19@gmail.com

Project Link: https://github.com/Danilo-Brito/library-api

[product-screenshot]: resources/bg.png

[ex]: resources/ex.png
