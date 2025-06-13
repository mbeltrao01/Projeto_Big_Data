# Relatório Técnico e Gerencial

## 1. Metodologia
O pipeline do projeto segue as melhores práticas de ciência de dados, integrando preprocessamento, modelagem, validação e visualização:

- **Coleta e Preprocessamento:**
    - Dados históricos de casos de dengue são coletados de fontes públicas e armazenados em CSV.
    - Realizamos limpeza, tratamento de valores ausentes e agregação temporal nos notebooks Jupyter.
    - Os dados são exportados para a pasta `data/` para uso no dashboard.
- **Modelagem Preditiva:**
    - Utilizamos o Prophet para previsão de séries temporais dos casos de dengue.
    - O modelo é treinado e avaliado em notebooks, com métricas como RMSE e MAE.
    - As previsões futuras são salvas em arquivos CSV específicos.
- **Visualização e Dashboard:**
    - O dashboard foi desenvolvido em Dash, permitindo filtros dinâmicos por ano e dataset.
    - Gráficos interativos (Plotly) e botões para download dos dados facilitam a análise.
    - O layout foi pensado para ser responsivo e intuitivo.

## 2. Segurança Aplicada
- **Autenticação:**
    - Login protegido por senha, com hash seguro usando `werkzeug.security`.
    - Usuários definidos em código, evitando exposição de credenciais.
- **Sessão e Segredos:**
    - Sessão Flask protegida por secret key (recomendado usar variável de ambiente em produção).
- **Logging e Auditoria:**
    - Todos os acessos são registrados em `access.log` para rastreabilidade.
- **Boas práticas:**
    - MFA preparado para implementação futura.
    - Arquivos sensíveis e grandes são ignorados pelo Git.
    - Recomenda-se rodar o app sempre em ambiente virtual isolado.

## 3. Qualidade Obtida
- **Validação dos Dados:**
    - Checagem de integridade e consistência nos notebooks.
    - Dados filtrados e agregados por ano para evitar distorções.
- **Métricas de Modelagem:**
    - Prophet avaliado por RMSE/MAE; resultados documentados.
- **Testes:**
    - Testes automatizados de autenticação garantem robustez do login.
    - Testes manuais do fluxo de dashboard e downloads.
- **Interface:**
    - Sem erros críticos de callback.
    - Layout responsivo, com feedback visual para login/logout.

## 4. Resultados Alcançados
- **Dashboard online:** https://projeto-big-data.onrender.com/
- Visualização clara das previsões e dados reais de dengue.
- Filtros dinâmicos por ano/dataset, exportação de CSV.
- Controle de acesso e logging funcionando.

## 5. Lições Aprendidas
- Importância do controle de versão para dados e código.
- Necessidade de ignorar arquivos grandes/sensíveis no Git.
- Facilidade de deploy com Render.com e Procfile.
- Valor de testes automatizados mesmo em projetos pequenos.
- Cuidados extras ao usar autenticação/sessão em apps Dash.

## 6. Referências
- [Dash Documentation](https://dash.plotly.com/)
- [Prophet Forecasting](https://facebook.github.io/prophet/)
- [Render.com Docs](https://render.com/docs)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/)
- [Python Logging](https://docs.python.org/3/library/logging.html)

---

## 7. Equipe
Projeto Big Data - Alexandre, Carla, Khyra, Mario e Sabrina
