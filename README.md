# 🧠 Monitor de Rede Neural

> IA para detecção de anomalias em tráfego de rede usando Machine Learning

Este projeto tem como objetivo analisar pacotes de rede e identificar comportamentos anômalos em uma rede local, utilizando algoritmos de machine learning. Ele foi criado no contexto de estudos práticos em Cibersegurança, com foco em coleta, processamento e análise de tráfego de rede.

---

## 📁 Estrutura do Projeto

```
MonitorRedeNeural/
├── capturas/              # Arquivos .pcap capturados com o tshark
├── dataset/               # Arquivos CSV extraídos dos pacotes
├── imagens/               # Screenshots do processo
├── modelos/               # Modelos de ML treinados (futuramente)
├── scripts/               # Scripts Python de pré-processamento e análise
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

---

## ⚙️ Requisitos

- Python 3.10+
- pandas

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧪 Etapas do Projeto

1. **Captura de tráfego com tshark**
   - Pacotes de tráfego normal e anômalo foram salvos como `.pcap` em `capturas/`

2. **Extração de dados com tshark para CSV**
   - Convertido para CSV com campos como: `frame.time_relative`, `ip.src`, `ip.dst`, `frame.len`, `ip.proto`

3. **Pré-processamento com Python (scripts/preprocessa_csv.py)**
   - Combina dados normais e anômalos
   - Adiciona coluna de `label`
   - Salva em `dataset/dados_final.csv`

4. **Análise Exploratória (scripts/analisa_csv.py)**
   - Mostra as 5 primeiras linhas
   - Verifica valores ausentes
   - Estatísticas descritivas

---

## 📊 Exemplo de Saída

```
Primeiras linhas do dataset:
   frame.time_relative    ip.src       ip.dst   frame.len   ip.proto   label
0          1.23456789   10.0.0.1    10.0.0.2     60          6         normal

Contagem de rótulos:
normal       8995
anomalous       4

Estatísticas descritivas:
                 frame.time_relative   frame.len     ip.proto
count                  8999.000000   8999.000000   8975.00000
mean                     12.29...    1759.05...     13.66...
```

---

## 🚀 Futuras melhorias

- Treinar modelos (Decision Tree, Random Forest, Isolation Forest)
- Adicionar interface com Streamlit ou Dash
- Classificação em tempo real com socket ou scapy

---

## 🧑‍💻 Autor

**Roger**  
Estudante de Cibersegurança | Projetos práticos com Python, redes e segurança ofensiva.  
[GitHub](https://github.com/) | [LinkedIn](https://linkedin.com)

---

> "Segurança não é um produto, é um processo." – Bruce Schneier