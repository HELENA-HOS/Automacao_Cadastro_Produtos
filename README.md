# Automação de Cadastro de Produtos

Este projeto foi desenvolvido com o objetivo de aprimorar minhas habilidades em automação de processos, manipulação de dados e integração de ferramentas Python. Ele automatiza o cadastro de produtos em um sistema web, utilizando as bibliotecas PyAutoGUI e pandas, e serve como um exemplo prático de aplicação de automação para ganho de produtividade.

## Sobre o Projeto

A automação de tarefas repetitivas é uma competência cada vez mais valorizada no mercado de tecnologia. Este projeto demonstra minha capacidade de:

- Analisar um processo manual e propor uma solução automatizada;
- Integrar diferentes bibliotecas Python para resolver um problema real;
- Trabalhar com manipulação de arquivos e dados estruturados (CSV);
- Utilizar técnicas de automação de interface gráfica para interagir com sistemas legados ou sem API pública.

## Funcionalidades

- Abertura automática do navegador e navegação até o sistema de cadastro.
- Login automatizado com credenciais parametrizáveis.
- Leitura e processamento de uma base de dados de produtos em formato CSV.
- Preenchimento automático do formulário de cadastro para cada produto.
- Execução repetida do processo até o cadastro de todos os itens.

## Habilidades Desenvolvidas

- **Automação de interface gráfica** com PyAutoGUI;
- **Manipulação de dados** com pandas;
- **Leitura e escrita de arquivos CSV**;
- **Controle de fluxo e tratamento de exceções** em Python;
- **Documentação e organização de código** para reprodutibilidade e manutenção.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `pyautogui`
  - `pandas`
- Navegador Microsoft Edge instalado
- Arquivo `produtos.csv` no mesmo diretório do script principal

Instale as dependências com:
```bash
pip install pyautogui pandas
```

## Como Executar

1. **Ajuste as posições do mouse:**  
   Use o script `posicao_cursor.py` para identificar as coordenadas dos campos do formulário no seu sistema. Atualize as coordenadas no script principal (`codigo.py`) conforme necessário.

2. **Configure as credenciais:**  
   No arquivo `codigo.py`, ajuste as variáveis `email` e `senha` com as credenciais de acesso ao sistema.

3. **Prepare o arquivo CSV:**  
   Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório do script e segue o formato esperado.

4. **Execute o script principal:**  
   ```bash
   python codigo.py
   ```

## Estrutura dos Arquivos

- `codigo.py`: Script principal de automação.
- `posicao_cursor.py`: Script auxiliar para identificar coordenadas do mouse.
- `produtos.csv`: Base de dados dos produtos a serem cadastrados.

## Exemplo de produtos.csv

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
CAHA000252,Hashtag,Camisa,2,25.00,11.00,Conferir estoque
```

## Aprendizados

Este é um projeto acadêmico desenvolvido para fins de estudo e aprimoramento profissional. Durante o desenvolvimento deste projeto, aprofundei meus conhecimentos em:

- Automação de tarefas utilizando Python e a biblioteca PyAutoGUI;
- Manipulação e leitura de dados estruturados com pandas;
- Organização e documentação de código para facilitar a manutenção e reprodutibilidade;
- Integração de diferentes ferramentas para resolver problemas reais de produtividade.