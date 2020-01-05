# ExampleGen TFX パイプラインコンポーネント

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

TFX パイプラインコンポーネントの1つである ExampleGen コンポーネントはデータを TFX のパイプラインに投入します。
これは外部のファイルやサービスからデータを読み取り、ほかの TFX のコンポーネントが読み取る Examples を生成します。
また、、一貫性のある方法でデータセットを分割します。分割は設定により変更可能です。
同時に機械学習のベストプラクティスに従い、データセットの並び替えを行います。

- 入力: CSV や `TFRecord`, BigQuery といった外部のデータソースからのデータ
- 出力: `tf.Example` レコード

## ExampleGen とその他のコンポーネント

ExampleGen は [TensorFlow Data Validation](tfdv.md) ライブラリを利用するコンポーネントにデータを提供します。
これには [SchemaGen](schemagen.md), [StatisticsGen](statsgen.md), [Example Validator](exampleval.md) が含まれます。
また、[TensorFlow Transform](tft.md) を利用する [Transform](transform.md) にもデータを提供し、最終的には推論時にデプロイメントターゲットへとデータを供給します。

## ExampleGen コンポーネントの使い方

サポートされるデータソース (現在、CSV ファイル、TF Example フォーマットの TFRecord ファイル、BigQuery のクエリ結果、の3つがサポートされています) を用いる場合、ExampleGen コンポーネントは典型的には非常に簡単にデプロイ可能で、ほとんど改修を必要とせずに利用できます。
典型的なコードは次のようになります:

```python
from tfx.utils.dsl_utils import csv_input
from tfx.components.example_gen.csv_example_gen.component import CsvExampleGen

examples = csv_input(os.path.join(base_dir, 'data/simple'))
example_gen = CsvExampleGen(input=examples)
```

次のように、外部の TF Example 形式のファイルを直接読み込むこともできます:

```python
from tfx.utils.dsl_utils import tfrecord_input
from tfx.components.example_gen.import_example_gen.component import ImportExampleGen

examples = tfrecord_input(path_to_tfrecord_dir)
example_gen = ImportExampleGen(input=examples)
```

## Span, Version and Split

A Span is a grouping of training examples. If your data is persisted on a
filesystem, each Span may be stored in a separate directory. The semantics of a
Span are not hardcoded into TFX; a Span may correspond to a day of data, an hour
of data, or any other grouping that is meaningful to your task.

Each Span can hold multiple Versions of data. To give an example, if you remove
some examples from a Span to clean up poor quality data, this could result in a
new Version of that Span. By default, TFX components operate on the latest
Version within a Span.

Each Version within a Span can further be subdivided into multiple Splits. The
most common use-case for splitting a Span is to split it into training and eval
data.

![Spans and Splits](images/spans_splits.png)

## カスタム input/output split

Note: この機能は TFX 0.14 以降でのみ利用可能です。

ExampleGen が出力する 学習/評価 データの比率を変更するためには、`output_config` を ExampleGen コンポーネントに設定してください。
例を次に示します:

```python
from  tfx.proto import example_gen_pb2

# Input has a single split 'input_dir/*'.
# Output 2 splits: train:eval=3:1.
output = example_gen_pb2.Output(
             split_config=example_gen_pb2.SplitConfig(splits=[
                 example_gen_pb2.SplitConfig.Split(name='train', hash_buckets=3),
                 example_gen_pb2.SplitConfig.Split(name='eval', hash_buckets=1)
             ]))
examples = csv_input(input_dir)
example_gen = CsvExampleGen(input=examples, output_config=output)
```

この例の中でどのように `hash_buckets` が設定されているかに注意してください。

すでに入力データが分割されている場合、`input_config` を ExampleGen コンポーネントに設定してください。
例を次に示します:

```python
from  tfx.proto import example_gen_pb2

# Input train split is 'input_dir/train/*', eval split is 'input_dir/eval/*'.
# Output splits are generated one-to-one mapping from input splits.
input = example_gen_pb2.Input(splits=[
                example_gen_pb2.Input.Split(name='train', pattern='train/*'),
                example_gen_pb2.Input.Split(name='eval', pattern='eval/*')
            ])
examples = csv_input(input_dir)
example_gen = CsvExampleGen(input=examples, input_config=input)
```

ファイルベースの ExampleGen コンポーネント (たとえば、 CsvExampleGen や ImportExampleGen) では、`pattern` は入力ファイルをまとめたディレクトリからの相対パスを glob 形式で記述したものになります。
クエリベースの ExampleGen コンポーネント (たとえば、BigQUeryExampleGen や PrestoExampleGen) では、`pattern` はSQLクエリになります。

デフォルトでは入力データをまとめたディレクトリには単一のファイルがあるものとして扱われます。また、学習/評価用のデータの分割は2:1の割合になるように行われます。

詳細については [proto/example_gen.proto](https://github.com/tensorflow/tfx/blob/master/tfx/proto/example_gen.proto) を参照してください。

### Span

Note: this feature is only available after TFX 0.15.

Span can be retrieved by using '{SPAN}' spec in the
[input glob pattern](https://github.com/tensorflow/tfx/blob/master/tfx/proto/example_gen.proto):

*   This spec matches digits and maps the data into the relevant SPAN numbers.
    For example, 'data_{SPAN}-*.tfrecord' will collect files like
    'data_12-a.tfrecord', 'date_12-b.tfrecord'.
*   When SPAN spec is missing, it's assumed to be always Span '0'.
*   If SPAN is specified, pipeline will process the latest span, and store the
    span number in metadata

For example, let's assume there are input data:

*   '/tmp/span-01/train/data'
*   '/tmp/span-01/eval/data'
*   '/tmp/span-02/train/data'
*   '/tmp/span-02/eval/data'

and the input config is shown as below:

```python
splits {
  name: 'train'
  pattern: 'span-{SPAN}/train/*'
}
splits {
  name: 'eval'
  pattern: 'span-{SPAN}/eval/*'
}
```

when triggering the pipeline, it will process:

*   '/tmp/span-02/train/data' as train split
*   '/tmp/span-02/eval/data' as eval split

with span number as '02'. If later on '/tmp/span-03/...' are ready, simply
trigger the pipeline again and it will pick up span '03' for processing. Below
shows the code example for using span spec:

```python
from  tfx.proto import example_gen_pb2

input = example_gen_pb2.Input(splits=[
                example_gen_pb2.Input.Split(name='train',
                                            pattern='span-{SPAN}/train/*'),
                example_gen_pb2.Input.Split(name='eval',
                                            pattern='span-{SPAN}/eval/*')
            ])
examples = csv_input('/tmp')
example_gen = CsvExampleGen(input=examples, input_config=input)
```

Note: Retrieving a certain span is not supported yet. You can only fix the
pattern for now (for example, 'span-2/eval/*' instead of 'span-{SPAN}/eval/*'),
but by doing this, span number stored in metadata will be zero.

### Version

Note: Version is not supported yet

## カスタム ExampleGen

Note: この機能は TFX 0.14 以降でのみ利用可能です。

現在利用可能な ExampleGen コンポーネントが利用者のニーズに合わない場合、BaseExampleGenExecutor を用いて専用の ExampleGen コンポーネントを自作できます。

### ファイルベースの ExampleGen の場合

BaseExampleGenExecutor を拡張するためには、まず、専用の Beam PTransform を作成し、学習/評価データを TF Example 形式に変換する処理を記述します。
たとえば、[CsvExampleGen executor](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/csv_example_gen/executor.py)では、分割されたCSVを入力とし、TF Example 形式に変換する処理を記述しています。

次に、BaseExampleGenExecutor を利用したコンポーネントを作成します。[CsvExampleGen コンポーネント](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/csv_example_gen/component.py) で同様のことを行っています。
他にも、専用の Executor を標準の ExampleGen コンポーネントに渡すことでも同様のことを実現できます。
例を次に示します:

```python
from tfx.components.base import executor_spec
from tfx.components.example_gen.component import FileBasedExampleGen
from tfx.components.example_gen.csv_example_gen import executor
from tfx.utils.dsl_utils import external_input

examples = external_input(os.path.join(base_dir, 'data/simple'))
example_gen = FileBasedExampleGen(
    input=examples,
    custom_executor_spec=executor_spec.ExecutorClassSpec(executor.Executor))
```

現在、[この手法を用いたAvro ファイルや Parquet ファイルの読み込み](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/custom_executors/avro_component_test.py) もサポートしています。

### クエリベースの ExampleGen の場合

BaseExampleGenExecutor を拡張するためには、まず、専用の Beam PTransform を作成し、外部のデータソースからデータを読み込む処理を記述します。
次に、QueryBasedExampleGen を拡張したシンプルなコンポーネントを作成します。

コンポーネントは接続に関する追加の設定が必要な場合も、必要のない場合もあります。
たとえば、[BigQuery executor](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/big_query_example_gen/executor.py) は接続設定の詳細を抽象化した、デフォルトの beam.io コネクタを読み込みます。

[Presto executor](https://github.com/tensorflow/tfx/blob/master/tfx/examples/custom_components/presto_example_gen/presto_component/executor.py)は専用の Beam PTransform と [専用の接続設定用 protobuf](https://github.com/tensorflow/tfx/blob/master/tfx/examples/custom_components/presto_example_gen/proto/presto_config.proto)が入力として必要になります。

専用の ExampleGen コンポーネントで接続の設定が必要な場合、新規に protobuf を作成し、オプションの execution パラメータである custom_config を通じてコンポーネントに渡してください。
次のコードは設定を行っているコンポーネントを利用する方法の例です。

```python
from tfx.examples.custom_components.presto_example_gen.proto import presto_config_pb2
from tfx.examples.custom_components.presto_example_gen.presto_component.component import PrestoExampleGen

presto_config = presto_config_pb2.PrestoConnConfig(host='localhost', port=8080)
example_gen = PrestoExampleGen(presto_config, query='SELECT * FROM chicago_taxi_trips')
```
