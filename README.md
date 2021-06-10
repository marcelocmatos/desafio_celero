<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Desafio Celero (Python 3 e Django Rest Framework)</h3>

---

<p align="center">  Projeto desenvolvido como parte do processo seletivo da empresa Celero em junho/2021
    <br> 
</p>

## 📝 Conteúdo

- [Sobre](#sobre)
- [Iniciando](#getting_started)
- [Como Usar a API](#usage)
- [Usado no Projeto](#built_using)
[//]: - [Testes realizados](#tests)
- [Authors](#authors)
- [árvore do Projeto](#arvore)

## 🧐 Sobre <a name = "sobre"></a>

A finalidade deste desafio é testar as habilidades e conhecimento com Python 3 e Django Rest Framework. O objetivo será criar uma API rest para servir os dados do dataset “120 years of Olympic history: athletes and results” presente no Kaggle (https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#
athlete_events.csv)

## 🏁 Iniciando <a name = "iniciando"></a>

Instruções para rodar o projeto.

### Pré Requisitos

Python 3.9 e os tens listados no arquivo requirements.txt.

```
asgiref==3.3.4
atomicwrites==1.4.0
attrs==21.2.0
colorama==0.4.4
Django==3.2.4
django-filter==2.4.0
djangorestframework==3.12.4
iniconfig==1.1.1
Markdown==3.3.4
numpy==1.20.3
packaging==20.9
pandas==1.2.4
pluggy==0.13.1
py==1.10.0
pyparsing==2.4.7
pytest==6.2.4
python-dateutil==2.8.1
pytz==2021.1
six==1.16.0
sqlparse==0.4.1
toml==0.10.2

```

### Instalando

No powershell, digitar o comando abaixo para instalar todos os pacotes usados no projeto:

```
pip install -r requirements.txt
```

[//]: ## 🔧 Testes realizados <a name = "tests"></a>

[//]: Como realizar os testes automatizados.

[//]: ### Quais os principais testes realizados

[//]: Explain what these tests test and why

[//]: ```
[//]: Give an example
[//]: ```

[//]: ### codificação dos testes

[//]: testes padrão do pytest

[//]: ```
[//]: Give an example
[//]: ```

## 🎈 Como Usar a API <a name="usage"></a>

- Para acessar a API você vai na página principal localizada no endereço padrão do Django: http://127.0.0.1:8000/.
- Para acessar o modelo todos os dados da API, vá na página pdrão da API: http://127.0.0.1:8000/athlete/
- Para acessar dado por dado, ir na página http://127.0.0.1:8000/athlete/<id_do_atleta>. Ex:
```
http://127.0.0.1:8000/athlete/43578
```
- Para fazer a atualização da base de dados atravéz de um arquivo CSV deve-se acessar a página http://127.0.0.1:8000/upload_csv/
  - OBS: Para atualizar via CSV deve-se ter no arquivo as seguintes colunas:

```
"Name","Sex","Age","Height","Weight", "Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
```


## ⛏️ Usado no Projeto <a name = "built_using"></a>

- [Python](https://www.python.org/) - Language
- [Django](https://www.djangoproject.com/) - Web Framework
- [Django REST Framework](https://www.django-rest-framework.org/) - REST API Framework
- [SQLite](https://sqlite.org/index.html/) - Database

## ✍️ Autor <a name = "autor"></a>

- [@marcelocmatos](https://github.com/marcelocmatos) - 


## 🌳 Árvore do Projeto <a name = "arvore"></a>