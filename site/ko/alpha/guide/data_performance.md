# tf.data Performance

## 개요

GPU와 TPU는 하나의 학습 단계를 실행하는데 필요한 시간을 급격하게 줄일 수 있습니다. 최대 성능을 위해서는 현재 단계가 종료되기 전에 다음 단계의 데이터를 운반하는 효율적인 입력 파이프라인이 필요합니다.`tf.data` API는 유연하고 효율적인 입력 파이프라인을 만드는데 도움이 됩니다. 이 문서는 `tf.data` API의 특성과 다양한 모델과 가속기를 걸친 고성능의 텐서플로 입력 파이프라인을 만드는 방법을 설명합니다.


이 가이드는 다음의 내용을 포함합니다:

*   텐서플로 입력 파이프라인이 필수적으로 [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) 프로세스라는 것을 설명합니다.
*   고성능 텐서플로 입력 파이프라인을 설계하기 위해 권장하는 방법을 설명합니다.
*   변환을 적용한 순서의 성능 영향에 대해 설명합니다.

## 입력 파이프라인 구조

전형적인 텐서플로 훈련 입력 파이프라인은 ETL 프로세스로 구성될 수 있습니다:

1.  **추출**: 메모리(NumPy)나 로컬(HDD 또는 SSD) 이나 원격(이를테면 [GCS](https://cloud.google.com/storage/)또는 [HDFS](https://en.wikipedia.org/wiki/Apache_Hadoop#Hadoop_distributed_file_system)) 영구 스토리지로부터 데이터를 읽어들입니다.
2.  **변환**: 분석하기 위해 CPU를 사용하고 셔플링(shuffling), 배칭(batching), 그리고 이미지 압축 해제와 확대(augmentation), 텍스트 벡터화 또는 비디오 시간 샘플링과 같은 특정 도메인의 변환과 같은 데이터에 대한 전처리를 수행합니다.
3.  **적재**: 변환된 데이터를 가속장치(들)에 적재합니다. (예를들면, 기계학습 모델을 실행하는 GPU나 TPU)

이 패턴은 CPU를 효과적으로 사용하면서 모델 훈련을 많이 수행하도록 가속기를 예비합니다. 게다가 입력 파이프라인을 ETL 프로세스로 보는 것은 성능 최적화를 쉽게 적용할 수 있는 프레임워크를 제공합니다.

아래 예제는 레이블된 이미지가 포함된 TFRecord 파일들을 읽고 이를 학습에 적합한 이미지-레이블 쌍의 배치(batch)로 변환하는 입력 파이프라인의 간단한 구현을 보여줍니다. 입력 파이프라인은 `tf.data.Dataset`로 표현되고 `tf.keras`와 같은 고수준의 텐서플로 API에 전달될 수 있습니다.

```
def parse_fn(example):
  "TFExample 레코드를 분석하고 간단한 데이터 확대를 수행합니다."
  example_fmt = {
    "image": tf.FixedLengthFeature((), tf.string, ""),
    "label": tf.FixedLengthFeature((), tf.int64, -1)
  }
  parsed = tf.parse_single_example(example, example_fmt)
  image = tf.io.image.decode_image(parsed["image"])
  image = _augment_helper(image)  # slice, reshape, resize_bilinear를 이용하여 이미지를 확대합니다
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

GPU나TPU같은 새로운 컴퓨팅 장치들이 인공신경망을 빠른 속도로 훈련시키는 것이 가능해져서 CPU에 의한 처리는 병목현상이 일어나기 쉽습니다. `tf.data` API는 사용자에게 CPU를 효율적으로 활용하고 ETL 프로세스의 각 단계를 최적화하는 입력 파이프라인 설계의 구성요소를 제공합니다.

### 파이프라이닝

훈련 단계를 수행하기 위해서 우선 훈련 데이터를 추출하고 변형해야 합니다. 그 뒤에 가속기에서 실행되는 모델에 넣습니다. 그러나, 단순 동기식 구현에서는 CPU가 데이터를 준비하는 동안 가속기가 유휴상태로 있습니다. 반대로, 가속기기가 모델을 훈련할 때 CPU는 유휴상태입니다. 훈련 스텝 타임은 그러므로 CPU에서의 전처리 시간과 가속기의 훈련 시간의 총합이 됩니다.

**파이프라이닝**은 전처리와 훈련 스텝의 모델 실행을 오버랩합니다. 가속기가 `N` 훈련 스텝을 수행하는 동안 CPU는 `N+1` 스텝의 데이터를 준비합니다. 이렇게 하면 스텝 시간과 데이터를 추출하고 변형하는 시간을 최대한 단축시킬 수 있습니다.

파이프라이닝이 없다면 CPU와 GPU/TPU는 많은 시간 동안 유휴상태입니다:

![without pipelining](https://www.tensorflow.org/images/datasets_without_pipelining.png)

파이프라이닝이 있다면 유휴 시간은 아주 많이 줄어듭니다:

![with pipelining](https://www.tensorflow.org/images/datasets_with_pipelining.png)

`tf.data` API는 소프트웨어 파이프라이닝 방법을 `tf.data.Dataset.prefetch` 변환을 통해 제공합니다. 이것은 데이터가 소비된 시간으로부터 데이터가 생성되는 시간을 분리하는데 사용될 수 있습니다. 특히, 변환은 백그라운드 스레드와 내부 버퍼를 사용하여 요청된 시간 전에 입력 데이터 세트에서 요소를 프리페치(prefetch)합니다. 프리페치할 요소의 수는 하나의 훈련 스텝에서 소비한 배치의 수와 같거나 커야 합니다. 이 값을 수동으로 조정하거나 `tf.data.experimental.AUTOTUNE`으로 설정하면 tf.data 런타임이 런타임에 동적으로 값을 조정하도록 프롬프트합니다.

이 변화를 예제에 적용하려면, 다음을 넣으세요:

```
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
```

입력 파이프라인의 마지막 변형으로서 말입니다.

프리페치 변환은 "생산자"의 작업을 "소비자"의 작업과 오버랩이 가능할 때마다 이점을 제공합니다.

### 데이터 변환 병렬화

배치를 준비할 때, 입력 요소들은 전처리가 필요할 수 있습니다. 이것 때문에 `tf.data` API가 `tf.data.Dataset.map` 변환을 제공하고, 그것은 사용자 정의 함수(예를 들어, 예제의 `parse_fn`)를 입력 데이터셋의 각 요소에 적용합니다. 입력 요소가 서로 독립적이기 때문에 전처리는 여러 개의 CPU 코어에서 병렬로 실행될 수 있습니다. 이를 가능하게 하기위해 `map` 변환은 병렬화 정도를 설정하는 `num_parallel_calls` 매개변수를 제공합니다. 예를 들어, 다음의 그림은 `map` 변환에서 `num_parallel_calls=2`로 설정하였을 때의 영향을 보여줍니다.

![parallel map](https://www.tensorflow.org/images/datasets_parallel_map.png)

가장 좋은 `num_parallel_calls` 값은 하드웨어, 훈련 데이터(사이즈와 모양), 맵 함수의 비용, 그리고 CPU에서 동시에 어떤 처리가 수행되는지에 따라 다릅니다; 단순한 방법으로 가용한 CPU 코어의 숫자로 설정할 수 있습니다. 예를 들어, 위의 예제를 4개의 코어를 가진 컴퓨터에서 실행시킨다면 `num_parallel_calls=4`로 설정하는 것이 더 효율적이었을 것입니다. 반면에, `num_parallel_calls`를 가용한 CPU 코어 숫자보다 훨씬 더 많이 설정한다면 비효율적인 스케줄링으로 느려질 것입니다. `prefetch` 변환과 비슷하게 `map` 변환은 tf.data 런타임에 가용되는 병렬화 수준을 결정하는 `tf.data.experimental.AUTOTUNE`을 제공합니다.

이 변화를 예제에 적용하려면, 다음의 코드를:

```
dataset = dataset.map(map_func=parse_fn)
```

다음처럼 변경하세요:

```
dataset = dataset.map(map_func=parse_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

### 데이터 추출 병렬화

In a real-world setting, the input data may be stored remotely (for example, GCS
or HDFS), either because the input data would not fit locally or because the
training is distributed and it would not make sense to replicate the input data
on every machine. A dataset pipeline that works well when reading data locally
might become bottlenecked on I/O when reading data remotely because of the
following differences between local and remote storage:

*   **Time-to-first-byte:** Reading the first byte of a file from remote storage
    can take orders of magnitude longer than from local storage.
*   **Read throughput:** While remote storage typically offers large aggregate
    bandwidth, reading a single file might only be able to utilize a small
    fraction of this bandwidth.

In addition, once the raw bytes are read into memory, it may also be necessary
to deserialize and/or decrypt the data (e.g.
[protobuf](https://developers.google.com/protocol-buffers/)), which requires
additional computation. This overhead is present irrespective of whether the
data is stored locally or remotely, but can be worse in the remote case if data
is not prefetched effectively.

To mitigate the impact of the various data extraction overheads, the
`tf.data.Dataset.interleave` transformation can be used to parallelize the data
extraction step, interleaving the contents of other datasets (such as data file
readers). The number of datasets to overlap can be specified by the
`cycle_length` argument, while the level of parallelism can be specified by the
`num_parallel_calls` argument. Similar to the `prefetch` and `map`
transformations, the `interleave` transformation supports
`tf.data.experimental.AUTOTUNE` which will delegate the decision about what
level of parallelism to use to the tf.data runtime.

The following diagram illustrates the effect of supplying `cycle_length=2` and
`num_parallel_calls=2` to the `interleave` transformation:

![parallel io](https://www.tensorflow.org/images/datasets_parallel_io.png)

To apply this change to our running example, replace:

```
dataset = tf.data.TFRecordDataset("/path/to/dataset/train-*.tfrecord")
```

with:

```
files = tf.data.Dataset.list_files("/path/to/dataset/train-*.tfrecord")
dataset = files.interleave(
    tf.data.TFRecordDataset, cycle_length=FLAGS.num_parallel_reads,
    num_parallel_calls=tf.data.experimental.AUTOTUNE)
```

## Performance Considerations

The `tf.data` API is designed around composable transformations to provide its
users with flexibility. Although many of these transformations are commutative,
the ordering of certain transformations has performance implications.

### Map and Batch

Invoking the user-defined function passed into the `map` transformation has
overhead related to scheduling and executing the user-defined function.
Normally, this overhead is small compared to the amount of computation performed
by the function. However, if `map` does little work, this overhead can dominate
the total cost. In such cases, we recommend vectorizing the user-defined
function (that is, have it operate over a batch of inputs at once) and apply the
`batch` transformation _before_ the `map` transformation.

### Map and Cache

The `tf.data.Dataset.cache` transformation can cache a dataset, either in memory
or on local storage. If the user-defined function passed into the `map`
transformation is expensive, apply the cache transformation after the `map`
transformation as long as the resulting dataset can still fit into memory or
local storage. If the user-defined function increases the space required to
store the dataset beyond the cache capacity, consider pre-processing your data
before your training job to reduce resource usage.

### Map and Interleave / Prefetch / Shuffle

A number of transformations, including `interleave`, `prefetch`, and `shuffle`,
maintain an internal buffer of elements. If the user-defined function passed
into the `map` transformation changes the size of the elements, then the
ordering of the map transformation and the transformations that buffer elements
affects the memory usage. In general, we recommend choosing the order that
results in lower memory footprint, unless different ordering is desirable for
performance (for example, to enable fusing of the map and batch
transformations).

### Repeat and Shuffle

The `tf.data.Dataset.repeat` transformation repeats the input data a finite (or
infinite) number of times; each repetition of the data is typically referred to
as an _epoch_. The `tf.data.Dataset.shuffle` transformation randomizes the order
of the dataset's examples.

If the `repeat` transformation is applied before the `shuffle` transformation,
then the epoch boundaries are blurred. That is, certain elements can be repeated
before other elements appear even once. On the other hand, if the `shuffle`
transformation is applied before the repeat transformation, then performance
might slow down at the beginning of each epoch related to initialization of the
internal state of the `shuffle` transformation. In other words, the former
(`repeat` before `shuffle`) provides better performance, while the latter
(`shuffle` before `repeat`) provides stronger ordering guarantees.

## Summary of Best Practices

Here is a summary of the best practices for designing performant TensorFlow
input pipelines:

*   Use the `prefetch` transformation to overlap the work of a producer and
    consumer. In particular, we recommend adding `prefetch` to the end of your
    input pipeline to overlap the transformations performed on the CPU with the
    training done on the accelerator. Either manually tuning the buffer size, or
    using `tf.data.experimental.AUTOTUNE` to delegate the decision to the
    tf.data runtime.
*   Parallelize the `map` transformation by setting the `num_parallel_calls`
    argument. Either manually tuning the level of parallelism, or using
    `tf.data.experimental.AUTOTUNE` to delegate the decision to the tf.data
    runtime.
*   If you are working with data stored remotely and / or requiring
    deserialization, we recommend using the `interleave` transformation to
    parallelize the reading (and deserialization) of data from different files.
*   Vectorize cheap user-defined functions passed in to the `map` transformation
    to amortize the overhead associated with scheduling and executing the
    function.
*   If your data can fit into memory, use the `cache` transformation to cache it
    in memory during the first epoch, so that subsequent epochs can avoid the
    overhead associated with reading, parsing, and transforming it.
*   If your pre-processing increases the size of your data, we recommend
    applying the `interleave`, `prefetch`, and `shuffle` first (if possible) to
    reduce memory usage.
*   We recommend applying the `shuffle` transformation _before_ the `repeat`
    transformation.
