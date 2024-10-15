# _Botcity_ Orientado a Objetos - Herança de Formulários

Este projeto aplica os conceitos de POO aos formulários _HTML_, utilizando o _BotCity_ para resolver o seguinte problema: "Criar uma hierarquia de classes que representem diferentes tipos de formulários (FormBase, FormularioContato, FormularioLogin). Utilizar BotCity para preencher automaticamente diferentes tipos de formulários em uma página web."

### Explicação

Foram implementadas três classes: _FormBase_, _FormContato_ e _FormLogin_. As duas últimas herdam de _FormBase_. No FormBase o método construtor declara um _WebBot_ que então é passado para as subclasses, não necessitando então utilizar um _WebBot_ na automação _bot.py_

## Início

Estas instruções detalham o fluxo que deve ser seguido para poder executar esta automação.

### Pré-requisitos
- Ter o _Python_ instalado na máquina

### Execução
* Criar um ambiente virtual para instalar as dependências:
  ```
  python -m venv venv
  venv/Scripts/Activate
  
  (venv) pip install -r requirements.txt
  ```

* Executar no terminal:
    ```
    python bot.py
    ```

