# Conversão de modelo

TensorFlow.js vem com uma variedade de modelos pré-treinados que estão prontos para uso no navegador - eles podem ser encontrados em nosso [repositório de modelos](https://github.com/tensorflow/tfjs-models). No entanto, você pode ter encontrado ou criado um modelo TensorFlow em outro lugar que gostaria de usar em seu aplicativo web. O TensorFlow.js fornece um modelo [conversor](https://github.com/tensorflow/tfjs/tree/master/tfjs-converter) para essa finalidade. O conversor possui dois componentes:

1.  Um utilitário de linha de comando que converte modelos Keras e TensorFlow para uso no TensorFlow.js.
2.  Uma API para carregar e executar o modelo no navegador com TensorFlow.js.


## Converta seu modelo

O conversor TensorFlow.js funciona com vários formatos de modelo diferentes:

**SavedModel**: Esse é o formato padrão em que modelos TensorFlow são salvos. O formato SavedModel é documentado [aqui](https://www.tensorflow.org/guide/saved_model).

**Modelo Keras**: Modelos Keras são geralmente salvos como um arquivo HDF5. Mais informações sobre salvar modelos Keras podem ser encontradas [aqui](https://keras.io/getting-started/faq/#savingloading-whole-models-architecture-weights-optimizer-state).

**Módulos do TensorFlow Hub**: Esses são modelos que foram empacotados para distribuição no TensorFlow Hub, uma plataforma para compartilhar e descobrir modelos. A biblioteca de modelos pode ser encontrada [aqui](https://tfhub.dev/).


Depending on which type of model you’re trying to convert, you’ll need to pass different arguments to the converter. For example, let’s say you have saved a Keras model named `model.h5` to your `tmp/` directory. To convert your model using the TensorFlow.js converter, you can run the following command:

Dependendo do tipo de modelo que você está tentando converter, será necessário passar diferentes argumentos para o conversor. Por exemplo, vamos dizer que você salvou um modelo Keras chamado `model.h5` em seu diretório `tmp/`. Para converter seu modelo usando o conversor TensorFlow.js, você pode executar o seguinte comando:


```
$ tensorflowjs_converter --input_format=keras /tmp/model.h5 /tmp/tfjs_model 
```


Isso converterá o modelo em `/tmp/model.h5` e produzirá um arquivo `model.json` junto com os arquivos binários de pesos para seu diretório `/tmp/tfjs_model`.

Mais detalhes sobre os argumentos de linha de comando correspondentes aos diferentes formatos de modelo podem ser encontrados no [README](https://github.com/tensorflow/tfjs/tree/master/tfjs-converter) do conversor TensorFlow.js.

Durante o processo de conversão, percorremos o grafo do modelo e verificamos se cada operação é suportada pelo TensorFlow.js. Nesse caso, escrevemos o grafo em um formato que o navegador possa consumir. Tentamos otimizar o modelo para ser servido na web dividindo os pesos em arquivos de 4MB - para que eles possam ser cacheados pelos navegadores. Nós também tentamos simplificar o próprio grafo do modelo usando o projeto open source [Grappler](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/grappler). As simplificações do grafo incluem dobrar operações adjacentes, eliminar subgrafos comuns, etc. Essas mudanças não tem efeito sobre as operações do modelo. Para otimização adicional, os usuários podem passar um argumento que instrui o conversor a quantizar o modelo para um determinado tamanho de bytes. Quantização é uma técnica para reduzir o tamanho do modelo representando os pesos com menos bits. Os usuários devem ter cuidado para garantir que o seu modelo mantenha um grau aceitável de precisão depois da quantização.

Se encontrarmos uma operação não suportada durante a conversão, o processo falhará e imprimiremos o nome da operação para o usuário. Sinta-se à vontade para submeter uma issue em nosso [GitHub](https://github.com/tensorflow/tfjs/issues) para nos informar sobre o assunto - nós tentamos implementar novas operações em reposta à demanda do usuário.


### Melhores práticas

Embora façamos todo esforço para otimizar seu modelo durante a conversão, geralmente a melhor forma de garantir que seu modelo tenha um bom desempenho é construí-lo com ambientes de recursos limitados em mente. Isso significa evitar arquiteturas excessivamente complexas e minimizar o número de parâmetros quando possível.


## Execute seu modelo

Após a conversão bem sucedida do seu modelo, você terá um conjunto de arquivos de pesos e um arquivo da topologia do modelo. O TensorFlow.js fornece APIs de carregamento de modelo que você pode usar para buscar esses arquivos do modelo e executar inferências no navegador.

Veja como é a API de um módulo TensorFlow Hub ou SavedModel TensorFlow convertido:


```js
const model = await tf.loadGraphModel(‘path/to/model.json’);
```


E eis o código de um modelo Keras convertido:


```js
const model = await tf.loadLayersModel(‘path/to/model.json’);
```


A API `tf.loadGraphModel` retorna um `tf.FrozenModel`, que significa que os parâmetros são fixados e você não poderá refinar seu modelo com novos dados. A API `tf.loadLayersModel` returna um `tf.Model`, que pode ser treinado. Para informação sobre como treinar um `tf.Model`, consulte o guia  de [treinamento de modelos](train_models.md).

Depois da conversão, é recomendável executar inferências algumas vezes e comparar a velocidade do seu modelo. Nós temos uma página de benchmarking que pode ser usada para esse propósito: https://github.com/tensorflow/tfjs-core/blob/master/integration_tests/benchmarks/benchmark.html. Você pode perceber que descartamos medidas de uma execução de aquecimento inicial - Isso é porque (em geral), a primeira inferência do seu modelo será muito mais lenta que as inferências subsequentes devido à sobrecarga da criação de texturas e compilação de shaders.