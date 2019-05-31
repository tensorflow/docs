# GPU 사용하기

Note: 이 문서는 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고
[공식 영문 문서](https://github.com/tensorflow/docs/blob/master/site/en/r2/guide/using_gpu.md)의
내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

## 지원하는 장치들

텐서플로는 `CPU`와 `GPU`를 포함한 다양한 타입의 장치에서 계산을 지원합니다. 그것들은 `strings`로 표현됩니다, 이를테면:

*   `"/cpu:0"`: 자신의 CPU
*   `"/device:GPU:0"`: 텐서플로에서 볼 수 있는 첫 번째 GPU
*   `"/device:GPU:1"`: 텐서플로 등에서 볼 수 있는 두 번째 GPU

텐서플로 연산이 CPU와 GPU 구현을 다 포함하고 있으면 연산이 장치에 할당될 때 기본값으로 GPU 장치가 우선적으로 할당됩니다. 예를들어 `matmul`은 CPU와 GPU 커널 모두 있습니다. `cpu:0`와 `gpu:0`, `gpu:1`이 있는 시스템에서는 명시적으로 장치를 지정하지 않으면 `gpu:0`가 선택되어 `matmul`을 실행합니다.


## 장치 할당 로깅

연산과 텐서가 어떤 장치에 할당되었는지 확인하려면 `tf.debugging.set_log_device_placement(True)`을 프로그램의 첫 번째 문장(statement)으로 하세요.

```python
tf.debugging.set_log_device_placement(True)

# 텐서 생성
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
print(c)
```

다음과 같은 출력이 나올 것입니다:

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
```

## 수동 장치 할당

장치를 자동으로 선택하지 않고 특정 연산을 실행할 장치를 직접 선택하고 싶다면, `with tf.device`로 장치 컨텍스트를 생성할 수 있고 해당 컨텍스트에서의 모든 연산은 지정된 장치에서 수행됩니다.

```python
tf.debugging.set_log_device_placement(True)

# 텐서를 CPU에 할당
with tf.device('/cpu:0'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
print(c)
```

`a`와 `b`가 `cpu:0`에 할당되었습니다. `MatMul`연산은 명시적으로 장치가 할당되어 있지 않기 때문에 텐서플로 런타임(runtime)은 연산과 가용한 장치들(이 예제에서는 `cpu:0`)에 기반으로 하나를 고를 것이고 필요하다면 장치들간에 텐서를 자동적으로 복사할 것입니다.

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
```

## GPU 메모리 증가 허용하기

기본적으로 텐서플로는 모든 GPU의 거의 모든 GPU 메모리를 프로세스가 볼 수 있도록 매핑합니다([`CUDA_VISIBLE_DEVICES`](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars)를 가정합니다). 이는 [메모리 단편화](https://en.wikipedia.org/wiki/Fragmentation_\(computing\))를 줄여서 상대적으로 귀한 GPU 메모리 리소스를 장치에서 보다 효율적으로 사용할 수 있게 합니다.

어떤 경우에는 프로세스가 가용한 메모리의 일부에만 할당되도록 하거나 프로세스의 요구량만큼 메모리 사용이 가능할 수 있도록 할 필요가 있습니다. 텐서플로에서는 이걸 조정하기 위한 두 가지 방법이 있습니다.

첫 번째는 `tf.config.gpu.set_per_process_memory_growth()`를 호출하여 메모리 증가를 허용하는 것입니다. 이 메서드는 런타임에서 할당하는데 필요한 양만큼의 GPU 메모리를 할당합니다: 처음에는 메모리를 조금만 할당하고, 프로그램이 실행되어 더 많은 GPU 메모리가 필요로 할때, 텐서플로 프로세스에 할당된 GPU 메모리 영역을 확장합니다. 메모리를 해제하는 것은 메모리 단편화를 악화시키므로 메모리 해제는 하지않는 것에 주의하세요. 프로세스 메모리를 증가시키려면 다음의 선언을 프로그램의 첫 번째 선언으로 하세요:

```python
tf.config.gpu.set_per_process_memory_growth()
```

두 번째 방법은 `tf.gpu.set_per_process_memory_fraction()`입니다. 이것은 보이는 GPU가 할당해야 하는 메모리 비율을 결정합니다. 예를 들어, 다음과 같이 입력하여 텐서플로가 각 GPU 메모리의 40%만 할당하도록 할 수 있습니다:

```python
tf.config.gpu.set_per_process_memory_fraction(0.4)
```

이는 텐서플로 프로세스에 사용가능한 GPU 메모리량을 제한하는데 유용합니다.

## 멀티 GPU 시스템에서 하나의 GPU 사용하기

시스템에 한 개 이상의 GPU가 있다면, 기본값으로 낮은 ID의 GPU가 선택됩니다. 
다른 GPU에서 실행하고 싶다면, 명시적으로 표시해야 합니다:

```python
tf.debugging.set_log_device_placement(True)

# 장치를 명시
with tf.device('/device:GPU:2'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

print(c)
```

명시한 장치가 없으면 `RuntimeError`가 나옵니다:

```
RuntimeError: Error copying tensor to device: /job:localhost/replica:0/task:0/device:GPU:2. /job:localhost/replica:0/task:0/device:GPU:2 unknown device.
```

명시된 장치가 없을 때 텐서플로가 자동으로 현재 지원하는 장치를 선택하게 하고 싶다면 `tf.config.set_soft_device_placement(True)`를 호출하세요.

```python
tf.config.set_soft_device_placement(True)
tf.debugging.set_log_device_placement(True)

# 텐서들 생성
with tf.device('/device:GPU:2'):
  a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
  b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
  c = tf.matmul(a, b)

print(c)
```

## 멀티 GPU 사용하기

#### `tf.distribute.Strategy` 사용

멀티 GPU를 사용하는 가장 좋은 방법은 `tf.distribute.Strategy`를 사용하는 것입니다. 
간단한 예제를 살펴봅시다:

```python
strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.2))
```

이 프로그램은 각 GPU에 모델을 복사하고 입력 데이터를 각 GPU에 나누어서 실행할 것입니다. 이는 "[데이터 병렬처리](https://en.wikipedia.org/wiki/Data_parallelism)"라고도 합니다.

병렬화 전략에 대한 더 많은 정보는 [가이드](./distribute_strategy.ipynb)를 참조하세요.


#### `tf.distribute.Strategy` 미사용

`tf.distribute.Strategy`는 여러 장치에 걸쳐 계산을 복제함으로써 동작합니다. 모델을 각 GPU에 구성하여 수동으로 이를 구현할 수 있습니다. 예를 들면:


``` python
tf.debugging.set_log_device_placement(True)

# 다수의 GPU에 계산을 복제
c = []
for d in ['/device:GPU:2', '/device:GPU:3']:
  with tf.device(d):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
    c.append(tf.matmul(a, b))
with tf.device('/cpu:0'):
  sum = tf.add_n(c)

print(sum)
```

다음과 같은 출력이 나옵니다.

```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[ 44.  56.]
 [ 98. 128.]], shape=(2, 2), dtype=float32)
```
