description: Replicates a model on different GPUs. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.multi_gpu_model" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.multi_gpu_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/utils/multi_gpu_utils.py#L39-L266">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Replicates a model on different GPUs. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.multi_gpu_model`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.multi_gpu_model(
    model, gpus, cpu_merge=(True), cpu_relocation=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2020-04-01.
Instructions for updating:
Use <a href="../../../tf/distribute/MirroredStrategy.md"><code>tf.distribute.MirroredStrategy</code></a> instead.

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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`
</td>
<td>
A Keras model instance. To avoid OOM errors,
this model could have been built on CPU, for instance
(see usage example below).
</td>
</tr><tr>
<td>
`gpus`
</td>
<td>
Integer >= 2, number of on GPUs on which to create
model replicas.
</td>
</tr><tr>
<td>
`cpu_merge`
</td>
<td>
A boolean value to identify whether to force
merging model weights under the scope of the CPU or not.
</td>
</tr><tr>
<td>
`cpu_relocation`
</td>
<td>
A boolean value to identify whether to
create the model's weights under the scope of the CPU.
If the model is not defined under any preceding device
scope, you can still rescue it by activating this option.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Keras `Model` instance which can be used just like the initial
`model` argument, but which distributes its workload on multiple GPUs.
</td>
</tr>

</table>


Example 1: Training models with weights merge on CPU

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

Example 2: Training models with weights merge on CPU using cpu_relocation

```python
     ..
     # Not needed to change the device scope for model definition:
     model = Xception(weights=None, ..)

     try:
         model = multi_gpu_model(model, cpu_relocation=True)
         print("Training using multiple GPUs..")
     except:
         print("Training using single GPU or CPU..")

     model.compile(..)
     ..
```

Example 3: Training models with weights merge on GPU (recommended for NV-link)

```python
     ..
     # Not needed to change the device scope for model definition:
     model = Xception(weights=None, ..)

     try:
         model = multi_gpu_model(model, cpu_merge=False)
         print("Training using multiple GPUs..")
     except:
         print("Training using single GPU or CPU..")
     model.compile(..)
     ..
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if the `gpus` argument does not match available devices.
</td>
</tr>
</table>

