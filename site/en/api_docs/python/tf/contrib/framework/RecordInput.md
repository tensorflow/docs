page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.RecordInput

## Class `RecordInput`





Defined in [`tensorflow/python/ops/data_flow_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/data_flow_ops.py).

RecordInput asynchronously reads and randomly yields TFRecords.

A RecordInput Op will continuously read a batch of records asynchronously
into a buffer of some fixed capacity. It can also asynchronously yield
random records from this buffer.

It will not start yielding until at least `buffer_size / 2` elements have been
placed into the buffer so that sufficient randomization can take place.

The order the files are read will be shifted each epoch by `shift_amount` so
that the data is presented in a different order every epoch.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    file_pattern,
    batch_size=1,
    buffer_size=1,
    parallelism=1,
    shift_ratio=0,
    seed=0,
    name=None,
    batches=None,
    compression_type=None
)
```

Constructs a RecordInput Op.

#### Args:

* <b>`file_pattern`</b>: File path to the dataset, possibly containing wildcards.
    All matching files will be iterated over each epoch.
* <b>`batch_size`</b>: How many records to return at a time.
* <b>`buffer_size`</b>: The maximum number of records the buffer will contain.
* <b>`parallelism`</b>: How many reader threads to use for reading from files.
* <b>`shift_ratio`</b>: What percentage of the total number files to move the start
    file forward by each epoch.
* <b>`seed`</b>: Specify the random number seed used by generator that randomizes
    records.
* <b>`name`</b>: Optional name for the operation.
* <b>`batches`</b>: None by default, creating a single batch op. Otherwise specifies
    how many batches to create, which are returned as a list when
    `get_yield_op()` is called. An example use case is to split processing
    between devices on one computer.
* <b>`compression_type`</b>: The type of compression for the file. Currently ZLIB and
    GZIP are supported. Defaults to none.


#### Raises:

* <b>`ValueError`</b>: If one of the arguments is invalid.



## Methods

<h3 id="get_yield_op"><code>get_yield_op</code></h3>

``` python
get_yield_op()
```

Adds a node that yields a group of records every time it is executed.
If RecordInput `batches` parameter is not None, it yields a list of
record batches with the specified `batch_size`.



