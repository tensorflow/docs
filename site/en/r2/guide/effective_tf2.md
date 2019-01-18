# Effective TensorFlow 2.0

There are multiple changes in TensorFlow 2.0 to make TensorFlow users more
productive. TensorFlow 2.0 removes
[redundant APIs](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
makes APIs more consistent
([Unified RNNs](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[Unified Optimizers](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
and better integrates with the Python runtime with
[Eager execution](https://www.tensorflow.org/guide/eager).

Many
[RFCs](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
have explained the changes that have gone into making TensorFlow 2.0. This
guide presents a vision for what development in TensorFlow 2.0 should look like.
It's assumeed you have some familiarity with TensorFlow 1.x.

## A brief summary of major changes

### API Cleanup

Many APIs are either
[gone or moved](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)
in TF 2.0. Some of the major changes include removing `tf.app`, `tf.flags`, and
`tf.logging` in favor of the now open-source
[absl-py](https://github.com/abseil/abseil-py), rehoming projects that lived in
`tf.contrib`, and cleaning up the main `tf.*` namespace by moving lesser used
functions into subpackages like `tf.math`. Some APIs have been replaced with
their 2.0 equivalents - `tf.summary`, `tf.keras.metrics`, and
`tf.keras.optimizers`. The easiest way to automatically apply these renames
is to use the [v2 upgrade script](upgrade.md).

### Eager execution

TensorFlow 1.X requires users to manually stitch together an
[abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (the
graph) by making `tf.*` API calls. It then requires users to manually compile
the abstract syntax tree by passing a set of output tensors and input tensors to
a `session.run()` call. TensorFlow 2.0 executes eagerly (like Python normally
does) and in 2.0, graphs and sessions should feel like implementation details.

One notable byproduct of eager execution is that `tf.control_dependencies()` is
no longer required, as all lines of code execute in order (within a
`tf.function`, code with side effects execute in the order written).

### No more globals

TensorFlow 1.X relied heavily on implicitly global namespaces. When you called
`tf.Variable()`, it would be put into the default graph, and it would remain
there, even if you lost track of the Python variable pointing to it. You could
then recover that `tf.Variable`, but only if you knew the name that it had been
created with. This was difficult to do if you were not in control of the
variable's creation. As a result, all sorts of mechanisms proliferated to
attempt to help users find their variables again, and for frameworks to find
user-created variables: Variable scopes, global collections, helper methods like
`tf.get_global_step()`, `tf.global_variables_initializer()`, optimizers
implicitly computing gradients over all trainable variables, and so on.
TensorFlow 2.0 eliminates all of these mechanisms
([Variables 2.0 RFC](https://github.com/tensorflow/community/pull/11)) in favor
of the default mechanism: Keep track of your variables! If you lose track of a
`tf.Variable`, it gets garbage collected.

The requirement to track variables creates some extra work for the user, but
with Keras objects (see below), the burden is minimized.

### Functions, not sessions

A `session.run()` call is almost like a function call: You specify the inputs
and the function to be called, and you get back a set of outputs. In TensorFlow
2.0, you can decorate a Python function using `tf.function()` to mark it for JIT
compilation so that TensorFlow runs it as a single graph
([Functions 2.0 RFC](https://github.com/tensorflow/community/pull/20)). This
mechanism allows TensorFlow 2.0 to gain all of the benefits of graph mode:

-   Performance: The function can be optimized (node pruning, kernel fusion,
    etc.)
-   Portability: The function can be exported/reimported
    ([SavedModel 2.0 RFC](https://github.com/tensorflow/community/pull/34)),
    allowing users to reuse and share modular TensorFlow functions.

```python
# TensorFlow 1.X
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TensorFlow 2.0
outputs = f(input)
```

With the power to freely intersperse Python and TensorFlow code, we expect that
users will take full advantage of Python's expressiveness. But portable
TensorFlow executes in contexts without a Python interpreter - mobile, C++, and
JS. To help users avoid having to rewrite their code when adding `@tf.function`,
[AutoGraph](autograph.ipynb) will convert a subset of
Python constructs into their TensorFlow equivalents:

*   `print` -> `tf.print`
*   `assert` -> `tf.Assert`
*   `for`/`while` -> `tf.while_loop` (`break` and `continue` are supported)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

AutoGraph supports arbitrary nestings of control flow, which makes it possible
to performantly and concisely implement many complex ML programs such as
sequence models, reinforcement learning, custom training loops, and more.

## Recommendations for idiomatic TensorFlow 2.0

For complete examples, see
[MNIST (basic example)](../tutorials/beginner/tf2_overview.ipynb)

### Refactor your code into smaller functions

A common usage pattern in TensorFlow 1.X was the "kitchen sink" strategy, where
the union of all possible computations was preemptively laid out, and then
selected tensors were evaluated via `session.run()`. In TensorFlow 2.0, users
should refactor their code into smaller functions which are called as needed. In
general, it's not necessary to decorate each of these smaller functions with
`tf.function`; only use `tf.function` to decorate high-level computations - for
example, one step of training, or the forward pass of your model.

### Use Keras layers and models to manage variables

Keras models and layers offer the convenient `variables` and
`trainable_variables` properties, which recursively gather up all dependent
variables. This makes it very easy to manage variables locally to where they are
being used.

Contrast:

```python
def dense(x, W, b):
  return tf.nn.sigmoid(tf.matmul(x, W) + b)

@tf.function
def multilayer_perceptron(x, w0, b0, w1, b1, w2, b2 ...):
  x = dense(x, w0, b0)
  x = dense(x, w1, b1)
  x = dense(x, w2, b2)
  ...

# You still have to manage w_i and b_i, and their shapes are defined far away from the code.
```

with the Keras version:

```python
# Each layer can be called, with a signature equivalent to linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].trainable_variables => returns [w3, b3]
# perceptron.trainable_variables => returns [w0, b0, ...]
```

Keras layers/models inherit from `tf.train.Checkpointable` and are integrated
with `@tf.function`, which makes it possible to directly checkpoint or export
SavedModels from Keras objects. You do not necessarily have to use Keras's
`.fit()` API to take advantage of these integrations.

Here's a transfer learning example that demonstrates how Keras makes it easy to
collect a subset of relevant variables. Let's say you're training a multi-headed
model with a shared trunk:

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# Train on primary dataset
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # Simultaneously optimize trunk and head1 weights.
  gradients = tape.gradients(loss, path1.trainable_variables)
  optimizer.apply_gradients(gradients, path1.trainable_variables)

# Fine-tune second head, reusing the trunk
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # Only optimize head2 weights, not trunk weights
  gradients = tape.gradients(loss, head2.trainable_variables)
  optimizer.apply_gradients(gradients, head2.trainable_variables)

# You can publish just the trunk computation for other people to reuse.
tf.saved_model.save(trunk, output_path)
```

### Combine tf.data.Datasets and @tf.function

When iterating over training data that fits in memory, feel free to use regular
Python iteration. Otherwise, `tf.data.Dataset` is the best way to stream
training data from disk. Datasets are
[iterables (not iterators)](https://docs.python.org/3/glossary.html#term-iterable),
and work just like other Python iterables in Eager mode. You can fully utilize
dataset async prefetching/streaming features by wrapping your code in
`tf.function()`, which replaces Python iteration with the equivalent graph
operations using AutoGraph.

```python
@tf.function
def train(model, dataset, optimizer):
  for x, y in dataset:
    with tf.GradientTape() as tape:
      prediction = model(x)
      loss = loss_fn(prediction, y)
    gradients = tape.gradients(loss, model.trainable_variables)
    optimizer.apply_gradients(gradients, model.trainable_variables)
```

If you use the Keras `.fit()` API, you won't have to worry about dataset
iteration.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### Take advantage of AutoGraph with Python control flow

AutoGraph provides a way to convert data-dependent control flow into graph-mode
equivalents like `tf.cond` and `tf.while_loop`.

One common place where data-dependent control flow appears is in sequence
models. `tf.keras.layers.RNN` wraps an RNN cell, allowing you to either
statically or dynamically unroll the recurrence. For demonstration's sake, you
could reimplement dynamic unroll as follows:

```python
class DynamicRNN(tf.keras.Model):

  def __init__(self, rnn_cell):
    super(DynamicRNN, self).__init__(self)
    self.cell = rnn_cell

  def call(self, input_data):
    # [batch, time, features] -> [time, batch, features]
    input_data = tf.transpose(input_data, [1, 0, 2])
    outputs = tf.TensorArray(tf.float32, input_data.shape[0])
    state = self.cell.zero_state(input_data.shape[1], dtype=tf.float32)
    for i in tf.range(input_data.shape[0]):
      output, state = self.cell(input_data[i], state)
      outputs = outputs.write(i, output)
    return tf.transpose(outputs.stack(), [1, 0, 2]), state
```

For a more detailed overview of AutoGraph's features, see
[the guide](./autograph.ipynb).

### Use tf.metrics to aggregate data and tf.summary to log it

A complete set of `tf.summary` symbols are coming soon. You can access the
2.0 version of `tf.summary` with:

```python
from tensorflow.python.ops import summary_ops_v2
```

To log summaries, use `tf.summary.(scalar|histogram|...)`. In isolation, this
doesn't actually do anything; the summaries need to be redirected to an
appropriate file writer by using a context manager. (This allows you to avoid
hardcoding summary output to a particular file writer.)

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  summary_ops_v2.scalar('loss', 0.1, step=42)
```

To aggregate data before logging them as summaries, use `tf.metrics`. Metrics
are stateful; they accumulate values and return a cumulative result when you
call `.result()`. Clear accumulated values with `.reset_states()`.

```python
def train(model, optimizer, dataset, log_freq=10):
  avg_loss = tf.keras.metrics.Mean(name='loss', dtype=tf.float32)
  for images, labels in dataset:
    loss = train_step(model, optimizer, images, labels)
    avg_loss.update_state(loss)
    if tf.equal(optimizer.iterations % log_freq, 0):
      summary_ops_v2.scalar('loss', avg_loss.result(), step=optimizer.iterations)
      avg_loss.reset_states()

def test(model, test_x, test_y, step_num):
  loss = loss_fn(model(test_x), test_y)
  summary_ops_v2.scalar('loss', step=step_num)

train_summary_writer = tf.summary.create_file_writer('/tmp/summaries/train')
test_summary_writer = tf.summary.create_file_writer('/tmp/summaries/test')

with train_summary_writer.as_default():
  train(model, optimizer, dataset)

with test_summary_writer.as_default():
  test(model, test_x, test_y, optimizer.iterations)
```

By then pointing TensorBoard at the summary directory (`tensorboard --logdir
/tmp/summaries`), you can then visualize the generated summaries.
