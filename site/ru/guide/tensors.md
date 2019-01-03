# Tensors

TensorFlow, as the name indicates, is a framework to define and run computations
involving tensors. A tensor is a generalization of vectors and matrices to
potentially higher dimensions. Internally, TensorFlow represents tensors as
n-dimensional arrays of base datatypes.

Как понятно из названия, TensorFlow ("поток тензоров") - это фреймворк для определения 
и вычисления операций с тензорами. Тензор - это обобщенное название векторов и матриц,
вплоть до потенциально высоких размерностей. Во внутренней структуре TensorFlow
векторы представлены как n-размерные массивы примитивных типов данных.

When writing a TensorFlow program, the main object you manipulate and pass
around is the `tf.Tensor`. A `tf.Tensor` object represents a partially defined
computation that will eventually produce a value. TensorFlow programs work by
first building a graph of `tf.Tensor` objects, detailing how each tensor is
computed based on the other available tensors and then by running parts of this
graph to achieve the desired results.

При написании программы в TensorFlow, ключевым объектом всех операций является
`tf.Tensor`. Этот объект представляет собой частично определенное вычисление,
которое в конечном итоге выдаст какое-либо значение. Программа TensorFlow
сначала строит граф объектов `tf.Tensor`, детализирует как каждый тензор будет
вычисляться на других доступных тензорах, а затем запускает построение этого
графа для получения желаемых результатов.

Объект `tf.Tensor` имеет следующие параметры:



 * тип данных (например`float32`, `int32`, или `string`)
 * размерность (a shape)


Each element in the Tensor has the same data type, and the data type is always
known. The shape (that is, the number of dimensions it has and the size of each
dimension) might be only partially known. Most operations produce tensors of
fully-known shapes if the shapes of their inputs are also fully known, but in
some cases it's only possible to find the shape of a tensor at graph execution
time.

Каждый элемент в тензоре имеет одинаковый тип данных, и этот тип всегда известен.
Размерность, которая определяется количеством размерностей и размером каждого
массива, может быть известна частично. Большинство операций производят
тензоры полностью известных размерностей, если эти входные размерности также
известны, но в некоторых случаях узнать размерность тензора можно только в режиме
graph execution.

Some types of tensors are special, and these will be covered in other
units of the TensorFlow guide. The main ones are:

Некоторые типы тензоров являются специализированными, и будут описаны в
других статьях руководства по TensorFlow. Ключевыми являются:

  * `tf.Variable`
  * `tf.constant`
  * `tf.placeholder`
  * `tf.SparseTensor`

With the exception of `tf.Variable`, the value of a tensor is immutable, which
means that in the context of a single execution tensors only have a single
value. However, evaluating the same tensor twice can return different values;
for example that tensor can be the result of reading data from disk, or
generating a random number.

За исключением `tf.Variable`, значение тензора является неизменным, что означает
в контексте единичного вычисления тензор будет иметь всего одно значение. Однако,
при расчете одного и того же тензора дважды, он может возвращать разные значения;
например, тензор может быть результатом прочтения данных с диска, или случайно
сгенерированного числа.


## Ранг

The **rank** of a `tf.Tensor` object is its number of dimensions. Synonyms for
rank include **order** or **degree** or **n-dimension**.
Note that rank in TensorFlow is not the same as matrix rank in mathematics.
As the following table shows, each rank in TensorFlow corresponds to a
different mathematical entity:

**Ранг** объекта `tf.Tensor` - это количество размерностей массива. Синонимомами
ранга являются **порядок**, **степень** или **n-размерность**.
Обрати внимание, что ранг в TensorFlow это не то же самое, что ранг матрицы в
математике. Из следующей таблицы видно, что каждый ранг в TensorFlow соответствует
разным математическим категориям:

Ранг | Математическая категория
--- | ---
0 | Scalar (magnitude only)
1 | Vector (magnitude and direction)
2 | Matrix (table of numbers)
3 | 3-Tensor (cube of numbers)
n | n-Tensor (you get the idea)

Ранг | Математическая категория
--- | ---
0 | Скаляр (только величина)
1 | Вектор (величина и направление)
2 | Матрица (таблица чисел)
3 | 3-Тензор (куб чисел)
n | n-Тензор (ты понял идею)


### Ранг 0

The following snippet demonstrates creating a few rank 0 variables:

Следующий пример кода демонстрирует создание нескольких переменных
ранга 0:

```python
mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)
```

Note: A string is treated as a single item in TensorFlow, not as a sequence of
characters. It is possible to have scalar strings, vectors of strings, etc.

Обрати внимание: строка в TensorFlow является одним объектом, а не последовательностью
символов. Возможно также использовать скалярные строки, вектор строк и так далее.

### Ранг 1

To create a rank 1 `tf.Tensor` object, you can pass a list of items as the
initial value. For example:

Чтобы создать объект `tf.Tensor` ранга 1, ты можешь передать список элементов
как первичное значение. Например:

```python
mystr = tf.Variable(["Hello"], tf.string)
cool_numbers  = tf.Variable([3.14159, 2.71828], tf.float32)
first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)
```


### Higher ranks
### Высшие ранги

A rank 2 `tf.Tensor` object consists of at least one row and at least
one column:

Ранг 2 объекта `tf.Tensor` состоит из как минимум одного ряда и одного
столбца:

```python
mymat = tf.Variable([[7],[11]], tf.int16)
myxor = tf.Variable([[False, True],[True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)
mymatC = tf.Variable([[7],[11]], tf.int32)
```

Higher-rank Tensors, similarly, consist of an n-dimensional array. For example,
during image processing, many tensors of rank 4 are used, with dimensions
corresponding to example-in-batch, image width, image height, and color channel.

Тензоры высшего ранга подобным образом состоят из n-размерных массивов. Например,
во время обработки изображения используются тензоры ранга 4 с соответствующими
им размерносятми примеров в батче, шириной и высотой изображения, и цветовой модели.

``` python
my_image = tf.zeros([10, 299, 299, 3])  # batch x height x width x color
```

### Getting a `tf.Tensor` object's rank
### Получаем ранг объекта `tf.Tensor`

To determine the rank of a `tf.Tensor` object, call the `tf.rank` method.
For example, the following method programmatically determines the rank
of the `tf.Tensor` defined in the previous section:

Чтобы определить ранг объекта `tf.Tensor`, вызови метод `tf.rank`. Например,
следующий метод программным способом определит ранг `tf.Tensor`, определенного
в предыдущем блоке кода:

```python
r = tf.rank(my_image)
# After the graph runs, r will hold the value 4.
# После запуска графа, r присвоится значения 4.
```

### Referring to `tf.Tensor` slices
### Работаем с частями `tf.Tensor`

Since a `tf.Tensor` is an n-dimensional array of cells, to access a single cell
in a `tf.Tensor` you need to specify n indices.

Поскольку `tf.Tensor` является n-размерным массивом элементов, для доступа к
конкретному элементу `tf.Tensor` потребуется уточнить индексы n.

For a rank 0 tensor (a scalar), no indices are necessary, since it is already a
single number.

Для тензора ранг 0 (скалярного) не требуется никаких индексов, посколько это
уже одно единственное значение.

For a rank 1 tensor (a vector), passing a single index allows you to access a
number:

Для тензора ранга 1 (вектора) потребуется передать всего один индекс, который
предоставит нам доступ к значению:

```python
my_scalar = my_vector[2]
```

Note that the index passed inside the `[]` can itself be a scalar `tf.Tensor`, if
you want to dynamically choose an element from the vector.

Обрати внимание, что индекс, передаваемый внутри `[]`, может сам быть скалярным
`tf.Tensor`, если ты хочешь динамически выбирать элементы из вектора.

For tensors of rank 2 or higher, the situation is more interesting. For a
`tf.Tensor` of rank 2, passing two numbers returns a scalar, as expected:

С тензорами ранга 2 и выше ситуация более интересная. Передавая два значения
`tf.Tenosor` ранга 2, он возвращает скаляр, что ожидаемо:

```python
my_scalar = my_matrix[1, 2]
```


Passing a single number, however, returns a subvector of a matrix, as follows:

Однако, передвая одно единственное значение, он возвращает подвектор матрицы как
в этом примере:


```python
my_row_vector = my_matrix[2]
my_column_vector = my_matrix[:, 3]
```

The `:` notation is python slicing syntax for "leave this dimension alone". This
is useful in higher-rank Tensors, as it allows you to access its subvectors,
submatrices, and even other subtensors.

Нотация `:` в Python делит синтаксис, оставляя эту размерность "в покое". Этот
прием полезен при работе с тензорами высшего ранга, поскольку предоставляет
доступ к его подвекторам, подматрицам и даже подтензорам.


## Shape
## Форма

The **shape** of a tensor is the number of elements in each dimension.
TensorFlow automatically infers shapes during graph construction. These inferred
shapes might have known or unknown rank. If the rank is known, the sizes of each
dimension might be known or unknown.

**Форма** тензора - это количество элементов в каждой размерности.
TensorFlow автоматически назначает формы во время работы в graph execution.
Назначенные формы могут иметь известный или неизвестный ранг. Если ранг
известен, то элементы каждой размерности также могут быть известны или
неизвестны.

The TensorFlow documentation uses three notational conventions to describe
tensor dimensionality: rank, shape, and dimension number. The following table
shows how these relate to one another:

В документации TensorFlow используются три правила для описания размерности
тензоров: ранг, форма и номер размерности. В следующией таблице видно, как эти
три параметра соотносятся друг с другом:

Rank | Shape | Dimension number | Example
--- | --- | --- | ---
0 | [] | 0-D | A 0-D tensor.  A scalar.
1 | [D0] | 1-D | A 1-D tensor with shape [5].
2 | [D0, D1] | 2-D | A 2-D tensor with shape [3, 4].
3 | [D0, D1, D2] | 3-D | A 3-D tensor with shape [1, 4, 3].
n | [D0, D1, ... Dn-1] | n-D | A tensor with shape [D0, D1, ... Dn-1].

Ранг | Форма | Номер размерности | Пример
--- | --- | --- | ---
0 | [] | 0-D | Тензор 0-D .  Скаляр.
1 | [D0] | 1-D | Тензор 1-D формы [5].
2 | [D0, D1] | 2-D | Тензор 2-D формы [3, 4].
3 | [D0, D1, D2] | 3-D | Тензор 3-D формы [1, 4, 3].
n | [D0, D1, ... Dn-1] | n-D | Тензор формы [D0, D1, ... Dn-1].

Shapes can be represented via Python lists / tuples of ints, or with the
`tf.TensorShape`.

Формы могут быть представлены в Python как списки или кортежи целых чисел,
или как `tf.TensorShape`

### Getting a `tf.Tensor` object's shape
### Получаем форму объекта `tf.Tensor`

There are two ways of accessing the shape of a `tf.Tensor`. While building the
graph, it is often useful to ask what is already known about a tensor's
shape. This can be done by reading the `shape` property of a `tf.Tensor` object.
This method returns a `TensorShape` object, which is a convenient way of
representing partially-specified shapes (since, when building the graph, not all
shapes will be fully known).

Есть два способа получить форму `tf.Tensor`. Во время построения графа часто
является полезным узнать, что уже известно о форме тензора. Это можно сделать
прочтя параметр `shape` объека `tf.Tensor`. Этот метод возвращает объект
`TensorShape`, который является весьма удобным способом представления
частично определенных форм, поскольку во время построения графа не все формы
известны полностью.

It is also possible to get a `tf.Tensor` that will represent the fully-defined
shape of another `tf.Tensor` at runtime. This is done by calling the `tf.shape`
operation. This way, you can build a graph that manipulates the shapes of
tensors by building other tensors that depend on the dynamic shape of the input
`tf.Tensor`.

Также возможно получить `tf.Tensor`, который будет представлять полностью
определенную форму другого объекта `tf.Tensor` в рабочей среде. Это достигается
путем вызова операции `tf.shape`. Таким образом ты можешь построить граф, который
манипулирует формами тензоров при помощи создания других тензоров, который зависят
от динамической формы входящего `tf.Tensor`.

For example, here is how to make a vector of zeros with the same size as the
number of columns in a given matrix:

Например, вот как мы можем сделать вектор нулей с одинаковым размером и числом
столбцов в матрице:

``` python
zeros = tf.zeros(my_matrix.shape[1])
```

### Changing the shape of a `tf.Tensor`
### Изменяем форму `tf.Tensor`

The **number of elements** of a tensor is the product of the sizes of all its
shapes. The number of elements of a scalar is always `1`. Since there are often
many different shapes that have the same number of elements, it's often
convenient to be able to change the shape of a `tf.Tensor`, keeping its elements
fixed. This can be done with `tf.reshape`.

**Количество элементов** тензора является продуктом размеров их форм. Количество
элементов - это скаляр, который всегда равен `1`. Посколько часто множесто разных
форм имеют одинаковое количество элементов, то часто удобно позволять менять форму
`tf.Tensor`, зафиксировав его элементы. Это можно сделать с помощью `tf.reshape`.

The following examples demonstrate how to reshape tensors:

В следующем примере показано как изменить форму тензоров:

```python
rank_three_tensor = tf.ones([3, 4, 5])
matrix = tf.reshape(rank_three_tensor, [6, 10])  # Reshape existing content into Изменяем существующую форму на
                                                 # a 6x10 matrix матрицу 6x10
matrixB = tf.reshape(matrix, [3, -1])  #  Reshape existing content into a 3x20 Изменяем форму на матрицу 3х20
                                       # matrix. -1 tells reshape to calculate -1 требует `reshape` рассчитать
                                       # the size of this dimension. размерность тензора.
matrixAlt = tf.reshape(matrixB, [4, 3, -1])  # Reshape existing content into a Изменяет форму на
                                             #4x3x5 tensor тензор 4х3х5

# Note that the number of elements of the reshaped Tensors has to match the
# original number of elements. Therefore, the following example generates an
# error because no possible value for the last dimension will match the number
# of elements.
# Обрати внимание, что количество элементов измененных тензоров должно совпадать
# с изначальным количеством элементов. Таким образом, следующий пример выдает
# ошибку, так как нет значения для последней размерности, которое бы совпадало
# с количеством элементов.
yet_another = tf.reshape(matrixAlt, [13, 2, -1])  # ERROR!
```

## Типы данных

In addition to dimensionality, Tensors have a data type. Refer to the
`tf.DType` page for a complete list of the data types.

В дополнение к размерностям, тензоры имеют тип данных. Смотри документацию
[`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType) для
ознакомления с полным списком типов данных.

It is not possible to have a `tf.Tensor` with more than one data type. It is
possible, however, to serialize arbitrary data structures as `string`s and store
those in `tf.Tensor`s.

Невозможно иметь `tf.Tensor` более чем с одним типом данных. Тем не менее возможно
сериализовать произвольные структуры данных как строки и сохранить их в `tf.Tensor`.

It is possible to cast `tf.Tensor`s from one datatype to another using
`tf.cast`:

Также возможно перенести тип данных из одного `tf.Tensor` в другой при помощи
метода `tf.cast`:

``` python
# Cast a constant integer tensor into floating point.
# Переводим константу тензора в число с плавающей запятой.
float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype=tf.float32)
```

To inspect a `tf.Tensor`'s data type use the `Tensor.dtype` property.

Для проверки тип данных `tf.Tensor` используй параметр `Tensor.dtype`.

When creating a `tf.Tensor` from a python object you may optionally specify the
datatype. If you don't, TensorFlow chooses a datatype that can represent your
data. TensorFlow converts Python integers to `tf.int32` and python floating
point numbers to `tf.float32`. Otherwise TensorFlow uses the same rules numpy
uses when converting to arrays.

## Evaluating Tensors

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
Graphs and Sessions for more information).

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

## Printing Tensors

For debugging purposes you might want to print the value of a `tf.Tensor`. While
 [tfdbg](../guide/debugger.md) provides advanced debugging support, TensorFlow also has an
 operation to directly print the value of a `tf.Tensor`.

Note that you rarely want to use the following pattern when printing a
`tf.Tensor`:

``` python
t = <<some tensorflow operation>>
print(t)  # This will print the symbolic tensor when the graph is being built.
          # This tensor does not have a value in this context.
```

This code prints the `tf.Tensor` object (which represents deferred computation)
and not its value. Instead, TensorFlow provides the `tf.Print` operation, which
returns its first tensor argument unchanged while printing the set of
`tf.Tensor`s it is passed as the second argument.

To correctly use `tf.Print` its return value must be used. See the example below

``` python
t = <<some tensorflow operation>>
tf.Print(t, [t])  # This does nothing
t = tf.Print(t, [t])  # Here we are using the value returned by tf.Print
result = t + 1  # Now when result is evaluated the value of `t` will be printed.
```

When you evaluate `result` you will evaluate everything `result` depends
upon. Since `result` depends upon `t`, and evaluating `t` has the side effect of
printing its input (the old value of `t`), `t` gets printed.

