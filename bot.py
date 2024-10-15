# from botcity.web import WebBot, Browser, By
from botcity.maestro import *
# from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from FormContato import FormContato
from FormLogin import FormLogin

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def realizar_login(form: FormLogin, qtd: range):
    fake = Faker()
    
    for _ in qtd:
        nome = fake.name()
        senha = fake.password()
        
        form.abrir_forms()
        form.inserir_nome(nome)
        form.inserir_senha(senha)
        form.enviar()
    

def colocar_contato(form: FormContato, qtd: range):
    fake = Faker()
    
    for _ in qtd:
        nome = fake.name()
        e_mail = fake.email()
        telefone = fake.phone_number()
        
        form.abrir_forms()
        form.inserir_nome(nome)
        form.inserir_email(e_mail)
        form.inserir_telefone(telefone)
        form.enviar()
        

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    try:
        contato = FormContato()
        login = FormLogin()
        
        realizar_login(login, range(5))
        colocar_contato(contato, range(5))
    
    except Exception as ex:
        print(ex)
    
    finally:
        contato.bot.stop_browser()
        login.bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
