# The ExampleGen TFX Pipeline Component

The ExampleGen TFX Pipeline component ingests data into TFX pipelines. It
consumes external files/services to generate Examples which will be read by
other TFX components. It also provides consistent and configurable partition,
and shuffles the dataset for ML best practice.

*   Consumes: Data from external data sources such as CSV, `TFRecord` and BigQuery
*   Emits: `tf.Example` records

## ExampleGen and Other Components

ExampleGen provides data to components that make use of the
[TensorFlow Data Validation](tfdv.md) library, such as
[SchemaGen](schemagen.md), [StatisticsGen](statsgen.md), and
[Example Validator](exampleval.md). It also provides data to
[Transform](transform.md), which makes use of the [TensorFlow Transform](tft.md)
library, and ultimately to deployment targets during inference.

## How to use an ExampleGen Component

For supported data sources (currently, CSV files, TFRecord files with TF Example
data format, and results of BigQuery queries) the ExampleGen pipeline component
is typically very easy to deploy and requires little customization. Typical code
looks like this:

```python
from tfx.utils.dsl_utils import csv_input
from tfx.components.example_gen.csv_example_gen.component import CsvExampleGen

examples = csv_input(os.path.join(base_dir, 'data/simple'))
example_gen = CsvExampleGen(input_base=examples)
```

or like below for importing external tf Examples directly:

```python
from tfx.utils.dsl_utils import tfrecord_input
from tfx.components.example_gen.import_example_gen.component import ImportExampleGen

examples = tfrecord_input(path_to_tfrecord_dir)
example_gen = ImportExampleGen(input_base=examples)
```

## Custom input/output split

Note: this feature is only available after TFX 0.14.

To customize the train/eval split ratio which ExampleGen will output, set the
`output_config` for ExampleGen component. For example:

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

Notice how the `hash_buckets` were set in this example.

For an input source which has already been split, set the `input_config` for
ExampleGen component:

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

For file based example gen (e.g. CsvExampleGen and ImportExampleGen), `pattern`
is a glob relative file pattern that maps to input files with root directory
given by input base path. For query-based example gen (e.g. BigQueryExampleGen,
PrestoExampleGen), `pattern` is a SQL query.

By default, the entire input base dir is treated as a single input split, and
the train and eval output split is generated with a 2:1 ratio.

Please refer to
[proto/example_gen.proto](https://github.com/tensorflow/tfx/blob/master/tfx/proto/example_gen.proto)
for details.

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
