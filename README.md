# ✈️ Sentiment Analyses of Tweets about US Airlines

Dashboard interativo em **Streamlit** para explorar e analisar sentimentos de tweets relacionados a companhias aéreas dos EUA. A aplicação permite visualizar a distribuição de sentimentos, localização geográfica dos tweets, comparações entre companhias aéreas e nuvens de palavras por sentimento.

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Base de dados](#-base-de-dados)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como executar](#-como-executar)
- [Tema e customização](#-tema-e-customização)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Possíveis melhorias](#-possíveis-melhorias)

## 📖 Sobre o projeto

Este projeto utiliza o dataset **Twitter US Airline Sentiment**, contendo tweets de usuários sobre as principais companhias aéreas americanas (American, Delta, Southwest, United, US Airways e Virgin America), classificados como `positive`, `neutral` ou `negative`.

A aplicação oferece um painel lateral (sidebar) com diversos filtros e opções de visualização, permitindo que o usuário explore os dados de forma interativa sem precisar escrever código.

## ✨ Funcionalidades

O dashboard é composto pelos seguintes recursos, acessíveis pela barra lateral:

1. **Tweet aleatório por sentimento** — exibe um tweet aleatório de acordo com o sentimento selecionado (`positive`, `neutral` ou `negative`).
2. **Número de tweets por sentimento** — gráfico de barras ou gráfico de pizza (donut) mostrando a quantidade total de tweets por categoria de sentimento.
3. **Quando e onde os usuários estão tweetando** — mapa interativo com a localização geográfica dos tweets filtrados por hora do dia (0–23h), com opção de exibir os dados brutos.
4. **Total de tweets por companhia aérea** — gráfico de barras horizontal ou gráfico de pizza com o volume de tweets por companhia.
5. **Detalhamento por companhia e sentimento** — histograma comparando múltiplas companhias aéreas selecionadas, separado por sentimento.
6. **Nuvem de palavras (Word Cloud)** — gera uma nuvem de palavras a partir do texto dos tweets filtrados por sentimento (positivo, neutro ou negativo), removendo menções (`@usuário`), links (`http`) e retweets (`RT`).

## 🗂 Estrutura do projeto

```
.
├── app.py                # Código principal da aplicação Streamlit
├── Tweets.csv             # Base de dados com os tweets
├── config.toml             # Arquivo de tema/configuração visual do Streamlit
└── requirements.txt        # Dependências do projeto
```

> **Importante:** o arquivo `config.toml` deve ficar dentro de uma pasta `.streamlit/` na raiz do projeto para que o Streamlit aplique o tema automaticamente (veja a seção [Tema e customização](#-tema-e-customização)).

## 🗃 Base de dados

O arquivo `Tweets.csv` contém, entre outras, as seguintes colunas utilizadas pela aplicação:

| Coluna | Descrição |
|---|---|
| `tweet_id` | Identificador único do tweet |
| `airline_sentiment` | Sentimento do tweet (`positive`, `neutral`, `negative`) |
| `airline_sentiment_confidence` | Grau de confiança da classificação do sentimento |
| `negativereason` | Motivo do sentimento negativo (quando aplicável) |
| `airline` | Companhia aérea mencionada |
| `name` | Nome de usuário do autor do tweet |
| `retweet_count` | Número de retweets |
| `text` | Texto do tweet |
| `tweet_created` | Data e hora de criação do tweet |
| `latitude` / `longitude` | Coordenadas geográficas associadas ao tweet |

## ✅ Pré-requisitos

- Python 3.8 ou superior
- pip

## ⚙️ Instalação

1. Clone ou baixe este repositório.
2. (Recomendado) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Dependências (`requirements.txt`)

```
streamlit
plotly
wordcloud
matplotlib
```

> Observação: `pandas` e `numpy` também são utilizados pela aplicação (importados em `app.py`). Caso não estejam instalados como dependências de `streamlit`/`plotly`, adicione-os manualmente:
> ```bash
> pip install pandas numpy
> ```

## ▶️ Como executar

Certifique-se de que o arquivo `Tweets.csv` está no mesmo diretório do `app.py` (o código carrega os dados a partir de `Data_URL = 'Tweets.csv'`, um caminho relativo).

Execute o comando:

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador, geralmente em `http://localhost:8501`.

## 🎨 Tema e customização

O arquivo `config.toml` define a paleta de cores e a fonte utilizadas no dashboard (tons de verde e bege). Para que o Streamlit reconheça essas configurações, mova o arquivo para dentro da pasta `.streamlit/`:

```
.streamlit/
└── config.toml
```

Estrutura final esperada:

```
.
├── .streamlit/
│   └── config.toml
├── app.py
├── Tweets.csv
└── requirements.txt
```

## 🛠 Tecnologias utilizadas

- [Streamlit](https://streamlit.io/) — construção do dashboard interativo
- [Pandas](https://pandas.pydata.org/) — manipulação e análise dos dados
- [Plotly Express](https://plotly.com/python/plotly-express/) — gráficos interativos (barras, pizza, histograma)
- [WordCloud](https://github.com/amueller/word_cloud) — geração de nuvens de palavras
- [Matplotlib](https://matplotlib.org/) — renderização da nuvem de palavras

Projeto baseado no dataset **Twitter US Airline Sentiment** para fins de estudo e demonstração de dashboards interativos com Streamlit.
