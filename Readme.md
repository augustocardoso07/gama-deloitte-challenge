# Desafio Gama-Deloitte
Construção de uma api CRUD para Serviços, Posts e Integrantes da Equipe (Membros)

## Tecnologia utilizada:
- Django
- Django Rest Framework
- Django Rest Swagger
- Postgres
- Heroku


## Demo
Live Demo da aplicação rodando nos serviços do Heroku.


### Dados de autentificação:
  - Usuário: **admin**
  - Senha: **senha1234**

### Links da live demo
- https://gama-deloitte-challenge.herokuapp.com/admin/ - Painel de administração do bando de dados
- https://gama-deloitte-challenge.herokuapp.com/api-auth/login/?next=/cronosapi/docs - Documentação da API
- **Importante**: para acessar os dois endereços é necessário autentificação


## Instação local
### Pre-requisitos: 
- python intalado no local
``` bash
git clone https://github.com/augustocardoso07/gama-deloitte-challenge.git
cd gama-deloitte-challenge
pip install -r requirements.txt
python manage.py migrate
python manage.py seed cronosapi
python manage.py createsuperuser
```
- Painel de administraçã: http://localhost:8000/admin/ . Acessar com os dados do usuário criado anteriormente
- Documentação da API: http://localhost:8000/cronosapi/docs 