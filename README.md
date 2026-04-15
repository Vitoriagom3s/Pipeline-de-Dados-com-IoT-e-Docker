# 📊 Pipeline de Dados IoT com Python, PostgreSQL e Streamlit

## 📌 Descrição do Projeto

Este projeto tem como objetivo desenvolver um pipeline completo de dados IoT, simulando a coleta, processamento, armazenamento e visualização de dados de sensores de temperatura.

A solução integra diferentes tecnologias para demonstrar um fluxo de dados desde a ingestão até a geração de insights por meio de um dashboard interativo.

---

## 🚀 Tecnologias Utilizadas

* Python
* PostgreSQL
* Streamlit
* SQLAlchemy
* Pandas
* Docker
* Supabase (como alternativa em nuvem)

---

## ⚙️ Estrutura do Projeto

```
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
├── README.md
└── requirements.txt
```

---

## 🔄 Pipeline de Dados

1. **Coleta de Dados**
   Os dados são simulados através de um arquivo CSV contendo:

   * device_id
   * temperature
   * timestamp

2. **Ingestão de Dados**
   O script `load_data.py` realiza a leitura do CSV e envia os dados para o banco PostgreSQL.

3. **Processamento (SQL)**
   Foram criadas 3 views para análise:

   * Média de temperatura por dispositivo
   * Quantidade de registros por hora
   * Temperatura máxima e mínima por dia

4. **Visualização**
   O dashboard foi desenvolvido com Streamlit, exibindo gráficos interativos.

---

## 🗄️ Banco de Dados

Durante o desenvolvimento, a arquitetura foi planejada para execução local com Docker.
Devido a limitações de virtualização, foi utilizada a plataforma Supabase para hospedar o banco PostgreSQL na nuvem, mantendo toda a lógica do projeto.

---

## 📊 Views SQL

### 🔹 Média de temperatura por dispositivo

```sql
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;
```

### 🔹 Registros por hora

```sql
SELECT EXTRACT(HOUR FROM timestamp::timestamp) as hora, COUNT(*) as total
FROM temperature_readings
GROUP BY hora;
```

### 🔹 Temperatura máxima e mínima por dia

```sql
SELECT DATE(timestamp::timestamp) as data,
MAX(temperature) as max_temp,
MIN(temperature) as min_temp
FROM temperature_readings
GROUP BY data;
```

---

## ▶️ Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar conexão com banco

Editar a string de conexão nos arquivos Python com suas credenciais do banco.

---

### 3. Carregar os dados

```bash
python src/load_data.py
```

---

### 4. Executar o dashboard

```bash
cd dashboard
python -m streamlit run dashboard.py
```

---

## 📈 Resultados

O dashboard apresenta:

* Média de temperatura por dispositivo
* Volume de dados por hora
* Variação de temperatura ao longo dos dias

---

## 💡 Insights

* Diferenças de comportamento entre dispositivos
* Identificação de horários com maior volume de dados
* Variações térmicas ao longo do tempo

---

## 🌍 Aplicações Reais

Este projeto pode ser aplicado em:

* Monitoramento industrial
* Cidades inteligentes
* Controle ambiental
* IoT em agricultura

---

## 📸 Demonstração

<img width="1909" height="1013" alt="Captura de tela 2026-04-14 221819" src="https://github.com/user-attachments/assets/d6ded24a-ef8e-4275-a41b-fae29f6a2010" />

<img width="693" height="924" alt="imagem geral10" src="https://github.com/user-attachments/assets/6b20dd3e-083f-4641-9d41-de6f76b7945a" />

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos na disciplina de
**Disruptive Architectures: IoT, Big Data e IA**
- Adoraria receber dicas: viviamorimgomes0@gmail.com
---
