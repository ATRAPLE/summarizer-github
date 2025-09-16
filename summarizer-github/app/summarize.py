from typing import List

def summarize_chunks(chunks: List[str]) -> str:
    if len(chunks) == 1:
        # Apenas um chunk: retorna o texto sem resumir
        return chunks[0]
    else:
        # Mais de um chunk: consolida (une) as informações sem resumir
        return "\n\n".join(chunks)
