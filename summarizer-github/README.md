# Summarizer OSS

Sistema de sumarização offline de PDFs, inspirado no pdf-offline-summarizer-nodocker, com melhorias:

- Suporte aos modelos: gpt-oss:20b, gpt-oss:120b, qwen3:30b, qwen3:235b
- Se houver apenas um chunk, retorna o texto do chunk sem resumir
- Se houver mais de um chunk, consolida as informações sem resumir, apenas unindo os chunks

## Como rodar

1. Instale as dependências: `pip install -r requirements.txt`
2. Execute: `python app/main.py`
