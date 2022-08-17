import os
import psycopg2
import datetime


def db_connect():
    try:
        
        DATABASE_URL = os.environ['DATABASE_URL']
        # DATABASE_URL = 'postgres://yatwqnvoxzxgtf:8f1982a27190a66c3146bfc023ab3ed794ba461eca338238a5fe48a4bf742713@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d4ilpms9p76v4p'
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        
        return conn
    except:
        conn.close()
        return "Erro ao conectar ao banco de dados" 

def manipulate_data(body):
    
    conn = db_connect()
    cur = conn.cursor()

    try:
        #salva usuário no banco de dados e retorna o id dele
        user_id = save_user(body['user_data']['name'],body['user_data']['email'],body['user_data']['phone_number'],body['user_data']['birth_date'],body['user_data']['genre'],body['user_data']['cep'],body['user_data']['linkedin_link'],body['user_data']['instagram_link'],body['user_data']['facebook_link'],cur)

        #salva o relatório de soft skills do usuário
        save_user_soft(body['user_soft']['soft_a'],body['user_soft']['soft_b'],body['user_soft']['soft_c'],body['user_soft']['soft_d'],user_id,cur)
        
        #salva o relatório de hard skills do usuário
        save_user_hard(user_id,body['user_hard']['jobs'],body['user_hard']['courses'],body['user_hard']['languages'],cur)
    except:
        return 'Erro ao salvar usuario'
     
    try:
        conn.commit()
        cur.close()
        conn.close()
        return True
    except:
        return 'Erro ao fechar conexão com o banco de dados'

def save_user(nome,email,phone_number,birth_date,sexo,cep,linkedin_link,instagram_link,facebook_link,cur):
    
    data_de_registro = datetime.datetime.now()
    data_atual = datetime.datetime.now() 
    try:
        cur.execute('INSERT INTO user_data (name,email,phone,birth_date,genre,registration_date,last_modification,cep,linkedin_link,instagram_link,facebook_link) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s) returning id',
        (nome,email,phone_number,birth_date,sexo,data_de_registro,data_atual,cep,linkedin_link,instagram_link,facebook_link))
        
        return cur.fetchone()

    except:
        
        return 'Erro ao salvar usuario'

def save_user_soft(soft_a,soft_b,soft_c,soft_d,user_id,cur):
    
    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO user_soft (user_id,last_modification,executor,comunicador,planejador,analista) VALUES (%s, %s, %s, %s,%s, %s)',
        (user_id,data_atual,soft_a,soft_b,soft_c,soft_d,))
        
        return True  
    except:
        print('Erro ao salvar soft skills do usuario')

def save_user_hard(user_id,last_jobs,courses,languages,cur):

    data_atual = datetime.datetime.now() 
    
    try:
        cur.execute('INSERT INTO user_hard ( user_id,last_modification,last_jobs,courses,languages) VALUES (%s, %s, %s, %s,%s)',
        (user_id,data_atual,str(last_jobs),str(courses),str(languages)))
        
        return True  
    except:
        print('Erro ao salvar hard skills do usuario')
