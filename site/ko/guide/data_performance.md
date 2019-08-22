# tf.data Performance

Note: 이 문서는 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고
[공식 영문 문서](https://github.com/tensorflow/docs/blob/master/site/en/guide/data_performance.md)의
내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

## 개요

GPU와 TPU는 하나의 학습 단계를 실행하는데 필요한 시간을 급격하게 줄일 수 있습니다. 최대 성능을 위해서는 현재 단계가 종료되기 전에 다음
단계의 데이터를 운반하는 효율적인 입력 파이프라인이 필요합니다.`tf.data` API는 유연하고 효율적인 입력 파이프라인을 만드는데 도움이
됩니다. 이 문서는 다양한 모델과 가속기에서 고성능의 텐서플로 입력 파이프라인을 만드는 방법과 `tf.data` API의 특정을 설명합니다.

이 가이드는 다음의 내용을 포함합니다:

*   텐서플로 입력 파이프라인이 기본적으로
    [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) 프로세스라는 것을
    설명합니다.
*   고성능 텐서플로 입력 파이프라인을 설계하기 위해 권장하는 방법을 설명합니다.
*   변환 순서에 따른 성능 영향에 대해 설명합니다.

## 입력 파이프라인 구조

전형적인 텐서플로 훈련 입력 파이프라인은 ETL 프로세스로 구성될 수 있습니다:

1.  **추출**: 메모리(NumPy)나 로컬(HDD 또는 SSD) 이나 원격(이를테면
    [GCS](https://cloud.google.com/storage/)또는
    [HDFS](https://en.wikipedia.org/wiki/Apache_Hadoop#Hadoop_distributed_file_system))
    영구 스토리지로부터 데이터를 읽어들입니다.
2.  **변환**: 분석하기 위해 CPU를 사용하여 셔플링(shuffling), 배칭(batching), 그리고 이미지 압축 해제와
    증식(augmentation), 텍스트 벡터화 또는 비디오 시간 샘플링과 같은 특정 도메인의 변환과 같은 데이터에 대한 전처리를
    수행합니다.
3.  **적재**: 변환된 데이터를 가속장치(들)에 적재합니다. (예를들면, 기계학습 모델을 실행하는 GPU나 TPU)

이 패턴은 CPU를 효과적으로 사용하면서 모델 훈련을 많이 수행하도록 가속기를 예비합니다. 게다가 입력 파이프라인을 ETL 프로세스로 보는 것은
성능 최적화를 쉽게 적용할 수 있는 프레임워크를 제공합니다.

아래 예제는 레이블된 이미지가 포함된 TFRecord 파일들을 읽고 이를 학습에 적합한 이미지-레이블 쌍의 배치(batch)로 변환하는 입력
파이프라인의 간단한 구현을 보여줍니다. 입력 파이프라인은 `tf.data.Dataset`로 표현되고 `tf.keras`와 같은 고수준의 텐서플로
API에 전달될 수 있습니다.

```
def parse_fn(example):
  "TFExample 레코드를 분석하고 간단한 데이터 증식을 수행합니다."
  example_fmt = {
    "image": tf.FixedLengthFeature((), tf.string, ""),
    "label": tf.FixedLengthFeature((), tf.int64, -1)
  }
  parsed = tf.parse_single_example(example, example_fmt)
  image = tf.io.image.decode_image(parsed["image"])
  image = _augment_helper(image)  # slice, reshape, resize_bilinear를 이용하여 이미지 증식을 수행합니다
  return image, parsed["label"]

def make_dataset():
  dataset = tf.data.TFRecordDataset("/path/to/dataset/train-*.tfrecord")
  dataset = dataset.shuffle(buffer_size=FLAGS.shuffle_buffer_size)
  dataset = dataset.map(map_func=parse_fn)
  dataset = dataset.batch(batch_size=FLAGS.batch_size)
  return dataset
```

다음 섹션은 이 입력 파이프라인을 기반으로 하고 고성능의 텐서플로 입력 파이프라인을 설계하기 위한 최상의 사례를 포함하고 있습니다.

## 성능 최적화

GPU나 TPU같은 새로운 컴퓨팅 장치들이 인공신경망을 빠른 속도로 훈련시키는 것이 가능해져서 CPU에 의한 처리는 병목현상이 일어나기
쉽습니다. `tf.data` API는 사용자에게 CPU를 효율적으로 활용하고 ETL 프로세스의 각 단계를 최적화하는 입력 파이프라인 설계의
구성요소를 제공합니다.

### 파이프라이닝

훈련 단계를 수행하기 위해서 우선 훈련 데이터를 추출하고 변환해야 합니다. 그 뒤에 가속기에서 실행되는 모델에 넣습니다. 그러나, 단순 동기식
구현에서는 CPU가 데이터를 준비하는 동안 가속기가 유휴상태로 있습니다. 반대로, 가속기가 모델을 훈련할 때 CPU는 유휴상태입니다. 그러므로
훈련 스텝 타임은 CPU에서의 전처리 시간과 가속기의 훈련 시간의 총합이 됩니다.

**파이프라이닝**은 전처리와 훈련 스텝의 모델 실행을 오버랩합니다. 가속기가 `N` 훈련 스텝을 수행하는 동안 CPU는 `N+1` 스텝의
데이터를 준비합니다. 이렇게 하면 스텝 시간과 데이터를 추출하고 변형하는 시간을 최대한 단축시킬 수 있습니다.

파이프라이닝이 없다면 CPU와 GPU/TPU는 많은 시간 동안 유휴상태입니다:

![without pipelining](https://www.tensorflow.org/images/datasets_without_pipelining.png)

파이프라이닝이 있다면 유휴 시간은 아주 많이 줄어듭니다:

![with pipelining](https://www.tensorflow.org/images/datasets_with_pipelining.png)

`tf.data` API는 소프트웨어 파이프라이닝 방법을 `tf.data.Dataset.prefetch` 변환을 통해 제공합니다. 이것은
데이터가 소비되는 시간과 데이터가 생성되는 시간 간의 의존성을 줄일 수 있습니다. 특히, 이 변환은 백그라운드 스레드와 내부 버퍼를 사용하여
요청된 시간 전에 입력 데이터 세트에서 요소를 프리페치(prefetch)합니다. 프리페치할 요소의 수는 하나의 훈련 스텝에서 소비한 배치의 수와
같거나 커야 합니다. 이 값을 수동으로 조정하거나 `tf.data.experimental.AUTOTUNE`으로 설정하면 tf.data 런타임이
실행 시에 동적으로 값을 조정하도록 만듭니다.

이 변화를 예제에 적용하려면, 다음을 넣으세요:

```
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
```

입력 파이프라인의 마지막 변형으로서 말입니다.

프리페치 변환은 "프로듀서"의 작업과 "컨슈머"의 작업과 오버랩이 가능할 때마다 이점을 제공합니다.

### 데이터 변환 병렬화

배치를 준비할 때, 입력 요소들은 전처리가 필요할 수 있습니다. 이것 때문에 `tf.data` API가 `tf.data.Dataset.map`
변환을 제공하고, 그것은 사용자 정의 함수(예를 들어, 예제의 `parse_fn`)를 입력 데이터셋의 각 요소에 적용합니다. 입력 요소가 서로
독립적이기 때문에 전처리는 여러 개의 CPU 코어에서 병렬로 실행될 수 있습니다. 이를 가능하게 하기위해 `map` 변환은 병렬화 정도를
설정하는 `num_parallel_calls` 매개변수를 제공합니다. 예를 들어, 다음의 그림은 `map` 변환에서
`num_parallel_calls=2`로 설정하였을 때의 영향을 보여줍니다.

![parallel map](https://www.tensorflow.org/images/datasets_parallel_map.png)

가장 좋은 `num_parallel_calls` 값은 하드웨어, 훈련 데이터(사이즈와 모양), 맵 함수의 비용, 그리고 CPU에서 동시에 어떤
처리가 수행되는지에 따라 다릅니다; 단순한 방법으로 가용한 CPU 코어의 숫자로 설정할 수 있습니다. 예를 들어, 위의 예제를 4개의 코어를
가진 컴퓨터에서 실행시킨다면 `num_parallel_calls=4`로 설정하는 것이 더 효율적이었을 것입니다. 반면에,
`num_parallel_calls`를 가용한 CPU 코어 숫자보다 훨씬 더 많이 설정한다면 비효율적인 스케줄링으로 느려질 것입니다.
`prefetch` 변환과 비슷하게 `map` 변환은 tf.data 런타임에 가용되는 병렬화 수준을 결정하는
`tf.data.experimental.AUTOTUNE`을 제공합니다.

이 변화를 예제에 적용하려면, 다음의 코드를:

```
dataset = dataset.map(map_func=parse_fn)
```

다음처럼 변경하세요:

```
dataset = dataset.map(map_func=parse_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

### 데이터 추출 병렬화

실제 환경에서는 입력 데이터가 로컬에 맞지 않거나 학습이 분산되어 있고 입력 데이터를 모든 컴퓨터에 복제하는 것은 적절하지 않기 때문에 입력
데이터를 원격으로(이를테면, GCS나 HDFS) 저장할 수 있습니다. 데이터를 로컬에서 읽는 데이터셋 파이프라인은 다음과 같은 로컬과 원격
저장소의 차이 때문에 원격으로 데이터를 읽을 때 입출력에 병목이 발생할 수 있습니다:

*   **첫 번째 바이트(Time-to-first-byte):** 원격 저장소에서 파일의 첫 번째 바이트를 읽는 것은 로컬 저장소에서 읽어
    들이는 것보다 훨씬 오래 걸립니다.
*   **읽기 처리량(Read throughput):** 원격 저장소는 보통 큰 총 대역폭을 가지지만 하나의 파일을 읽을 때 이 대역폭의
    일부만 활용할 수 있습니다.

게다가 바이트들이 메모리로 읽혀지면 데이터를 역직렬화 그리고/또는 해독할 필요가 있을 수 있습니다(예를 들면,
[protobuf](https://developers.google.com/protocol-buffers/)). 이 작업은 추가적인 계산이
필요합니다. 이 오버헤드는 데이터가 로컬 또는 원격으로 저장되는지와는 관계없이 존재하지만 데이터가 효과적으로 프리페치되지 않으면 원격의 경우에
나빠질 수 있습니다.

다양한 데이터 추출 오버헤드의 영향을 줄이기 위해 `tf.data.Dataset.interleave` 변환은 (데이터 파일 판독기와 같은)다른
데이터셋의 내용을 인터리빙(interleaving)하여 데이터 추출 단계를 병렬화하는데 사용할 수 있습니다. 중첩할 데이터셋은
`cycle_length` 매개변수에 의해 지정될 수 있는 반면, 병렬처리 수준은 `num_parallel_calls` 매개변수에 의해 지정될
수 있습니다. `prefetch`와 `map` 변환과 비슷하게 `interleave` 변환은
`tf.data.experimental.AUTOTUNE`을 지원합니다. 이것은 어떤 수준의 병렬처리가 tf.data 런타임에 사용되는지에 대해
결정합니다.

다음의 그림은 `interleave` 변환에 `cycle_length=2` 그리고 `num_parallel_calls=2`로 설정했을 때의
영향을 보여줍니다:

![parallel io](https://www.tensorflow.org/images/datasets_parallel_io.png)

이 변화를 예제에 적용하려면 다음의 코드를:

```
dataset = tf.data.TFRecordDataset("/path/to/dataset/train-*.tfrecord")
```

다음처럼 변경하세요:

```
files = tf.data.Dataset.list_files("/path/to/dataset/train-*.tfrecord")
dataset = files.interleave(
    tf.data.TFRecordDataset, cycle_length=FLAGS.num_parallel_reads,
    num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

## 성능 고려사항

`tf.data` API는 사용자들에게 유연성을 제공할 수 있도록 구성할 수 있는 변환을 중심으로 설계되었습니다. 이러한 변환들의 다수가
교환적이지만, 특정 변환의 순서는 성능에 영향을 줍니다.

### 맵과 배치

`map`변환에 전달된 사용자 정의 함수를 호출하는 것은 사용자 정의 함수의 스케줄링과 실행에 관련된 오버헤드가 있습니다. 보통의 경우 이
오버헤드는 함수에 의해 수행되는 계산량보다 작습니다. 그러나 `map`이 거의 작동하지 않는다면 이 오버헤드가 총 비용에서 가장 클 수
있습니다. 이러한 경우에 사용자 정의 함수를 벡터화(즉, 한번에 입력 배치를 통해 작동하도록)하고 `batch` 변환을 `map` 변환
_이전에_ 적용하는 것이 좋습니다.

### 맵과 캐시

`tf.data.Dataset.cache` 변환은 데이터셋을 메모리 또는 로컬 저장소에 캐시할 수 있습니다. 만약 `map`변환에 전달된 사용자
정의 함수가 비싸다면 결과로 나온 데이터셋이 메모리나 로컬 저장소에 들어갈 수 있는 한은 `map`변환 후에 캐시 변환을 적용하세요. 사용자
정의 함수가 캐시 용량을 초과해서 데이터셋을 저장하는데 필요한 공간을 늘리면 훈련 작업 전에 데이터를 전처리하여 리소스 사용을 줄이는 것이
좋습니다.

### 맵과 인터리브(Interleave) / 프리페치 / 셔플(Shuffle)

`interleave`, `prefetch`, `shuffle`을 포함한 많은 변환은 요소들의 내부 버퍼를 유지합니다. 사용자 정의 함수가
`map` 변환에 전달된 경우 요소의 크기가 변경되고 맵 변환의 순서와 버퍼 요소가 메모리 사용에 영향을 줍니다. 일반적으로 순서를 다르게 하는
것이 성능에 도움이 되는 경우(예를 들어, 맵과 배치 처리를 융합(fusing)하는 경우) 메모리 사용량이 낮아지는 순서를 선택하는 것이
좋습니다.

### 반복과 셔플

`tf.data.Dataset.repeat` 변환은 입력 데이터를 유한하게(또는 무한하게) 반복합니다; 데이터의 각 반복은 보통
_에포크_(epoch)라고 합니다. `tf.data.Dataset.shuffle` 변환은 데이터셋의 샘플 순서를 랜덤화합니다.

`shuffle` 변환 전에 `repeat` 변환이 적용되면 에포크의 경계가 모호해집니다. 즉, 특정 요소는 다른 요소가 한번 나타나기 전에
반복될 수 있습니다. 반면에, `shuffle` 변환이 `repeat` 변환 전에 적용되면 `shuffle` 변환의 내부 상태 초기화와 관련되어
각 에포크 시작 부분에서 성능이 저하될 수 있습니다. 다시 말해서, 전자(`shuffle` 전에 `repeat`)는 성능이 더 좋고
후자(`repeat` 전에 `shuffle`)은 순서를 더 강하게 보장합니다.

## 가장 좋은 예제 요약

다음은 성능이 좋은 텐서플로 입력 파이프라인을 설계하기 위한 가장 좋은 예제를 요약한 것입니다:

*   `prefetch` 변환을 사용하여 프로듀서와 컨슈머의 작업을 오버랩하세요. 특히 입력 파이프라인의 끝 부분에 `prefetch`를
    추가하여 CPU에서 수행된 변환과 가속기에서 수행된 훈련을 오버랩하는 것이 좋습니다. 버퍼 크기를 수동으로 조정하거나
    `tf.data.experimental.AUTOTUNE`을 사용하여 결정을 tf.data 런타임에 맡기세요.
*   `num_parallel_calls` 매개변수를 설정하여 `map` 변환을 병렬 처리하세요. 병렬 처리 수준을 수동으로 조정하거나
    `tf.data.experimental.AUTOTUNE`을 사용하여 tf.data 런타임에 결정을 맡기세요.
*   원격으로 저장된 데이터를 작업하거나 역직렬화(deserialization)가 필요하다면 서로 다른 파일로부터의 데이터 읽기(그리고
    역직렬화)를 병렬화하기 위해 `interleave` 변환을 사용하는 것이 좋습니다.
*   `map` 변환에 전달된 저렴한 사용자 정의 함수를 벡터화하여 함수의 스케줄링 및 실행과 관련된 오버헤드를 상환합니다.
*   데이터가 메모리에 저장될 수 있는 경우, `cache` 변환을 사용하여 첫 번째 에포크동안 데이터를 메모리에 캐시하세요, 그렇게 하면
    뒤따르는 에포크들은 읽기, 파싱, 그리고 변환에 관련한 오버헤드를 피할 수 있습니다.
*   전처리해서 데이터 사이즈가 증가한다면 `interleave`, `prefetch`, 그리고 `shuffle`을 (가능하다면)먼저 적용하여
    메모리 사용을 줄이는 것이 좋습니다.
*   `repeat` 변환 _이전에_ `shuffle` 변환을 적용하는 것이 좋습니다.
