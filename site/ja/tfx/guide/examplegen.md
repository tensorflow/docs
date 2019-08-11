# ExampleGen TFX パイプラインコンポーネント

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

ExampleGen はデータを TFX のパイプラインに投入するコンポーネントです。
これは外部のファイルやサービスからデータを読み取り、他の TFX のコンポーネントが読み取る Examples を生成します。
また、機械学習のベストプラクティスに従い、データセットの分割や並び替えについて、一貫性のある設定可能な方法で提供します。

- 入力: CSV や `TFRecord`, BigQuery といった外部のデータソースからのデータ
- 出力: `tf.Example` レコード

## ExampleGen とその他のコンポーネント

ExampleGen は [TensorFlow Data Validation](tfdv.md) を利用するコンポーネントにデータを提供します。
これには [SchemaGen](schemagen.md), [StatisticsGen](statsgen.md), [Example Validator](exampleval.md) が含まれます。
また、[TensorFlow Transform](tft.md) を利用する [Transform](transform.md) にもデータを提供し、最終的には推論時にデプロイメントターゲットへとデータを供給します。

## ExampleGen コンポーネントの使い方

サポートされるデータソース (現在、CSV ファイル、TF Example フォーマットの TFRecord ファイル、BigQuery にクエリした結果、の3つがサポートされています) を用いる場合、ExampleGen コンポーネントは典型的な場合、非常に簡単にデプロイ可能で、ほとんど改修を必要とせずに利用できます。
典型的なコードは次のようになります:

```python
from tfx.utils.dsl_utils import csv_input
from tfx.components.example_gen.csv_example_gen.component import CsvExampleGen

examples = csv_input(os.path.join(base_dir, 'data/simple'))
example_gen = CsvExampleGen(input_base=examples)
```

次のように、外部の TF Example 形式のファイルを直接読み込むこともできます:

```python
from tfx.utils.dsl_utils import tfrecord_input
from tfx.components.example_gen.import_example_gen.component import ImportExampleGen

examples = tfrecord_input(path_to_tfrecord_dir)
example_gen = ImportExampleGen(input_base=examples)
```

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
example_gen = CsvExampleGen(input_base=examples, output_config=output)
```

この例の中でどのように `hash_backets` が設定されているかに注意してください。

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
example_gen = CsvExampleGen(input_base=examples, input_config=input)
```

ファイルベースの ExampleGen コンポーネント (例えば、 CsvExampleGen や ImportExampleGen) では、`pattern` は入力ファイルをまとめたディレクトリからの相対パスを glob 形式で記述したものになります。
クエリベースの ExampleGen コンポーネント (例えば、BigQUeryExampleGen や PrestoExampleGen) では、`pattern` はSQLクエリになります。

デフォルトでは入力データをまとめたディレクトリには単一のファイルがあるものとして扱われます。また、学習/評価用のデータの分割は2:1の割合になるように行われます。

詳細については [proto/example_gen.proto](https://github.com/tensorflow/tfx/blob/master/tfx/proto/example_gen.proto) を参照してください。

## Custom ExampleGen

Note: this feature is only available after TFX 0.14.

If the currently available ExampleGen components don't fit your needs, create
a custom ExampleGen, which will include a new executor extended from BaseExampleGenExecutor.

### File-Based ExampleGen

First, extend BaseExampleGenExecutor with a custom Beam PTransform, which
provides the conversion from your train/eval input split to TF examples. For
example, the
[CsvExampleGen executor](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/csv_example_gen/executor.py)
provides the conversion from an input CSV split to TF examples.

Then, create a component with above executor, as done in [CsvExampleGen component](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/csv_example_gen/component.py).
Alternatively, pass a custom executor into the standard
ExampleGen component as shown below.

```python
from tfx.components.example_gen.component import FileBasedExampleGen
from tfx.components.example_gen.csv_example_gen import executor
from tfx.utils.dsl_utils import external_input

examples = external_input(os.path.join(base_dir, 'data/simple'))
example_gen = FileBasedExampleGen(input_base=examples,
                                  executor_class=executor.Executor)
```

Now, we also support reading Avro and Parquet files using this
[method](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/custom_executors/avro_component_test.py).

### Query-Based ExampleGen

First, extend BaseExampleGenExecutor with a custom Beam PTransform, which reads
from the external data source. Then, create a simple component by
extending QueryBasedExampleGen.

This may or may not require additional connection configurations. For example,
the
[BigQuery executor](https://github.com/tensorflow/tfx/blob/master/tfx/components/example_gen/big_query_example_gen/executor.py)
reads using a default beam.io connector, which abstracts the connection
configuration details. The
[Presto executor](https://github.com/tensorflow/tfx/blob/master/tfx/examples/custom_components/presto_example_gen/presto_component/executor.py),
requires a custom Beam PTransform and a
[custom connection configuration protobuf](https://github.com/tensorflow/tfx/blob/master/tfx/examples/custom_components/presto_example_gen/proto/presto_config.proto)
as input.

If a connection configuration is required for a custom ExampleGen component, create
a new protobuf and pass it in through custom_config, which is now an optional
execution parameter. Below is an example of how to use a configured component.

```python
from tfx.examples.custom_components.presto_example_gen.proto import presto_config_pb2
from tfx.examples.custom_components.presto_example_gen.presto_component.component import PrestoExampleGen

presto_config = presto_config_pb2.PrestoConnConfig(host='localhost', port=8080)
example_gen = PrestoExampleGen(presto_config, query='SELECT * FROM chicago_taxi_trips')
```
