### Tecnologias utilizadas

<p><a href="https://www.python.org/"> - Python</a></p>
<p><a href="https://www.javascript.com/"> - JavaScript</a></p>
<p><a href=""> - HTML/CSS</a></p>
<p><a href="https://www.djangoproject.com/"> - Django</a></p>
<p><a href="https://django-allauth.readthedocs.io/en/latest/"> - Django-allauth</a></p>
<p><a href="https://getbootstrap.com/"> - Bootstrap</a></p>
<p><a href="https://viacep.com.br/"> - API Viacep</a></p>

### 🎲 Rodando o projeto

```bash
# Clone este repositório
$ git clone <https://github.com/Kassiaavieira/desafioFullStack.git>

# Crie o ambiente virtual
$ python -m venv venv

# Ative o ambiente virtual
$ venv\Scripts\activate

# Instale o django (windows)
$ py -m pip install Django

# Instale as dependências
$ pip freeze > requirements.txt

# Instale as dependências
$ pip install -r requirements.txt

# Autenticação
$ pip install django-allauth

# Criação das migrations
$ python manage.py migrate

# Crie um super usuário
$ python manage.py createsuperuser

# Execute a aplicação em modo de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000/>
```
