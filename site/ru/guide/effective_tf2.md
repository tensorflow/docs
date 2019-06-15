# Как использовать TensorFlow 2.0?

Note: Вся информация в этом разделе переведена с помощью русскоговорящего
Tensorflow сообщества на общественных началах. Поскольку этот перевод не
является официальным, мы не гарантируем что он на 100% аккуратен и соответствует
[официальной документации на английском языке](https://www.tensorflow.org/?hl=en).
Если у вас есть предложение как исправить этот перевод, мы будем очень рады
увидеть pull request в [tensorflow/docs](https://github.com/tensorflow/docs)
репозиторий GitHub. Если вы хотите помочь сделать документацию по Tensorflow
лучше (сделать сам перевод или проверить перевод подготовленный кем-то другим),
напишите нам на
[docs-ru@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru).

В TensorFlow 2.0 были сделаны несколько изменений, которые позволят всем пользователям TensorFlow 
работать более продуктивно. В TensorFlow 2.0 были удалены
[ненужные API](https://github.com/tensorflow/community/blob/master/rfcs/20180827-api-names.md),
существующие и используемые API были проработаны 
([объединены RNN](https://github.com/tensorflow/community/blob/master/rfcs/20180920-unify-rnn-interface.md),
[а также оптимизаторы](https://github.com/tensorflow/community/blob/master/rfcs/20181016-optimizer-unification.md)),
улучшена интеграция с рабочей средой Python в режиме
[Eager execution](https://www.tensorflow.org/guide/eager).

Во многих
[запросах RFC](https://github.com/tensorflow/community/pulls?utf8=%E2%9C%93&q=is%3Apr)
объяснялись основные изменения, которые затронут TensorFlow 2.0. В этом документе
будет показано, как должен выглядеть процесс работы с новым TensorFlow 2.0.
Подразумевается, что вы уже знакомы с TensorFlow 1.x.

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

Раньше побочным продуктом eager execution был метод `tf.control_dependencies()`,
который теперь не треубется, и все строки кода будут исполняться в последовательном
порядке, определенном `tf.function`. Сторонний код будет выполняться в 
определенном ему порядке.

### Никаких глобальных переменных

TensorFlow 1.X внутренне полагался на глобальные переменные. Когда вы вызывали
`tf.Variable()`, то эта переменная помещалась в стандартный граф и оставалась там
даже если уже было изменено имя, присвоенное этой переменной. Вы могли восстановить
эту переменную `tf.Variable`, но только если тебе было известно имя, которое было
присвоено ей при создании. В результате все механизмы были направлены на то, чтобы
помочь пользователю отыскать имя их переменных еще раз: `tf.get_global_step()`, 
`tf.global_variables_initializer()`, оптимизаторы, которые рассчитывали
градиенты по всем обучаемым перменным и так далее. В TensorFlow 2.0 эти механизмы были
устранены ([Переменные 2.0 RFC](https://github.com/tensorflow/community/pull/11))
в пользу нового: следи за состоянием рабочих переменных! Если вы потеряете `tf.Variable`
(например, ей будет присвоено новое имя), то старая будет удалена из памяти в порядке
процесса garbage collection.

Требование следить за переменными создает дополнительную нагрузку на пользователя,
но в случае с объектами Keras (см. ниже), это нагрузка - минимальная.

### Функции, а не сессии

Вызов `session.run()` работал почти как вызов функции: вы определяли вводные данные
и вызывал функцию, получая на выходе результаты. В TensorFlow 2.0, вы можете
декорировать функцию Python при помощи `tf.function()`, отметив её как JIT-компилируемую,
чтобы TensorFlow запустил ее на одном единственном графе
([Функции 2.0 RFC](https://github.com/tensorflow/community/pull/20)). Этот
механизм позволяет TensorFlow 2.0 получить все преимущества режима graph:

-   Производительность: функции могут быть оптимизированы (отсечение узлов графа,
    слияние ядра и так далее)
-   Портативность: Функции могут быть экспортированы
    или импортированы повторно ([Сохранение моделей 2.0 RFC](https://github.com/tensorflow/community/pull/34)),
    позволяя пользователям использовать модульные функции TensorFlow и делиться ими.

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

### Рефакторинг кода на малые функции

Часто используемый шаблон использования в TensorFlow 1.X работал по принципу
kitchen sink ("кухонной раковины"), когда быа выложена совокупность всех возможных вычислений,
а затем выбранные тензоры вычислялись с помощью `session.run()`. В TensorFlow 2.0
пользователи должны сами разбивать код на более мелкие функции и вызывать каждую
когда это необходимо. Необязательно декорировать каждую из этих небольших функций
с `tf.function`; используй `tf.function` для декорирования только высокоуровневых
вычислений - например, один шаг обучения или прямого прохода для модели.

### Используй слои и модели Keras для управления переменными

Модели и слои Keras предлагают использовать удобное свойство `.variables`, которое
рекурсивно собирает все зависимые переменные. Это значительно облегчает локальное управление
переменными.

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

# Нам все равно придется управлять w_i и b_i, так как их формы определяются не в коде.
```

Версия с использованием Keras:

```python
# Каждый слой может быть вызван с сигнатурой равной linear(x)
layers = [tf.keras.layers.Dense(hidden_size, activation=tf.nn.sigmoid) for _ in range(n)]
perceptron = tf.keras.Sequential(layers)

# layers[3].variables => returns [w3, b3]
# perceptron.variables => returns [w0, b0, ...]
```

Модели и слои Keras наследуются из `tf.train.Checkpointable` и интегрируются с
`@tf.function`, что делает возможным сохранить или непосредственно экспортировать
сохраненные модели из объектов Keras. Необязательно использовать метод `.fit()` из
Keras API для этих интеграций.

Вот пример transfer learning (переноса обучения), который демонстрирует как легко
собрать подмножество необходимых переменных с помощью Keras. Предположим, мы обучаем
разветвленную (multi-head) модель с общим корнем (trunk):

```python
trunk = tf.keras.Sequential([...])
head1 = tf.keras.Sequential([...])
head2 = tf.keras.Sequential([...])

path1 = tf.keras.Sequential([trunk, head1])
path2 = tf.keras.Sequential([trunk, head2])

# Обучаем на основном датасете:
for x, y in main_dataset:
  with tf.GradientTape() as tape:
    prediction = path1(x)
    loss = loss_fn_head1(prediction, y)
  # Одновременно оптимизируем корень и веса первой ветви:
  gradients = tape.gradients(loss, path1.variables)
  optimizer.apply_gradients(gradients, path1.variables)

# Настраиваем вторую ветвь, повторно используя корень:
for x, y in small_dataset:
  with tf.GradientTape() as tape:
    prediction = path2(x)
    loss = loss_fn_head2(prediction, y)
  # Оптимизируем веса только второй ветви, без весов корня:
  gradients = tape.gradients(loss, head2.variables)
  optimizer.apply_gradients(gradients, head2.variables)

# 
# Можем сохранить вычисления корня, чтобы другие также могли им воспользоваться.
tf.saved_model.save(trunk, output_path)
```

### Объединение tf.data.Datasets и @tf.function

При обучении модели на данных, которые находятся в памяти, используй стандартный
итератор Python. В остальных случаях `tf.data.Dataset` является лучшим способом
для потока тренировочных данных с диска. Датасеты являются
[итерируемыми (не итераторами)](https://docs.python.org/3/glossary.html#term-iterable),
и работают так же, как и другие итераторы Python в режиме Eager. Вы можете наиболее
полно использовать асинхронные возможности prefetch и stream при помощи
`tf.function()`, которая заменяет итерации Python их эквивалентами операций графов
посредством AutoGraph.

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

Если вы используете метод `.fit()` из Keras API, то вам не придется
волноваться об итерации датасета.

```python
model.compile(optimizer=optimizer, loss=loss_fn)
model.fit(dataset)
```

### Воспользуйтесь премиуществами AutoGraph с порядком выполнения Python

AutoGraph обеспечивает способ конвертации зависимого от данных порядка
выполнения в его эквиваленты в режиме graph, например `tf.cond` и `tf.while_loop`.

Единственное место, где появляется зависимый от данных порядок выполнения это
последовательные модели. `tf.keras.layers.RNN` использует элемент RNN, позволяя
вам развернуть повтор статически или динамически. Для примера, вы можете
использовать динамическое развертывание:

```python
class DynamicRNN(tf.keras.Model):

  def __init__(self, rnn_cell):
    super(DynamicRNN, self).__init__(self)
    self.cell = rnn_cell

  def call(self, input_data):
    # [батч, время, параметры] -> [время, батч, параметры]
    input_data = tf.transpose(input_data, [1, 0, 2])
    outputs = tf.TensorArray(tf.float32, input_data.shape[0])
    state = self.cell.zero_state(input_data.shape[1], dtype=tf.float32)
    for i in tf.range(input_data.shape[0]):
      output, state = self.cell(input_data[i], state)
      outputs = outputs.write(i, output)
    return tf.transpose(outputs.stack(), [1, 0, 2]), state
```

Для более детального описание возможностей AutoGraph ознакомьтесь с
[руководством](./autograph.ipynb).

### Используйте tf.metrics для сбора данных и tf.summary для логов

Для записи логов, используйте `tf.summary.(scalar|histogram|...)`. Если использовать
данные методы отдельно, то они не будут ничего делать; результаты должны быть
перенаправлены к соответствующему file writer, при помощи контекстного менеджера
(это позволит вам избежать записи логов в file writer).

```python
summary_writer = tf.summary.create_file_writer('/tmp/summaries')
with summary_writer.as_default():
  tf.summary.scalar('loss', 0.1, step=42)
```

Чтобы собрать данные перед записью в лог, используйте `tf.metrics`. Метрики
сохраняют свое состояние; они накапливают значения и возвращают собирательный 
результат, когда вы вызываете метод `.result()`. Чтобы очистить все значения 
используйте метод `.reset_states()`.

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

Указав папку с результами в TensorBoard (`tensorboard --logdir
/tmp/summaries`), вы можете визуализировать полученные в ходе обучения
данные на графиках.


