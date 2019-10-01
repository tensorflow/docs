# 텐서플로 텐서

이름에서 알 수 있듯이, 텐서플로는 텐서를 포함한 계산을 정의하고 실행하는 프레임워크입니다.
*텐서*는 벡터와 행렬을 일반화한 것이고 고차원으로 확장가능합니다.
내부적으로 텐서플로는 텐서를 n-차원의 기본 데이터형식의 배열로 표현합니다.

텐서플로 프로그램을 작성할 때, 조작하고 전달하는 중요 객체는 `tf.Tensor`입니다.
`tf.Tensor` 객체는 부분적으로 결과적으로는 값으로 변환될 수 있는 계산으로 표현됩니다.
텐서플로 프로그램은  `tf.Tensor` 객체 그래프를 먼저 만드는 것으로 시작하고,
각가의 텐서가 다른 텐서를 기반으로 어떤식으로 계산될 수 있는지 구체화하고,
그 다음 그래프를 실행하서 원하는 결과를 얻게 됩니다.

`tf.Tensor`는 다음과 같은 속성을 가지고 있습니다:

 * 데이터 타입 (예를 들어, `float32` 또는 `int32`, `string`)
 * 모양(shape)

텐서안의 각각 요소(element)는 동일한 데이터 타입이고 항상 그 데이터 타입을 알 수 있습니다.
모양(즉, 차원 크기와 각 차원마다 길이(size))는 일부만 알 수 있습니다.
대부분 연산은 입력값 모양을 알 수 있다면 모든 정보를 알 수 있는 텐서를 만들지만,
일부 경우에서는 그래프를 실행한 이후에 텐서 모양을 알 수 있기도 합니다.

일부 특별한 텐서는 텐서플로 가이드문서의 다른 부분에서 다뤄질 것입니다.
핵심인 텐서는 다음과 같습니다:

  * `tf.Variable`
  * `tf.constant`
  * `tf.placeholder`
  * `tf.SparseTensor`

예외인 `tf.Variable`을 제외한다면, 텐서 값은 변경불가능(immutable) 합니다.
즉, 텐서를 한번만 실행시킨 경우에는 오직 하나의 값만을 가집니다.
그러나, 동일한 텐서를 다시 실행시킨다면 다른 값을 가질 수 있습니다:
예를 들어 텐서가 디스크로부터 데이터를 읽어들인 결과 이거나,
무작위 숫자를 생성하는 경우입니다.

## 랭크(Rank)

`tf.Tensor` 객체의 **랭크**는 그 차원의 수입니다.
랭크의 동의어는 **order** 또는 **degree**, **n-차원**입니다.
텐서플로의 랭크는 수학에서 사용하는 행렬의 랭크와는 다릅니다.
다음 표에서 알 수 있는 것처럼, 텐서플로의 각 랭크는 각각 다른 수학적 용어(entity)에 해당됩니다.

랭크 | 수학적 용어(entity)
--- | ---
0 | 스칼라(Scalar) (크기(magnitude)만)
1 | 벡터(Vector) (크기와 방향(direction))
2 | 행렬(Matrix) (숫자 표)
3 | 3-텐서 (숫자 큐브(cube))
n | n-텐서 (you get the idea)


### 랭크 0

다음 일부 랭크 0 변수 생성 예입니다:

```python
mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)
```

Note: 문자열은 텐서에서 문자 시퀀스(sequence)가 아니라 단일 객체로 다뤄집니다.
객체는 단일 문자열과 문자열 벡터 등 모두 가능합니다.

### 랭크 1

랭크 1 `tf.Tensor` 객체를 생성하기 위해서 초기값으로 아이템 리스트를 사용할 수 있습니다.
예를 들어:

```python
mystr = tf.Variable(["Hello"], tf.string)
cool_numbers  = tf.Variable([3.14159, 2.71828], tf.float32)
first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)
```


### 고차원 랭크

랭크 2 `tf.Tensor` 객체는 최소 한 개 이상의 열(column)과 행(row)으로 구성됩니다:

```python
mymat = tf.Variable([[7],[11]], tf.int16)
myxor = tf.Variable([[False, True],[True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)
mymatC = tf.Variable([[7],[11]], tf.int32)
```

유사하게 고차원 랭크 텐서는 n-차원 배열로 구성됩니다.
예를 들어, 이미지 처리에서 각각 배치 수와 이미지 높이, 이미지 너비, 색상 채널에 해당하는 4차원 랭크 텐서가 사용됩니다.

``` python
my_image = tf.zeros([10, 299, 299, 3])  # 배치 x 높이 x 너비 x 색상
```

### `tf.Tensor` 객체 랭크 구하기

`tf.Tensor` 객체의 랭크를 알기 위해서는 `tf.rank` 메서드를 호출합니다.
예를 들어, 다음 메서드는 프로그램적으로 이전 섹션에서 정의된 `tf.Tensor`의 랭크를 알려줍니다.

```python
r = tf.rank(my_image)
# 그래프가 실행된 후 r은 4라는 값을 가지게 됩니다.
```

### `tf.Tensor` 일부분 참조하기

`tf.Tensor`는 n-차원 배열로 구성된 셀이기 대문에,
`tf.Tensor`의 셀 하나에 접근하기 위해서는 n개의 인덱스가 필요합니다.

랭크 0 텐서(스칼라)인 경우 그것이 이미 하나의 숫자이기 때문에 인덱스가 필요없습니다.

랭크 1 텐서(벡터)인 경우 숫자 하나에 접근하기 위해서는 인덱스 한 개를 전달해야 합니다:

```python
my_scalar = my_vector[2]
```

벡터로부터 값 한 개를 동적으로 선택하기 위해서
`[]`안에 스칼라형 `tf.Tensor`를 인덱스로 사용할 수 있습니다.

랭크 2이상의 고차원 텐서인 경우에는 좀 더 흥미롭습니다.
예상한 것처럼 랭크 2인 `tf.Tensor`를 위해 인덱스로 2개를 전달해야 스칼라 한 개를 반환합니다:


```python
my_scalar = my_matrix[1, 2]
```


그러나, 한 개만 전달한다면 다음과 같이 행렬의 부분 벡터를 반환합니다:


```python
my_row_vector = my_matrix[2]
my_column_vector = my_matrix[:, 3]
```

`:` 표기는 "해당 차원를 남겨라"라는 파이썬 슬라이싱(slicing) 문법입니다.
이러한 표기법은 고차원 텐서에서 부분 벡터와 부분 행렬, 다른 부분 텐서들까지도 접근할 수 있도록 만들어 주기 때문에 유용합니다.


## Shape

The **shape** of a tensor is the number of elements in each dimension.
TensorFlow automatically infers shapes during graph construction. These inferred
shapes might have known or unknown rank. If the rank is known, the sizes of each
dimension might be known or unknown.

The TensorFlow documentation uses three notational conventions to describe
tensor dimensionality: rank, shape, and dimension number. The following table
shows how these relate to one another:

Rank | Shape | Dimension number | Example
--- | --- | --- | ---
0 | [] | 0-D | A 0-D tensor.  A scalar.
1 | [D0] | 1-D | A 1-D tensor with shape [5].
2 | [D0, D1] | 2-D | A 2-D tensor with shape [3, 4].
3 | [D0, D1, D2] | 3-D | A 3-D tensor with shape [1, 4, 3].
n | [D0, D1, ... Dn-1] | n-D | A tensor with shape [D0, D1, ... Dn-1].

Shapes can be represented via Python lists / tuples of ints, or with the
`tf.TensorShape`.

### Getting a `tf.Tensor` object's shape

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

## Print a tensor

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

