# Sobre o Projeto 

- Quinto projeto do modulo de Ciências da Computação da trybe.
- Durante essa seção foi apresentado EA (Estrutura de dados) e TAD (tipos abstratos de dados), focando em apresentar a estrutura de Lista encadeada, Pilhas(LIFO) e filas(FIFO).
- Neste projeto, foram desenvolvidos métodos usando a estrutura de fila, para coleta de informações de um arquivo por linha, marcando cada linha e a frase daquela determinada linha, onde é possível salva-las e depois buscar por palavras específicas se existem no arquivo, retornando um relatório, de onde a palavra se encontra no arquivo(qual linha), e também trazer a frase juntamente com o relatório.

<details>
  <summary>
    <strong>
      :telescope: Detalhes do projeto:
    </strong>
  </summary>

# Classe Queue

Initialmente foi criado uma classe `Queue`, na pasta `ting_file_management/queue.py`, responsável por padronizar a estrutura de fila, por recomandações da trybe e da documentação do python, optei por criar o atributo dessa classe usando a coleção deque, que é mais performática quando relacionado a estrutura de filas, por questão de deslocamento dos elementos ao inserir ou remover elementos da fila. [fonte](https://docs.python.org/pt-br/3/tutorial/datastructures.html#using-lists-as-queues)

# Método txt_importer

Método encontrado na pasta `ting_file_management/file_manament.py`, responsável por coletar as informações de um arquivo txt, aceitando somente arquivos com extensões txt, ele retorna uma lista sendo cada elemento da lista uma linha do arquivo.

# Método process

Encontrado em `ting_file_management/file_process.py`, ele que processa as informação dentro da `Queue`, ele recebe como parâmetro o caminho onde está o arquivo txt juntamente com uma instância da `Queue`, para realizar o enfileiramento das informação dos arquivos, por padrão ele não enfileira arquivos com o mesmo nome/caminho(duplicando dados).

# Método remove

Encontrado em `ting_file_management/file_process.py`, responsável por quando a instância da `Queue` não está vázia de remover o primeiro elemento dela(FIFO).

# Método file_metadata

Encontrado em `ting_file_management/file_process.py`, método responsavel por mostrar na tela os dados salvos na posição do indice passada como parâmetro, do primeiro ao último elemento na `Queue`.

# Método exists_word

Encontrado em `ting_search_word/word_search.py`, esse método recebe 2 parâmetros, uma instância de `Queue` a palavra que deseja procurar nos arquivos que foram processados com o método process da `Queue`, retornando um relatório, passando em quais linhas a palavra foi encontrada de qual arquivo, e caso não seja encontrada a palavra, o relatório trás uma lista vazia.

# Método search_by_word

Encontrado em `ting_search_word/word_search.py`, assim como o método exists, ele cria um relatório referente a palavra com base na `Queue`, trazendo uma informação adicional, que é o conteudo da linha, que ele encontrou a palavra.
Nesse método eu fragmentei o código do exists word, para reutiliza-lo, adicionando um parametro, onde eu determino se ele deve trazer o relatório com ou sem frase, evitando de criar a repetição do código, para tazer uma informação adicional.
Fazendo isso, veio em mente, e se existirem outro métodos parecidos com esse pegando mais informações adicionais, provavelmente trocaria o if, para um object literal, onde faria como extensão, para criar métodos que extraem a informação desejada.

</details>

#

# Tecnologias e ferramentas usadas 🛠

![Python](https://img.shields.io/badge/-Python-%23F7DF1C?style=flat-square&logo=python)


# Desafios

- 

# Conclusão

- 

<details>
  <summary>
    <strong>
      ⚠️ Configurações mínimas para execução do projeto
    </strong>
  </summary>

   - Sistema Operacional Distribuição Unix
 - Python versão >= 3.8.10 

</details>

</details>

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos solicitados durante o desenvolvimento do projeto
    </strong>
  </summary>

 
### Resultado por requisito
*Nome* | *Avaliação*
--- | :---:
1.1 - Será validado que o método `enqueue` deve adicionar um valor a fila, modificando seu tamanho | :heavy_check_mark:
1.2 - Será validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho | :heavy_check_mark:
1.3 - Será validado que o método `search` deve buscar um valor na lista à partir de um índice | :heavy_check_mark:
1.4 - Será validado que o método `search` deve lançar uma exceção quando o índice for inválido | :heavy_check_mark:
2.1 - Será validado que ao executar o método `txt_importer` deve retornar uma estrutura contendo as linhas do arquivo | :heavy_check_mark:
2.2 - Será validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem: `Arquivo {path_file} não encontrado` | :heavy_check_mark:
2.3 - Será validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida uma mensagem: `Formato inválido` | :heavy_check_mark:
3.1 - Será validado que ao executar a função `process` com o mesmo nome a execução deverá ser ignorada | :heavy_check_mark:
3.2 - Será validado que ao executar a função `process` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
4.1 - Será validado que ao executar a função `remove` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
4.2 - Será validado que ao executar a função `remove` um arquivo inexistente deverá retornar a mensagem `Não há elementos` | :heavy_check_mark:
5.1 - Será validado que ao executar a função `file_metadata` com sucesso deverá retornar mensagem via `stdout` | :heavy_check_mark:
5.2 - Será validado que ao executar a função `file_metadata` com posição inválida deverá retornar a mensagem `Posição inválida` | :heavy_check_mark:
6.1 - Será validado que ao executar a função `exists_word` com sucesso deverá retornar a mensagem | :heavy_check_mark:
6.2 - Será validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia | :heavy_check_mark:
7.1 - Será validado que ao executar a função `search_by_word` com sucesso deverá retornar a mensagem | :heavy_check_mark:
7.2 - Será validado que ao executar a função `search_by_word` com palavra inexistente deverá retornar uma lista vazia | :heavy_check_mark:



</details>
