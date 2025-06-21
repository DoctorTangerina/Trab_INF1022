# Trabalho de INF1022 - Analisadores Léxicos e Sintáticos

## 📚 Índice

- [🔄 Conversor de Obsact para Lua/Java/C](#conversor-de-obsact-para-luajavac)
- [📦 Requisitos](#-requisitos)
- [🚀 Como usar](#-como-usar)
- [📜 Listar linguagens disponíveis](#-listar-linguagens-disponíveis)
- [🧪 Rodar os testes](#-rodar-os-testes)
- [📂 Saída](#-saída)
- [⚠️ Observações](#-observações)
- [📄 Licença](#-licença)
- [📄 Relatório Completo](#-relatório-completo)
- [👥 Integrantes](#-integrantes)
- [🔗 Links importantes](#-links-importantes)

# Conversor de Obsact para Lua/Java/C
Este script Python converte arquivos escritos na linguagem Obsact para uma linguagem de destino: Lua, Java ou C.

## 📦 Requisitos

Instale dependências:

```
pip install -r requirements.txt
```
## 🚀 Como usar


```
python main.py <nome_do_arquivo> <linguagem_destino>
```

### 📥 Parâmetros
`nome_do_arquivo`: Caminho para o arquivo-fonte em linguagem Obsact.<br>
Exemplo: exemplo.obsact, ./entradas/codigo.obsact

`linguagem_destino`: Linguagem para a qual deseja converter.<br>
Valores possíveis: Lua, Java, C (insensível a maiúsculas e minúsculas)

### ✅ Exemplo de uso

```
python main.py exemplo.obsact Lua
```

Esse comando converte o conteúdo do arquivo exemplo.obsact da linguagem Obsact para a linguagem Lua.

## 📜 Listar linguagens disponíveis
Você pode listar todas as linguagens de destino suportadas com:

```
python main.py --list
```
ou
```
python main.py -l
```
Saída esperada:
```
Linguagens disponíveis:
    - Lua
    - Java
    - C
```

## 🧪 Rodar os testes
Este projeto inclui uma suíte de testes automatizados para garantir o bom funcionamento do conversor.

Para executá-los:
```
python tests.py
```
Os testes cobrem os principais casos de conversão e validação do parser e lexer.

## 📂 Saída
O script irá gerar um novo arquivo com nome `output`, mas com a extensão correspondente à linguagem de destino.
Por exemplo:

Entrada: exemplo.obsact

Saída (para linguagem Lua): output.lua

## ⚠️ Observações
O script espera que o arquivo de entrada esteja no formato válido da linguagem Obsact.<br>
Caso haja um erro sintático ou léxico, será exibida uma mensagem de erro.

## 📄 Licença
Este projeto está licenciado sob a MIT License.


## 📄 Relatório Completo:
https://docs.google.com/document/d/1161eO2iewS9MAFvN3UelFDLjBZv2Md8HUEfulOr0gz4/edit?usp=sharing

## 👥 Integrantes:
- Arthur Augusto Claro Sardella - 2212763 - 3WA
- Julia Guimarães Simão - 2211834 - 3WB

## 🔗 Links importantes:
- PLY: https://www.dabeaz.com/ply/ply.html#ply_nn3
- SLY: https://sly.readthedocs.io/en/latest/