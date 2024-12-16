# File System Analysis

## Descrição
O **File System Analysis** é um software desenvolvido em Python para realizar buscas avançadas por palavras-chave em uma série de documentos armazenados em sistemas de arquivos. Ele utiliza uma integração com o **Gemini** para interpretar e contextualizar os resultados, proporcionando insights mais detalhados e relevantes.

---

## Funcionalidades
- Busca por palavras-chave em múltiplos documentos;
- Suporte a diversos formatos de arquivos (TXT, PDF, DOCX, etc.);
- Análise contextual dos resultados utilizando **Gemini**;
- Interface simples e eficiente para configuração e uso;
- Resultados organizados e exportáveis para outros formatos (CSV, JSON).

---

## Como Funciona
1. **Entrada:** O usuário fornece o diretório de busca e as palavras-chave desejadas.
2. **Processamento:** O software percorre os documentos do diretório indicado, realiza a busca e coleta as informações relevantes.
3. **Interpretação:** Os resultados são analisados com auxílio do **Gemini**, fornecendo contexto e insights.
4. **Saída:** Os resultados são apresentados em formato estruturado, com opções de exportação.
   
<img width="830" alt="FluxogramaProcessos" src="https://github.com/user-attachments/assets/9ddcdd00-c051-49a9-be4b-633f2753d7ce" />

---

## Requisitos
- Python 3.8 ou superior;
- Pacotes necessários (especificados no `requirements.txt`);
- Conta configurada no **Gemini** para integração.

---

## Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/file-system-analysis.git](https://github.com/rodrigomendes47/system-file-analysis.git)
