# Dashboard de Casos de Dengue

Este projeto é um dashboard interativo desenvolvido em Dash (Python) para análise e previsão de casos de dengue no Brasil, com autenticação segura, logging de acessos e pronto para deploy em nuvem.

---

## 📦 Estrutura do Projeto

```
projeto-bigdatas2/
├── app.py               # Código principal do Dash/Flask
├── requirements.txt     # Dependências Python
├── Procfile             # Comando de start para deploy (Render)
├── README.md            # Este arquivo
├── RELATORIO.md         # Relatório técnico e gerencial
├── .gitignore           # Arquivos/pastas ignorados pelo Git
├── data/                # Dados CSV usados pelo app
│   ├── dados_agrupados.csv
│   ├── previsao_futura.csv
│   └── pdf_2024_exportado.csv
├── security/            # Autenticação e logging
│   └── auth.py
├── tests/               # Testes automatizados
│   └── test_auth.py
├── notebooks/           # Notebooks de preprocessamento/modelagem
│   └── preprocessing.ipynb
└── ...
```

---

## 🚀 Como executar localmente

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/mbeltrao01/Projeto_Big_Data.git
   cd Projeto_Big_Data
   ```
2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Garanta que os arquivos CSV estão em `data/`.**
4. **Execute o app:**
   ```sh
   python app.py
   ```
5. **Acesse:**
   - http://localhost:8050

---

## 🔒 Autenticação e Segurança
- Login com usuário e senha (hash seguro via werkzeug).
- Sessão protegida por Flask secret key (troque para variável de ambiente em produção).
- Logging de acessos para auditoria.
- Estrutura pronta para autenticação multifator (MFA).
- Usuários definidos em `security/auth.py`.

---

## 🧪 Testes Automatizados
- Testes básicos de autenticação em `tests/test_auth.py`.
- Para rodar:
  ```sh
  pip install pytest
  pytest
  ```
- Expanda os testes conforme desejar!

---

## 📊 Dados e Modelagem
- Dados processados em notebooks Jupyter e exportados para a pasta `data/`.
- Modelagem preditiva feita com Prophet.
- Dashboard permite filtrar por ano e dataset, visualizar gráficos e baixar CSVs.

---

## 📝 Documentação dos Arquivos
- **app.py**: Código principal. Define layout, callbacks, autenticação e rotas de download.
- **security/auth.py**: Funções de autenticação, hashing de senha e logging de acesso.
- **data/**: Contém os arquivos CSV usados no dashboard.
- **tests/**: Testes automatizados (pytest).
- **notebooks/**: Notebooks para análise e processamento dos dados.
- **Procfile**: Comando de start para deploy no Render.
- **requirements.txt**: Lista de dependências do projeto.

---

## 👥 Equipe
Projeto Big Data - Alexandre, Carla, Khyra, Mario e Sabrina

---

## 💡 Observações Finais
- Não suba arquivos CSV muito grandes (>100MB) para o GitHub.
- Para produção, proteja o secret key via variável de ambiente.
- Relatório técnico detalhado disponível em `RELATORIO.md`.
- Dúvidas ou sugestões? Abra uma issue!
