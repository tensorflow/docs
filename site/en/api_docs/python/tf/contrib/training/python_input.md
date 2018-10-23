

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.python_input

### `tf.contrib.training.python_input`

``` python
python_input(
    generator,
    features,
    name=None
)
```



Defined in [`tensorflow/contrib/training/python/training/python_input.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/training/python/training/python_input.py).

Easily feed data from a python generator into TensorFlow queues.

Example usage:

```python
def generator():
  for i in range(3):
    yield {"value": i}

features = {
  "value": tf.FixedLenFeature(shape=[], dtype=dtypes.int32)
}

tensor_dict = tf.contrib.training.python_input(generator, features)
batched_dict = tf.train.batch(
  tensor_dict, batch_size=2, allow_smaller_final_batch=True)

s = tf.Session()
tf.train.start_queue_runners()

batch1 = s.run(batched_dict)  # returns {"value": np.array([0, 1])}
batch2 = s.run(batched_dict)  # returns {"value": np.array([2])}
s.run(batched_dict)  # error: Queue is closed (generator finished at i==3)
```

#### Args:

* <b>`generator`</b>: A python generator that takes no arguments, and yields dicts
    containing a single minibatch entry one at a time.
* <b>`features`</b>: A python `dict` mapping keys expected from the generator to
    instances of `tf.FixedLenFeature`, or `tf.FixedLenSequenceFeature`.
* <b>`name`</b>: (Optional) A name for the operations.


#### Returns:

  A dict mapping keys of the `features` dict to `Tensor` objects.
  These `Tensor` objects are outputs of a queue that is fed by `generator`.


#### Raises:

* <b>`TypeError`</b>: If generator is not callable or features is not a dict.
* <b>`TypeError`</b>: If any of features' values are not a Feature object.
* <b>`NotImplementedError`</b>: If any of features' values are instances of
    `SparseFeature` or `VarLenFeature`  (these are not currently supported).
* <b>`ValueError`</b>: If any FixedLenSequenceFeatures contain a default value
    (this field is not supported).
* <b>`ValueError`</b>: if any FixedLenSequenceFeatures have allow_missing=False
    (this field is not supported).