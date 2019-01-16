# Как использовать TensorFlow 2.0?

В TensorFlow 2.0 были сделаны несколько изменений, которые позволят более продуктивно работать всем 
пользователям TensorFlow. В TensorFlow 2.0 были удалены
[ненужные APIs](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
существующие и используемые API были проработаны 
([объединены RNN](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[а также оптимизаторы](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
улучшена интеграция с рабочей средой Python в режиме
[Eager execution](https://www.tensorflow.org/guide/eager).

Во многих
[запросах RFC](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
объяснялись основные изменения, которые затронут TensorFlow 2.0. В этом документе
будет показан, как должен выглядеть процесс работы с новым TensorFlow 2.0.
Подразумевается, что ты уже знаком с TensorFlow 1.x.

## Краткий список основных изменений

### Чистка API

Многие API были либо
[удалены, либо перемещены](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)
в TF 2.0. Самыми крупными изменениями являются удаление `tf.app`, `tf.flags`, а также
`tf.logging` в пользу новой библиотеки с открытым исходным кодом
[absl-py](https://github.com/abseil/abseil-py), перемещение проектов, которые были в
`tf.contrib`, а также чистка основного имени `tf.*`: редко используемые функции 
были объединены в отдельные модули, например `tf.math`. Некоторые API были заменены
их 2.0 эквивалентами - `tf.summary`, `tf.keras.metrics`, и
`tf.keras.optimizers`. Самый простой способ автоматически переименовать все функции -
это воспользоваться [скриптом для обновления до 2.0](upgrade.md).

### Активный Eager execution

В TensorFlow 1.X от пользователя требовалось вручную строить
[абстрактное синтаксическое дерево](https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%BE%D0%B5_%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE) (граф) при помощи API вызовов `tf.*`. Для этого было нужно вручную
компилировать дерево, передавая набор получаемых и входящих тензоров к вызову 
`session.run()`. TensorFlow 2.0 теперь выполняет все операции мгновенно (точно
так же, как и обычный Python), все графы и сессии теперь будут работать как
стандартное выполнение операций.

Раньше побочным продуктом eager execution метод `tf.control_dependencies()`,
который теперь не треубется, и все строки кода будут исполняться в последовательном
порядке, определенном `tf.function`. Сторонний код будет выполняться в 
определенном ему порядке.

### Никаких глобальных переменных

TensorFlow 1.X внутренне полагался на глобальные переменные. Когда ты вызывал
`tf.Variable()`, то эта переменная помещалась в стандартный граф и оставалась там
даже если уже было изменено имя, присвоенное этой переменной. Ты мог восстановить
эту переменную `tf.Variable`, но только если тебе было известно имя, которое было
присвоено ей при создании. В результате все механизмы были направлены на то, чтобы
помочь пользователю отыскать имя их переменных еще раз: `tf.get_global_step()`, 
`tf.global_variables_initializer()`, оптимизаторы, которые рассчитывали
градиенты по всем обучаемым перменным и так далее. В TensorFlow 2.0 были устранены
все эти механизмы ([Переменные 2.0 RFC](https://github.com/tensorflow/community/pull/11))
в пользу нового: следи за состоянием рабочих переменных! Если ты потеряешь `tf.Variable`
(например, ей будет присвоено новое имя), то старая будет удалена из памяти в порядке
процесса garbage collection.

Требование следить за переменными создает дополнительную нагрузку на пользователя,
но в случае с объектами Keras (см. ниже), это нагрузка - минимальная.

### Функции, а не сессии

Вызов `session.run()` работал почти как вызов функции: ты определял вводные данные
и вызывал функцию, получая на выходе результаты. В TensorFlow 2.0, ты можешь
декорировать функцию Python при помощи `tf.function()`, отметив ее как JIT
компиляцию, чтобы TensorFlow запустил ее на одном единственном графе
([Функции 2.0 RFC](https://github.com/tensorflow/community/pull/20)). Этот
механизм позволяет TensorFlow 2.0 получить все преимущества режима graph:

-   Производительность: функции могут быть оптимизированы (отсечение узлов графа,
    слияние ядра и так далее)
-   Портативность: The function can be exported/reimported функции могут быть экспортированы
    или импортированы повторно ([Сохранение моделей 2.0 RFC](https://github.com/tensorflow/community/pull/34)),
    позволяя пользователям использовать и делиться модульными функциями TensorFlow.

```python
# TensorFlow 1.X
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TensorFlow 2.0
outputs = f(input)
```

С новой возможностью просто использовать вместе код Python и TensorFlow, мы ожидаем
что пользователи воспользуются всеми преимуществами выразительности языка Python.
Но портативный TensorFlow выполняет операции в окружении без интерпретатора Python -
на мобильных устройствах, C++ и JavaScript. Чтобы помочь пользователям легко переписать
свой код при использовании новой `@tf.function`, используй [AutoGraph](autograph.ipynb)
для конвертации кода Python в их эквиваленты TensorFlow:

*   `print` -> `tf.print`
*   `assert` -> `tf.Assert`
*   `for`/`while` -> `tf.while_loop` (поддерживаются `break` и `continue`)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

AutoGraph поддерживает вложенные функции в порядке выполнения программы, что
делает возможным производительно и точно внедрять комплексные программы
машинного обучения, например такие как последовательные модели, обучение с
подкреплением, собственные циклы обучения и многие другие.

## Рекомендации и идиомы TensorFlow 2.0

Смотри все примеры использования
[MNIST (стандартный пример)](../tutorials/beginner/tf2_overview.ipynb)

### Рефакторинг кода на малые функции

A common usage pattern in TensorFlow 1.X was the "kitchen sink" strategy, where
the union of all possible computations was preemptively laid out, and then
selected tensors were evaluated via `session.run()`. In TensorFlow 2.0, users
should refactor their code into smaller functions which are called as needed. In
general, it's not necessary to decorate each of these smaller functions with
`tf.function`; only use `tf.function` to decorate high-level computations - for
example, one step of training, or the forward pass of your model.

### Используй слои и модели Keras для управления переменными

Keras models and layers offer the convenient `.variables` property, which
recursively gather up all dependent variables. This makes it very easy to manage
variables locally to where they are being used.

Сравни:

```python
def dense(x, W, b):
  return tf.nn.sigmoid(tf.matmul(x, W) + b)

@tf.function
def multilayer_perceptron(x, w0, b0, w1, b1, w2, b2 ...):
  x = dense(x, w0, b0)
  x = dense(x, w1, b1)
  x = dense(x, w2, b2)
  ...

# Тебе все равно придется управлять w_i и b_i, так как их формы определяются не в коде.
```

Версия с использованием Keras:

```python
# Each layer can be called, with a signature equivalent to linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].variables => returns [w3, b3]
# perceptron.variables => returns [w0, b0, ...]
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
  gradients = tape.gradients(loss, path1.variables)
  optimizer.apply_gradients(gradients, path1.variables)

# Fine-tune second head, reusing the trunk
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # Only optimize head2 weights, not trunk weights
  gradients = tape.gradients(loss, head2.variables)
  optimizer.apply_gradients(gradients, head2.variables)

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
    gradients = tape.gradients(loss, model.variables)
    optimizer.apply_gradients(gradients, model.variables)
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
