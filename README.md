# Simulador Visual Interativo e Implementacao de Arvore Binaria de Busca (BST)

**Disciplina:** Estrutura de Dados  
**Curso:** Analise e Desenvolvimento de Sistemas (ADS) - Fatec Ribeirao Preto  
**Professor:** Eduardo Cruz Araujo  
**Aluno:** [Seu Nome Completo Aqui]  
**RA:** [Seu Numero de RA Aqui]  
**Tema Escolhido:** Tema B (Tema 2) - Arvores Binarias de Busca (*Binary Search Tree - BST*)  

---

## Video Explicativo (Defesa Tecnica)

> **[CLIQUE AQUI PARA ASSISTIR AO VIDEO EXPLICATIVO](https://seu-link-do-youtube-ou-drive-aqui)**  
> *(Certifique-se de que o video esteja configurado como "Nao Listado" no YouTube ou com acesso publico no Google Drive).*

---

## Resumo Teorico e Aplicacoes Reais

Uma **Arvore Binaria de Busca (BST)** e uma estrutura de dados hierarquica baseada em nos, onde cada no armazena uma chave (valor) e possui no maximo dois filhos: o **filho a esquerda** (*left*) e o **filho a direita** (*right*). A estrutura obedece a seguinte propriedade invariante fundamental para qualquer no $N$:

1. Todos os elementos na subarvore **esquerda** de $N$ possuem chaves **menores** que a chave de $N$.
2. Todos os elementos na subarvore **direita** de $N$ possuem chaves **maiores** que a chave de $N$.
3. Nao sao permitidas chaves duplicadas (na implementacao padrao).

### Onde e utilizada no mundo real?
* **Sistemas de Gerenciamento de Bancos de Dados (SGBDs):** Estruturas derivadas de BST (como Arvores B e B+) sao o nucleo da indexacao de registros para consultas rapidas.
* **Sistemas de Arquivos e Diretorios:** Organizacao hierarquica de pastas e arquivos em sistemas operacionais.
* **Compiladores e Analisadores Sintaticos:** Construcao de Arvores Sintaticas Abstratas (AST) e tabelas de simbolos.
* **Autocompletar e Dicionarios:** Armazenamento ordenado de chaves para buscas e travessias em ordem alfabetica/numerica.

---

## Analise de Complexidade Assintotica (Big-O)

O desempenho das operacoes fundamentais (`insert`, `search` e `delete`) em uma BST depende diretamente da **altura ($h$)** da arvore:

| Operacao | Melhor Caso | Caso Medio | Pior Caso | Espaco Auxiliar (Pilha de Recursao) |
| :--- | :---: | :---: | :---: | :---: |
| **Busca (`search`)** | $O(1)$ | $O(\log n)$ | $O(n)$ | $O(h)$ - de $O(\log n)$ a $O(n)$ |
| **Insercao (`insert`)** | $O(1)$ | $O(\log n)$ | $O(n)$ | $O(h)$ - de $O(\log n)$ a $O(n)$ |
| **Remocao (`delete`)** | $O(\log n)$ | $O(\log n)$ | $O(n)$ | $O(h)$ - de $O(\log n)$ a $O(n)$ |
| **Travessias (`in/pre/post`)** | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n)$ | $O(h)$ - de $O(\log n)$ a $O(n)$ |
| **Altura (`height`)** | $\Theta(n)$ | $\Theta(n)$ | $\Theta(n)$ | $O(h)$ - de $O(\log n)$ a $O(n)$ |

### Por que o Pior Caso $O(n)$ ocorre?
Diferente de arvores auto-balanceadas (como AVL ou Rubro-Negra), a BST classica nao realiza rotacoes estruturais apos insercoes ou remocoes. Quando os dados sao inseridos em **ordem estritamente crescente ou decrescente** (ex.: `[10, 20, 30, 40, 50]`), cada novo elemento e inserido sempre a direita (ou sempre a esquerda) do anterior. Isso transforma a arvore em uma **estrutura degenerada** (linear), equivalente a uma **Lista Encadeada**, onde a altura $h$ torna-se igual a $n - 1$, degradando o tempo de busca de logaritmico $O(\log n)$ para linear $O(n)$.

---

## Diario de Engenharia com IA

* **Ferramenta / Modelo Utilizado:** Google Gemini.

### Principais Prompts Utilizados
1. **Prompt 1 (Arquitetura da Estrutura em Python):**  
   *"Implemente uma classe BST (Arvore Binaria de Busca) em Python puro com type hints e docstrings, contendo os metodos insert, search, delete (tratando os 3 casos de remocao), travessias in_order, pre_order, post_order e calculo de height, incluindo um contador interno de comparacoes para demonstrar a diferenca entre insercao balanceada e degenerada."*
2. **Prompt 2 (Construcao do Simulador Visual Interativo):**  
   *"Crie uma aplicacao web autocontida em HTML, CSS e JavaScript puro para simular visualmente uma Arvore Binaria de Busca. O simulador deve desenhar os nos e arestas em SVG, permitir controle passo a passo (Play, Step, Pause, Reset), animar buscas, insercoes e as 3 travessias, e ter botoes de cenario rapido comparando Insercao Aleatoria O(log n) vs. Insercao Ordenada Degenerada O(n)."*
3. **Prompt 3 (Refinamento Visual e Metricas):**  
   *"Adicione ao simulador um painel de metricas em tempo real mostrando a altura atual da arvore, o numero total de nos, o contador de comparacoes acumuladas e um log textual detalhado explicando a decisao tomada a cada no visitado."*

### Analise Critica e Ajuste Manual Realizado
* **Limitacao Identificada:** Na primeira versao gerada do posicionamento visual dos nos no SVG (`app.js`), quando a arvore assumia o cenario de **Pior Caso (Insercao Ordenada)** com varios nos consecutivos a direita, o calculo simples de deslocamento horizontal fixo fazia os nos mais profundos ultrapassarem a borda direita do conteiner visivel.
* **Ajuste Manual:** Foi implementado um fator de reducao exponencial do espacamento horizontal ($dx / 2^{\text{nivel}}$) aliado a uma largura dinamica do elemento `<svg>` e centralizacao automatica da camera, garantindo que tanto arvores equilibradas quanto arvores degeneradas sejam exibidas integralmente sem cortes.

