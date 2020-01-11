# Plataforma e ambiente

TensorFlow.js funciona no navegador e no Node.js, e em ambas as plataformas existem muitas configurações diferente disponíveis. Cada plataforma tem um conjunto único de considerações que afetarão a forma como as aplicações são desenvolvidas.

No navegador, TensorFlow.js suporta dispositivos mobile e também computadores. Cada dispositivo tem um conjunto específico de restrições, como APIs WebGL disponíveis, que são automaticamente determinadas e configuradas para você.

No Node.js, TensorFlow.js oferece suporte à conexão diretamente à API do TensorFlow ou à execução mais lenta com implementações vanilla do CPU.


## Ambientes

Quando uma aplicação TensorFlow.js é executada, a configuração específica é chamada de ambiente. O ambiente é composto por um único backend global e por um conjunto de flags que controlam os recursos refinados do TensorFlow.js.


### Backends

O TensorFlow.js oferece suporte a vários backends diferentes que implementam armazenamento de tensores e operações matemáticas. A qualquer momento, apenas um backend está ativo. Na maioria das vezes, TensorFlow.js escolherá automaticamente o melhor backend para você de acordo com o ambiente atual. No entanto, às vezes é importante saber qual backend está sendo usado e como trocá-lo.

Para identificar qual backend você está usando:


```js
console.log(tf.getBackend());
```


Se você quer mudar o backend manualmente:


```js
tf.setBackend('cpu');
console.log(tf.getBackend());
```



#### Backend WebGL

O backend WebGL, 'webgl', é atualmente o backend mais poderoso para navegador. Este backend é até 100 vezes mais rápido que o backend CPU vanilla. Tensores são armazenados como texturas WebGL e operações matemáticas são implementadas nos shaders WebGL. Aqui estão algumas coisas úteis para saber ao usar este backend:



##### Evite bloquear a thread da interface do usuário

Quando uma operação é chamada, como tf.matMul(a, b), o tf.Tensor resultante é retornado de forma síncrona, no entanto, o cálculo da multiplicação de matrizes pode ainda não estar pronto. Isso significa que o tf.Tensor retornado é apenas um identificador para o cálculo. Quando você chama `x.data()` ou `x.array()`, os valores serão resolvidos quando o cálculo for realmente concluído. Isso torna importante o uso dos métodos assíncronos `x.data()` e `x.array()` sobre suas versões síncronas `x.dataSync()` e `x.arraySync()` para evitar o bloqueio da thread da interface do usuário enquanto o cálculo é concluído.


##### Gerenciamento de memória

Um obstáculo ao usar o backend WebGL é a necessidade do gerencimaneto explícito de memória. O WebGLTextures, que é onde os dados do Tensor são finalmente armazenados, não tem sua memória automaticamente coletada pelo navegador.

Para liberar/desalocar a memória de um `tf.Tensor`, você pode usar o método `dispose()`:


```js
const a = tf.tensor([[1, 2], [3, 4]]);
a.dispose();
```

É muito comum encadear várias operações juntas em uma aplicação. Manter uma referência para todos as variáveis intermediárias, para descartá-las, pode reduzir a ligibilidade do código. Para resolver este problema, TensorFlow.js fornece um método `tf.tidy()` que limpa todos os `tf.Tensor`s que não são retornados por uma função após executá-la, semelhante à maneira como as variáveis locais são limpas quando a função é executada:


```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```


> Note: não há desvantagem em usar `dispose()` ou `tidy()` em ambientes diferentes do WebGL (Como os backends Node.js ou CPU) que tem coleta de memória automática. De fato, muitas vezes pode ser uma conquista de desempenho liberar memória de tensor mais rapidamente do que aconteceria naturalmente com a coleta de memória.


##### Precisão

Em dispositivos móveis, WebGL pode suportar apenas texturas de ponto flutuante de 16 bits. No entanto, a maioria dos modelos de machine learning são treinados com pesos e ativações com ponto flutuante de 32 bits. Isso pode causar problemas de precisão ao portar um modelo para um dispositivo móvel, pois os números flutuantes de 16 bits podem representar apenas números no intervalo `[0.000000059605, 65504]`. Isso significa que você deve tomar cuidado para que os pesos e ativações em seu modelo não excedam esse intervalo. Para verificar se o dispositivo suporta texturas de 32 bits, verifique o valor de `tf.ENV.getBool('WEBGL_RENDER_FLOAT32_CAPABLE')`, se isso for falso, o dispositivo suporta apenas texturas de ponto flutuante de 16 bits. Você pode usar o `tf.ENV.getBool('WEBGL_RENDER_FLOAT32_ENABLED')` para verificar se o TensorFlow.js está atualmente usando texturas de 32bits.


##### Compilação de shader e atualização de textura

O TensorFlow.js executa operações na GPU rodando programas de sombreamento WebGL. Esses sombreadores (shaders) são montados e compilados lentamente quando o usuário pede para executar uma operação. A compilação de um shader acontece na thread principal na CPU e pode ser lenta. O TensorFlow.js armazenará em cache os shaders compilados automaticamente, tornando a segunda chamada para a mesma operação com tensores entrada e saída de mesmo formato muito mais rápida. Normalmente, aplicações TensorFlow.js usarão a mesma operação várias vezes durante o tempo de vida da aplicação, portanto, a segunda passagem por um modelo de machine learning é muito mais rápida.

O TensorFlow.js também armazena dados tf.Tensor como WebGLTextures. Quando um `tf.Tensor` é criado, não enviamos dados imediatamente para a GPU, mas mantemos os dados na CPU até que o `tf.Tensor` seja usado em uma operação. Se o `tf.Tensor` for usado uma segunda vez, os dados já estão na GPU, portanto não haverá custo de upload. Em um modelo típico de machine learning, isso significa que pesos são carregados durante a primeira predição através do modelo e a segunda passagem pelo modelo será muito mais rápida.

Se você se importa com o desempenho da primeira predição através do seu modelo ou código TensorFlow.js, nós recomendamos aquecer o modelo passando um Tensor de entrada do mesmo formato antes que dados reais sejam usados.

Por exemplo:


```js
const model = await tf.loadLayersModel(modelUrl);

// Aqueça o modelo antes de usar dados reais.
const warmupResult = model.predict(tf.zeros(inputShape));
warmupResult.dataSync();
warmupResult.dispose();

// O segundo predict() será muito mais rápido.
const result = model.predict(userData);
```



#### Backend TensorFlow Node.js

No backend TensorFlow Node.js, 'node', a API TensorFlow C é usada para acelerar as operações. Isso usará a aceleração de hardware disponível da máquina, como CUDA, se disponível.

Neste backend, assim como o backend WebGL, operações retornam `tf.Tensor`s síncronamente. Contudo, diferente do backend WebGL, a operação é concluída antes de você obter o tensor de volta. Isso significa que uma chamada para `tf.matMul(a, b)` bloqueará a thread da interface do usuário.

Por esta razão, se você pretende usá-lo em uma aplicação de produção, você deve executar TensorFlow.js em threads workers para não bloquear a thread principal.

Para mais informação sobre o Node.js, veja este guia.


#### Backend CPU

O backend CPU, 'cpu', é o backend com menos desempenho, mas é o mais simples. Operações são todas implementadas em JavaScript vanilla, o que as torna menos paralelizáveis. Eles também bloqueiam a thread da interface do usuário.

Esse backend pode ser muito útil para testes ou em dispositivos no quais WebGL não está disponível.


### Flags

O TensorFlow.js tem um conjunto de flags (sinalizadores) de ambiente que são automaticamente avaliadas e determinam a melhor configuração na plataforma atual. Essas flags são principalmente internas, mas algumas flags globais podem ser controladas com a API pública.

*   `tf.enableProdMode()`: Habilita o modo de produção, que removerá a validação do modelo, verificações de NaN, e outras verificações de correção a favor do desempenho.
*   `tf.enableDebugMode()`: Habilita o modo de debug, que registrará no console todas as operações executadas, além de informações de desempenho em tempo de execução, como presença de memória e tempo total de execução do kernel. Perceba que isso desacelerará bastante sua aplicação, não use isso em produção.

> Note: Estes dois métodos devem ser usados antes de usar qualquer outro código TensorFlow.js, pois afetam os valores de outras flags que serão armazenadas em cache. Pelo mesmo motivo, não há função análoga para "desativar".

> Note: Você pode ver todas as flags que foram avaliadas imprimindo `tf.ENV.features` no console. Embora esses **não façam parte da API pública** (E, portanto, não tenham garantia de estabilidade entre as versões), eles podem ser úteis para depurar ou ajustar o comportamento entre plataformas e dispositivos. Você pode usar o `tf.ENV.set` para substituir o valor de uma flag.