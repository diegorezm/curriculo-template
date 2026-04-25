# Gerador de Currículo em PDF

Sistema para gerar currículos em PDF a partir de Markdown com configuração personalizável.

## Como Usar

### 1. Configurar suas informações pessoais

Edite o arquivo `config.json`:

```json
{
  "name": "Seu Nome Completo",
  "contacts": [
    {
      "type": "website",
      "icon": "icons/web.svg",
      "url": "https://seusite.com",
      "display": "seusite.com"
    },
    {
      "type": "email",
      "icon": "icons/gmail.svg",
      "url": "mailto:seu@email.com",
      "display": "seu@email.com"
    },
    {
      "type": "github",
      "icon": "icons/github.svg",
      "url": "https://github.com/seuusuario",
      "display": "seuusuario"
    },
    {
      "type": "linkedin",
      "icon": "icons/linkedin.webp",
      "url": "https://linkedin.com/in/seuusuario",
      "display": "seuusuario"
    }
  ]
}
```

### 2. Editar o conteúdo do currículo

Edite o arquivo `curriculo.md` com suas informações seguindo o template.

### 3. Gerar o PDF

```bash
# Uso básico (usa config.json por padrão)
python convert.py curriculo.md curriculo.pdf

# Ou especifique um arquivo de configuração diferente
python convert.py curriculo.md curriculo.pdf meu_config.json
```

## Estrutura de Arquivos

```
.
├── convert.py          # Script de conversão
├── config.json         # Suas informações pessoais
├── curriculo.md        # Conteúdo do currículo
├── style.css           # Estilos do PDF
├── icons/              # Ícones usados no cabeçalho
│   ├── web.svg
│   ├── gmail.svg
│   ├── github.svg
│   └── linkedin.webp
└── curriculo.pdf       # PDF gerado
```

## Personalizações Disponíveis

### Adicionar/Remover Contatos

Você pode adicionar ou remover itens no array `contacts`:

```json
{
  "type": "telefone",
  "icon": "icons/phone.svg",
  "url": "tel:+5511999999999",
  "display": "(11) 99999-9999"
}
```

### Ordem dos Contatos

A ordem no array `contacts` define a ordem de exibição no PDF.

### Usar Múltiplos Perfis

Crie diferentes arquivos de configuração:

```bash
python convert.py curriculo.md curriculo_tech.pdf config_tech.json
python convert.py curriculo.md curriculo_design.pdf config_design.json
```

## Requisitos

```bash
pip install markdown weasyprint
```

## Dicas

- Mantenha o `display` curto para não quebrar o layout
- Use ícones SVG para melhor qualidade
- O separador `·` é adicionado automaticamente entre os contatos
- Você pode mudar o nome do arquivo config.json para qualquer outro nome
