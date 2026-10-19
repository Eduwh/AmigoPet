# AmigoPet — Mockup

Apresentação navegável de um sistema de gestão para petshop, com clientes, pets com múltiplos tutores, vacinas, agenda e banho e tosa. Todos os dados são fictícios. Os formulários e confirmações são demonstrativos; não há backend ou armazenamento.

## Arquivos para o Git

```text
.gitignore
README.md
public/
  index.html
  AmigoPet-Gestao.figcraft
```

O HTML contém os estilos, ícones, telas e navegação. O arquivo `.figcraft` é o destino do botão de download da apresentação. Não é necessário instalar dependências ou compilar o site.

As pastas `prototype/` e `example/` ficam locais, ignoradas pelo Git. Apenas o conteúdo de `public/` deve ser publicado.

## Cloudflare Pages com Git

1. Envie os arquivos acima para um repositório no GitHub ou GitLab.
2. No painel do Cloudflare, crie um projeto **Pages** com integração Git e selecione o repositório. Escolha Pages, em vez de um projeto Workers.
3. Configure:

| Campo | Valor |
| --- | --- |
| Production branch | `main`, ou a branch utilizada no repositório |
| Framework preset | `None` |
| Build command | `exit 0` |
| Build output directory | `public` |
| Root directory | Raiz do repositório; deixe o padrão |
| Environment variables | Nenhuma |

4. Inicie o deploy. A página inicial será `public/index.html`. A navegação usa fragmentos (`#agenda`, `#pet`), sem necessidade de regras de redirecionamento.
5. A integração Git publicará novamente após cada push na branch de produção.

Documentação oficial: [HTML estático no Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/) e [integração Git](https://developers.cloudflare.com/pages/get-started/git-integration/).

## Primeiro envio

Se a pasta ainda não for um repositório Git, execute no seu terminal:

```sh
git init -b main
git add .gitignore README.md public/
git commit -m "Adiciona mockup AmigoPet para Cloudflare Pages"
```

Crie um repositório remoto vazio e adicione a URL fornecida por ele:

```sh
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

Se já existir um repositório, use a branch e o remote existentes, sem repetir `git init` ou `git remote add`.

## Prévia local

Abra `public/index.html` no navegador ou execute:

```sh
python3 -m http.server 8080 --directory public
```

Acesse `http://localhost:8080`.

## Atualizar o mockup

Se alterar a apresentação na pasta local `prototype/`, copie `prototype/apresentacao.html` para `public/index.html`. Se alterar o documento de design, atualize também `public/AmigoPet-Gestao.figcraft`. Faça commit e push dos arquivos de `public/`.
