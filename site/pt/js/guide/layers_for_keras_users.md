# API de Camadas TensorFlow.js para usuários do Keras

A API de camadas do TensorFlow.js é modelada com base no Keras e nos esforçamos para fazer a [API de camadas](https://js.tensorflow.org/api/latest/) razoalmente semelhante ao Keras, dadas as diferenças entre JavaScript e Python. Isso facilita para usuários com experiência no desenvolvimento de modelos Keras no Python a migrar para Camadas TensorFlow.js em JavaScript. Por exemplo, o seguinte código Kera se traduz em JavaScript:


```python
# Python:
import keras
import numpy as np

# Cria e compila modelo.
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, input_shape=[1]))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Gera alguns dados sintéticos para o treinamento.
xs = np.array([[1], [2], [3], [4]])
ys = np.array([[1], [3], [5], [7]])

# Treina modelo com fit().
model.fit(xs, ys, epochs=1000)

# Executa inferência com predict().
print(model.predict(np.array([[5]])))
```


```js
// JavaScript:
import * as tf from '@tensorlowjs/tfjs';

// Cria e compila modelo.
const model = tf.sequential();
model.add(tf.layers.dense({units: 1, inputShape: [1]}));
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});

// Gera alguns dados sintéticos para treinamento.
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
const ys = tf.tensor2d([[1], [3], [5], [7]], [4, 1]);

// Treina modelo com fit().
await model.fit(xs, ys, {epochs: 1000});

// Executa inferência com predict().
model.predict(tf.tensor2d([[5]], [1, 1])).print();
```


No entanto, existem algumas diferenças que gostaríamos de chamar e explicar nesse documento. Depois de entender essas diferenças e a lógica por trás delas, sua migração de Python para JavaScript (ou na direção reversa) deve ser uma experiência relativamente tranquila.


## Construtores recebem objetos JavaScript como configuração

Compare as seguintes linhas Python e JavaScript do exemplo dado acima: ambos criam uma camada [Dense](https://keras.io/layers/core/#dense).


```python
# Python:
keras.layers.Dense(units=1, inputShape=[1])
```


```js
// JavaScript:
tf.layers.dense({units: 1, inputShape: [1]});
```


Funções JavaScript não tem um equivalente aos argumentos keyword das funções Python. Queremos evitar implementar opções de construtores como argumentos posicionais no JavaScript, o que seria especialmente complicado de lembrar e de usar quando são construtores com um grande número de argumentos (Por exemplo, [LSTM](https://keras.io/layers/recurrent/#lstm)). Este é o motivo de usarmos objetos JavaScript para configuração. Esses objetos fornecem o mesmo nível de invariância posicional e flexibilidade como os argumentos keyword do Python.

Alguns métodos da classe `Model`, por exemplo [`Model.compile()`](https://keras.io/models/model/#model-class-api), também recebem um objeto JavaScript de configuração como a entrada. No entanto, lembre-se que `Model.fit()`, `Model.evaluate()` e `Model.predict()` são ligeiramente diferentes. Uma vez que esses métodos recebem obrigatoriamente `x` (features) e `y` (labels ou targets) como dados de entrada, `x` e `y` são argumentos posicionais separados de um objeto de configuração que desempenha o papel dos argumentos keyword. Por exemplo:


```js
// JavaScript:
await model.fit(xs, ys, {epochs: 1000});
```


## Model.fit() é assíncrono

`Model.fit()` é o método principal com o qual os usuários realizam o treinamento do modelo em TensorFlow.js. Esse método geralmente pode levar muito tempo, com duração de segundos ou minutos. Portanto, nós utilizamos a feature `async` da linguagem JavaScript, para que essa função possa ser usada de uma maneira que não bloqueie a thread principal da interface do usuário quando rodamos ela no navegador.

Isso é semelhante à outras funções potencialmente de longa duração no JavaScript, como a `async` [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). Observe que `async` é uma construção que não existe no Python. Enquanto o método [`fit()`](https://keras.io/models/model/#model-class-api) no Keras retorna um objeto de histórico, a contrapartida do método `fit()` no JavaScript retorna uma [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) do histórico, que pode ser tratada com [await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) (como no exemplo acima) ou usando o método `.then()`.


## Sem NumPy para TensorFlow.js

Os usuários do Python Keras geralmente usam [NumPy](http://www.numpy.org/) para realizar operações numéricas básicas e operações de array, como gerar tensores 2D no exemplo abaixo.


```python
# Python:
xs = np.array([[1], [2], [3], [4]])
```


No TensorFlow.js, esses tipos de operações numéricas básicas são feita com o próprio pacote. Por exemplo:


```js
// JavaScript:
const xs = tf.tensor2d([[1], [2], [3], [4]], [4, 1]);
```


O namespace `tf.*` também fornece várias outras funções para array e operações de álgebra linear, como multiplicação de matrizes. Veja a [Documentação principal TensorFlow.js](https://js.tensorflow.org/api/latest/) para mais informação.


## Use métodos factory, não construtores.

Essa linha em Python (do código abaixo) é uma chamada de um construtor:


```python
# Python:
model = keras.Sequential()
```


Se traduzida estritamente para JavaScript, a chamada do construtor equivalente seria parecido com o seguinte:


```js
// JavaScript:
const model = new tf.Sequential();  // !!! NÃO FAÇA ISSO !!!
```


No entanto, decidimos não usar os construtores "new" porque 1) a palavra-chave "new" pode tornar o código mais inchado e 2) o construtor "new" é considerado como uma "parte ruim" do JavaScript: uma potencial armadilha, como é argumentado em [*JavaScript: the Good Parts*](http://archive.oreilly.com/pub/a/javascript/excerpts/javascript-good-parts/bad-parts.html).

Para criar modelos e camadas em TensorFlow.js, você chama métodos factory, que tem nomes lowerCamelCase, por exemplo:


```js
// JavaScript:
const model = tf.sequential();

const layer = tf.layers.batchNormalization({axis: 1});
```


## Os valores das string opções são lowerCamelCase, não snake_case

No JavaScript, é mais comum usar camel case para nomes simbólicos (Por exemplo, [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html#naming-camel-case-defined)), em comparação com o Python, onde snake case é comum (Por exemplo, no Keras). Assim sendo, decidimos usar lowerCamelCase para valores strings para opções incluindo as seguintes:

*  DataFormat, por exemplo, **`channelsFirst`** em vez de `channels_first`
*  Inicializador, por exemplo, **`glorotNormal`** em vez de `glorot_normal`
*  Função de perda e métricas, por exemplo, **`meanSquaredError`** em vez de `mean_squared_error`, **`categoricalCrossentropy`** em vez de `categorical_crossentropy`.

Por exemplo, como no exemplo abaixo:


```js
// JavaScript:
model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});
```


Com relação à serialização e desserialização do modelo, tenha certeza: o mecanismo interno do TensorFlow.js garante que snake cases nos objetos JSON são manipulados corretamente, por exemplo, ao carregar modelos pré-treinados do Python Keras.


## Execute objetos Layer com apply(), não chamando-os como funções.

No Keras, um objeto Layer tem o método `__call__` definido. Portanto, o usuário pode invocar a lógica da camada chamando o objeto como uma função, por exemplo:


```python
# Python:
my_input = keras.Input(shape=[2, 4])
flatten = keras.layers.Flatten()

print(flatten(my_input).shape)
```


Esse "açúcar sintático" do Python é implementado como o método apply() no TensorFlow.js:


```js
// JavaScript:
const myInput = tf.input({shape: [2, 4]});
const flatten = tf.layers.flatten();

console.log(flatten.apply(myInput).shape);
```


## Layer.apply() suporta avaliação imperativa em tensores concretos

Atualmente, no Keras, o método __call__ só pode operar em objetos `tf.Tensor` do TensorFlow (assumindo o backend do TensorFlow), que são simbólicos e não são reais valores numéricos. Isso é o que é mostrado na seção anterior. No entanto, no TensorFlow.js, o método apply() das camadas pode operar nos modos simbólico e imperativo. Se `apply()` é invocado com um SymbolicTensor (uma analogia próxima de tf.Tensor), o valor de retorno será um SymbolicTensor. Isso acontece tipicamente durante a construção do modelo. Mas se `apply()` é invocado com um tensor concreto, ele retornará um tensor concreto. Por exemplo:


```js
// JavaScript:
const flatten = tf.layers.flatten();

flatten.apply(tf.ones([2, 3, 4])).print();
```


Esse recurso é reminiscência da [Execução Eager](https://www.tensorflow.org/guide/eager) do TensorFlow (Python). Oferece maior interatividade e depuração durante o desenvolvimento do modelo, além de abrir portas para compor redes neurais dinâmicas.


## Otimizadores estão sob train.*, não optimizers.*

No Keras, os construtores para objetos Optimizer estão sob o namespace `keras.optimizers.*`. No TensorFlow.js, os métodos factory para Optimizers estão sob o namespace `tf.train.*`. Por exemplo:


```python
# Python:
my_sgd = keras.optimizers.sgd(lr=0.2)
```


```js
// JavaScript:
const mySGD = tf.train.sgd({lr: 0.2});
```


## loadLayersModel() carrega de uma URL, não um arquivo HDF5

No Keras, modelos são geralmente [salvos](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model) como um arquivo HDF5 (.h5), que pode ser posteriormente carregado usando o método `keras.models.load_model()`. O método recebe um caminho para o arquivo `.h5`. A contraparte do `load_model()` no TensorFlow.js é [`tf.loadLayersModel()`](https://js.tensorflow.org/api/latest/#loadLayersModel).

Como o HDF5 não é um formato de arquivo amigável ao navegador, `tf.loadLayersModel()` recebe um formato de arquivo específico do TensorFlow.js. `tf.loadLayersModel()` recebe um arquivo model.json como argumento de entrada. O model.json pode ser convertido de um arquivo HDF5 do Keras usando o pacote do pip tensorflowjs.


```js
// JavaScript:
const model = await tf.loadLayersModel('https://foo.bar/model.json');
```


Observe também que `tf.loadLayersModel()` retorna uma [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) de [`tf.Model`](https://js.tensorflow.org/api/latest/#class:Model).

Em geral, salvar e carregar `tf.Model`s  no TensorFlow.js é feito usando os métodos `tf.Model.save` e `tf.loadLayersModel`, respectivamente. Nós projetamos essas APIs para serem similares à API [save/load_model](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model) do Keras. Mas, o ambiente do nevegador é bastante diferente do ambiente backend nos quais estruturas básicas de deep learning, como Keras, são executadas, particularmente na matriz de rotas para persistir e transmitir dados. Portanto, existem algumas diferenças interessantes entre as APIs save/load no TensorFlow.js e no Keras. Veja nosso tutorial [Salvar e carregar modelos](./save_load.md) para mais detalhes.


## Use `fitDataset()` para treinar modelos usando objetos `tf.data.Dataset`

No tf.keras do TensorFlow Python, um modelo pode ser treinado usando um objeto [Dataset](https://www.tensorflow.org/guide/datasets). O método `fit()` do modelo aceita esse objeto diretamente. Um modelo TensorFlow.js pode ser treinado com o equivalente JavaScript dos objetos Dataset (Veja a [documentação da API tf.data no TensorFlow.js](https://js.tensorflow.org/api/latest/#Data)).

No entanto, diferente do Python, treinamento baseado em Dataset é feio através de um método dedicado, nomeado [fitDataset](https://js.tensorflow.org/api/0.15.1/#tf.Model.fitDataset). O método [fit()](https://js.tensorflow.org/api/latest/#tf.Model.fitDataset) é apenas para treinamento baseado em tensor.


## Gerenciamento de memória de objetos Layer e Model

O TensorFlow.js executa no WebGL no navegador, one os pesos dos objetos Layer e Model são suportados por texturas WebGL. No entanto, WebGL não tem suporte à coleta de memória interna (Garbage collector). Objetos Layer e Model internamente gerenciam memória de tensor para o usuário durante suas chamadas de inferência e treinamento. Mas, eles também permitem o usuário descarte-os para liberar memória WebGL que eles ocupam. Isso é útil nos casos em que muitas instâncias de modelo são criadas e liberadas em um único carregamento da página. Para descartar ,um objeto Layer ou Model, use o método `dispose()`.