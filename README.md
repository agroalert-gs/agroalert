# 🌱 AgroAlert — Monitoramento e Apoio ao Planejamento Agrícola

**Global Solution 2026.2 — CitizenTech | Engenharia de Software — FIAP**

O AgroAlert é um projeto tecnológico desenvolvido para auxiliar pequenos e médios produtores rurais na organização de informações sobre suas plantações e na conscientização sobre o uso responsável da água.

## 📋 Ficha da CitizenTech

| Campo | Descrição |
|---|---|
| **Nome da CitizenTech** | AgroAlert |
| **Cidade e região** | Mogi das Cruzes — região do Alto Tietê, São Paulo |
| **Cidadão beneficiado** | Pequenos e médios produtores rurais, especialmente produtores de hortaliças |
| **Problema** | A dificuldade de organizar informações agrícolas e acompanhar as condições do solo e do clima pode prejudicar o planejamento das plantações e o uso eficiente da água. |
| **Como funciona** | O projeto reúne uma plataforma web para apresentação e cadastro de informações, uma aplicação em Python para consulta de plantações e orientações de irrigação e uma simulação de sistema físico. |
| **O que cada parte faz** | A plataforma web apresenta o projeto e permite cadastrar e visualizar informações. O Python realiza cadastros, consultas e classificações de umidade. O Wokwi demonstra uma simulação de monitoramento físico. |
| **Repositório** | https://github.com/agroalert-gs/agroalert.git |
| **Indicador de impacto** | Potencial de redução do consumo de água na irrigação, avaliado inicialmente por cenários matemáticos hipotéticos. |
| **ODS conectados** | ODS 2, ODS 6 e ODS 13 |

## 🎯 Problema e objetivo

Pequenos e médios produtores rurais enfrentam desafios relacionados às mudanças climáticas, ao planejamento agrícola e à utilização adequada dos recursos hídricos.

A falta de informações organizadas pode dificultar a tomada de decisões sobre as plantações.

O AgroAlert busca oferecer uma solução simples e acessível para apoiar esses produtores, incentivando uma agricultura mais consciente e sustentável.

## 💻 Funcionalidades desenvolvidas

### Plataforma web — HTML, CSS e JavaScript

- Apresentação das principais informações do AgroAlert.
- Cadastro de informações agrícolas.
- Interface organizada e acessível para o usuário.

### Aplicação em Python

- Cadastro de plantações com nome, cidade, estado e tipo de cultivo.
- Consulta das plantações cadastradas.
- Classificação da umidade do solo em baixa, moderada ou alta.
- Orientações básicas de irrigação conforme o percentual informado.

### Simulação de sistema físico — Wokwi

- Simulação de um sistema de monitoramento agrícola.
- Demonstração do funcionamento de componentes eletrônicos e da lógica de monitoramento.
- Representação de uma possível aplicação futura de sensores no campo.

## 🛠️ Tecnologias utilizadas

- **HTML:** estrutura da plataforma web.
- **CSS:** estilização e apresentação visual.
- **JavaScript:** interatividade e funcionalidades de cadastro.
- **Python:** aplicação de terminal para gerenciamento de plantações e orientações.
- **Wokwi:** simulação do sistema físico.
- **GeoGebra:** modelagem matemática do consumo de água.
- **Git e GitHub:** organização e versionamento do projeto.

## 📊 Modelagem matemática

Para estudar o uso consciente da água na agricultura, desenvolvemos uma comparação entre dois cenários hipotéticos de consumo acumulado.

**Cenário convencional:**

\(f(x)=100x\)

**Cenário de consumo reduzido:**

\(g(x)=70x\)

Em que:

- \(x\) representa o tempo em dias.
- \(f(x)\) representa o consumo acumulado de água, em litros, no cenário convencional.
- \(g(x)\) representa o consumo acumulado de água, em litros, no cenário reduzido.

Após 10 dias:

- Consumo convencional: 1.000 litros.
- Consumo reduzido: 700 litros.
- Diferença: 300 litros, equivalente a 30%.

Os valores são ilustrativos e não representam resultados obtidos em testes reais.

## 🌎 Sustentabilidade e impacto social

O AgroAlert está relacionado aos seguintes Objetivos de Desenvolvimento Sustentável:

- **ODS 2 — Fome Zero e Agricultura Sustentável:** apoio à organização e ao planejamento da produção agrícola.
- **ODS 6 — Água Potável e Saneamento:** incentivo ao uso consciente da água.
- **ODS 13 — Ação Contra a Mudança Global do Clima:** conscientização sobre os desafios climáticos enfrentados pelos produtores.

## 🚀 Melhorias futuras

O AgroAlert é um protótipo acadêmico e poderá ser ampliado com:

- Integração de dados meteorológicos em tempo real.
- Alertas automáticos de chuva e condições climáticas.
- Integração com sensores físicos de umidade do solo.
- Recomendações mais específicas conforme o tipo de cultivo.
- Monitoramento contínuo das condições das plantações.
- Parcerias com cooperativas e produtores rurais.

## 👥 Integrantes

| Nome | RM |
|---|---|
| Beatriz Martin da Paz | 575399 |
| Luiz Gustavo dos Santos | 574689 |
| Maria Eduarda Basilio | 575711 |

## 📚 Contexto acadêmico

Projeto desenvolvido para a **Global Solution 2026.2 — CitizenTech**, do curso de Engenharia de Software da FIAP.

A proposta integra conhecimentos de desenvolvimento web, programação em Python, sistemas físicos, modelagem matemática, experiência do usuário e empreendedorismo.