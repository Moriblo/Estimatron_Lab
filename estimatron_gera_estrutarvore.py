"""
╭────────────────────────────────────────────────────────────╮
│                                                            │
│   Estimatron — Gerador Visual de Estrutura de Diretórios   │
│                                                            │
│   Percorre todo o projeto e gera uma árvore estilizada     │
│   com pseudografias, emojis por tipo, e comentários.       │
│   Ignora arquivos e pastas conforme padrões do .gitignore, │
│   inclusive diretórios e arquivos com curinga.             │
│                                                            │
│   Saída gerada: docs/estrutura_formatada.md                │
│   Autor: MOACYR & Copilot • Atualizado: 2025-07-16         │
╰────────────────────────────────────────────────────────────╯
"""

import os
import fnmatch
from pathlib import Path

# Emojis para pastas conhecidas
EMOJI_PASTA = {
    'tests': '🧪', 'modules': '🧠', 'docs': '📚', 'venv': '🐍', 'arquivos': '🗂️',
    'htmlcov': '📊', '.vscode': '🔧', '.pytest_cache': '🚫'
}

# Emojis para tipos de arquivos por extensão
EMOJI_ARQUIVO = {
    '.py': '⚗️', '.xml': '🧾', '.xsd': '🧾', '.md': '📄', '.txt': '📄', '.json': '🧷',
    '.bat': '📦', '.cfg': '🧩', '.html': '🌐', '.css': '🎨', '.js': '🧠',
    '.png': '🖼️', '.jpg': '🖼️', '.jpeg': '🖼️', '.gif': '🖼️', '.pdf': '🖼️',
    '.pyc': '📄', '.log': '🧻', '.db': '🗃️'
}

# Comentários para itens específicos da estrutura
COMENTARIOS = {
    'tests': '# Testes unitários com dados sintéticos',
    'modelo_xml_curto.xml': '# Modelo UML simplificado para teste de LOC',
    'xsd_simples.xsd': '# Schema com baixa complexidade (<10)',
    'main.py': '# Interface Streamlit com entrada manual ou via config.json',
    'requirements.txt': '# Dependências principais para rodar o Estimatron',
    'requirements-dev.txt': '# Ferramentas extras para testes e qualidade de código',
    'docs': '# Documentação técnica e estrutura gerada',
    'htmlcov': '# Relatórios de cobertura de testes em HTML',
    'modules': '# Módulos funcionais do sistema',
    '.vscode': '# Configurações internas do editor',
    'CHANGELOG.md': '# Log de Features e Releases',
    'estimatron_gera_estrutarvore.py': '# Geração da estrutura de pastas',
}

def ler_gitignore():
    """
    Lê os padrões definidos no .gitignore.
    Retorna um conjunto de strings limpas (sem comentários).
    """
    ignorados = set()
    caminho = Path('.gitignore')
    if caminho.exists():
        with caminho.open(encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha and not linha.startswith('#'):
                    ignorados.add(linha)
    return ignorados

def deve_ignorar(caminho_relativo, ignorados):
    """
    Verifica se o caminho atual deve ser ignorado com base nos padrões.
    Compatível com curinga, diretórios e nomes exatos.
    """
    caminho_relativo = caminho_relativo.replace("\\", "/")
    partes = caminho_relativo.split("/")

    for padrao in ignorados:
        padrao = padrao.strip().replace("\\", "/")
        if not padrao:
            continue

        # Padrões de diretório (com barra final)
        if padrao.endswith("/"):
            if caminho_relativo.startswith(padrao) or partes[0] == padrao.rstrip("/"):
                return True

        # Padrões com curinga ou nomes simples
        if fnmatch.fnmatch(caminho_relativo, padrao) or fnmatch.fnmatch(os.path.basename(caminho_relativo), padrao):
            return True

    return False

def listar(caminho, prefixo='', saida=[], ignorados=[], permitir_ocultos=set()):
    """
    Percorre os diretórios aplicando filtros e gera visual com emojis e comentários.
    """
    try:
        itens = sorted(os.listdir(caminho))
    except PermissionError:
        return saida

    for i, nome in enumerate(itens):
        caminho_completo = os.path.join(caminho, nome)
        caminho_relativo = os.path.relpath(caminho_completo, start='.')

        if nome.startswith('.') and nome not in permitir_ocultos:
            continue
        if deve_ignorar(caminho_relativo, ignorados):
            continue

        eh_ultimo = (i == len(itens) - 1)
        marcador = '└──' if eh_ultimo else '├──'
        proximo_prefixo = prefixo + ('    ' if eh_ultimo else '│   ')
        comentario = COMENTARIOS.get(nome, '')

        if os.path.isdir(caminho_completo):
            emoji = EMOJI_PASTA.get(nome, '📁')
            linha = f"{prefixo}{marcador} {emoji} {nome}/ {comentario}".rstrip()
            saida.append(linha)
            listar(caminho_completo, proximo_prefixo, saida, ignorados, permitir_ocultos)
        else:
            ext = os.path.splitext(nome)[1].lower()
            emoji = EMOJI_ARQUIVO.get(ext, '📄')
            linha = f"{prefixo}{marcador} {emoji} {nome} {comentario}".rstrip()
            saida.append(linha)

    return saida

def gerar_arquivo():
    """
    Executa a geração automática do arquivo Markdown da estrutura do projeto.
    Cria docs/estrutura_de_pastas.md com árvore visual estilizada.
    """
    os.makedirs('docs', exist_ok=True)
    ignorados = ler_gitignore()
    permitir_ocultos = {'.vscode'}  # Exceções permitidas

    estrutura = ["## 📁 Estrutura de Pastas do Projeto Estimatron\n"]
    estrutura += listar('.', ignorados=ignorados, permitir_ocultos=permitir_ocultos)

    destino = os.path.join('docs', 'estrutura_de_pastas.md')
    with open(destino, 'w', encoding='utf-8') as f:
        f.write('\n'.join(estrutura))

    print(f"\n✅ Estrutura salva com sucesso em: {destino}")

if __name__ == '__main__':
    gerar_arquivo()
