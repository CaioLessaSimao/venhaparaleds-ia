# Lerpdf Crew

Bem-vindo ao projeto Lerpdf Crew, desenvolvido com o [crewAI](https://crewai.com). Este template foi criado para ajudá-lo a configurar um sistema de IA multiagente com facilidade, aproveitando o poderoso e flexível framework fornecido pelo crewAI. Nosso objetivo é permitir que seus agentes colaborem de forma eficaz em tarefas complexas, maximizando sua inteligência coletiva e capacidades.

## Instalação

Certifique-se de ter o Python >=3.10 <=3.13 instalado em seu sistema. Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciamento de dependências e pacotes, proporcionando uma experiência de configuração e execução fluida.

Primeiro, caso ainda não tenha instalado o Poetry, instale-o com o seguinte comando:

```bash
pip install poetry
```

Em seguida, navegue até o diretório do projeto e instale as dependências:

1. Primeiro, bloqueie as dependências e depois instale-as:

```bash
poetry lock
```

```bash
poetry install
```

### Estrutura do projeto

O projeto é composto por três arquivos principais:

1. **`crew.py`** - Define os agentes, tarefas e a equipe.
2. **`agents.yaml`** - Configura os agentes e suas funções.
3. **`task.yaml`** - Define as tarefas que os agentes executarão.

## Dependências

- `CrewAI`
- `Langchain`
- `Google Generative AI`
- `yaml`
- `os`
- `lerpdf.tools.custom_tool` (Ferramenta personalizada para leitura de PDF)

## Compreendendo sua Equipe

O Lerpdf Crew é composto por vários agentes de IA, cada um com funções, objetivos e ferramentas específicas. Esses agentes colaboram em uma série de tarefas, definidas no arquivo `config/tasks.yaml`, aproveitando suas habilidades coletivas para atingir objetivos complexos. O arquivo `config/agents.yaml` descreve as capacidades e configurações de cada agente da equipe.

## Configuração dos Agentes

Os agentes estão definidos no arquivo `agents.yaml` e são criados em `crew.py` com a decoração `@agent`. Cada agente tem um papel específico:

### `pdf_reader_agent`

- **Função:** Extrai texto de arquivos PDF.
- **Ferramenta utilizada:** `PDFReaderTool`

### `analysis_agent`

- **Função:** Identifica os pontos-chave do texto extraído.

### `sumary_agent`

- **Função:** Gera um resumo informativo do texto filtrado.

### `blog_agent`

- **Função:** Formata o resumo para que possa ser postado em um blog.

## Configuração das Tarefas

As tarefas estão definidas em `tasks.yaml` e são implementadas em `crew.py` com a decoração `@task`. Cada tarefa está associada a um agente específico.

### `extraction_task`

- **Descrição:** Extrai o texto de arquivos PDF localizados em `{pasta_pdf}`.
- **Agente:** `pdf_reader_agent`
- **Saída esperada:** Texto extraído do PDF.

### `analysis_task`

- **Descrição:** Identifica os pontos-chave do texto extraído.
- **Agente:** `analysis_agent`
- **Saída esperada:** Pontos-chave extraídos do texto.

### `sumarize_task`

- **Descrição:** Gera um resumo do texto filtrado.
- **Agente:** `sumary_agent`
- **Saída esperada:** Um resumo conciso.

### `blog_task`

- **Descrição:** Formata o resumo para publicação em um blog, incluindo título, subtítulos e conclusão.
- **Agente:** `blog_agent`
- **Saída esperada:** Texto formatado para blog.

## Executando o Projeto

**Adicione sua ****`GOOGLE_API_KEY`**** ao arquivo ****`.env`**

Para iniciar sua equipe de agentes de IA e começar a execução das tarefas, execute o seguinte comando na raiz do projeto:

```bash
poetry run lerpdf
```

Este comando inicializa o Lerpdf Crew, reunindo os agentes e atribuindo-lhes tarefas conforme definido na sua configuração.

Este exemplo, sem modificações, gerará um arquivo `report.md` na raiz do projeto com o resultado de uma pesquisa sobre LLMs.

