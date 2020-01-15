# TensorFlow tensors

TensorFlow, как видно из названия, является платформой для определения и выполнения вычислений 
с использованием тензоров. *Тензор* - это обобщение векторов и матриц на более высокие 
измерения. Внутри TensorFlow тензоры представлены в виде n-мерных массивов 
базовых типов данных.

При написании программы TensorFlow основным объектом, которым вы манипулируете и передаете, 
является `tf.Tensor`. Объект `tf.Tensor` представляет собой частично определенное 
вычисление, которое в итоге дает результат вычислений. Программы TensorFlow работают,
сначала создавая граф объектов `tf.Tensor` и подробно описывая, как вычисляется каждый 
тензор  на основе других доступных тензоров, а затем запуская части этого 
графа для получения результатов вычисления.

`tf.Tensor` обладает следующими свойствами:

 * тип данных (`float32`, `int32`, или `string`, например)
 * размеры (shape)

Все элементы Tensor-а имеют одинаковый тип данных, и он всегда известен. 
Размеры (количество измерений и размер каждого измерения) 
могут быть известны только частично. Большинство операций производятся тензорами
с известными размерами, если размеры их входов также полностью известны, но в некоторых
случаях узнать размеры тензора можно только во время исполнения графа.

Есть несколько специальных видов тензоров, они будут рассмотрены в других 
разделах руководства TensorFlow. Основные виды тензоров следующие:

  * `tf.Variable`
  * `tf.constant`
  * `tf.placeholder`
  * `tf.SparseTensor`

За исключением `tf.Variable`, значение тензора неизменяемо, т.е.
в контексте одного выполнения тензором может иметь только одно значение.
Однако вычисление одного и того же тензора дважды может вернуть различные значения;
например, тот тензор может быть результатом чтения данных с диска, или 
генерации случайного числа.

## Ранг

**Ранг** объекта `tf.Tensor` это количество его измерений. Синонимы ранга
включают **порядок**, **степень**, **размерность**.
Обратите внимание, что ранг в TensorFlow это не то же самое, что 
и ранг матрицы в математике.
Как показывает следующая таблица, каждый ранг в Tensorflow соотвествует
некоторой математической сущности:

Ранг | Математическая сущность
--- | ---
0 | Скаляр (только величина)
1 | Вектор (величина и направление)
2 | Матрица (таблица чисел)
3 | 3-Тензор (куб чисел)
n | n-Тензор (ну вы поняли идею)


### Ранг 0

Следующий фрагмент демонстрирует создание нескольких переменных ранга 0:

```python
mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)
```

Замечание: Строка считается единым объектом в TensorFlow, не последовательностью
символов. Возможно иметь строковые скаляры, векторы строк и т.д..

### Ранг 1

Для создания объекта `tf.Tensor` ранга 1, вы можете передать список элементов
в качестве начальных значений. Например:

```python
mystr = tf.Variable(["Hello"], tf.string)
cool_numbers  = tf.Variable([3.14159, 2.71828], tf.float32)
first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)
```


### Ранги более высокого порядка

Ранг 2 объекта `tf.Tensor` состоит как минимум из одной 
строки и одного столбца:

```python
mymat = tf.Variable([[7],[11]], tf.int16)
myxor = tf.Variable([[False, True],[True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)
mymatC = tf.Variable([[7],[11]], tf.int32)
```

Тензоры более высокого ранга, аналогично, состоят из n-мерных массивов. Например,
при обработке изображений используется много тензоров ранга 4, с размерностями
соответствующими номеру примера в пакете, высоте изображения, ширине изображения, и цветовому каналу.

``` python
my_image = tf.zeros([10, 299, 299, 3])  # размер пакета x высота x ширина x количество цветовых каналов
```

### Получение ранга объекта `tf.Tensor` 

Для определения ранга объекта `tf.Tensor`, вызовите метод `tf.rank`.
Например, следующий метод программно определяет ранг
 `tf.Tensor` заданного выше:

```python
r = tf.rank(my_image)
# После запуска графа, r станет равным 4.
```

### Ссылки на слои `tf.Tensor`

Поскольку `tf.Tensor` это n-мерный массив ячеек, для получения доступа к одной ячейке
в `tf.Tensor` вам нужно указать n индексов.

Для тензоров ранга 0 (скаляров), индексы не нужны, поскольку это уже
просто число.

Для тензора ранга 1 (вектор), передача единственного индекса даст вам доступ
к числу:

```python
my_scalar = my_vector[2]
```

Заметьте что индекс передаваемый в `[]` может сам быть скаляром `tf.Tensor`, если
вы хотите динамически выбрать элемент из вектора.

Для тензоров ранга 2 или выше ситуация интереснее. Для
`tf.Tensor` ранга 2, передача двух чисел возвращает как и ожидалось скаляр:


```python
my_scalar = my_matrix[1, 2]
```


Передача одного числа, однако, возвращает подвектор матрицы следующим образом:


```python
my_row_vector = my_matrix[2]
my_column_vector = my_matrix[:, 3]
```

Нотация `:` в синтаксисе выделения подмассива в python используется как "оставьте это измерение в покое". 
Это полезно в тензорах высокого ранга, поскольку позволяет получить доступ к подвекторам,
подматрицам и даже другим подтензорам.


## Размеры

**Размеры** тензора это количество элементов в каждом измерении.
TensorFlow автоматически выводит размеры по ходу построения графа. Эти выведенные
размеры могут иметь известный или неизвестный ранг. Если ранг известен, размеры тензора
по каждому измерению могут быть известны или неизвестны.

Документация TensorFlow использует три условных обозначения для описания
размерности тензора: ранг, размеры и количество измерений. Следующая таблица
показывает как они соотносятся друг с другом:

Ранг | Размеры | Количество измерений | Пример
--- | --- | --- | ---
0 | [] | 0-D | 0-D тензор.  Скаляр.
1 | [D0] | 1-D | 1-D тензор размера [5].
2 | [D0, D1] | 2-D | 2-D тензор размера [3, 4].
3 | [D0, D1, D2] | 3-D | 3-D тензор размера [1, 4, 3].
n | [D0, D1, ... Dn-1] | n-D | Тензор размера [D0, D1, ... Dn-1].

Размеры могут быть представлены в виде списковPython / кортежей целых чисел, или с
`tf.TensorShape`.

### Получение размера объекта `tf.Tensor`

There are two ways of accessing the shape of a `tf.Tensor`. While building the
graph, it is often useful to ask what is already known about a tensor's
shape. This can be done by reading the `shape` property of a `tf.Tensor` object.
This method returns a `TensorShape` object, which is a convenient way of
representing partially-specified shapes (since, when building the graph, not all
shapes will be fully known).

It is also possible to get a `tf.Tensor` that will represent the fully-defined
shape of another `tf.Tensor` at runtime. This is done by calling the `tf.shape`
operation. This way, you can build a graph that manipulates the shapes of
tensors by building other tensors that depend on the dynamic shape of the input
`tf.Tensor`.

For example, here is how to make a vector of zeros with the same size as the
number of columns in a given matrix:

``` python
zeros = tf.zeros(my_matrix.shape[1])
```

### Changing the shape of a `tf.Tensor`

The **number of elements** of a tensor is the product of the sizes of all its
shapes. The number of elements of a scalar is always `1`. Since there are often
many different shapes that have the same number of elements, it's often
convenient to be able to change the shape of a `tf.Tensor`, keeping its elements
fixed. This can be done with `tf.reshape`.

The following examples demonstrate how to reshape tensors:

```python
rank_three_tensor = tf.ones([3, 4, 5])
matrix = tf.reshape(rank_three_tensor, [6, 10])  # Reshape existing content into
                                                 # a 6x10 matrix
matrixB = tf.reshape(matrix, [3, -1])  #  Reshape existing content into a 3x20
                                       # matrix. -1 tells reshape to calculate
                                       # the size of this dimension.
matrixAlt = tf.reshape(matrixB, [4, 3, -1])  # Reshape existing content into a
                                             #4x3x5 tensor

# Note that the number of elements of the reshaped Tensors has to match the
# original number of elements. Therefore, the following example generates an
# error because no possible value for the last dimension will match the number
# of elements.
yet_another = tf.reshape(matrixAlt, [13, 2, -1])  # ERROR!
```

## Data types

In addition to dimensionality, Tensors have a data type. Refer to the
`tf.DType` page for a complete list of the data types.

It is not possible to have a `tf.Tensor` with more than one data type. It is
possible, however, to serialize arbitrary data structures as `string`s and store
those in `tf.Tensor`s.

It is possible to cast `tf.Tensor`s from one datatype to another using
`tf.cast`:

``` python
# Cast a constant integer tensor into floating point.
float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype=tf.float32)
```

To inspect a `tf.Tensor`'s data type use the `Tensor.dtype` property.

When creating a `tf.Tensor` from a python object you may optionally specify the
datatype. If you don't, TensorFlow chooses a datatype that can represent your
data. TensorFlow converts Python integers to `tf.int32` and python floating
point numbers to `tf.float32`. Otherwise TensorFlow uses the same rules numpy
uses when converting to arrays.

## Evaluate tensors

Once the computation graph has been built, you can run the computation that
produces a particular `tf.Tensor` and fetch the value assigned to it. This is
often useful for debugging as well as being required for much of TensorFlow to
work.

The simplest way to evaluate a Tensor is using the `Tensor.eval` method. For
example:

```python
constant = tf.constant([1, 2, 3])
tensor = constant * constant
print(tensor.eval())
```

The `eval` method only works when a default `tf.Session` is active (see
[Graphs and Sessions](./graphs.md) for more information).

`Tensor.eval` returns a numpy array with the same contents as the tensor.

Sometimes it is not possible to evaluate a `tf.Tensor` with no context because
its value might depend on dynamic information that is not available. For
example, tensors that depend on `placeholder`s can't be evaluated without
providing a value for the `placeholder`.

``` python
p = tf.placeholder(tf.float32)
t = p + 1.0
t.eval()  # This will fail, since the placeholder did not get a value.
t.eval(feed_dict={p:2.0})  # This will succeed because we're feeding a value
                           # to the placeholder.
```

Note that it is possible to feed any `tf.Tensor`, not just placeholders.

Other model constructs might make evaluating a `tf.Tensor`
complicated. TensorFlow can't directly evaluate `tf.Tensor`s defined inside
functions or inside control flow constructs. If a `tf.Tensor` depends on a value
from a queue, evaluating the `tf.Tensor` will only work once something has been
enqueued; otherwise, evaluating it will hang. When working with queues, remember
to call `tf.train.start_queue_runners` before evaluating any `tf.Tensor`s.
