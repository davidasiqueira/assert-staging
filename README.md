# assert-staging

API de teste 

 Observações de uso:
 API somente para testes e base na hora de criar o front, não existe nenhuma proteção ou conexão com o banco de dados no backend. 
 Nem todas as informações precisam ser de preenchimento obrigatório.
 retorno padrão 200
 ela só valida se o json tá certinho 

 observações "user_soft"
    Nele precisam ser passadas os números de cada opção preenchido no teste exemplo:
    "user_soft": {
      "a": "15",
      "b": "5",
      "c": "10",
      "d": "10"
    }
    A soma tem que dar sempre 40




metodo = POST
URL: /api/formulario_candidato
Body:
JSON

[{
  "user_data": {
     "nome": "",
     "email": "",
     "phone_number": "",
     "birth_date": "",
     "sexo": "",
     "cpf": "",
     "cep": "",
     "linkedin_link": "",
     "user_description": ""
  },
  "user_soft": {
      "a": "",
      "b": "",
      "c": "",
      "d": ""
  },
  "user_hard": {
      "jobs": {
          "job1": {
              "company_name": "",
              "admission_date": "",
              "departure_date": "",
              "description": ""

          },
          "job2": {
              "company_name": "",
              "admission_date": "",
              "departure_date": "",
              "description": ""

          },
          "job3": {
              "company_name": "",
              "admission_date": "",
              "departure_date": "",
              "description": ""

          },
          "job4": {
              "company_name": "",
              "admission_date": "",
              "departure_date": "",
              "description": ""

          }
      },
      "courses": {
          "course1":{
              "formation": "",
              "institution": "",
              "entry_date": "",
              "departure_date": ""
             },
          "course2":{
              "formation": "",
              "institution": "",
              "entry_date": "",
              "departure_date": ""
             },
          "course3":{
              "formation": "",
              "institution": "",
              "entry_date": "",
              "departure_date": ""
             },
          "course4":{
              "formation": "",
              "institution": "",
              "entry_date": "",
              "departure_date": ""
             }         
      },
      "languages": {
          "language1": {
              "language_name": "",
              "level": ""
          },
          "language2": {
              "language_name": "",
              "level": ""
          },
          "language3": {
              "language_name": "",
              "level": ""
          }
      }
  }   
 }
   
 ]


