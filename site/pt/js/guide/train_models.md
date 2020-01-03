# Treinando Modelos

Esse guia assume que você já leu o guia [modelos e camadas](models_and_layers.md).

No TensorFlow.js, existem duas maneiras de treinar um modelo de machine learning:

1.  usando a API de camadas com <code>[LayersModel.fit()](https://js.tensorflow.org/api/latest/#tf.Model.fit)</code> ou <code>[LayersModel.fitDataset()](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset)</code>.
2.  usando a API principal com <code>[Optimizer.minimize()](https://js.tensorflow.org/api/latest/#tf.train.Optimizer.minimize)</code>.

Primeiro, veremos a API de camadas, que é uma API de alto nível para criar e treinar modelos. Em seguida, mostraremos como treinar o mesmo modelo usando a API principal.


## Introdução

Um _modelo_ de machine learning é uma função com parâmetros aprendíveis que mapeia uma entrada para uma saída desejada. Os parâmetros ótimos são obtidos pelo treinamento do modelo em dados.

O treinamento envolve várias etapas:

*   Obtendo um [lote](https://developers.google.com/machine-learning/glossary/#batch) de dados para o modelo.
*   Pedindo ao modelo para fazer uma predição.
*   Comparando essa predicação com o valor "verdadeiro".
*   Decidindo quanto alterar em cada parâmetro para que o modelo possa fazer uma melhor predição no futuro para esse lote.

Um modelo bem treinado fornecerá um mapeamento preciso da entrada para a saída desejada.


## Parâmetros do modelo

Vamos definir um modelo simples de 2 camadas usando a API de camadas:


```js
const model = tf.sequential({
 layers: [
   tf.layers.dense({inputShape: [784], units: 32, activation: 'relu'}),
   tf.layers.dense({units: 10, activation: 'softmax'}),
 ]
});
```


Por debaixo dos panos, modelos têm parâmetros (geralmento chamados de _pesos_) que são aprendíveis com o treinamento em dados. Vamos imprimir os nomes dos pesos associados com esse modelo e seus formatos:


```js
model.weights.forEach(w => {
 console.log(w.name, w.shape);
});
```


Temos a seguinte saída:


```
> dense_Dense1/kernel [784, 32]
> dense_Dense1/bias [32]
> dense_Dense2/kernel [32, 10]
> dense_Dense2/bias [10]
```


Existem 4 pesos no total, 2 por camada densa. Isso é esperado, já que camadas densas representam uma função que mapeia o tensor de entrada `x` para um tensor de saída `y` através da equação `y = Ax + b` onde A (o kernel) e `b` (o bias) são parâmetros da camada densa.

> NOTA: Por padrão, camadas densas incluem um bias, mas você pode excluí-lo especificando `{useBias: false}` nas opções ao criar uma camada densa.

`model.summary()` é um método útil se você quer obter uma visão geral do seu modelo e ver o número total de parâmetros:


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
   <td colspan="3" >Total params: 25450<br>Trainable params: 25450<br>Non-trainable params: 0
   </td>
  </tr>
</table>


Cada peso no modelo é suportado por um objeto <code>[Variable](https://js.tensorflow.org/api/0.14.2/#class:Variable)</code>. No TensorFlow.js, um `Variable` é um `Tensor` de ponto flutuante com um método adicional `assign()` usado para atualizar seus valores. A API de camadas automaticamente inicializa os pesos usando as práticas recomendadas. Para fins de demonstração, podemos sobrescrever os pesos chamando `assign()` nas variáveis subjacentes:


```js
model.weights.forEach(w => {
  const newVals = tf.randomNormal(w.shape);
  // w.val é uma instância de tf.Variable
  w.val.assign(newVals);
});
```


## Otimizador, função de perda e métrica

Antes de fazer qualquer treinamento, você precisa decidir três coisas:

1.  **Um otimizador**. A função de um otimizador é decidir quanto mudar em cada parâmetro do modelo, de acordo com a predição atual do modelo. Ao usar a API de camadas, você pode fornecer uma string identificadora de um otimizador existente (assim como `'sgd'` ou `'adam'`), ou uma instância da classe [Optimizer](https://js.tensorflow.org/api/latest/#Training-Optimizers).
2.  **Uma função de perda**. Um objetivo que o modelo tentará minimizar. Seu objetivo é dar um único número para representar o "quão errada" a predição do modelo foi. A perda é calculada em todo lote de dados para que o modelo possa ajustar seus pesos. Ao usar a API de Camadas, você pode fornecer uma string identificadora de uma função de perda existente (Assim como `'categoricalCrossentropy'`), ou qualquer função que receba o valor predito e o valor real e retorne uma perda. Veja uma [lista de funções de perda disponíveis](https://js.tensorflow.org/api/latest/#Training-Losses) em nossa documentação da API.
3.  **Lista de métricas**. Semelhante às funções de perda, métricas calculam um único número, resumindo o desempenho do nosso modelo. As métricas são geralmente calculadas em todos os dados no final de cada época. No mínimo, queremos monitorar que nossa perda está diminuindo ao longo do tempo. No entanto, geralmente queremos uma métrica mais amigável ao ser humano, como precisão. Ao usar a API de Camadas, você pode fornecer uma string identificadora de uma métrica existente (Assim como `'accuracy'`), ou qualquer função que receba um valor predito e um valor real e retorne uma pontuação. Veja uma [lista de métricas disponíveis](https://js.tensorflow.org/api/latest/#Metrics) em nossa documentação da API.

Quando você decidir, compile um `LayersModel` chamando o método `model.compile()` com as opções fornecidas:


```js
model.compile({
  optimizer: 'sgd',
  loss: 'categoricalCrossentropy',
  metrics: ['accuracy']
});
```


Durante a compilação, o modelo fará alguma validações para garantir que as opções que você escolheu são compatíveis uma com a outra.


## Treinamento

Existem duas formas de treinar um `LayersModel`:

*  Usando `model.fit()` e fornecendo os dados como um grande tensor.
*  Usando `model.fitDataset()` e fornecendo os dados através de um objeto `Dataset`.


### model.fit()

Se o seu conjunto de dados cabe na memória principal e está disponível como um único tensor, você pode treinar um modelo chamando o método `fit()`:


```js
// Gera dados aleatórios.
const data = tf.randomNormal([100, 784]);
const labels = tf.randomUniform([100, 10]);

function onBatchEnd(batch, logs) {
  console.log('Precisão', logs.acc);
}

// Treina por 5 épocas com tamanho de lote 32.
model.fit(data, labels, {
   epochs: 5,
   batchSize: 32,
   callbacks: {onBatchEnd}
 }).then(info => {
   console.log('Precisão final', info.history.acc);
 });
```


Por debaixo dos panos, `model.fit()` pode fazer muito por nós:

*  Divide os dados em um conjunto de treinamento e um conjunto de validação, e usa o conjunto de validação para medir o progresso durante o treino.
*  Embaralha os dados, mas somente após a divisão. Para estar seguro, você deve pré-embaralhar os dados antes de passá-los para `fit()`.
*  Divide o tensor de dados grande em tensores menores de tamanho `batchSize`.
*  Chama `optimizer.minimize()` enquanto calcula a perda do modelo em relação ao lote de dados.
*  Ele pode notificá-lo no início e no final de cada época ou lote. Em nosso caso, nós somos notificados no final de cada lote usando a opção  `callbacks.onBatchEnd`. Outras opções incluem: `onTrainBegin`, `onTrainEnd`, `onEpochBegin`, `onEpochEnd` e `onBatchBegin`.
*  Ele cede à thread principal para garantir que as tarefas enfileiradas no event loop JS possam ser tratadas em tempo hábil.

Para mais informação, veja a [documentação](https://js.tensorflow.org/api/latest/#tf.Sequential.fit) de `fit()`. Observe que, se você escolher usar a API Core, você terá que implementar esta lógica por conta própria.


### model.fitDataset()

Se seus dados não cabem inteiramente na memória ou estiverem sendo transmitidos, você pode treinar um modelo chamando `fitDataset()`, que recebe um objeto `Dataset`. Aqui é o mesmo código de trainamento, mas com um conjunto de dados que envolve uma função geradora:


```js
function* data() {
 for (let i = 0; i < 100; i++) {
   // Gera uma amostra de cada vez.
   yield tf.randomNormal([784]);
 }
}

function* labels() {
 for (let i = 0; i < 100; i++) {
   // Gera uma amostra de cada vez.
   yield tf.randomUniform([10]);
 }
}

const xs = tf.data.generator(data);
const ys = tf.data.generator(labels);
// Nós compactamos os dados e os rótulos juntos, embaralhamos e agrupamos 32 amostras por vez.
const ds = tf.data.zip({xs, ys}).shuffle(100 /* bufferSize */).batch(32);

// Treina o modelo por 5 épocas.
model.fitDataset(ds, {epochs: 5}).then(info => {
 console.log('Accuracy', info.history.acc);
});
```


Para mais informação sobre conjuntos de dados, veja a [documentação](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset) de `model.fitDataset()`.


## Predizendo novos dados

Depois que o modelo foi treinado, você pode chamar o método `model.predict()` para fazer predição de dados nunca vistos pelo modelo antes.


```js
// Prediz 3 amostras aleatórias.
const prediction = model.predict(tf.randomNormal([3, 784]));
prediction.print();
```


Note: Como nós mencionamos no guia [Modelos e Camadas](models_and_layers), o `LayersModel` espera que a dimensão mais externa da entrada seja o tamanho do lote. No exemplo anterior, o tamanho do lote é 3.


## API principal

Anteriormente, mencionamos que existem duas formas de treinar um modelo de machine learning no TensorFlow.js.

A regra geral é tentar usar a API de camadas primeiro, pois ela é modelada sobre a bem adotada API do Keras. A API de Camadas também oferece diversas soluções prontas para uso, como a inicialização de peso, serialização de modelo, monitoramento do treinamento, portabilidade e verificação de segurança.

Você pode usar a API principal sempre que:

*  Você precisa do máximo de flexibilidade ou controle.
*  E você não precisa de serialização ou pode implementar sua própria lógica de serialização.

Para mais informação sobre esta API, leia a seção "API principal" no guia [Modelos e Camadas](models_and_layers.md).

O mesmo modelo escrito acima, usando a API Core, se parece com isso:


```js
// Os pesos e bias para as duas camadas densas.
const w1 = tf.variable(tf.randomNormal([784, 32]));
const b1 = tf.variable(tf.randomNormal([32]));
const w2 = tf.variable(tf.randomNormal([32, 10]));
const b2 = tf.variable(tf.randomNormal([10]));

function model(x) {
  return x.matMul(w1).add(b1).relu().matMul(w2).add(b2);
}
```


Além da API de Camadas, a API de Dados também funciona perfeitamente com a API principal. Vamos reusar o conjunto de dados que nós definimos anteriormente na seção [model.fitDataset](#model.fitDataset()), que embaralha e agrupa pra nós:


```js
const xs = tf.data.generator(data);
const ys = tf.data.generator(labels);
// Nós compactamos os dados e os rótulos juntos, embaralhamos e agrupamos 32 amostras por vez.
const ds = tf.data.zip({xs, ys}).shuffle(100 /* bufferSize */).batch(32);
```


Vamos treinar o modelo:


```js
const optimizer = tf.train.sgd(0.1 /* learningRate */);
// Treina por 5 épocas.
for (let epoch = 0; epoch < 5; epoch++) {
  await ds.forEachAsync(({xs, ys}) => {
    optimizer.minimize(() => {
      const predYs = model(xs);
      const loss = tf.losses.softmaxCrossEntropy(ys, predYs);
      loss.data().then(l => console.log('Perda', l));
      return loss;
    });
  });
  console.log('Época', epoch);
}
```


O código acima é receita padrão ao treinar um modelo com a API principal:

*  Iterar sobre o número de épocas.
*  Dentro de cada época, iterar sobre seu lote de dados. Ao usar um `Dataset`, <code>[dataset.forEachAsync()](https://js.tensorflow.org/api/0.15.1/#tf.data.Dataset.forEachAsync)</code> é uma forma conveniente de iterar sobre seus lotes.
*  Para cada lote, chamar <code>[optimizer.minimize(f)](https://js.tensorflow.org/api/latest/#tf.train.Optimizer.minimize)</code>, que executa `f` e minimiza sua saída calculando gradientes em relação às quatro variáveis que definimos anteriormente.
*  `f` calcula a perda. Ele chama uma das funções de perda pré-definidas usando a predição do modelo e o valor real.