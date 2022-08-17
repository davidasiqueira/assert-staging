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

{
    "user_data": {
        "name": "David",
        "email": "teste@teste.com.br",
        "phone_number": "21988887777",
        "birth_date": "01/04/2001",
        "genre": "Masculino",
        "cep": "12345678",
        "linkedin_link": "www.linkdeteste.com.br",
        "instagram_link": "www.linkdeteste.com.br",
        "facebook_link": "www.linkdeteste.com.br",
        "user_description": "poderia colocar um pouco de lorem ipsum aqui, mas achei mais fácil fazer isso, já é o suficiente para testar."
    },
    "user_soft": {
        "soft_a": 1,
        "soft_b": 2,
        "soft_c": 3,
        "soft_d": 4
    },
    "user_hard": {
        "jobs": [
            {
                "company_name": "Alterdata",
                "admission_date": "01/02/2020",
                "departure_date": "",
                "description": "QA"
            }
        ],
        "courses": [
            {
                "formation": "Análise e desenvolvimento de sistemas",
                "institution": "Estácio",
                "entry_date": "01/04/2018",
                "departure_date": "01/04/2022"
            }
        ],
        "languages": [
            {
                "language_name": "english",
                "level": 5
            }
            
        ]
    }
}



