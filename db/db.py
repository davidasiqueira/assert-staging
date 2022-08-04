import sqlite3
from datetime import datetime

con = sqlite3.connect('assert.db3')
cur = con.cursor()

def save_user(nome,email,phone_number,birth_date,sexo,cep,linkedin_link,instagram_link,facebook_link):
    
    data_de_registro = datetime.datetime.now()
    data_atual = datetime.datetime.now() 
    try:
        cur.execute('INSERT INTO user (name,email,phone,hash,salt,born_date,genre,registration_date,last_modification,adress,linkedin_link,instagram_link,facebook_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (nome,email,phone_number,0,0,birth_date,sexo,data_de_registro,data_atual,cep,linkedin_link,instagram_link,facebook_link))
        con.commit()
        return True  
    except:
        print('Erro ao salvar usuario')

def save_user_soft(soft_a,soft_b,soft_c,soft_d,user_id):
    
    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO soft_skills (user_id,registration_date,executor,comunicador,planejador,analista) VALUES (?, ?, ?, ?, ?, ?)',
        (user_id,data_atual,soft_a,soft_b,soft_c,soft_d,))
        con.commit()
        return True  
    except:
        print('Erro ao salvar soft skills do usuario')

def save_user_hard(user_id,last_jobs,courses,languages):

    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO hard_skills (user_id,registration_date,last_jobs,courses,languages) VALUES (?, ?, ?, ?, ?)',
        (user_id,data_atual,last_jobs,courses,languages))
        con.commit()
        return True  
    except:
        print('Erro ao salvar hard skills do usuario')
