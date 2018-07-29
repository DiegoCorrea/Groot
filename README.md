# Groot  
Rádio Groot um sistema de Recomendação de música baseado em conteúdo sem personalização. Que aceita uma música de início e fim, para então gerar uma lista de músicas com o máximo de similaridade. Fazendo-se uso das informações como titulo, album e artista para encontrar a similaridade entre as músicas.  
Utilizando técnicas de aprendizado de máquina em um ambiente não supervisionado, descrevendo assim o meio ao qual esse estudo é realizado. Constrído com o uso de Árvore de Decisão utilizando tanto o gini, quanto a entropia. Para encontrar a similaridade entre as músicas o Cosine Similarity em conjunto com o Term Frequency e o Inverse Document Frequency foram usados. O peso do campo mais importante foi retirado da arvore de decisão e multiplicado por sua matrix de similaridade equivalente. A busca do caminho da música de inicio e a música de termino na matrix de similaridade é feita utilizando o algoritmo Simulated Annealing.

Tecnologias usadas:  
Python 3.6, Pip 3, Virtual Environment  
Pandas  
Sklearn  
Numpy  
Graphviz  
Scipy  
NLTK  
PyCharm  
MatPlotLib  
  
Para saber mais acesse: https://docs.google.com/presentation/d/14Q-kye8G2oXgLf_1t_CQwJqj6W7cHxadFN0zVf0N41E/edit?usp=sharing  

## Utilizando o Groot
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
6. Executando a rádio: `python main.py`  
