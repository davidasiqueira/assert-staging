import os
import psycopg2
from datetime import datetime

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

def manipulate_data():
    

def save_user(nome,email,phone_number,birth_date,sexo,cep,linkedin_link,instagram_link,facebook_link):
    
    data_de_registro = datetime.datetime.now()
    data_atual = datetime.datetime.now() 
    try:
        cur.execute('INSERT INTO user (name,email,phone,hash,salt,born_date,genre,registration_date,last_modification,adress,linkedin_link,instagram_link,facebook_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (nome,email,phone_number,0,0,birth_date,sexo,data_de_registro,data_atual,cep,linkedin_link,instagram_link,facebook_link))
        
        return True  
    except:
        print('Erro ao salvar usuario')

def save_user_soft(soft_a,soft_b,soft_c,soft_d,user_id):
    
    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO soft_skills (user_id,registration_date,executor,comunicador,planejador,analista) VALUES (?, ?, ?, ?, ?, ?)',
        (user_id,data_atual,soft_a,soft_b,soft_c,soft_d,))
        
        return True  
    except:
        print('Erro ao salvar soft skills do usuario')

def save_user_hard(user_id,last_jobs,courses,languages):

    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO hard_skills (user_id,registration_date,last_jobs,courses,languages) VALUES (?, ?, ?, ?, ?)',
        (user_id,data_atual,last_jobs,courses,languages))
        
        return True  
    except:
        print('Erro ao salvar hard skills do usuario')
