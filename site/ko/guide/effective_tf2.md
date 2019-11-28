# 이펙티브 텐서플로 2.0

Note: 이 문서는 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고
[공식 영문 문서](https://github.com/tensorflow/docs/blob/master/site/en/guide/effective_tf2.md)의
내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

텐서플로 2.0은 사용자의 생산성을 향상시키기 위해서 많은 것을 바꾸었습니다. [불필요한 API](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)를 제거하고 API의 일관성을 높였으며([Unified RNNs](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[Unified Optimizers](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)) 파이썬 런타임(runtime)과 [즉시 실행](https://www.tensorflow.org/guide/eager)(eager execution)을 통합하였습니다.

여러 [RFC](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr) 문서에서 텐서플로 2.0의 변경 내용을 확인할 수 있습니다. 이 가이드에서는 텐서플로 2.0을 사용한 개발 방식을 소개합니다. 여러분이 텐서플로 1.x에 친숙하다고 가정하겠습니다.

## 주요 변경 사항 요약

### API 정리

많은 API가 TF 2.0에서 [삭제 또는 이동](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)되었습니다. 주요한 변화는 다음과 같습니다. `tf.app`, `tf.flags`, `tf.logging`을 삭제하고 [absl-py](https://github.com/abseil/abseil-py) 오픈 소스를 권장합니다. `tf.contrib` 아래에 있던 프로젝트를 이동했습니다. 자주 사용하지 않는 함수를 `tf.math` 같은 서브패키지(subpackage)로 이동하는 식으로 `tf.*` 네임스페이스(namespace)를 정리하였습니다. `tf.summary`, `tf.keras.metrics`, `tf.keras.optimizers`와 같은 일부 API는 2.0 버전으로 교체되었습니다. 교체된 이름을 자동으로 적용하려면 [v2 upgrade script](upgrade.md) 사용하는 것이 가장 편리합니다.

### 즉시 실행

텐서플로 1.x에서는 사용자가 `tf.*` API를 호출해서 [추상 구문 트리](https://ko.wikipedia.org/wiki/%EC%B6%94%EC%83%81_%EA%B5%AC%EB%AC%B8_%ED%8A%B8%EB%A6%AC)를 수동으로 구성했습니다. 그다음 `session.run()`을 호출할 때 출력 텐서와 입력 텐서를 전달하여 추상 구문 트리를 수동으로 컴파일합니다. 텐서플로 2.0은 (보통의 파이썬처럼) 즉시 실행됩니다. 텐서플로 2.0에서 그래프와 세션은 구현 상세(implementation detail)처럼 느껴질 것입니다.

즉시 실행으로 인한 부수효과 중 하나는 더이상 `tf.control_dependencies()`이 필요하지 않다는 것입니다. 모든 코드는 라인 순서대로 실행됩니다(`tf.function` 안의 코드도 이 효과로 쓰여진 순서대로 실행됩니다).

### 전역 메커니즘 제거

텐서플로 1.x는 겉으로 드러나진 않았지만 전역 이름 공간(namespace)에 크게 의존했습니다. `tf.Variable()`를 호출하면 기본 그래프에 노드(node)를 추가합니다. 노드를 참조하는 파이썬 변수가 삭제되더라도 그래프에 그대로 남아 있습니다. 이 `tf.Variable` 노드를 다시 참조할 수 있지만 생성할 때 지정한 이름을 알아야만 가능합니다. 변수를 직접 만들지 않았다면 어려운 일입니다. 이 때문에 사용자와 프레임워크가 변수를 추적할 수 있도록 여러 종류의 메커니즘이 늘어 났습니다. 변수 범위(variable scope), 전역 컬렉션(global collection), `tf.get_global_step()`이나 `tf.global_variables_initializer()` 같은 헬퍼 메서드 등입니다. 또 옵티마이저(optimizer)는 암묵적으로 훈련 가능한 모든 변수의 그래디언트(graident)를 계산합니다. 텐서플로 2.0은 이런 모든 메커니즘을 삭제했습니다([Variables 2.0 RFC](https://github.com/tensorflow/community/pull/11)). 대신 파이썬 변수를 추적하는 기본 메커니즘을 사용합니다! `tf.Variable`의 참조를 잃어 버렸다면 자동으로 가비지 컬렉션(garbage collection)될 것입니다.

사용자가 변수를 관리하는 일이 늘어나지만 케라스(Keras)(아래 참조)를 사용하면 최소화할 수 있습니다.

### 세션 대신 함수

`session.run()`은 거의 함수 호출과 비슷합니다. 입력과 함수를 지정하면 일련의 출력을 얻습니다. 텐서플로 2.0에서는 `tf.function()` 데코레이터(decorator)로 파이썬 함수를 감쌀 수 있습니다. 이렇게 하면 텐서플로가 이 함수를 하나의 그래프로 실행하기 위해 JIT 컴파일합니다([Functions 2.0 RFC](https://github.com/tensorflow/community/pull/20)). 이 메커니즘 덕택에 텐서플로 2.0에서 그래프 모드의 장점을 모두 계승할 수 있습니다.

-   성능: 함수를 최적화할 수 있습니다(노드 가지치기(pruning), 커널 융합(kernel fusion) 등).
-   이식성(portability): 함수를 저장하고 다시 불러올 수 있습니다([SavedModel 2.0 RFC](https://github.com/tensorflow/community/pull/34)). 모듈화된 텐서플로 함수를 재사용하고 공유할 수 있습니다.

```python
# 텐서플로 1.x
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# 텐서플로 2.0
outputs = f(input)
```

파이썬과 텐서플로 코드를 자유롭게 섞어 쓸 수 있기 때문에 파이썬의 장점을 최대한 활용할 수 있습니다. 텐서플로는 파이썬 인터프리터가 없는 모바일, C++, 자바스크립트 같은 환경에서도 실행됩니다. 사용자가 환경에 따라 코드를 재작성하지 않도록 `@tf.function`를 추가하면 [오토그래프](function.ipynb)(AutoGraph)가 파이썬 코드를 동일한 텐서플로 코드로 변경합니다.

*   `for`/`while` -> `tf.while_loop` (`break`과 `continue` 문을 지원합니다.)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

오토그래프는 임의의 중첩된 제어 흐름도 지원합니다. 시퀀스(sequence) 모델, 강화 학습(reinforcement learning), 독자적인 훈련 루프 등 복잡한 머신러닝 프로그램을 간결하면서 높은 성능을 내도록 구현할 수 있습니다.

## 텐서플로 2.0의 권장 사항

### 작은 함수로 코드를 리팩토링하세요.

텐서플로 1.x의 일반적인 사용 패턴은 "키친 싱크(kitchen sink)" 전략입니다. 먼저 모든 연산을 결합하여 준비한 다음 `session.run()`을 사용해 선택한 텐서를 평가합니다. 텐서플로 2.0에서는 필요할 때 호출할 수 있는 작은 함수로 코드를 리팩토링(refactoring)해야 합니다. 모든 함수에 `tf.function` 데코레이터를 적용할 필요는 없습니다. 모델 훈련의 한 단계(step)나 정방향 연산(forward pass) 같은 고수준 연산에만 `tf.function` 데코레이터를 적용하세요.

### 케라스 층과 모델을 사용해 변수를 관리하세요.

케라스 모델과 층(layer)은 재귀적으로 의존하는 모든 변수를 수집하여 `variables`와 `trainable_variables` 속성으로 제공합니다. 따라서 변수를 지역 범위로 관리하기 매우 쉽습니다.

기본 버전:

```python
def dense(x, W, b):
  return tf.nn.sigmoid(tf.matmul(x, W) + b)

@tf.function
def multilayer_perceptron(x, w0, b0, w1, b1, w2, b2 ...):
  x = dense(x, w0, b0)
  x = dense(x, w1, b1)
  x = dense(x, w2, b2)
  ...

# 여전히 w_i, b_i 변수를 직접 관리해야 합니다. 이 코드와 떨어져서 크기가 정의됩니다.
```

케라스 버전:

```python
# 각 층은 linear(x)처럼 호출 가능합니다.
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].trainable_variables => returns [w3, b3]
# perceptron.trainable_variables => returns [w0, b0, ...]
```

케라스의 층과 모델은 `tf.train.Checkpointable`을 상속하고 `@tf.function`를 사용하여 통합되어 있습니다. 케라스 객체에서 바로 체크포인트나 SavedModels로 저장할 수 있습니다. 케라스 `.fit()` API를 호출하지 않더라도 이런 기능을 사용할 수 있습니다.

전이 학습(transfer learning) 예제를 통해서 케라스가 어떻게 관련된 변수를 쉽게 모으는지 알아 보겠습니다. 몸통(trunk)을 공유하는 다중 출력(multi-headed) 모델을 훈련한다고 가정해 보죠.

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# 주된 데이터셋에서 훈련합니다.
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # trunk와 head1 가중치를 동시에 최적화합니다.
  gradients = tape.gradient(loss, path1.trainable_variables)
  optimizer.apply_gradients(zip(gradients, path1.trainable_variables))

# trunk를 재사용하여 head2를 세부 튜닝합니다.
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # trunk 가중치는 제외하고 head2 가중치만 최적화합니다.
  gradients = tape.gradient(loss, head2.trainable_variables)
  optimizer.apply_gradients(zip(gradients, head2.trainable_variables))

# trunk 연산만 재사용을 위해 저장할 수 있습니다.
tf.saved_model.save(trunk, output_path)
```

### tf.data.Datasets과 @tf.function을 연결하세요.

메모리 크기에 맞는 훈련 데이터를 반복할 때는 보통의 파이썬 반복자를 사용해도 좋습니다. 그렇지 않다면 디스크에서 훈련 데이터를 읽는 가장 좋은 방법은 `tf.data.Dataset`입니다. 데이터셋이 [반복 가능](https://docs.python.org/ko/3/glossary.html#term-iterable)(반복자가 아닙니다)하면 즉시 실행 모드에서는 파이썬의 다른 반복 가능 객체처럼 동작합니다. `tf.function()`으로 코드를 감싸서 비동기 프리페치(prefetch)/스트리밍(streaming) 기능을 모두 사용할 수 있습니다. `tf.function()`은 오토그래프를 사용하여 파이썬 반복문을 동일한 그래프 연산으로 바꾸어 줍니다.

```python
@tf.function
def train(model, dataset, optimizer):
  for x, y in dataset:
    with tf.GradientTape() as tape:
      prediction = model(x)
      loss = loss_fn(prediction, y)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

케라스의 `.fit()` API를 사용하면 데이터셋 반복에 관해 신경 쓸 필요가 없습니다.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### 파이썬의 제어 흐름과 함께 오토그래프를 사용하세요.

오토그래프는 데이터에 따라 결정되는 제어 흐름(control flow)을 `tf.cond`와 `tf.while_loop` 같은 그래프 모드 연산으로 변환시켜 줍니다.

데이터에 의존하는 제어 흐름이 나타나는 대표적인 곳은 시퀀스(sequence) 모델입니다. `tf.keras.layers.RNN`은 RNN 셀(cell)을 감싸서 순환(recurrent) 셀을 정적으로 또는 동적으로 펼칠 수 있습니다. 다음처럼 직접 동적으로 펼치는 구현을 만들어서 확인할 수 있습니다.

```python
class DynamicRNN(tf.keras.Model):

  def __init__(self, rnn_cell):
    super(DynamicRNN, self).__init__(self)
    self.cell = rnn_cell

  def call(self, input_data):
    # [batch, time, features] -> [time, batch, features]
    input_data = tf.transpose(input_data, [1, 0, 2])
    outputs = tf.TensorArray(tf.float32, input_data.shape[0])
    state = self.cell.zero_state(input_data.shape[1], dtype=tf.float32)
    for i in tf.range(input_data.shape[0]):
      output, state = self.cell(input_data[i], state)
      outputs = outputs.write(i, output)
    return tf.transpose(outputs.stack(), [1, 0, 2]), state
```

오토그래프의 특징에 관한 더 자세한 내용은 이 [가이드](./function.ipynb)를 참고하세요.

### tf.metrics로 데이터를 수집하고 tf.summary로 기록하세요.

서머리(summary) 로그를 기록하려면 `tf.summary.(scalar|histogram|...)`를 사용합니다. 컨텍스트 관리자(context manager)를 사용하는 파일 쓰기 객체에 전달해야 합니다. (컨텍스트 관리자를 사용하지 않으면 아무 일도 일어나지 않습니다.) TF 1.x과 달리 서머리는 바로 파일 쓰기 객체에 전달됩니다. 별도의 "머지(merge)" 연산이나 `add_summary()` 호출이 없습니다. 따라서 로그를 기록할 때 `step` 값이 함께 제공되어야 합니다.

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  tf.summary.scalar('loss', 0.1, step=42)
```

`summary`로 기록할 데이터를 수집하려면 `tf.metrics`를 사용하세요. 측정 정보들은 상태가 있습니다. 이 값들은 누적되어 `.result()`를 호출하면 누적된 결과가 반환됩니다. `.reset_stats()`를 사용하여 누적된 값을 초기화할 수 있습니다.

```python
def train(model, optimizer, dataset, log_freq=10):
  avg_loss = tf.keras.metrics.Mean(name='loss', dtype=tf.float32)
  for images, labels in dataset:
    loss = train_step(model, optimizer, images, labels)
    avg_loss.update_state(loss)
    if tf.equal(optimizer.iterations % log_freq, 0):
      tf.summary.scalar('loss', avg_loss.result(), step=optimizer.iterations)
      avg_loss.reset_states()

def test(model, test_x, test_y, step_num):
  loss = loss_fn(model(test_x), test_y)
  tf.summary.scalar('loss', loss, step=step_num)

train_summary_writer = tf.summary.create_file_writer('/tmp/summaries/train')
test_summary_writer = tf.summary.create_file_writer('/tmp/summaries/test')

with train_summary_writer.as_default():
  train(model, optimizer, dataset)

with test_summary_writer.as_default():
  test(model, test_x, test_y, optimizer.iterations)
```

텐서보드(TensorBoard)에 로그 디렉토리를 지정하여 생성된 서머리 로그를 시각화해 보세요: `tensorboard --logdir /tmp/summaries`
