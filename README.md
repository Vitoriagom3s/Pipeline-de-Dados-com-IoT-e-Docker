# Pipeline de Dados com IoT e Docker

## Descrição do Projeto
Este projeto implementa um pipeline de dados para processar leituras de temperatura de dispositivos IoT, armazenar os dados em um banco PostgreSQL executando em Docker e disponibilizar visualizações interativas com Streamlit.

O objetivo é demonstrar, na prática, a integração entre IoT, Big Data, banco de dados relacional, conteinerização e visualização de dados. :contentReference[oaicite:0]{index=0}

---

## Tecnologias Utilizadas
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Streamlit
- Plotly
- Git/GitHub

---

## Estrutura do Projeto

pipeline-iot-docker/
│
├── data/
│   └── temperature_readings.csv
│
├── src/
│   ├── load_data.py
│   └── create_views.sql
│
├── dashboard/
│   └── dashboard.py
│
├── docs/
│   └── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore





##Fonte dos Dados

Dataset do Kaggle:
Temperature Readings: IoT Devices

Link: adicione aqui o link do dataset baixado no Kaggle.

##Pré-requisitos

-Antes de executar o projeto, instale:

Python 3.10+
Docker Desktop
Git
Instalação do Ambiente

#Clonar o repositório
git clone URL_DO_SEU_REPOSITORIO
cd pipeline-iot-docker

#Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
-Windows
venv\Scripts\activate

-Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

#Dependências do Projeto

Arquivo requirements.txt:

pandas
psycopg2-binary
sqlalchemy
streamlit
plotly

# Subindo o PostgreSQL com Docker
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -e POSTGRES_DB=iotdb -p 5432:5432 -d postgres

Se quiser iniciar novamente um container já criado:
docker start postgres-iot

#Configuração do Banco

-Credenciais usadas no exemplo:

Usuário: postgres
Senha: sua_senha
Banco: iotdb
Porta: 5432

# Execução do Pipeline de Carga

O script abaixo lê o CSV, trata os dados e envia para o PostgreSQL:
python src/load_data.py

# Criação das Views SQL

-Após inserir os dados, execute os comandos SQL do arquivo src/create_views.sql.

-Você pode executar via DBeaver, pgAdmin ou terminal SQL.

# Views Criadas
1. Média de temperatura por dispositivo

Permite identificar dispositivos com temperaturas médias mais altas ou mais baixas.

2. Leituras por hora

Mostra a distribuição do volume de leituras ao longo do dia.

3. Temperaturas máximas e mínimas por dia

Ajuda a visualizar a variação térmica diária dos dispositivos.

#Executando o Dashboard
streamlit run dashboard/dashboard.py

# Capturas de Tela

Adicione na pasta docs/screenshots/ imagens do dashboard em funcionamento.

Exemplos:

gráfico média por dispositivo
gráfico leituras por hora
gráfico máximas e mínimas por dia


# Insights Obtidos

Dispositivos com temperaturas fora do padrão podem indicar falhas ou necessidade de manutenção.
Horários com mais leituras podem revelar picos de atividade.
Acompanhar máximas e mínimas diárias permite entender tendências de aquecimento e resfriamento.

# Possíveis Aplicações Reais
Monitoramento agrícola
Controle térmico em ambientes industriais
Monitoramento de sensores em cidades inteligentes
Gestão de equipamentos em data centers


# Comandos Git Utilizados
-Inicializar repositório
git init

-Adicionar arquivos
git add .

-Criar commit
git commit -m "Projeto inicial: Pipeline de Dados IoT"

-Adicionar repositório remoto
git remote add origin URL_DO_SEU_REPOSITORIO

-Enviar para o GitHub
git push -u origin main

-Atualizar repositório local
git pull

Conclusão

Este projeto demonstra a construção de um pipeline completo de dados utilizando Python, Docker, PostgreSQL e Streamlit, integrando conceitos modernos de IoT, armazenamento e visualização de dados de forma prática e escalável.
