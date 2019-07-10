page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cloud.BigQueryReader

## Class `BigQueryReader`

Inherits From: [`ReaderBase`](../../../tf/ReaderBase)



Defined in [`tensorflow/contrib/cloud/python/ops/bigquery_reader_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/cloud/python/ops/bigquery_reader_ops.py).

A Reader that outputs keys and tf.Example values from a BigQuery table.

Example use:

>     # Assume a BigQuery has the following schema,
>     #     name      STRING,
>     #     age       INT,
>     #     state     STRING
>     
>     # Create the parse_examples list of features.
>     features = dict(
>       name=tf.FixedLenFeature([1], tf.string),
>       age=tf.FixedLenFeature([1], tf.int32),
>       state=tf.FixedLenFeature([1], dtype=tf.string, default_value="UNK"))
>     
>     # Create a Reader.
>     reader = bigquery_reader_ops.BigQueryReader(project_id=PROJECT,
>                                                 dataset_id=DATASET,
>                                                 table_id=TABLE,
>                                                 timestamp_millis=TIME,
>                                                 num_partitions=NUM_PARTITIONS,
>                                                 features=features)
>     
>     # Populate a queue with the BigQuery Table partitions.
>     queue = tf.train.string_input_producer(reader.partitions())
>     
>     # Read and parse examples.
>     row_id, examples_serialized = reader.read(queue)
>     examples = tf.parse_example(examples_serialized, features=features)
>     
>     # Process the Tensors examples["name"], examples["age"], etc...

Note that to create a reader a snapshot timestamp is necessary. This
will enable the reader to look at a consistent snapshot of the table.
For more information, see 'Table Decorators' in BigQuery docs.

See ReaderBase for supported methods.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    project_id,
    dataset_id,
    table_id,
    timestamp_millis,
    num_partitions,
    features=None,
    columns=None,
    test_end_point=None,
    name=None
)
```

Creates a BigQueryReader.

#### Args:

* <b>`project_id`</b>: GCP project ID.
* <b>`dataset_id`</b>: BigQuery dataset ID.
* <b>`table_id`</b>: BigQuery table ID.
* <b>`timestamp_millis`</b>: timestamp to snapshot the table in milliseconds since
    the epoch. Relative (negative or zero) snapshot times are not allowed.
    For more details, see 'Table Decorators' in BigQuery docs.
* <b>`num_partitions`</b>: Number of non-overlapping partitions to read from.
* <b>`features`</b>: parse_example compatible dict from keys to `VarLenFeature` and
    `FixedLenFeature` objects.  Keys are read as columns from the db.
* <b>`columns`</b>: list of columns to read, can be set iff features is None.
* <b>`test_end_point`</b>: Used only for testing purposes (optional).
* <b>`name`</b>: a name for the operation (optional).


#### Raises:

* <b>`TypeError`</b>: - If features is neither None nor a dict or
             - If columns is neither None nor a list or
             - If both features and columns are None or set.



## Properties

<h3 id="reader_ref"><code>reader_ref</code></h3>

Op that implements the reader.

<h3 id="supports_serialize"><code>supports_serialize</code></h3>

Whether the Reader implementation can serialize its state.



## Methods

<h3 id="num_records_produced"><code>num_records_produced</code></h3>

``` python
num_records_produced(name=None)
```

Returns the number of records this reader has produced.

This is the same as the number of Read executions that have
succeeded.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

An int64 Tensor.

<h3 id="num_work_units_completed"><code>num_work_units_completed</code></h3>

``` python
num_work_units_completed(name=None)
```

Returns the number of work units this reader has finished processing.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

An int64 Tensor.

<h3 id="partitions"><code>partitions</code></h3>

``` python
partitions(name=None)
```

Returns serialized BigQueryTablePartition messages.

These messages represent a non-overlapping division of a table for a
bulk read.

#### Args:

* <b>`name`</b>: a name for the operation (optional).


#### Returns:

`1-D` string `Tensor` of serialized `BigQueryTablePartition` messages.

<h3 id="read"><code>read</code></h3>

``` python
read(
    queue,
    name=None
)
```

Returns the next record (key, value) pair produced by a reader.

Will dequeue a work unit from queue if necessary (e.g. when the
Reader needs to start reading from a new file since it has
finished with the previous file).

#### Args:

* <b>`queue`</b>: A Queue or a mutable string Tensor representing a handle
    to a Queue, with string work items.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of Tensors (key, value).
* <b>`key`</b>: A string scalar Tensor.
* <b>`value`</b>: A string scalar Tensor.

<h3 id="read_up_to"><code>read_up_to</code></h3>

``` python
read_up_to(
    queue,
    num_records,
    name=None
)
```

Returns up to num_records (key, value) pairs produced by a reader.

Will dequeue a work unit from queue if necessary (e.g., when the
Reader needs to start reading from a new file since it has
finished with the previous file).
It may return less than num_records even before the last batch.

#### Args:

* <b>`queue`</b>: A Queue or a mutable string Tensor representing a handle
    to a Queue, with string work items.
* <b>`num_records`</b>: Number of records to read.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of Tensors (keys, values).
* <b>`keys`</b>: A 1-D string Tensor.
* <b>`values`</b>: A 1-D string Tensor.

<h3 id="reset"><code>reset</code></h3>

``` python
reset(name=None)
```

Restore a reader to its initial clean state.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.

<h3 id="restore_state"><code>restore_state</code></h3>

``` python
restore_state(
    state,
    name=None
)
```

Restore a reader to a previously saved state.

Not all Readers support being restored, so this can produce an
Unimplemented error.

#### Args:

* <b>`state`</b>: A string Tensor.
    Result of a SerializeState of a Reader with matching type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.

<h3 id="serialize_state"><code>serialize_state</code></h3>

``` python
serialize_state(name=None)
```

Produce a string tensor that encodes the state of a reader.

Not all Readers support being serialized, so this can produce an
Unimplemented error.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A string Tensor.



