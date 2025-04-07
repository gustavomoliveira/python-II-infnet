# Sistema de Caixa de Supermercado (Português-Br)

## Descrição
Sistema de gerenciamento de caixa de supermercado que permite o atendimento de clientes, controle de estoque e fechamento diário de caixa. O sistema possibilita cadastrar clientes e produtos, processar compras e emitir relatórios de vendas.

## Funcionalidades

- **Atendimento ao Cliente**: 
  - Busca de clientes cadastrados
  - Cadastro de novos clientes
  - Adição de produtos ao carrinho
  - Controle de estoque em tempo real

- **Gerenciamento de Estoque**:
  - Visualização de produtos sem estoque
  - Atualização automática após compras
  - Cadastro de novos produtos

- **Fechamento de Caixa**:
  - Relatório de vendas por cliente
  - Total de vendas
  - Relatório de produtos sem estoque

## Requisitos

- Python 3.x
- MySQL
- Bibliotecas Python:
  - mysql-connector
  - tabulate
  - pandas

## Configuração

1. Clone o repositório
2. Crie um banco de dados MySQL usando o script `script_mercado.sql`
3. Ajuste as configurações de conexão no arquivo `conectar_bd.py`
4. Certifique-se de ter os arquivos CSV necessários na pasta CSV:
   - produtos.csv
   - clientes.csv

## Estrutura do Projeto

- **CRUD**: Módulos para operações de banco de dados
- **CRUD_BD**: Módulos de acesso direto ao banco de dados
- **UTIL**: Funções utilitárias e de gerenciamento
- **CSV**: Arquivos de dados iniciais

## Como Usar

1. Execute o arquivo `caixa.py` para iniciar o sistema
2. Escolha uma das opções do menu:
   - [1] - Iniciar Atendimento
   - [2] - Exibir Estoque
   - [0] - Fechar Caixa

## Fluxo de Atendimento

1. Busca ou cadastro de cliente
2. Adição de produtos ao pedido
3. Atualização do estoque após finalização
4. Emissão de nota fiscal com detalhes da compra

## Notas para Desenvolvimento

- O formato dos nomes deve seguir o padrão: 7 letras + espaço + números
- Os dados iniciais são carregados automaticamente na primeira execução
- A atualização do estoque é feita em lote ao finalizar o atendimento

# Supermarket Checkout System (English)

## Description
A supermarket checkout management system that enables customer service, inventory control, and daily cash register closing. The system allows for registering customers and products, processing purchases, and generating sales reports.

## Features

- **Customer Service**: 
  - Search for registered customers
  - Register new customers
  - Add products to cart
  - Real-time inventory control

- **Inventory Management**:
  - View out-of-stock products
  - Automatic updates after purchases
  - Register new products

- **Cash Register Closing**:
  - Sales report by customer
  - Total sales
  - Out-of-stock products report

## Requirements

- Python 3.x
- MySQL
- Python Libraries:
  - mysql-connector
  - tabulate
  - pandas

## Setup

1. Clone the repository
2. Create a MySQL database using the `script_mercado.sql` script
3. Adjust the connection settings in the `conectar_bd.py` file
4. Make sure you have the necessary CSV files in the CSV folder:
   - produtos.csv (products)
   - clientes.csv (customers)

## Project Structure

- **CRUD**: Modules for database operations
- **CRUD_BD**: Direct database access modules
- **UTIL**: Utility and management functions
- **CSV**: Initial data files

## How to Use

1. Run the `caixa.py` file to start the system
2. Choose one of the menu options:
   - [1] - Start Customer Service
   - [2] - Display Inventory
   - [0] - Close Cash Register

## Service Flow

1. Search for or register a customer
2. Add products to the order
3. Update inventory after completion
4. Issue receipt with purchase details

## Development Notes

- Names must follow the pattern: 7 letters + space + numbers
- Initial data is automatically loaded on first execution
- Inventory updates are processed in batch when finalizing service