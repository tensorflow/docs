

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.utils.multi_gpu_model

``` python
tf.keras.utils.multi_gpu_model(
    model,
    gpus
)
```



Defined in [`tensorflow/python/keras/_impl/keras/utils/training_utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/utils/training_utils.py).

Replicates a model on different GPUs.

Specifically, this function implements single-machine
multi-GPU data parallelism. It works in the following way:

- Divide the model's input(s) into multiple sub-batches.
- Apply a model copy on each sub-batch. Every model copy
    is executed on a dedicated GPU.
- Concatenate the results (on CPU) into one big batch.

E.g. if your `batch_size` is 64 and you use `gpus=2`,
then we will divide the input into 2 sub-batches of 32 samples,
process each sub-batch on one GPU, then return the full
batch of 64 processed samples.

This induces quasi-linear speedup on up to 8 GPUs.

This function is only available with the TensorFlow backend
for the time being.

#### Arguments:

* <b>`model`</b>: A Keras model instance. To avoid OOM errors,
        this model could have been built on CPU, for instance
        (see usage example below).
* <b>`gpus`</b>: Integer >= 2, number of on GPUs on which to create
        model replicas.


#### Returns:

    A Keras `Model` instance which can be used just like the initial
    `model` argument, but which distributes its workload on multiple GPUs.

Example:

```python
    import tensorflow as tf
    from keras.applications import Xception
    from keras.utils import multi_gpu_model
    import numpy as np

    num_samples = 1000
    height = 224
    width = 224
    num_classes = 1000

    # Instantiate the base model (or "template" model).
    # We recommend doing this with under a CPU device scope,
    # so that the model's weights are hosted on CPU memory.
    # Otherwise they may end up hosted on a GPU, which would
    # complicate weight sharing.
    with tf.device('/cpu:0'):
        model = Xception(weights=None,
                         input_shape=(height, width, 3),
                         classes=num_classes)

    # Replicates the model on 8 GPUs.
    # This assumes that your machine has 8 available GPUs.
    parallel_model = multi_gpu_model(model, gpus=8)
    parallel_model.compile(loss='categorical_crossentropy',
                           optimizer='rmsprop')

    # Generate dummy data.
    x = np.random.random((num_samples, height, width, 3))
    y = np.random.random((num_samples, num_classes))

    # This `fit` call will be distributed on 8 GPUs.
    # Since the batch size is 256, each GPU will process 32 samples.
    parallel_model.fit(x, y, epochs=20, batch_size=256)

    # Save model via the template model (which shares the same weights):
    model.save('my_model.h5')
```


#### Raises:

* <b>`ValueError`</b>: if the `gpus` argument does not match available devices.