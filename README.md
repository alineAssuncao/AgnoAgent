# 🧠 Agno Agent

## 💡 Visão Geral

Este projeto foi desenvolvido como parte dos estudos do curso [Desenvolvimento de Agentes de IA: Do Zero ao Avançado](https://www.udemy.com/course/desenvolvimento-de-agentes-de-ia-do-zero-ao-avancado) na Udemy, ministrado por Rodrigo Macedo e Paulo Andrade, PhD.

O objetivo é criar um agente inteligente com lógica baseada em regras, utilizando uma estrutura simples, modular e extensível. O agente é capaz de interpretar comandos, tomar decisões e responder com base em um conjunto de regras definidas, sendo ideal para testes de raciocínio simbólico e comportamento adaptativo.

---

## 🧠 Arquitetura do Projeto

- `agent.py`: Lógica principal do agente  
- `rules.yaml`: Arquivo de regras configuráveis  
- `main.py`: Ponto de entrada para execução  
- `requirements.txt`: Dependências do projeto

O agente pode ser facilmente adaptado para novos contextos, bastando alterar ou expandir o conjunto de regras.

---

## 🛠️ Tecnologias Utilizadas

- `Python`  
- `YAML` para configuração de regras  
- `Agno` (estrutura personalizada de agente)  
- Opcional: `LangChain`, `LLMs`, `Streamlit` para integração futura

---

## 🚀 Primeiros Passos

### ✅ Pré-requisitos
- Python 3.7 ou superior
- pip instalado

### 📦 Instalação e Ambiente Virtual

Crie e ative o ambiente virtual com os comandos abaixo:

```bash
python -m venv .venv
```

No PowerShell (Windows):

```bash
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Executando o Projet

```bash
python main.py
```

> _O agente será iniciado e poderá processar comandos com base nas regras definidas em `rules.yaml`._

## ⚙️ Exemplo de Regras (`rules.yaml`)
```yaml
rules:

  - condition: "input contains 'risco'"
    
    response: "Cuidado! Este cenário envolve risco elevado."
    
  - condition: "input contains 'dados'"
    
    response: "Os dados estão sendo processados com segurança."
```

Você pode adicionar, remover ou modificar regras conforme o comportamento desejado.

## 📚 Aprendizados
- Criação de agentes com lógica baseada em regras
- Configuração modular com YAML
- Estruturação de agentes para testes e simulações
- Aplicação de conceitos de IA simbólica

## 🔮 Próximos Passos
- Integrar com LLMs para raciocínio híbrido
- Adicionar interface com Streamlit
- Criar agentes especializados com base em perfis de usuário
- Testar integração com CrewAI ou LangGraph

## 👩‍💻 Autora

Aline Assunção

Engenheira de Qualidade em transição para Inteligência Artificial

📫 [LinkedIn](https://www.linkedin.com/in/alineassuncaoai/)  

📬 aline.jassuncao@gmail.com

>_"Agentes inteligentes começam com regras simples — e evoluem com propósito."_
