## Projeto Tech News

> Terceiro projeto do módulo de Ciência da Computação do curso de desenvolvimento web da Trybe.

**Contexto**

No bloco desse projeto, somos aprentados às técnicas de raspagem de dados e às inúmeras possibilidades trazidas por elas.  Por exemplo, elas podem fornecer dados para construção de matérias jornalísticas, permitir a comparação de preços de produtos em sites concorrentes ou automatizar processos massantes como buscar por artigos científicos em bases acadêmicas. 

A raspagem de dados em si consiste na extração de dados de sites (geralmente, manipulando tags HTML) e transformação desses dados para um formato mais simples e maleável para que possam ser analisados com mais facilidade. Nesse projeto foi construído um raspador de dados na linguagem Python, utilizando os módulos externos `Requests` e `Parsel`.

**Objetivo do projeto**

Fazer consultas em notícias sobre tecnologia. Para isso será necessário criar um banco de dados, obter dados para popular este banco, e preparar consultas a serem feitas nestas notícias. As notícias devem ser obtidas por meio da **raspagem de dados** no site do [TecMundo](https://www.tecmundo.com.br/novidades). Após a raspagem, devem ser utilizadas as funções já existentes para salvá-las no banco de dados MongoDB.

**Principais habilidades desenvolvidas nesse trabalho**

- Aplicar técnicas de raspagem de dados;
- Extrair dados de conteúdo HTML;
- Armazenar os dados obtidos em um banco de dados.

**Tecnologia utilizada**

- <a href="https://www.python.org"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" title="Python" height="35" align="center"/> - Python</a> 
- <a href="https://www.mongodb.com/"><img src="https://www.svgrepo.com/show/331488/mongodb.svg" title="MongoDB" align="center" height="34"/> - MongoDB</a>

---

### Lista de requisitos propostos pela Trybe:

#### Obrigatórios

#### 1 - Crie a função `fetch`
local: `tech_news/scraper.py`

Antes de fazer scrape, precisamos de uma página! Esta função será responsável por fazer a requisição HTTP ao site Tecmundo e obter o conteúdo HTML.
Alguns cuidados deverão ser tomados: como a nossa função poderá ser utilizada váras vezes em sucessão, na nossa implementação devemos nos assegurar que um [Rate Limit](https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/4edde8f1-9d55-4c98-a593-e3043848a127/alguns-problemas/) será respeitado.

- A função deve receber uma URL
- A função deve fazer uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
- A função deve retornar o conteúdo HTML da resposta.
- A função deve respeitar um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada requisição que fizer.
**Dica:** Uma forma simples de garantir que cada requisição seja feita com um intervalo mínimo de um segundo é utilizar `time.sleep(1)` antes de cada requisição. (Existem outras formas mais eficientes.)
- Caso a requisição seja bem sucedida com `Status Code 200: OK`, deve ser retornado seu conteúdo de texto;
- Caso a resposta tenha o código de status diferente de `200`, deve-se retornar `None`;
- Caso a requisição não receba resposta em até 3 segundos, ela deve ser abandonada (este caso é conhecido como "Timeout") e a função deve retornar None.

✍️ Teste manual: abra um terminal Python importando estas funções através do comando `python3 -i tech_news/scraper.py` e as invoque utilizando diferentes parâmetros. Exemplo: 
```python
>>> html = fetch(url_da_noticia)
>>> scrape_noticia(html)
```

#### 2 - Crie a função `scrape_novidades`
local: `tech_news/scraper.py`

Para conseguirmos fazer o scrape da página de uma notícia, primeiro precisamos de links para várias páginas de notícias. Estes links estão contidos na página Novidades (https://www.tecmundo.com.br/novidades). 

Esta função fará o scrape da página Novidades para obter as URLs das páginas de notícias. Vamos utilizar as ferramentas que aprendemos no curso, como a biblioteca Parsel, para obter os dados que queremos de cada página.

- A função deve receber uma string com o conteúdo HTML da página Novidades (https://www.tecmundo.com.br/novidades)
- A função deve fazer o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
- A função deve retornar esta lista.
- Caso não encontre nenhuma URL de notícia, a função deve retornar uma lista vazia.

✍️ Teste manual: abra um terminal Python importando estas funções através do comando `python3 -i tech_news/scraper.py` e as invoque utilizando diferentes parâmetros. Exemplo: 
```python
>>> html = fetch(url_da_noticia)
>>> scrape_novidades(html)
```

#### 3 - Crie a função `scrape_next_page_link`
local: `tech_news/scraper.py`

Para buscar mais notícias, precisaremos fazer a paginação, e para isto, vamos precisar do link da próxima página. Esta função será responsável por fazer o scrape deste link.

- A função deve receber como parâmetro uma `string` contendo o conteúdo HTML da página de novidades (https://www.tecmundo.com.br/novidades)
- A função deve fazer o scrape deste HTML para obter a URL da próxima página.
- A função deve retornar a URL obtida.
- Caso não encontre o link da próxima página, a função deve retornar `None`

#### 4 - Crie a função `scrape_noticia`
local: `tech_news/scraper.py`

Agora que sabemos pegar páginas HTML, e descobrir o link de notícias, é hora de fazer o scrape dos dados que procuramos! 

- A função deve receber como parâmetro o conteúdo HTML da página de uma única notícia da Tecmundo
- A função deve, no conteúdo recebido, buscar as informações das notícias para preencher um dicionário com os seguintes atributos:
  - `url` - link para acesso da notícia. Ex: "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
  - `title` - título da notícia. Ex: "Musk: Tesla está muito perto de carros totalmente autônomos"
  - `timestamp` - data e hora da notícia. Ex: "2020-07-09T11:00:00"
  - `writer` - nome da pessoa autora da notícia. Ex: "Nilton Kleina". Se a informação não for encontrada, salve este atributo como `None`
  - `shares_count` - número de compartilhamento da notícia. Ex: `61`. Se a informação não for encontrada, salve este atributo como `0` (zero)
  - `comments_count` - número de comentários que a notícia recebeu. Ex: `26`
  - `summary` - o primeiro parágrafo da notícia. Ex:"O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado."
  - `sources` - lista contendo fontes da notícia. Ex: ["Venture Beat", "Source 2"]
  - `categories` - lista de categorias que classificam a notícia. Ex: ["Mobilidade Urbana/Smart Cities", "Veículos autônomos", "Tesla", "Elon Musk"]

- Exemplo de um retorno da função com uma notícia específica:

```json
{
  "url": "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm",
  "title": "Musk: Tesla está muito perto de carros totalmente autônomos",
  "timestamp": "2020-07-09T11:00:00",
  "writer": "Nilton Kleina",
  "shares_count": 61,
  "comments_count": 26,
  "summary": "O CEO da Tesla, Elon Musk, garantiu que a montadora está muito perto de atingir o chamado nível 5 de autonomia de sistemas de piloto automático de carros. A informação foi confirmada em uma mensagem enviada pelo executivo aos participantes da Conferência Anual de Inteligência Artificial (WAIC, na sigla em inglês). O evento aconteceu em Xangai, na China, onde a montadora comemora resultados positivos de mercado.",
  "sources": ["Venture Beat"],
  "categories": [
    "Mobilidade Urbana/Smart Cities",
    "Veículos autônomos",
    "Tesla",
    "Elon Musk"
  ]
}
```

📌 Muita atenção aos tipos dos campos, por exemplo, `sources` e `categories` são listas, assim como `shares_count` e `comments_count` são numéricos.

📌 **Dica para fazer o scraping:** Caso uma tag possua outras tags aninhadas, para obter todos os textos da tag ancestral e de suas tags descendentes, utilize `*::text` no seletor.

- Exemplo:
  ```html
  <p>
    Recentemente, a Alemanha fez a
    <a
      href="https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
      rel="noopener noreferrer"
      target="_blank"
      >Tesla</a
    >
    “pisar no freio” quanto ao uso de termos comerciais relacionados a carros
    autônomos, mas quem pensa que esse é um sinal de resistência à introdução de
    novas tecnologias se engana. Isso porque, de acordo o
    <em>Automotive News Europe</em>, o país está se preparando para se tornar o
    primeiro do mundo a criar uma ampla estrutura para regulamentar tais
    veículos de nível 4.
  </p>
  ```
  Repare que no exemplo dentro da tag _p_ encontram-se duas outras tags. Esse é um caso onde a tag _p_ é um ancestral e as tags _a_ e _em_ são as descendentes. Para obter todo o texto do exemplo, utiliza-se `*::text` no seletor.

📌 **É bom saber que** ao fazer scraping na vida real, você está sempre "refém" de quem construiu o site. Por exemplo, pode ser que nem toda notícia tenha **exatamente** o mesmo HTML/CSS e você precise de criatividade para contornar isso. 

#### 5 - Crie a função `get_tech_news` para obter as notícias!
local: `tech_news/scraper.py`

Agora, chegou a hora de aplicar todas as funções que você acabou de fazer. Com estas ferramentas prontas, podemos fazer nosso scraper mais robusto com a paginação.

- A função deve receber como parâmetro um número inteiro `n` e buscar as últimas `n` notícias do site.
- Utilize as funções `fetch`, `scrape_novidades`, `scrape_next_page_link` e `scrape_noticia` para buscar as notícias e processar seu conteúdo.
- As notícias buscadas devem ser inseridas no MongoDB; Para acessar o banco de dados, importe e utilize as funções que já temos prontas em `tech_news/database.py`
- Após inserir as notícias no banco, a função deve retornar estas mesmas notícias.

📌 De aqui em diante, usaremos o MongoDB. Para instalar e rodar o servidor MongoDB, siga as instruções no tutorial oficial:
Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
MacOS:  https://docs.mongodb.com/guides/server/install/
Com o servidor rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
Não altere as funções deste módulo; elas serão utilizadas nos testes.

#### 6 - Crie a função `search_by_title`
local: `tech_news/analyzer/search_engine.py`

Agora que temos meios de popular nosso banco de dados com notícias, podemos começar a fazer as buscas! Esta função irá fazer buscas por título.

- A função deve receber uma string com um título de notícia
- A função deve buscar as notícias do banco de dados por título
- A função deve retornar uma lista de tuplas com as notícias encontradas nesta busca. 
Exemplo: 
```python
[
  ("Título1_aqui", "url1_aqui"),
  ("Título2_aqui", "url2_aqui"),
  ("Título3_aqui", "url3_aqui"),
]
```
- A busca deve ser _case insensitive_
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

📌 Lembre-se; para acesso ao banco de dados importe `db` definido no módulo `tech_news/database.py`.

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_title("Musk")`.

#### 7 - Crie a função `search_by_date`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias do banco de dados por data.

- A função deve receber como parâmetro uma data no formato "aaaa-mm-dd"
- A função deve buscar as notícias do banco de dados por data.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` deve ser lançada com a mensagem `Data inválida`.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_date("2020-11-11")`.

#### 8 - Crie a função `search_by_source`,
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por fonte.

- A função deve receber como parâmetro o nome da fonte completo.
- A função deve buscar as notícias do banco de dados por fonte.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
- A busca deve ser _case insensitive_

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_source("Venture Beat")`.

#### 9 - Crie a função `search_by_category`
local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por categoria.

- A função deve receber como parâmetro o nome da categoria completo.
- A função deve buscar as notícias do banco de dados por categoria.
- A função deve ter retorno no mesmo formato do requisito anterior.
- Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
- A busca deve ser _case insensitive_

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/search_engine.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `search_by_category("Tesla")`.

#### 10 - Crie a função `top_5_news`
local: `tech_news/analyzer/ratings.py`

Esta função irá listar as cinco notícias mais populares; nosso critério de popularidade será a soma dos compartilhamentos e comentários.

- A função deve buscar as notícias do banco de dados e calcular a sua "popularidade" somando seu número de compartilhamentos e comentários.
- A função deve ordenar as notícias por ordem de popularidade.
- Em caso de empate, o desempate deve ser por ordem alfabética de título.
- A função deve ter retorno no mesmo formato do requisito anterior, porém limitado a 5 notícias.
- Caso haja menos de cinco notícias, no banco de dados, deve-se retornar todas as notícias existentes;
- Caso não haja notícias disponíveis, deve-se retornar uma lista vazia.

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/ratings.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `top_5_news()`.

#### 11 - Crie a função `top_5_categories`
local: `tech_news/analyzer/ratings.py`

Esta função irá listar as cinco categorias com maior ocorrência no banco de dados. 

- As categorias devem ser ordenadas por ordem alfabética.
- As top 5 categorias da análise devem ser retornadas em uma lista no formato `["category1", "category2"]`;
- Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;
- Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

✍️ Teste manual: abra um terminal Python importando esta função através do comando `python3 -i tech_news/analyzer/ratings.py` e invoque a função utilizando diferentes parâmetros. Exemplo: `top_5_categories()`.

#### Bônus:

#### 12 - Crie a função `analyzer_menu`
local: `tech_news/menu.py`

Esta função é o menu do nosso programa. Através dele poderemos operar as funcionalidades que criamos. Será um menu de opções, em que cada opção pede as informações necessárias para disparar uma ação.

- O texto exibido pelo menu deve ser exatamente:
```
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
```

- Caso a opção `0` seja selecionada, seve-se exibir a mensagem "Digite quantas notícias serão buscadas:"

- Caso a opção `1` seja selecionada, deve-se exibir a mensagem "Digite o título:";

- Caso a opção `2` seja selecionada, deve-se exibir a mensagem "Digite a data no formato aaaa-mm-dd:";

- Caso a opção `3` seja selecionada, deve-se exibir a mensagem "Digite a fonte:";

- Caso a opção `4` seja selecionada, deve-se exibir a mensagem "Digite a categoria:";

- Caso a opção não exista, exiba a mensagem de erro "Opção inválida" na `stderr`.

📌 A função `input` deve ser utilizada para receber a entrada de dados da pessoa usuária.

✍️ Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-analyzer`, o menu deve ser exibido. Isto acontece pois durante a configuração inicial do projeto já configuramos para que a função seja corretamente chamada quando este comando seja invocado.

#### 13 - Implemente as funcionalidades do menu
local: `tech_news/menu.py`

- Quando selecionada uma opção do menu, e inseridas as informações necessárias, a ação adequada deve ser realizada.

- Caso a opção `0` seja selecionada, a importação deve ser feita utilizando a função `get_tech_news`;

- Caso a opção `1` seja selecionada, a importação deve ser feita utilizando a função `search_by_title` e seu resultado deve ser impresso em tela;

- Caso a opção `2` seja selecionada, a exportação deve ser feita utilizando a função `search_by_date` e seu resultado deve ser impresso em tela;

- Caso a opção `3` seja selecionada, a importação deve ser feita utilizando a função `search_by_source` e seu resultado deve ser impresso em tela;

- Caso a opção `4` seja selecionada, a exportação deve ser feita utilizando a função `search_by_category` e seu resultado deve ser impresso em tela;

- Caso a opção `5` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_news` e seu resultado deve ser impresso em tela;

- Caso a opção `6` seja selecionada, a raspagem deve ser feita utilizando a função `top_5_categories` e seu resultado deve ser impresso em tela;

- Caso a opção `7` seja selecionada, deve-se encerrar a execução do script e deve-se exibir a mensagem "Encerrando script";

- Caso alguma exceção seja lançada, a mesma deve ser capturada e sua mensagem deve ser exibida na saída padrão de erros (`stderr`).

✍️ Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `tech-news-analyzer`, assim você conseguirá interagir com o menu.
