# Эффективный TensorFlow 2.0

В TensorFlow 2.0 сделан ряд изменений делающих пользователей TensorFlow более
продуктивными. TensorFlow 2.0 удалил
[избыточные API](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
после чего API стали более согласованными
([Unified RNNs](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[Unified Optimizers](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
и лучше интегрировался с Python runtime, с
[Eager execution](https://www.tensorflow.org/guide/eager).

Многие
[RFCs](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
объяснили изменения которые вошли в TensorFlow 2.0. Это руководство
представляет взгляд на кто как должна выглядеть разработка в TensorFlow 2.0.
Предполагается, что вы знакомы с TensorFlow 1.x.

## Короткая выдержка основных изменений

### Очистка API

Много API либо
[удалены либо перемещены](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md)
в TF 2.0. Некоторые из основных изменений включают удаление `tf.app`,
`tf.flags`, и `tf.logging` в пользу
[absl-py](https://github.com/abseil/abseil-py) который сейчас с открытым
исходным кодом, перенос проектов которые находились в `tf.contrib`, и очистки
основного пространства имен `tf.*` путем перемещения редко используемых функций
в подпакеты наподобие `tf.math`. Неокторые API были замещены своими
эквивалентами 2.0 - `tf.summary`, `tf.keras.metrics`, и `tf.keras.optimizers`.
Наиболее простым способом автоматически применить эти переименования является
использование [скрипта обновления v2](upgrade.md).

### Eager execution

В TensorFlow 1.X от пользователей требовалось вручную собирать
[абстрактное синтаксическое дерево](https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%81%D1%82%D1%80%D0%B0%D0%BA%D1%82%D0%BD%D0%BE%D0%B5_%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE)
(граф) выполняя `tf.*` API запросы. Затем пользователи должны вручную
скомпилировать абстрактное синтаксическое дерево путем передачи множества
выходных и входных тензоров в вызов `session.run()`. TensorFlow 2.0 выполняется
сразу же (как это обычно делает Python) и в 2.0, графы и сессии должны
рассматриваться как детали реализации.

Одним заметным побочным продуктом eager execution является то, что
`tf.control_dependencies()` более не требуется, так как все строки кода
выполняются по очереди (в пределах `tf.function`, код с побочными эффектами
выполняется в том порядке в котором он написан).

### Нет больше глобалов

TensorFlow 1.X значительно зависел от неявных глобальных пространств имен. Когда
вы вызывали `tf.Variable()`, она помещалась в граф по умолчанию, и она
оставалась там даже если вы потеряли track переменной Python указывавшей на
него. Вы можете затем восстановить ту `tf.Variable`, но только если вы знали имя
с которым она была создана. Это было сложно сделать если вы не контролировали
создание переменных. В результате этого, размножались все виды механизмов
пытавшиеся помочь пользователям снова найти их переменные, а для фреймворков -
найти созданные пользователями переменные: Области переменных, глобальные
коллекции, методы помощники такие как `tf.get_global_step()`,
`tf.global_variables_initializer()`, оптимизаторы неявно вычисляющие градиенты
по всем обучаемым переменным, и т.д. TensorFlow 2.0 устраняет все эти механизмы
([Variables 2.0 RFC](https://github.com/tensorflow/community/pull/11)) в пользу
механизма по умолчанию: Отслеживайте свои переменные! Если вы потеряли след
`tf.Variable`, он будет очищен сборщиком мусора.

Требование отслеживать мусор создает дополнительную работу для пользователя,
но с объектами Keras (см. ниже), нагрузка минимизирована.

### Функции, не сессии

Вызов `session.run()` почти похож на вызов функции: Вы определяете вводные
данные, функция вызывается и вы получаете набор результатов. В TensorFlow 2.0,
вы можете декорировать функцию Python используя `tf.function()` чтобы отметить
ее для JIT компиляции так что TensorFlow выполняет его как единый граф
([Functions 2.0 RFC](https://github.com/tensorflow/community/pull/20)). Этот
механизм позволяет TensorFlow 2.0 получить все преимущества режима графа:

-   Производительность: функция может быть оптимизирована (node pruning, kernel
    fusion, etc.)
-   Портативность: функция может быть экспортирована / реимпортирована
    ([RFC SavedModel 2.0](https://github.com/tensorflow/community/pull/34), что
    позволяет пользователям повторно использовать и делиться модульными
    функциями TensorFlow.

```python
# TensorFlow 1.X
outputs = session.run(f(placeholder), feed_dict={placeholder: input})
# TensorFlow 2.0
outputs = f(input)
```

Благодаря возможности свободно перемежать код Python и TensorFlow пользователи
могут воспользоваться преимуществами выразительности Python. Но переносимый
TensorFlow выполняется в контекстах, таких как mobile, C ++ и JavaScript без
интерпретатора Python. Чтобы пользователям не нужно было переписывать свой код
при добавлении `@ tf.function`, [AutoGraph](function.ipynb) преобразует
подмножество Python конструируя его в эквивалентах TensorFlow:

*   `for`/`while` -> `tf.while_loop` (`break` and `continue` are supported)
*   `if` -> `tf.cond`
*   `for _ in dataset` -> `dataset.reduce`

AutoGraph поддерживает произвольные вложения control flow, что делает возможным
эффективно и кратко реализовать многие сложные программы машинного обучения,
такие как реккурентные модели, обучение с подкреплением, пользовательские циклы
обучения и многое другое.

## Рекомендации характерные для TensorFlow 2.0

### Рефакторьте ваш код в меньшие функции

Обычный пользовательский паттерн в TensorFlow 1.X была стратегия "kitchen
sink"(кухонная мойка), где предварительно выкладывалось объединение всех
возможных вычислений, а потом выбранные тензоры оценивались с `session.run()`. В
TensorFlow 2.0, пользователям необходимо отрефакторить свой код в меньшие
функции которые вызываются по мере необходимости. В общем, не обязательно
декорировать каждую из этих функций с `tf.function`; используйте `tf.function`
только для декорирования высокоуровневых вычислений - например, один шаг
обучения или проход вперед в вашей модели.

### Используйте слои и модели Keras для управления переменными


Keras models and layers offer the convenient `variables` and
`trainable_variables` properties, which recursively gather up all dependent
variables. This makes it easy to manage variables locally to where they are
being used.

Модели и слои Keras предлагают удобные свойства `variables` и
`trainable_variables`, которые рекурсивно собирают все зависимые переменные. Это
облегчает локальное управление переменными в том месте, где они использовались.

Сравните:

```python
def dense(x, W, b):
  return tf.nn.sigmoid(tf.matmul(x, W) + b)

@tf.function
def multilayer_perceptron(x, w0, b0, w1, b1, w2, b2 ...):
  x = dense(x, w0, b0)
  x = dense(x, w1, b1)
  x = dense(x, w2, b2)
  ...

# Вам необходимо управлять w_i and b_i, а их размерности определены далеко от кода.
```

с версией Keras:

```python
# Каждый слой может быть вызван с сигнатурой эквивалентной linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].trainable_variables => returns [w3, b3]
# perceptron.trainable_variables => returns [w0, b0, ...]
```

Слои/модели Keras наследуются от `tf.train.Checkpointable` и интегрированы
с `@ tf.function`, что позволяет напрямую проверять или экспортировать
SavedModels из объектов Keras. Вам не обязательно использовать Keras
`.fit ()` API чтобы воспользоваться этими интеграциями.

Вот пример transfer learning, который демонстрирует, как Keras облегчает
сбор подмножества релевантных переменных. Допустим, вы обучаете multi-headed
model with a shared trunk:

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# Обучение на первичных данных
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # Одновременная оптимизация весов trunk и head1.
  gradients = tape.gradient(loss, path1.trainable_variables)
  optimizer.apply_gradients(zip(gradients, path1.trainable_variables))

# Тонкая настройка второй head, переиспользование trunk
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # Оптимизируются только веса head2, не веса trunk
  gradients = tape.gradient(loss, head2.trainable_variables)
  optimizer.apply_gradients(zip(gradients, head2.trainable_variables))

# Вы можете опубликовать только вычисления trunk чтобы другие люди могли ими воспользоваться.
tf.saved_model.save(trunk, output_path)
```

### Комбинируйте tf.data.Datasets и @tf.function

При итерации по тренировочным данным, которые помещаются в память, свободно
используйте регулярную итерацию Python. Иначе, `tf.data.Dataset` - лучший способ
для передачи тренировочных данных с диска. Данные являются
[iterables (не iterators)](https://docs.python.org/3/glossary.html#term-iterable),
и работают так же, как и другие Python iterables в режиме Eager. Вы можете
полностью использовать свойства dataset async prefetching/streaming упаковав
свой код в `tf.function ()`, которая заменяет итерацию Python эквивалентным
графом операции использующим AutoGraph.

```python
@tf.function
def train(model, dataset, optimizer):
  for x, y in dataset:
    with tf.GradientTape() as tape:
      prediction = model(x)
      loss = loss_fn(prediction, y)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

If you use the Keras `.fit()` API, you won't have to worry about dataset
iteration.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### Воспользуйтесь преимуществами AutoGraph с Python control flow

AutoGraph предоставляет способ преобразования зависящего от данных control flow
в эквивалентый режим графа, например `tf.cond` и `tf.while_loop`.

Одно обычное место, где появляется зависящий от данных control flow находится
sequence models. `tf.keras.layers.RNN` оборачивает ячейку RNN, позволяя вам
статически или динамически развернуть recurrence. Например, вы может
переопределить динамическую развертку следующим образом:

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

Для более подробного обзора свойств AutoGraph, смотри
[руководство](./function.ipynb).

### tf.metrics аггрегирует данные and tf.summary ведет их лог

Для лога summaries используйте `tf.summary. (Scalar | histogram | ...)` и
перенаправьте его на writer используя context manager. (Если вы опустите context
manager, ничего случится.) В отличие от TF 1.x, summaries отправляются
непосредственно writer; там нет отдельной операции "merge" и отдельного вызова
`add_summary()`, что означает, что значение `step` должно быть указано на месте
вызова.

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  tf.summary.scalar('loss', 0.1, step=42)
```

Чтобы объединить данные перед их записью в виде summaries, используйте
`tf.metrics`. Метрика являются stateful: они накапливают значения и возвращают
совокупный результат, когда вы вызовите `.result()`. Очистите накопленные
значения с помощью `.reset_states ()`.

```python
def train(model, optimizer, dataset, log_freq=10):
  avg_loss = tf.keras.metrics.Mean(name='loss', dtype=tf.float32)
  for images, labels in dataset:
    loss = train_step(model, optimizer, images, labels)
    avg_loss.update_state(loss)
    if tf.equal(optimizer.iterations % log_freq, 0):
      tf.summary.scalar('loss', avg_loss.result(), step=optimizer.iterations)
      avg_loss.reset_states()

def test(model, test_x, test_y, step_num):
  loss = loss_fn(model(test_x), test_y)
  tf.summary.scalar('loss', loss, step=step_num)

train_summary_writer = tf.summary.create_file_writer('/tmp/summaries/train')
test_summary_writer = tf.summary.create_file_writer('/tmp/summaries/test')

with train_summary_writer.as_default():
  train(model, optimizer, dataset)

with test_summary_writer.as_default():
  test(model, test_x, test_y, optimizer.iterations)
```

Визуализируйте сгенерированные результаты направив TensorBoard в директорий с
summary log:

```
tensorboard --logdir /tmp/summaries
```
