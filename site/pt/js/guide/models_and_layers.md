# Modelos e Camadas

Em machine learning, um _modelo_ é uma função com [parâmetros](https://developers.google.com/machine-learning/glossary/#parameter) _"aprendíveis"_ que mapeia uma entrada para uma saída. Os parâmetros ótimos são obtidos treinando o modelo com dados. Um modelo bem treinado fornecerá um mapeamento preciso de uma entrada até a saída desejada.

No TensorFlow.js, existem duas maneiras de criar um modelo de machine learning:

1.  Usando a API de camadas onde você constrói um modelo usando _camadas_.
2.  Usando a API principal com operações de baixo nível como `tf.matMul()`, `tf.add()`, etc.

Primeiro, veremos a API de camadas, que é uma API de alto nível para construir modelos. Em seguida, mostraremos como construir o mesmo modelo usando a API Principal.


## Criando modelos com a API de camadas

Existem duas formas de criar um modelo usando a API de camadas: Um modelo _sequencial_ e um modelo _funcional_. As próximas duas seções examinam cada tipo mais de perto.

### O modelo sequencial

O tipo mais comum de modelo é o modelo <code>[Sequencial](https://js.tensorflow.org/api/0.15.1/#class:Sequential)</code>, que é uma pilha linear de camadas. Você pode criar um modelo `Sequencial` passando uma lista de camadas para a função <code>[sequential()](https://js.tensorflow.org/api/0.15.1/#sequential)</code>:


```js
const model = tf.sequential({
 layers: [
   tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}),
   tf.layers.dense({units: 10, activation: 'softmax'}),
 ]
});
```


Ou através do método `add()`:


```js
const model = tf.sequential();
model.add(tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}));
model.add(tf.layers.dense({units: 10, activation: 'softmax'}));
```


> IMPORTANTE: A primeira camada no modelo precisa de um `inputShape`. Certifique-se de excluir o tamanho do lote quando fornecer o `inputShape`. Por exemplo, se você planeja alimentar o modelo com tensores de formato `[B, 784]`, onde `B` pode ser qualquer tamanho de lote, especifique `inputShape` como `[784]` ao criar o modelo.

Você pode acessar as camadas do modelo em `model.layers`, a mais especificamente em `model.inputLayers` e `model.outputLayers`.


### O modelo funcional

Uma outra forma de criar um `LayersModel` é através da função `tf.model()`. A diferença chave entre `tf.model()` e `tf.sequential()` é que `tf.model()` permite você criar um grafo arbitrário de camadas, desde que elas não tenham ciclos.

Aqui está um trecho de código que define o mesmo modelo acima, usando a API `tf.model()`:


```js
/*
Cria um grafo de camadas arbitrário, conectando-as
através do método apply().
*/
const input = tf.input({shape: [784]});
const dense1 = tf.layers.dense({units: 32, activation: 'relu'}).apply(input);
const dense2 = tf.layers.dense({units: 10, activation: 'softmax'}).apply(dense1);
const model = tf.model({inputs: input, outputs: dense2});
```


Nós chamamos `apply()` em cada camada para conectá-la à saída de outra camada. O resultado de `apply()` nesse caso é um `SymbolicTensor`, que age como um `Tensor`, mas sem valores concretos.

Perceba que, diferente do modelo sequencial, nós criamos um `SymbolicTensor` através de `tf.input()` em vez de fornecer um `inputShape` para a primeira camada.

`apply()` também pode fornecer um `Tensor` concreto, se você passar um `Tensor` concreto para ela:


```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = tf.layers.activation({activation: 'relu'}).apply(t);
o.print(); // [0, 1, 0, 5]
```


Isso pode ser útil ao testar camadas de forma isolada e ver sua saída.

Assim como em um modelo sequencial, você pode acessar as camadas de um modelo através de `model.layers`, e mais especificamente `model.inputLayers` e `model.outputLayers`.


## Validação

O modelo sequencial e o modelo funcional são instâncias da classe `LayersModel`. Um dos maiores benefícios de trabalhar com uma `LayersModel` é a validação: obriga a especificar o formato da entrada e o utilizará posteriormente para validar sua entrada. A `LayersModel` também faz inferência automática do formato à medida que os dados fluem pelas camadas. O conhecimento prévio do formato permite que o modelo crie automaticamente seu parâmetros e pode informar se duas camadas consecutivas não são compatíveis entre si.

## Resumo do modelo

Chame `model.summary` para imprimir um resumo útil do modelo, que inclue:

*   Nome e tipo de todas as camadas no modelo.
*   Formato da saída para cada camada.
*   Número de pesos de cada camada.
*   Se o modelo tem topologia geral (discutida abaixo), as entradas que cada camada recebe.
*   O número total de parâmetros aprendíveis e não aprendíveis do modelo.

Para o modelo que definimos acima, nós obtemos a seguinte saída no console:


<table>
  <tr>
   <td>Layer (type)
   </td>
   <td>Output shape
   </td>
   <td>Param #
   </td>
  </tr>
  <tr>
   <td>dense_Dense1 (Dense)
   </td>
   <td>[null,32]
   </td>
   <td>25120
   </td>
  </tr>
  <tr>
   <td>dense_Dense2 (Dense)
   </td>
   <td>[null,10]
   </td>
   <td>330
   </td>
  </tr>
  <tr>
   <td colspan="3" >Total params: 25450<br/>Trainable params: 25450<br/> Non-trainable params: 0
   </td>
  </tr>
</table>


Observe os valores `null` nos formatos da saída: um lembrete de que o modelo espera que a entrada tenha um tamanho do lote como a dimensão mais externa, que neste caso pode ser flexível devido ao valor `null`.


## Serialização

Um dos maiores benefícios de usar uma `LayersModel` sobre a API de baixo nível é a capacidade de salvar e carregar um modelo. Uma `LayersModel` sabe sobre:

*   A arquitetura do modelo, permitindo recriar o modelo.
*   Os pesos do modelo.
*   A configuração de treinamento (função de perda, otimizador, métricas).
*   O estado do otimizador, permitindo que você retome o treinamento.

Salvar ou carregar um modelo é apenas 1 linha de código:


```js
const saveResult = await model.save('localstorage://my-model-1');
const model = await tf.loadLayersModel('localstorage://my-model-1');
```


O exemplo acima salva o modelo no local storage do navegador. Veja a <code>[documentação de model.save()](https://js.tensorflow.org/api/latest/#tf.Model.save)</code> e o guia de [salvar e carregar](save_load.md) para saber como salvar em diferentes mídias (Por exemplo, armazenamento de arquivos, IndexedDB, acionar o download de um navegador, etc.)


## Camadas personalizadas

Camadas são os blocos de construção de um modelo. Se o seu modelo estiver fazendo um cálculo personalizado, você pode definir uma camada personalizada, que interage bem com o resto das camadas. Abaixo, nós definimos uma camada personalizada que calcula a soma dos quadrados:


```js
class SquaredSumLayer extends tf.layers.Layer {
 constructor() {
   super({});
 }
 // Nesse caso, a saída é um escalar.
 computeOutputShape(inputShape) { return []; }

 // call() é onde fazemos o cálculo.
 call(input, kwargs) { return input.square().sum();}

 // Todas as camadas precisam de um nome único.
 getClassName() { return 'SquaredSum'; }
}
```


Para testar isso, podemos chamar o método `apply()` com um tensor concreto:


```js
const t = tf.tensor([-2, 1, 0, 5]);
const o = new SquaredSumLayer().apply(t);
o.print(); // imprime 30
```


> IMPORTANTE: Se você adicionar uma camada personalizada, você perde a capacidade de serializar o modelo.


## Criando modelos com a API principal

No início deste guia, mencionamos que há duas maneiras de criar um modelo de machine learning no TensorFlow.js.

A regra geral é sempre tentar usar a API de camadas primeiro, pois ela é modelada em cima da bem adotada API Keras que segue as [melhores práticas e reduz carga cognitiva](https://keras.io/why-use-keras/). A API de camadas também oferece várias soluções prontas para uso, como inicialização de peso, serialização de modelo, treinamento de monitoramento, portabilidade e verificação de segurança.

Você pode usar a API principal sempre que:

*   Você precisa do máximo de flexibilidade ou controle.
*   Você não precisa de serialização ou pode implementar sua própria lógica de serialização.

Os modelos na API principal são apenas funções que pegam um ou mais `Tensors` e retornam um `Tensor`. O mesmo modelo descrito acima, usando a API principal, se parece com isso:


```js
// Os pesos e viéses para as duas camadas densas.
const w1 = tf.variable(tf.randomNormal([784, 32]));
const b1 = tf.variable(tf.randomNormal([32]));
const w2 = tf.variable(tf.randomNormal([32, 10]));
const b2 = tf.variable(tf.randomNormal([10]));

function model(x) {
  return x.matMul(w1).add(b1).relu().matMul(w2).add(b2).softmax();
}
```


Observe que na API principal nós somos responsáveis por criar e inicializar os pesos do modelo. Todos os pesos são apoiados por uma `Variable`, que sinaliza ao TensorFlow.js que estes tensores são aprendíveis. Você pode criar uma `Variable` usando [tf.variable()](https://js.tensorflow.org/api/latest/#variable) e passando um `Tensor` existente.

Neste guia, você se familiarizou com as diferentes maneiras de criar um modelo usando as camadas e a API principal. A seguir, consulte o guia [Treinando Modelos](train_models.md) para saber como treinar um modelo.