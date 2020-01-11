# Salvar e carregar modelos

O TensorFlow.js fornece funcionalidade para salvar e carregar modelos que foram criados com a [API de camadas](https://js.tensorflow.org/api/0.14.2/#Models) ou convertidos à partir de modelos TensorFlow.js existentes. Estes podem ser modelos que você treinou ou aqueles treinados por outros. Um dos principais benefícios do uso da API de camadas é que os modelos criados com ela são serializáveis e é isso que exploraremos nesse tutorial.

Este tutorial focará em salvar e carregar modelos TensorFlow.js (identificáveis por arquivos JSON). Nós também podemos importar modelos TensorFlow Python. O carregamento desses modelos é abordado nos dois tutoriais a seguir:

*  [Importar modelos Keras](https://www.tensorflow.org/js/tutorials/conversion/import_keras)
*  [Importar modelos GraphDef](https://www.tensorflow.org/js/tutorials/conversion/import_saved_model)


## Salvar um tf.Model

[`tf.Model`](https://js.tensorflow.org/api/0.14.2/#class:Model) e [`tf.Sequential`](https://js.tensorflow.org/api/0.14.2/#class:Sequential) fornecem uma função [model.save](https://www.tensorflow.org/js/guide/save_load) que permite você salvar a _topologia_ e os _pesos_ de um modelo.

*  Topologia: Este é um arquivo descrevendo a arquitetura de um modelo (ou seja, quais operações ele usa). Ele contém referências aos pesos do modelo que são armazenados externamente.

*  Pesos: Estes são arquivos binários que armazenam os pesos de um determinado modelo em um formato eficiente. Eles são geralmente armazenados na mesma pasta que a topologia.

Vamos dar uma olhada no que o código para salvar um modelo se parece:


```js
const saveResult = await model.save('localstorage://my-model-1');
```


Algumas coisas a serem observadas:

*  O método `save` recebe um argumento string semelhante à uma URL que começa com um **esquema**. Isso descreve o tipo de destino no qual estamos tentado salvar um modelo. No exemplo acima, o esquema é `localstorage://`.
*  O esquema é seguido por um **caminho**. No exemplo acima, o caminho é `my-model-1`.
*  O método `save` é assíncrono.
*  O valor do retorno de `model.save` é um objeto JSON que carrega informações como o tamanho de bytes da topologia e dos pesos do modelo.
*  O ambiente usado para salvar o modelo não afeta quais ambientes pode carregá-lo. Salvar um modelo em node.js não impede que ele seja carregado no navegador.

A seguir, examinaremos os diferentes esquemas disponíveis:


### Local Storage (Somente navegador)

**Esquema:** `localstorage://`


```js
await model.save('localstorage://my-model');
```


Isso salva um modelo com o nome `my-model` no [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) do navegador. Isso persistirá entre atualizações, embora o local storage possa ser limpo pelos usuários ou pelo navegador se o espaço se tornar um problema. Cada navegador também define seu próprio limite de quantos dados podem ser armazenados no local storage para um determinado domínio.


### IndexedDB (Somente navegador)

**Esquema:** `indexeddb://`


```js
await model.save('indexeddb://my-model');
```


Isso salva um modelo no armazenamento do [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) do navegador. Como o local storage, ele persiste entre atualizações, também tende a ter limites maiores no tamanho dos objetos armazenados.


### Downloads de Arquivos (Somente navegador)

**Esquema:** `downloads://`


```js
await model.save('downloads://my-model');
```


Isso fará com que o navegador faça o download dos arquivos do modelo na máquina do usuário. Dois arquivos serão produzidos:

1.  Uma arquivo de JSON chamado `[my-model].json`, que carrega a topologia e a referência ao arquivo de pesos descrito abaixo.
2.  Um arquivo binário com os valores dos pesos nomeado `[my-model].weights.bin`.

Você pode mudar o nome `[my-model]` para obter arquivo com um nome diferente.

Como o arquivo `.json` aponta para o arquivo `.bin` usando caminho relativo, os dois arquivos devem estar na mesma pasta.

> Nota: alguns navegadores exigem que o usuário conceda permissão antes que mais de um arquivo possa ser baixado ao mesmo tempo.


### Requisição HTTP(S)

**Esquema:** `http://` ou `https://`


```js
await model.save('http://model-server.domain/upload')
```


Isso criará uma requisição web para salvar um modelo em um servidor remoto. Você deve estar no controle desse servidor remoto para garantir que ele possa lidar com a solicitação.

O modelo será enviado para o servidor HTTP especificado através de uma requisição [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST).

O corpo do POST está no formato `multipart/form-data` e consiste de dois arquivos.

1.  Uma arquivo JSON nomeado `model.json`, que carrega a topologia e a referência ao arquivo de pesos descrito abaixo.
2.  Um arquivo binário com os valores dos pesos nomeado `model.weights.bin`.

Observe que os nomes dos arquivos serão sempre como especificado anteriormente (o nome está incorporado à função). Esta [documentação da api](https://js.tensorflow.org/api/latest/#tf.io.browserHTTPRequest) contém um trecho de código Python que demonstra como alguém pode usar framework web [flask](https://palletsprojects.com/p/flask/) para lidar com a solicitação originada pelo `save`.

Geralmente, você precisará passar mais argumentos ou headers na requisição para o seu servidor HTTP (por exemplo, para autenticação ou se desejar especificar uma pasta na qual o modelo deve ser salvo). Você pode obter controle refinado sobre esses aspectos das solicitações de `save` substituindo o argumento da string de URL em `tf.io.browserHTTPRequest`. Esta API oferece maior flexibilidade no controle de solicitações HTTP.

Por exemplo:


```js
await model.save(tf.io.browserHTTPRequest(
    'http://model-server.domain/upload',
    {method: 'PUT', headers: {'header_key_1': 'header_value_1'}}));
```


### Sistema de Arquivo Nativo (Somente Node.js)

**Esquema:** `file://`


```js
await model.save('file:///path/to/my-model');
```


Ao rodar no Node.js, também temos acesso direto ao sistema de arquivos e podemos salvar modelos lá. O comando acima salvará dois arquivos no `caminho` especificado após o `esquema`.

1.  Uma arquivo JSON nomeado `[model].json`, que carrega a topologia e a referência para o arquivo de pesos descrito abaixo.
2.  Um arquivo binário carregando os valores dos pesos nomeado `[model].weights.bin`.

Observe que o nome dos dois arquivos será sempre exatamente como especificado acima (o nome está incorporado à função).


## Carregando um tf.Model

Dado um modelo que foi salvo usando um dos método acima, podemos carregar o modelo usando a API `tf.loadLayersModel`.

Vamos dar uma olhada em como é um código para carregar um modelo:


```js
const model = await tf.loadLayersModel('localstorage://my-model-1');
```


Algumas coisas para observar:

*  Assim como `model.save()`, a função `loadLayersModel` recebe uma string semelhante à URL que começa com um **esquema**. Isso descreve o tipo de destino do qual estamos tentando carregar um modelo.
*  O esquema é seguido por um **caminho**. No exemplo acima, o caminho é `my-model-1`.
*  A string semelhante à URL pode ser substituída por um objeto que condiz com a interface IOHandler.
*  A função `tf.loadLayersModel()` é assíncrona.
*  O valor de retorno de `tf.loadLayersModel` é um `tf.Model`.

A seguir, examinaremos os diferentes esquemas disponíveis.


### Local Storage (Somente no navegador)


**Esquema:** `localstorage://`


```js
const model = await tf.loadLayersModel('localstorage://my-model');
```


Isso carrega um modelo chamado `my-model` do [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) do navegador.


### IndexedDB (Somente no navegador)

**Esquema:** `indexeddb://`


```js
const model = await tf.loadLayersModel('indexeddb://my-model');
```


Isso carrega um modelo do armazenamento do [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) do navegador.


### HTTP(S)

**Esquema:** `http://` ou `https://`


```js
const model = await tf.loadLayersModel('http://model-server.domain/download/model.json');
```


Isso carrega um modelo de um endpoint http. Depois de carregar um arquivo `json`, a função fará requisições para os arquivo `.bin` correspondentes que o arquivo `json` referencia.

> NOTA: Essa implementação depende da presença do método [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). Se você está em um ambiente que não fornece o método fetch nativamente, você pode fornecer um método global nomeado [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) que satisfaça a interface ou use uma biblioteca como [`node-fetch`](https://www.npmjs.com/package/node-fetch).


### Sistema de Arquivo Nativo (Somente no Node.j)

**Esquema:** `file://`


```js
const model = await tf.loadLayersModel('file://path/to/my-model/model.json');
```


Ao executar no Node.js, também temos acesso direto ao sistema de arquivo e podemos carregar modelos de lá. Observe que na chamada da função acima, nós referenciamos o próprio arquivo `model.json` (enquanto que ao salvar, especificamos a pasta). O(s) arquivo(s) `.bin` correspondente(s) deve estar na mesma pasta do arquivo `.json`.


## Carregando modelos com IOHandlers

Se os esquemas acima não são suficientes para sua necessidade, você pode implementar um comportamento de carregamento personalizado com um `IOHandler`. Um `IOHandler` fornecido pelo TensorFlow.js é [`tf.io.browserFiles`](https://js.tensorflow.org/api/latest/#io.browserFiles) que permite os usuários do navegador carregarem arquivos do modelo no navegador. Veja a [documentação](https://js.tensorflow.org/api/latest/#io.browserFiles) para mais informação.


## Salvando e Carregando Modelos com IOHandlers personalizados.

Se os esquemas acima não são suficientes para carregar ou salvar seu modelo, você precisa implementar um comportamento de serialização personalizado implementando um `IOHandler`.

Uma `IOHandler` é um objeto com um método `save` e `load`.

A função `save` recebe um parâmetro que obedece a interface [ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165) e deve retornar uma promise que resolve com um objeto [SaveResult](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L107).

A função `load` não recebe parâmetros e deve retornar uma promise que resolve com um objeto [ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165). Isso é o mesmo objeto que é passado para `save`.

Veja [BrowserHTTPRequest](https://github.com/tensorflow/tfjs-core/blob/master/src/io/browser_http.ts) para um exemplo de como implementar um IOHandler.