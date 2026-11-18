# AgroAlert — Sistema de Monitoramento Agrícola

## Sobre o projeto

O AgroAlert é um projeto desenvolvido para a Global Solution 2026.2 da FIAP, com o objetivo de auxiliar produtores rurais no acompanhamento das plantações e na conscientização sobre o uso responsável da água.

A aplicação em Python funciona pelo terminal e permite cadastrar plantações, consultar informações cadastradas, verificar níveis de umidade do solo e receber orientações básicas de irrigação.

## Funcionalidades

1. **Cadastrar plantação:** registra nome, cidade, estado e tipo de cultivo.
2. **Consultar plantações:** apresenta os cadastros realizados durante a execução.
3. **Verificar umidade do solo:** classifica o percentual informado como baixo, moderado ou alto.
4. **Orientações de irrigação:** apresenta recomendações conforme a umidade informada.
5. **Sair:** encerra o sistema.

## Tecnologias utilizadas

- Python 3.10 ou superior
- Biblioteca padrão `os` para limpeza do terminal no Windows

## Como executar

1. Ter o Python 3.10 ou superior instalado.
2. Abrir o terminal na pasta que contém o arquivo `main.py`.
3. Executar o comando `python main.py`.
4. Selecionar uma das opções do menu.

## Regras de umidade

- Abaixo de 30%: umidade baixa.
- De 30% até 70%: umidade moderada.
- Acima de 70%: umidade alta.

As faixas são ilustrativas e utilizadas para fins acadêmicos.

## Integrantes

| Nome | RM |
|---|---|
| Beatriz Martin da Paz | 575399 |
| Luiz Gustavo dos Santos | 574689 |
| Maria Eduarda Basilio | 575711 |

## Contexto acadêmico

Global Solution 2026.2 — CitizenTech  
Engenharia de Software — FIAP