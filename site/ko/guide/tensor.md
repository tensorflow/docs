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


## 쉐이프(Shape)

텐서의 **쉐이프**는 각 차원에 있는 원소 개수입니다.
텐서플로는 그래프 계산 과정에서 자동으로 쉐이프를 추론합니다.
이렇게 추론된 쉐이프는 랭크를 알고 있는 경우도 있고 그렇지 않는 경우도 있습니다.
만약에 랭크를 알고 있는 경우라도 각 차원의 개수를 알고 경우도 있고 그렇지 않는 경우도 있습니다.

텐서플로 문서에서 텐서 차원을 표현하기 위해서 3가지 용어를 사용합니다: 랭크, 쉐이프, 차원수.
다음 표는 각 용어가 다른 용어와 연관되어 있는지를 보여줍니다.

랭크 | 쉐이프 | 차원수 | 예제
--- | --- | --- | ---
0 | [] | 0-D | 스칼라인 0-D 텐서.
1 | [D0] | 1-D | 쉐이프 [5]인 1-D 텐서.
2 | [D0, D1] | 2-D | 쉐이프 [3, 4]인 2-D 텐서.
3 | [D0, D1, D2] | 3-D | 쉐이프 [1, 4, 3]인 3-D 텐서.
n | [D0, D1, ... Dn-1] | n-D | 쉐이프 [D0, D1, ... Dn-1]인 텐서.

쉐이프는 파이썬 리스트 / 정수형 튜플 또는 `tf.TensorShape`으로 표현될 수 있습니다.

### `tf.Tensor` 객체 쉐이프 얻기

`tf.Tensor`의 쉐이프를 알기 위한 2가지 방법이 있습니다.
그래프를 생성하는 동안 텐서의 쉐이프를 알 수 있는 것은 종종 유용합니다.
쉐이프는 `tf.Tensor`객체의 `shape` 속성으로 알 수 있습니다.
이 메서드는 `TensorShape`를 반환하고, 이러한 방식은 완벽하게 알려지지 않는 쉐이프를 표현하는데 편리한 방법입니다
(그래프를 생성할 때 모든 쉐이프를 알 수 없기 때문에).

`tf.Tensor`를 얻는 것은 실행 시점에 쉐이프를 알고 있는 다른 `tf.Tensor`로 표현할 수 있습니다.
이것은 `tf.shape` 연산을 통해서 확인할 수 있습니다.
이를 통해, 입력 `tf.Tensor`의 동적인 쉐이프에 연동된 다른 텐서를 생성함으로써
텐서 쉐이프를 변경하는 그래프를 생성할 수 있습니다.

예를 들어 다음은 주어진 행렬의 열 개수와 동일한 크기의 0으로 구성된 벡터를 만드는 예입니다.

``` python
zeros = tf.zeros(my_matrix.shape[1])
```

### `tf.Tensor` 쉐이프 변경

텐서의 **원소 개수**는 모든 쉐이프 크기를 곱한 것입니다.
스칼라의 원소 개수는 항상 `1`입니다.
원소 개수가 같은 경우라도 쉐이프는 다양할 수 있기 때문에, 그 원소 개수를 유지하면서 `tf.Tensor`의 쉐이프를 변경할 수 있는 것은 유용합니다.
이것은 `tf.reshape`으로 처리할 수 있습니다.

다음은 텐서 쉐이프를 변경하는 예입니다:

```python
rank_three_tensor = tf.ones([3, 4, 5])
matrix = tf.reshape(rank_three_tensor, [6, 10])  # 기존 내용을 6x10 행렬로
                                                 # 쉐이프 변경
matrixB = tf.reshape(matrix, [3, -1])  # 기존 내용을 3x20 행렬로 쉐이프 변경
                                       # -1은 차원 크기를 계산한 후에
                                       # 쉐이프를 변경하라는 의미
matrixAlt = tf.reshape(matrixB, [4, 3, -1])  # 기존 내용을 4x3x5 텐서로
                                             # 쉐이프 변경

# 쉐이프가 변경된 텐서의 원소 개수는
# 원래 텐서의 원소 개수와 같습니다.
# 그러므로 다음은 원소 개수를 유지하면서
# 마지막 차원에 사용 가능한 수가 없기 때문에 에러를 발생합니다.
yet_another = tf.reshape(matrixAlt, [13, 2, -1])  # 에러!
```

## 데이터 타입(type)

차원뿐만 아니라, 텐서는 테이터 타입도 가지고 있습니다.
전체 데이터 타입을 확인하려면 `tf.DType`를 참고하세요.

`tf.Tensor`가 한 개이상의 데이터 타입을 가지는 것은 불가능합니다.
임의의 데이터 구조를 직렬화한 `string`를 저장한 `tf.Tensor`는 예외입니다.

`tf.cast`를 이용해서 `tf.Tensor`의 데이터 타입을 다른 것으로 변경하는 것은 가능합니다:

``` python
# 정수형 텐서를 실수형으로 변환.
float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype=tf.float32)
```

`tf.Tensor`의 데이터 타입을 확인하기 위해서는 `Tensor.dtype` 속성을 활용하세요.

파이썬 객체를 이용해서 `tf.Tensor`를 생성할 때 데이터 타입을 선택적으로 명시할 수 있습니다.
그렇지 않으면 텐서플로가 데이터 표현에 적합한 데이터 타입을 선택합니다.
텐서플로는 파이썬 정수를 `tf.int32`로 변환하고 파이썬 실수는 `tf.float32`으로 변환합니다.
그외에 동일한 규칙을 numpy를 배열로 변경할 때 사용합니다.

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

