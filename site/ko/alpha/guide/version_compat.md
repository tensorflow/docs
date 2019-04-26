# 텐서플로 버전 호환성

이 문서는 텐서플로(코드이거나 데이터)의 다른 버전들간의 하위 호환성이 필요한 사용자와 텐서플로의 호환성을 유지하면서 텐서플로를 수정하고 싶어하는 개발자들을 위한 문서입니다.

## 유의적 버저닝 2.0

텐서플로는 공개 API에 유의적 버저닝 2.0([semver](http://semver.org))을 준수합니다. 텐서플로의 각 릴리즈 버전은 `MAJOR.MINOR.PATCH` 형식입니다. 이를테면 텐서플로 버전 1.2.3은 `MAJOR` 버전 1, `MINOR` 버전 2, `PATCH` 버전 3을 뜻합니다. 각 숫자의 변화는 다음을 뜻합니다:

* **MAJOR**: 하위 호환성이 없는 변동일 수 있습니다. 이전 주(major) 버전에서 동작했었던 코드와 데이터는 새로운 버전에서 동작하지 않을 수 있습니다. 그러나, 어떤 경우에는 기존 텐서플로 그래프와 체크포인트를 새로운 버전에 마이그레이션할 수도 있습니다; 자세한 사항은 [그래프와 체크포인트의 호환성](#compatibility_of_graphs_and_checkpoints)을 참고하세요.

* **MINOR**: 하위 호환되는 특성, 속도 개선 등 입니다. 이전 부(minor) 버전*과* 이전 부 버전의 비실험적인 공개 API를 사용했던 코드와 데이터는 정상적으로 동작합니다. 공개 API에 무엇이 포함되고 포함되지 않는지는 [포함되는 것들](#What_is_covered)를 참조하세요.

* **PATCH**: 하위 호환되는 버그 픽스들

이를테면 릴리즈 1.0.0은 릴리즈 0.12.1에서 하위 호환성이 *없는* 변동사항이 있습니다. 그러나, 릴리즈 1.1.1은 릴리즈 1.0.0과 하위 호환성이 있습니다.

## 포함되는 것들

텐서플로의 공개 API만이 마이너와 패치 버전에서 하위 호환성을 가집니다. 공개 API는 다음을 포함합니다.

* 모든 문서화된 [파이썬](../api_docs/python) `tensorflow` 모듈과 서브모듈에 있는 함수와 클래스, 다음은 제외

    * 개인 심볼(private symbol): `_`로 시작하는 어떠한 함수나 클래스 등
    * 실험적인 그리고 `tf.contrib` 심볼, 자세한건 [아래](#not_covered)를 참조하세요.

  `examples/`와 `tools/` 경로에 있는 코드는 `tensorflow` 파이썬 모듈을 통해 접근할 수 없고 따라서 호환성을 보장할 수 없습니다.

  한 심볼이 `tensorflow` 파이썬 모듈이나 서브모듈에서 사용가능하지만 문서화되지는 않은 경우, 공개 API의 일부로 간주하지 **않습니다**.

* 호환성 API(파이썬의 `tf.compat` 모듈). 주 버전에서 사용자들이 새로운 주 버전으로 옮겨가는 것을 도와주는 유틸리티와 추가적인 엔드포인트가 공개될 수도 있습니다. 이러한 API 심볼들은 없어지고 지원되지 않지만(즉, 기능을 추가하지 않고 취약성 이외의 버그를 수정하지 않습니다) 호환성은 보장됩니다.

* [C API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/c/c_api.h).

* 다음의 프로토콜 버퍼 파일들:

    * [`attr_value`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/attr_value.proto)
    * [`config`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/protobuf/config.proto)
    * [`event`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/util/event.proto)
    * [`graph`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/graph.proto)
    * [`op_def`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/op_def.proto)
    * [`reader_base`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/reader_base.proto)
    * [`summary`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/summary.proto)
    * [`tensor`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor.proto)
    * [`tensor_shape`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/tensor_shape.proto)
    * [`types`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/types.proto)

<a name="not_covered"></a>
## 포함되지 *않는* 것들

텐서플로의 어떤 부분은 모든 곳에서 하위 호환성이 없도록 변동될 수 있습니다. 이는 다음을 포함합니다:

*   **실험적인 API**: 개발을 용이하게 하기 위해, 어떤 API 심볼들은 실험적인 것으로 규정하고 하위 호환성을 보장하지 않습니다. 특히 다음은 어떠한 호환성 보장도 하지 않습니다:

  - `tf.contrib` 모듈이나 서브모듈에 있는 모든 심볼들
  - `experimental` 또는 `Experimental`이라는 이름을 포함하는 모든 심볼(모듈, 함수, 매개변수, 속성, 클래스, 상수); 또는
  - 모듈이나 클래스가 포함하는 절대 표기가 그 자체로 실험적인 모든 심볼들. `experimental`로 분류되는 모든 프로토콜 버퍼의 필드나 서브메시지 포함.

*   **다른 언어들:** 파이썬과 C 이외의 텐서플로 API 언어들, 이를테면:

  - [C++](../api_guides/cc/guide.md) ([`tensorflow/cc`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/cc)의 헤더파일들을 통해 공개되어 있음).
  - [Java](../api_docs/java/reference/org/tensorflow/package-summary),
  - [Go](https://godoc.org/github.com/tensorflow/tensorflow/tensorflow/go)
  - [JavaScript](https://js.tensorflow.org)

*   **합성 연산 세부사항:** 파이썬의 많은 공개함수가 그래프의 몇몇의 원시 연산에 확장됩니다, 그리고 이러한 세부사항은 `GraphDef`로 디스크에 저장되는 그래프의 한 부분입니다. 이러한 세부사항은 부(minor) 버전에서 변경될 수 있습니다. 특히, 그래프간 정확한 매칭이 되는지 확인하는 회귀테스트는 그래프의 행동이 변경되지 않고 기존의 체크포인트가 아직 동작할지라도 서로 다른 부 버전에서는 호환되지 않을 가능성이 높습니다.

*   **부동 소수점 세부사항:** 연산을 통해 계산되는 특정 부동 소수점 값은 언제든지 변경될 수 있습니다. 사용자는 계산된 특정 비트에 의존하면 안되고, 근사적인 정밀도와 수치적 안정성에 초점을 두어야 합니다. 부 버전과 패치에서 수식의 변화는 상당히 정확도를 높입니다. (기계학습에서 특정 공식의 향상된 정확도는 전체 시스템에서의 정확도를 낮추는 경우도 있습니다.)

*   **랜덤 숫자:** 특정한 랜덤 숫자가 [random ops](../api_guides/python/constant_op.md#Random_Tensors)를 통해 계산되고 언제든지 바뀔 수 있습니다. 사용자는 계산된 특정 비트에 의존하지 말고, 근사적으로 적절한 분포와 통계적 강도에 초점을 두어야 합니다. 그러나, 패치 버전에서는 특정한 비트를 거의 바꾸지 않도록 합니다. 당연히 이러한 모든 변동사항은 문서화합니다.

*   **분산 텐서플로에서의 버전 엇갈림:** 하나의 클러스터에서 서로 다른 두 버전의 텐서플로를 실행하는 것은 지원되지 않습니다. 와이어 프로토콜(wire protocol)의 하위 호환성을 보장할 수 없습니다. 

*   **버그들:** 현재의 구현이 명백하게 문제가 있는 경우, 하위 호환성을 유지하지 않는 변동사항을 만들 수 있습니다. 문서와 구현이 서로 모순되는 경우 또는 잘 알려져있고 잘 정의된 의도를 가진 행동이 버그때문에 적절하게 구현되지 않은 경우가 이에 해당됩니다. 이를테면, 잘 알려진 최적화 알고리즘이 최적화기에 구현되어야 하지만 버그때문에 그 알고리즘과 매치되지 않는다면, 최적화기를 수정할 것입니다. 수정사항은 통합을 위해서 잘못 동작하는 부분에 의존하는 코드를 포함합니다. 릴리즈 노트에 그러한 변동사항들이 기록될 것입니다.

*   **에러 동작:** 에러를 에러가 없는 동작으로 수정합니다. 이를테면, 어떤 에러가 문서화되더라도 결과를 계산하거나 에러를 올리는 함수를 변경할 수 있습니다. 또한 에러 메시지의 텍스트를 수정할 수 있습니다. 덧붙여, 에러의 타입은 에러가 나는 특정한 조건에 대해 기대하는 타입이 문서에 기술되지 않는다면 변경될 수 있습니다.

## 저장된 모델의 호환성, 그래프와 체크포인트

저장된 모델은 텐서플로 프로그램에서 사용하기 위해서 직렬화된 형식(serialization format)이 좋습니다. 저장된 모델은 두 부분으로 이루어져 있습니다: 하나 또는 더 많은 그래프들이 `GraphDefs`와 체크포인트로 인코드 됩니다. 그래프는 실행할 연산의 데이터 흐름를 기술하고 체크포인트는 그래프 변수들의 저장된 텐서값을 포함합니다.

많은 텐서플로 사용자들이 저장된 모델을 만들고 나중에 릴리즈된 텐서플로에서 로드하여 실행합니다. [semver](https://semver.org)에 따라 어떤 버전의 텐서플로에서 저장된 모델은 같은 주 버전에 속한 나중 버전의 텐서플로에서는 로드되고 실행될 수 있습니다.

*지원하는* 저장된 모델에서는 추가적인 보장이 있습니다. 텐서플로 주 버전 `N`에서 **사라지지 않고 실험적이지도 않으며 호환되지 않는 API**를 사용하여 만든 저장된 모델은 *버전 `N`에서 지원됩니다.* 텐서플로 주 버전 `N`에서 지원하는 모든 저장된 모델은 텐서플로 주 버전 `N+1`에서도 로드되고 실행될 수 있습니다. 그러나, 그 모델을 만들고 수정하기 위해 필요한 기능들을 더 이상 사용할 수 없는 경우, 이 보장은 수정하지 않은 저장된 모델에만 적용됩니다.

가능하면 하위 호환성을 유지하기위해 노력할 것이라서 직렬화된 파일들은 오랫동안 사용가능합니다.

### GraphDef 호환성

그래프는 `GraphDef` 프로토콜 버퍼에 의해 직렬화됩니다. 하위 호환되는 변경사항들을 그래프에 적용하기 위해 각 `GraphDef`는 텐서플로 버전과는 분리된 버전을 가집니다. 예를들어, `GraphDef` 버전 17은 `reciprocal`을 위해 `inv` 연산을 제거하였습니다. 그 의미는:

* 텐서플로의 각 버전은 `GraphDef` 버전들간 지원됩니다. 버전 간격은 패치 릴리즈에서는 일정하고 부 릴리즈에서만 증가합니다. `GraphDef` 버전에 대한 지원 중단은 텐서플로 주 버전일때만 발생합니다. (그리고 저장된 모델에 대한 보장된 버전 지원과 함께합니다.)

* 새롭게 생성된 그래프는 최신 `GraphDef` 버전으로 할당됩니다.

* 텐서플로의 주 버전과는 상관없이 주어진 텐서플로의 버전이 그래프의 `GraphDef` 버전을 지원한다면, 해당 텐서플로 버전이 그래프를 생성하는 방식과 같이 로드하고 실행할 것입니다. (위에 기술된 것과 같은 부동 소수점의 세부값과 랜덤 숫자는 제외). 특히, 하나의 GraphDef 어떠한 버전의 텐서플로 체크포인트 파일과 호환되는 하나의 GraphDef는 GraphDef가 지원되는 동안에는 차후 버전의 체크포인트와 호환이 가능합니다. 

  GraphDef의 직렬화된 그래프(와 저장된 모델)에만 적용되는 사항임에 유의하세요. 체크포인트를 읽는 *코드*는 다른 버전에서 동작하는 같은 코드가 생성한 체크포인트를 읽지 못할 수 있습니다.

* `GraphDef`의 *상한*이 부 버전 안에서 X로 올라가면, *하한*이 X로 올라가는데 적어도 6개월이 걸립니다. 예를 들어서 (여기서의 버전은 가상 버전입니다):

    * 텐서플로 1.2는 `GraphDef` 버전 4에서 7까지 지원할 수 있습니다.
    * 텐서플로 1.3은 `GraphDef` 버전 8을 추가할 수 있고 버전 4에서 7까지 지원할 수 있습니다.
    * 적어도 6개월 이후에, 텐서플로 2.0.0은 버전 4에서 7을 지원하지 않고 버전 8만 지원할 예정입니다.

  텐서플로의 주 버전은 보통 6개월 이상의 간격으로 출시되기 때문에, 위에 설명된 저장된 모델 지원에 대한 보장은 GraphDef의 6개월 보장보다 더 강력합니다.

최종적으로, `GraphDef` 버전의 지원이 끝났을 때, 새롭게 지원하는 `GraphDef` 버전으로 자동적으로 그래프를 변환하는 툴을 제공할 계획입니다.

## 텐서플로 확장시 그래프와 체크포인트 호환성

이 섹션은 연산을 추가하거나 제거하거나 기존 연산의 기능을 바꾸는 것과 같은 `GraphDef` 형식에 호환이 안되는 변동사항이 생겼을 때만 해당합니다. 대부분의 사용자들은 이전 섹션으로 충분합니다.

<a id="backward_forward"/>

### 하위 호환성과 부분적 상위 호환성

Our versioning scheme has three requirements:

*   **Backward compatibility** to support loading graphs and checkpoints
    created with older versions of TensorFlow.
*   **Forward compatibility** to support scenarios where the producer of a
    graph or checkpoint is upgraded to a newer version of TensorFlow before
    the consumer.
*   Enable evolving TensorFlow in incompatible ways. For example, removing ops,
    adding attributes, and removing attributes.

Note that while the `GraphDef` version mechanism is separate from the TensorFlow
version, backwards incompatible changes to the `GraphDef` format are still
restricted by Semantic Versioning.  This means functionality can only be removed
or changed between `MAJOR` versions of TensorFlow (such as `1.7` to `2.0`).
Additionally, forward compatibility is enforced within Patch releases (`1.x.1`
to `1.x.2` for example).

To achieve backward and forward compatibility and to know when to enforce changes
in formats, graphs and checkpoints have metadata that describes when they
were produced. The sections below detail the TensorFlow implementation and
guidelines for evolving `GraphDef` versions.

### Independent data version schemes

There are different data versions for graphs and checkpoints. The two data
formats evolve at different rates from each other and also at different rates
from TensorFlow. Both versioning systems are defined in
[`core/public/version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/public/version.h).
Whenever a new version is added, a note is added to the header detailing what
changed and the date.

### Data, producers, and consumers

We distinguish between the following kinds of data version information:
* **producers**: binaries that produce data.  Producers have a version
  (`producer`) and a minimum consumer version that they are compatible with
  (`min_consumer`).
* **consumers**: binaries that consume data.  Consumers have a version
  (`consumer`) and a minimum producer version that they are compatible with
  (`min_producer`).

Each piece of versioned data has a [`VersionDef
versions`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/versions.proto)
field which records the `producer` that made the data, the `min_consumer`
that it is compatible with, and a list of `bad_consumers` versions that are
disallowed.

By default, when a producer makes some data, the data inherits the producer's
`producer` and `min_consumer` versions. `bad_consumers` can be set if specific
consumer versions are known to contain bugs and must be avoided. A consumer can
accept a piece of data if the following are all true:

*   `consumer` >= data's `min_consumer`
*   data's `producer` >= consumer's `min_producer`
*   `consumer` not in data's `bad_consumers`

Since both producers and consumers come from the same TensorFlow code base,
[`core/public/version.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/public/version.h)
contains a main data version which is treated as either `producer` or
`consumer` depending on context and both `min_consumer` and `min_producer`
(needed by producers and consumers, respectively). Specifically,

*   For `GraphDef` versions, we have `TF_GRAPH_DEF_VERSION`,
    `TF_GRAPH_DEF_VERSION_MIN_CONSUMER`, and
    `TF_GRAPH_DEF_VERSION_MIN_PRODUCER`.
*   For checkpoint versions, we have `TF_CHECKPOINT_VERSION`,
    `TF_CHECKPOINT_VERSION_MIN_CONSUMER`, and
    `TF_CHECKPOINT_VERSION_MIN_PRODUCER`.

### Add a new attribute with default to an existing op

Following the guidance below gives you forward compatibility only if the set of
ops has not changed:

1. If forward compatibility is desired, set `strip_default_attrs` to `True`
   while exporting the model using either the
   `tf.saved_model.SavedModelBuilder.add_meta_graph_and_variables`
   and `tf.saved_model.SavedModelBuilder.add_meta_graph`
   methods of the `SavedModelBuilder` class, or
   `tf.estimator.Estimator.export_saved_model`
2. This strips off the default valued attributes at the time of
   producing/exporting the models. This makes sure that the exported
   `tf.MetaGraphDef` does not contain the new op-attribute when the default
   value is used.
3. Having this control could allow out-of-date consumers (for example, serving
   binaries that lag behind training binaries) to continue loading the models
   and prevent interruptions in model serving.

### Evolving GraphDef versions

This section explains how to use this versioning mechanism to make different
types of changes to the `GraphDef` format.

#### Add an op

Add the new op to both consumers and producers at the same time, and do not
change any `GraphDef` versions. This type of change is automatically
backward compatible, and does not impact forward compatibility plan since
existing producer scripts will not suddenly use the new functionality.

#### Add an op and switch existing Python wrappers to use it

1.  Implement new consumer functionality and increment the `GraphDef` version.
2.  If it is possible to make the wrappers use the new functionality only in
    cases that did not work before, the wrappers can be updated now.
3.  Change Python wrappers to use the new functionality. Do not increment
    `min_consumer`, since models that do not use this op should not break.

#### Remove or restrict an op's functionality

1.  Fix all producer scripts (not TensorFlow itself) to not use the banned op or
    functionality.
2.  Increment the `GraphDef` version and implement new consumer functionality
    that bans the removed op or functionality for GraphDefs at the new version
    and above. If possible, make TensorFlow stop producing `GraphDefs` with the
    banned functionality. To do so, add the
    [`REGISTER_OP(...).Deprecated(deprecated_at_version,
    message)`](https://github.com/tensorflow/tensorflow/blob/b289bc7a50fc0254970c60aaeba01c33de61a728/tensorflow/core/ops/array_ops.cc#L1009).
3.  Wait for a major release for backward compatibility purposes.
4.  Increase `min_producer` to the GraphDef version from (2) and remove the
    functionality entirely.

#### Change an op's functionality

1.  Add a new similar op named `SomethingV2` or similar and go through the
    process of adding it and switching existing Python wrappers to use it.
    To ensure forward compatibility use the checks suggested in
    [compat.py](https://www.tensorflow.org/code/tensorflow/python/compat/compat.py)
    when changing the Python wrappers.
2.  Remove the old op (Can only take place with a major version change due to
    backward compatibility).
3.  Increase `min_consumer` to rule out consumers with the old op, add back the
    old op as an alias for `SomethingV2`, and go through the process to switch
    existing Python wrappers to use it.
4.  Go through the process to remove `SomethingV2`.

#### Ban a single unsafe consumer version

1.  Bump the `GraphDef` version and add the bad version to `bad_consumers` for
    all new GraphDefs. If possible, add to `bad_consumers` only for GraphDefs
    which contain a certain op or similar.
2.  If existing consumers have the bad version, push them out as soon as
    possible.
