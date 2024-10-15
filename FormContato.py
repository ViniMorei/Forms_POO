import os
from botcity.web import By
from FormBase import FormBase

class FormContato(FormBase):
    def __init__(self):
        super().__init__()
        
    
    def abrir_forms(self):
        caminho_relativo = 'templates/contato.html'
        caminho = os.path.abspath(caminho_relativo)
        self.bot.browse(f'file:///{caminho.replace("\\", "/")}')
        self.bot.wait(500)
        
        
    def inserir_nome(self, nome):
        self.bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(nome)
        self.bot.wait(500)
        
    
    def inserir_email(self, e_mail):
        self.bot.find_element('//*[@id="email"]', By.XPATH).send_keys(e_mail)
        self.bot.wait(500)
        
    
    def inserir_telefone(self, telefone):
        self.bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(telefone)
        self.bot.wait(500)
        
        
    def enviar(self):
        btn = self.bot.find_element('/html/body/div/form/input[4]', By.XPATH)
        btn.click()
        self.bot.wait(3000)
        
        