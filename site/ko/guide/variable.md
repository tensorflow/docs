# 변수

Note: 이 문서는 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고
[공식 영문 문서](https://github.com/tensorflow/docs/blob/master/site/en/guide/variable.md)의
내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

텐서플로 **변수**는 프로그램에 의해 변화하는 공유된 지속 상태를 표현하는 가장 좋은 방법입니다.

변수는 `tf.Variable` 클래스에서 처리됩니다. 하나의 `tf.Variable`은 하나의 텐서를 표현하는데, 텐서값은 텐서에 연산을
수행하여 변경시킬 수 있습니다. 특정한 연산은 이 텐서값을 읽고 수정합니다. `tf.keras` 같은 좀 더 고수준의 라이브러리는 모델
파라미터를 저장하는데 `tf.Variable`을 사용합니다. 이 가이드는 텐서플로에서 `tf.Variable`의 생성, 업데이트, 관리 방법을
다룹니다.

## 변수 생성

변수를 생성하려면 단순하게 초기값을 설정하면 됩니다.

``` python
my_variable = tf.Variable(tf.zeros([1., 2., 3.]))
```

이렇게 하면 모양이 `[1, 2, 3]`이고 값은 0으로 채워진 3차원 텐서가 변수로 생성됩니다. 이 변수는 기본적으로 `dtype`
`tf.float32`로 설정될 것입니다. dtype을 지정하지 않은 경우 초기값으로부터 추정됩니다.

`tf.device` 범위(scope)가 유효하다면, 변수는 해당 장치에 위치합니다; 그렇지 않다면, 변수는 dtype에 호환되는 "가장 빠른"
장치에 위치합니다.(GPU가 가용하다면 대부분의 변수들이 자동적으로 GPU에 위치한다는 의미입니다) 예를들어, 다음의 코드는 `v`라는 변수를
만들고 두 번째 GPU에 위치시킵니다:

``` python
with tf.device("/device:GPU:1"):
  v = tf.Variable(tf.zeros([10, 10]))
```

이상적으로는 `tf.distribute` API를 통해 코드를 한번 작성하고 다양한 분산 설정에서 작동되도록 하세요.

## 변수의 사용

텐서플로 그래프에서 `tf.Variable`의 값을 사용하려면 이를 단순히 `tf.Tensor`로 취급하면 됩니다:

``` python
v = tf.Variable(0.0)
w = v + 1  # w는 v값 기준으로 계산되는 tf.Tensor 입니다.
           # 변수가 수식에 사용될 때, 변수는 자동적으로
           # tf.Tensor로 변환되어 값을 표현합니다.
```

값을 변수에 할당하려면 `assign`, `assign_add` 메소드와 `tf.Variable` 클래스에 있는 친구들(friends)을
사용하세요. 예를들어, 여기에 이 메서드를 호출하는 방법이 있습니다:

``` python
v = tf.Variable(0.0)
v.assign_add(1)
```

대부분의 텐서플로 옵티마이저(optimizer)는 경사 하강법과 같은 알고리즘에 따라 변수값을 효율적으로 업데이트하는 전문적인 연산이 있습니다.
`tf.keras.optimizers.Optimizer`을 보면 옵티마이저 사용방법이 설명되어 있습니다.

또한, `read_value`를 사용하여 현재 변수값을 명시적으로 읽어올 수 있습니다:

```python
v = tf.Variable(0.0)
v.assign_add(1)
v.read_value()  # 1.0
```

`tf.Variable`에 대한 마지막 참조가 범위(scope)에서 벗어났을때 메모리가 해제됩니다.

### 변수 추적

텐서플로에서 하나의 변수는 하나의 파이썬 객체입니다. 층, 모델, 옵티마이저, 그리고 다른 관련된 도구들을 작성할때 모델 안에 있는 모든 변수의
리스트가 필요할 수 있습니다.

자신의 파이썬 코드에서 필요에 따라 변수들을 추적하는 동안 변수를 소유하는 자신의 클래스에 기본 클래스로 `tf.Module` 사용을
권장합니다. `tf.Module`의 인스턴스는 `variables`와 다른 모듈들을 탐색할 수 있는 모델에서 접근할 수 있는 모든 (훈련
가능한) 변수을 리턴하는 `trainable_variables` 메서드가 포함되어 있습니다.

```python
class MyModuleOne(tf.Module):
  def __init__(self):
    self.v0 = tf.Variable(1.0)
    self.vs = [tf.Variable(x) for x in range(10)]
    
class MyOtherModule(tf.Module):
  def __init__(self):
    self.m = MyModuleOne()
    self.v = tf.Variable(10.0)
    
m = MyOtherModule()
len(m.variables)  # 12; 11은 m.m에서 다른 것은 m.v에서

```

층을 구현하고 있다면 `tf.keras.Layer`가 기본 클래스로 더 좋을 수 있습니다. 인터페이스를 구현하는 것은 층이 케라스에 완전하게
통합되기 때문에 `model.fit`과 잘 통합된 다른 API들을 사용할 수 있게 됩니다. `tf.keras.Layer`의 변수 추적은
`tf.Module`의 변수 추적과 동일합니다.
