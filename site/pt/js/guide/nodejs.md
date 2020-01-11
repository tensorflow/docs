# TensorFlow.js no Node


## TensorFlow CPU

O pacote TensorFlow CPU pode ser importado da seguinte forma:


```js
import * as tf from '@tensorflow/tfjs-node'
```


Ao importar TensorFlow.js à partir desse pacote, o módulo que você obtém será acelerado pelo binário do TensorFlow C e executado na CPU. TensorFlow na CPU usa aceleração do hardware para executar o cálculo de álgebra linear por debaixo dos panos.

Este pacote funcionará nas plataformas Linux, Windows e Mac nas quais o TensorFlow é suportado.

> Nota: Você não precisa importar '@tensorflow/tfjs' ou adicioná-lo ao seu package.json. Este pacote é importado indiretamente pela biblioteca do node.


## TensorFlow GPU

O pacote TensorFlow GPU pode ser importado da seguinte forma:


```js
import * as tf from '@tensorflow/tfjs-node-gpu'
```


Assim como o pacote CPU, o módulo que você obtém será acelarado pelo binário do TensorFlow C, no entanto, ele executará operações de tensores na GPU com CUDA e, portanto, apenas linux. Essa conexão pode ser, pelo menos em uma ordem de magnitude, mais rápida que as outras opções.

> Nota: Atualmente, este pacote funciona apenas com CUDA. Você precisa ter o CUDA instalado em sua máquina com uma placa gráfica NVIDIA antes de seguir esta rota.

> Nota: Você não precisa importar '@tensorflow/tfjs' ou adicioná-lo ao seu package.json. Este pacote é importado indiretamente pela biblioteca do node.


## CPU Vanilla

A versão do TensorFlow.js rodando com CPU vanilla pode ser importado da seguinte forma:


```js
import * as tf from '@tensorflow/tfjs'
```


Este pacote é o mesmo pacote que você usaria no navegador. Neste pacote, as operações são executadas com JavaScript vanilla na CPU. Este pacote é muito menor que os outros porque ele não precisa dos binários do TensorFlow, no entanto, é muito mais lento.

Como este pacote não depende do TensorFlow, ele pode ser usado em mais dispositivos compatíveis com Node.js do que apenas Linux, Windows e Mac.


## Considerações de produção

As ligações do Node.js fornecem um backend para TensorFlow.js que implementa operações de forma síncrona. Isso significa que quando você chama uma operação `tf.matMul(a, b)`, por exemplo, ele bloqueará a thread principal até que a operação seja concluída.

Por esta razão, as ligações atualmente são adequadas para script e tarefas offline. Se você deseja usar as ligações Node.js em produção, como em um servidor, você deve configurar uma fila de tarefas ou threads workers, para que seu código TensorFlow.js não bloqueie a thread principal.


## APIs

Depoir de importar o pacote como `tf` em qualquer das opções acima, todos os símbolos normais do TensorFlow.js aparecerão no módulo importado.


### tf.browser

No pacote TensorFlow.js normal, os símbolos no namespace `tf.browser.*` não serão úteis no Node.js, pois eles usam APIs específicas do navegador.

Atualmente, são eles:

*  tf.browser.fromPixels
*  tf.browser.toPixels


### tf.node

Os dois pacotes Node.js também fornecem um namespace, `tf.node`, que contém APIs específicas do Node.

TensorBoard é um exemplo notável das APIs específicas do Node.js.

Um exemplo de exportação de resumos para o TensorBoard no Node.js:


```js
const model = tf.sequential();
model.add(tf.layers.dense({ units: 1, inputShape: [200] }));
model.compile({
  loss: 'meanSquaredError',
  optimizer: 'sgd',
  metrics: ['MAE']
});


// Gera alguns dados falsos aleatórios com propósito demonstrativo.
const xs = tf.randomUniform([10000, 200]);
const ys = tf.randomUniform([10000, 1]);
const valXs = tf.randomUniform([1000, 200]);
const valYs = tf.randomUniform([1000, 1]);


// Inicial o processo de treinamento do modelo.
async function train() {
  await model.fit(xs, ys, {
    epochs: 100,
    validationData: [valXs, valYs],
    // Adiciona o callback do tensorBoard aqui.
    callbacks: tf.node.tensorBoard('/tmp/fit_logs_1')
  });
}
train();
```