import os
from botcity.web import By
from FormBase import FormBase

class FormLogin(FormBase):
    def __init__(self):
        super().__init__()
        
    
    def abrir_forms(self):
        caminho_relativo = 'templates/login.html'
        caminho = os.path.abspath(caminho_relativo)
        self.bot.browse(f'file:///{caminho.replace("\\", "/")}')
        self.bot.wait(500)
        
        
    def inserir_nome(self, nome):
        self.bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(nome)
        self.bot.wait(500)
        
    
    def inserir_senha(self, senha):
        self.bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(senha)
        self.bot.wait(500)
        
        
    def enviar(self):
        btn = self.bot.find_element('/html/body/div/form/input[3]', By.XPATH)
        btn.click()
        self.bot.wait(3000)
    
        