# Desafio Planilha Médica

Projeto Desafio Planilha Médica tem como objetivo uma implementação Python+Django+mongoDB+Heroku 

**Publicação online do projeto**

Foi publicado no Heroku para fim de estudo da plataforma visto que possuo conhecimento prévio da Azure e AWS
https://medicalform.herokuapp.com/medicalRecord/

**Sobre a interface html**
- Utilização do framework Bootstrap
- Template base para reutilização nos dois templates
- Recurso de caixa de diálogo modal para inserção de novos pacientes
- Javascript para habilitar/desabilitar botão de salvar

**Sobre a base de dados**

Foi utilizado para testes o MongoDB através do MongoDB Atlas, também a fins de estudo pois tinha pouco conhecimento desta base de dados NoSQL. 
Toda manipulação dos dados foi realizada através do Django Models, com isto uma simples configuração no arquivo settings.py é possível utilizar praticamente qualquer base de dados.

**Testes unitários**

Foram criados testes unitários básicos para ilustrar o cuidado com a manutenção do formato do model do sitema e outro para garantir a atualização das informações do sistema. 

**API REST**

Foi disponibilizada uma API REST para acesso aos dados das planilhas com o seguinte endpoint: https://medicalform.herokuapp.com/medicalRecord/api-patients/
