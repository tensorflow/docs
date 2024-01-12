
# Common issues

If your issue is not listed here, please search the
[github issues](https://github.com/tensorflow/hub/issues) before filling a new
one.

**Note:** This documentation uses TFhub.dev URL handles in examples. See more
information regarding other valid handle types [here](tf2_saved_model.md#model_handles).

## TypeError: 'AutoTrackable' object is not callable

```python
# BAD: Raises error
embed = hub.load('https://tfhub.dev/google/nnlm-en-dim128/1')
embed(['my text', 'batch'])
```

This error frequently arises when loading models in TF1 Hub format with the
`hub.load()` API in TF2. Adding the correct signature should fix this problem.
See the [TF-Hub migration guide for TF2](migration_tf2.md) for more details on
moving to TF2 and the use of models in TF1 Hub format in TF2.

```python

embed = hub.load('https://tfhub.dev/google/nnlm-en-dim128/1')
embed.signatures['default'](['my text', 'batch'])
```

## Cannot download a module

In the process of using a module from an URL there are many errors that can show
up due to the network stack. Often this is a problem specific to the machine
running the code and not an issue with the library. Here is a list of the common
ones:

*   **"EOF occurred in violation of protocol"** - This issue is likely to be
    generated if the installed python version does not support the TLS
    requirements of the server hosting the module. Notably, python 2.7.5 is
    known to fail resolving modules from tfhub.dev domain. **FIX**: Please
    update to a newer python version.

*   **"cannot verify tfhub.dev's certificate"** - This issue is likely to be
    generated if something on the network is trying to act as the dev gTLD.
    Before .dev was used as a gTLD, developers and frameworks would sometimes
    use .dev names to help testing code. **FIX:** Identify and reconfigure the
    software that intercepts name resolution in the ".dev" domain.

*   Failures to write to the cache directory `/tmp/tfhub_modules` (or similar):
    see [Caching](caching.md) for what that is and how to change its location.

If the above errors and fixes do not work, one can try to manually download a
module by simulating the protocol of attaching `?tf-hub-format=compressed` to
the URL to download a tar compressed file that has to be manually decompressed
into a local file. The path to the local file can then be used instead of the
URL. Here is a quick example:

```bash
# Create a folder for the TF hub module.
$ mkdir /tmp/moduleA
# Download the module, and uncompress it to the destination folder. You might want to do this manually.
$ curl -L "https://tfhub.dev/google/universal-sentence-encoder/2?tf-hub-format=compressed" | tar -zxvC /tmp/moduleA
# Test to make sure it works.
$ python
> import tensorflow_hub as hub
> hub.Module("/tmp/moduleA")
```

## Running inference on a pre-initialized module

If you are writing a Python program that applies a module many times on input
data, you can apply the following recipes. (Note: For serving requests in
production services, consider
[TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving) or other
scalable, Python-free solutions.)

Assuming your use-case model is **initialization** and subsequent **requests**
(for example Django, Flask, custom HTTP server, etc.), you can set-up the
serving as follows:

### TF2 SavedModels

*   In the initialization part:
    *   Load the TF2.0 model.

```python
import tensorflow_hub as hub

embedding_fn = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
```

*   In the request part:
    *   Use the embedding function to run inference.

```python
embedding_fn(["Hello world"])
```

This call of a tf.function is optimized for performance, see
[tf.function guide](https://www.tensorflow.org/guide/function).

### TF1 Hub modules

*   In the initialization part:
    *   Build the graph with a **placeholder** - entry point into the graph.
    *   Initialize the session.

```python
import tensorflow as tf
import tensorflow_hub as hub

# Create graph and finalize (finalizing optional but recommended).
g = tf.Graph()
with g.as_default():
  # We will be feeding 1D tensors of text into the graph.
  text_input = tf.placeholder(dtype=tf.string, shape=[None])
  embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
  embedded_text = embed(text_input)
  init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
g.finalize()

# Create session and initialize.
session = tf.Session(graph=g)
session.run(init_op)
```

*   In the request part:
    *   Use the session to feed data into the graph through the placeholder.

```python
result = session.run(embedded_text, feed_dict={text_input: ["Hello world"]})
```

## Cannot change a model's dtype (e.g., float32 to bfloat16)

TensorFlow's SavedModels (shared on TF Hub or otherwise) contain operations that
work on fixed data types (often, float32 for the weights and intermediate
activations of neural networks). These cannot be changed after the fact when
loading the SavedModel (but model publishers can choose to publish different
models with different data types).

## Update a model version

The documentation metadata of model versions can be updated. However, the
version's assets (model files) are immutable. If you want to change the model
assets, you can publish a newer version of the model. It's a good practice to
extend the documentation with a change log that describes what changed between
versions.
