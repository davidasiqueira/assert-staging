from jsonschema import validate
from json import load


def user(json):

    try:
        with open("api_validation/user_schema.json") as f:
            schema = load(f)
            validate(json["user_data"], schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    try:
        with open("api_validation/soft_schema.json") as f:
            schema = load(f)
            validate(json["user_soft"], schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    try:
        with open("api_validation/languages_schema.json") as f:
            schema = load(f)
            validate(json["user_hard"]["languages"], schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    try:
        with open("api_validation/job_schema.json") as f:
            schema = load(f)
            validate(json["user_hard"]["jobs"], schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    try:
        with open("api_validation/courses_schema.json") as f:
            schema = load(f)
            validate(json["user_hard"]["courses"], schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    return True


def company(json):

    try:
        with open("api_validation/company_schema.json") as f:
            schema = load(f)
            validate(json, schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    return True


def vaga(json):
    
    try:
        with open("api_validation/vacancy_schema.json") as f:
            schema = load(f)
            validate(json, schema)
    except:
        return "Erro ao validar o schema{}".format(str(schema))

    return True

    
