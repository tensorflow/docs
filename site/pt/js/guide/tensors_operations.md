# Tensores e Operações

TensorFlow.js é um framework para definir e executar computação usando tensores em JavaScript. Um *tensor* é uma generalização de vetores e matrizes para dimensões maiores.

## Tensores

A unidade central de dados em TensorFlow.js é o `tf.Tensor`: um conjunto de valores formatados dentro de um array de uma ou mais dimensões. `tf.Tensor`s são muito similares à arrays multidimensionais.

Um `tf.Tensor` também contém as seguintes propriedades:

*   `rank`: Define quantas dimensões tem o tensor.
*   `shape`: Que define o tamanho de cada dimensão do dado.
*   `dtype`: Que define o tipo de dado do tensor.

Note: Nós podemos usar o termo "dimensão" no lugar de rank. Às vezes, no aprendizado de máquina, "dimensionalidade" de um tensor também pode se referir ao tamanho de uma dimensão particular (Por exemplo, uma matriz de formato [10, 5] é um tensor rank-2, ou um tensor bidimensional. A dimensionalidade da primeira dimensão é 10. Isso pode ser confuso, mas colocamos essa nota aqui porque você provavelmente encontrará esses usos duplos do termo).

Um `tf.Tensor` pode ser criado a partir de um array com o método `tf.tensor()`:


```js
// Cria um tensor rank-2 (matriz) a partir de um array multidimensional.
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('shape:', a.shape);
a.print();

// Ou você pode criar um tensor a partir de um array "plano" e especificar o formato.
const shape = [2, 2];
const b = tf.tensor([1, 2, 3, 4], shape);
console.log('shape:', b.shape);
b.print();
```


Por padrão, `tf.Tensor`s terão `dtype` como `float32`. `tf.Tensor`s também podem ser criados com o dtype igual à bool, int32, complex64 e string:


```js
const a = tf.tensor([[1, 2], [3, 4]], [2, 2], 'int32');
console.log('shape:', a.shape);
console.log('dtype:', a.dtype);
a.print();
```


TensorFlow.js também fornece um conjunto de métodos convenientes para criar tensores aleatórios, tensores preenchidos com um valor específico, tensores a partir de `HTMLImageElement`s, e muito mais que você pode encontrar [aqui](https://js.tensorflow.org/api/latest/#Tensors-Creation).

#### Mudando o formato de um Tensor

O número de elementos em um `tf.Tensor` é o produto dos tamanhos em seu formato. Como muitas vezes podem haver múltiplas formas com o mesmo tamanho, é útil poder reformatar um `tf.Tensor` para outro formato com o mesmo tamanho. Isso pode ser feito com o método `reshape()`:


```js
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('a shape:', a.shape);
a.print();

const b = a.reshape([4, 1]);
console.log('b shape:', b.shape);
b.print();
```


#### Obtendo valores de um tensor

Você também pode obter os valores de um `tf.Tensor` usando os métodos `Tensor.array()` ou `Tensor.data()`:


```js
 const a = tf.tensor([[1, 2], [3, 4]]);
 // Retorna o array multidimensional de valores.
 a.array().then(array => console.log(array));
 // Retorna os dados vindos do tensor de forma "planificada".
 a.data().then(data => console.log(data));
```


Nós também fornecemos versões síncronas destes métodos que são mais simples de usar, mas que irão causar problemas de performance em sua aplicação. Você deve sempre preferir os métodos assíncronos em aplicações de produção.


```js
const a = tf.tensor([[1, 2], [3, 4]]);
// Retorna o array de valores multidimensional.
console.log(a.arraySync());
// Retorna os dados vindos do tensor de forma "planificada".
console.log(a.dataSync());
```



## Operações

Enquanto tensores permitem você armazenar dados, operações (ops) permitem você manipular estes dados. TensorFlow.js também fornece uma larga variedade de operações adequadas para álgebra linear e aprendizado de máquina que podem ser realizadas sobre tensores.

Exemplo: calcular x² de todos os elementos em um [tf.Tensor](link):


```js
const x = tf.tensor([1, 2, 3, 4]);
const y = x.square();  // Equivalennte à tf.square(x)
y.print();
```


Exemplo: adicionar elemento por elemento de dois `tf.Tensor`s:


```js
const a = tf.tensor([1, 2, 3, 4]);
const b = tf.tensor([10, 20, 30, 40]);
const y = a.add(b);  // Equivalente à tf.add(a, b)
y.print();
```


Como tensores são imutáveis, estas operações não mudam seus valores. Ao invés disso, o resultado de operações sempre retornam novos `tf.Tensor`s.

> Note: A maioria das operações retornam `tf.Tensor`s, no entanto, o resultado pode não estar pronto ainda. Isso significa que o `tf.Tensor` que você obtém é, na verdade, um identificador para o cálculo. Quando você chama `Tensor.data()` ou `Tensor.array()`, estes métodos retornam promises que resolvem com valores apenas quando o cálculo é finalizado. Ao executar em um contexto de interface do usuário (Como um aplicativo de navegador), você sempre deve preferir as versões assíncronas destes métodos em vez de suas contrapartes síncronas para evitar bloquear a thread da interface do usuário até que o cálculo seja concluído.

Você pode encontrar a lista de operações que o TensorFlow.js suporta [aqui](https://js.tensorflow.org/api/latest/#Operations).


## Memória

Ao usar o backend WebGL, a memória de um `tf.Tensor` deve ser gerenciada explicitamente (**Não é suficiente** deixar um `tf.Tensor` sair do sair para que sua memória seja liberada).

Para liberar/desalocar a memória de um `tf.Tensor`, você pode usar o método `dispose()` ou `tf.dispose()`:


```js
const a = tf.tensor([[1, 2], [3, 4]]);
a.dispose(); // Equivalente à tf.dispose(a)
```


É muito comum encadear várias operações juntas em uma aplicação. Manter uma referência para todos as variáveis intermediárias, para descartá-las, pode reduzir a ligibilidade do código. Para resolver este problema, TensorFlow.js fornece um método `tf.tidy()` que limpa todos os `tf.Tensor`s que não são retornados por uma função após executá-la, semelhante à maneira como as variáveis locais são limpas quando a função é executada:


```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```


Neste exemplo, o resultado de `square()` e `log()` serão automaticamente descartados. O resultado de `neg()` não será descartado já que é o valor de retorno de tf.tidy().

Você também pode obter o número de Tensores monitorados pelo TensorFlow.js:


```js
console.log(tf.memory());
```


O objeto impresso por `tf.memory()` conterá informação sobre quanta memória está atualmente alocada. Você pode encontrar mais informação [aqui](https://js.tensorflow.org/api/latest/#memory).