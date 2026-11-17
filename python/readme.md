# AgroAlert — Sistema de Monitoramento Agrícola

## Sobre o projeto

O AgroAlert é um projeto desenvolvido para a Global Solution 2026.2 da FIAP, com o objetivo de auxiliar produtores rurais no acompanhamento das plantações e na conscientização sobre o uso responsável da água.

Esta aplicação em Python funciona pelo terminal e permite cadastrar plantações, consultar os dados cadastrados, verificar níveis de umidade do solo e receber orientações básicas de irrigação.

## Funcionalidades

1. **Cadastrar plantação:** registra nome, cidade, estado e tipo de cultivo.
2. **Consultar plantações:** apresenta as plantações cadastradas durante a execução.
3. **Verificar umidade do solo:** classifica o percentual informado como baixo, moderado ou alto.
4. **Orientações de irrigação:** apresenta recomendações de acordo com a umidade informada.
5. **Sair:** encerra o sistema.

## Tecnologias utilizadas

- Python 3
- Biblioteca padrão `os`, para limpeza do terminal no Windows

## Como executar

1. Ter o Python 3.10 ou superior instalado.
2. Abrir o terminal na pasta que contém o arquivo `main.py`.
3. Executar o comando:

   `python main.py`

4. Escolher uma das opções apresentadas no menu.

## Regras de umidade utilizadas

- Abaixo de 30%: umidade baixa.
- De 30% até 70%: umidade moderada.
- Acima de 70%: umidade alta.

Essas faixas são ilustrativas e utilizadas para fins acadêmicos. Não substituem uma avaliação técnica das necessidades de cada cultivo.

## Limitações

- Os dados das plantações são armazenados temporariamente em memória e são perdidos quando o programa é encerrado.
- Os valores de umidade são informados manualmente, simulando uma leitura de sensor.
- A entrada de letras nos campos numéricos de umidade não possui tratamento específico.
- A limpeza do terminal utiliza o comando `cls`, voltado ao ambiente Windows.

## Contexto acadêmico

Projeto desenvolvido para a Global Solution 2026.2 — CitizenTech, no curso de Engenharia de Software da FIAP.

## Integrantes da equipe

| Nome completo | RM |
|---|---|
| Beatriz Martin da Paz | 575399 |
| Luiz Gustavo dos Santos | 574689 |
| Maria Eduarda Basilio | 575711 |