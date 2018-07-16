# Groot
1. Atualizando o S.O.: `sudo apt update && sudo apt -y upgrade`  
2. Python 3:  
2.1. Instalando Python 3: `sudo apt install python3`  
2.2. Verifique se o Python é maior que o 3.5: `python3 -V`  
3. Instalando Pip:  
3.1. Instalando o Pip: `sudo apt install -y python3-pip`  
3.2. Verificando se o Pip foi instalado: `pip3 -V`  
3.3. Atualizando o Pip, caso já o tenha instalado: `sudo pip install --upgrade pip`  
4. Virtual Env:  
4.1. Instalando o Virtual Environment: `sudo pip3 install virtualenv`  
4.2. Verificando se o Virtual Environment foi instalado: `virtualenv --version`
5. Importando bibliotecas:  
5.1. Criando uma virtual environment: `virtualenv venv`   
5.2. Inicie o Virtual Env: `. venv/bin/activate`    
5.3. Instalando os modulos: `pip install requirements.txt`
