# Estimators

В этом документе представлен `tf.estimator` - высокоуровневый TensorFlow API,
который значительно упрощает процесс создания моделей машинного обучения.
Estimators включает в себя следующие операции:

*   обучение
*   оценку
*   предсказание
*   экспорт модели на сервер

Ты можешь использовать либо уже готовые Estimators или написать свои
собственные для оценки. Все Estimators основаны на классе `tf.estimator.Estimator`

Для быстрого ознакомления попробуй запустить [интерактивные уроки по Estimator](../tutorials/estimators/linear.ipynb)
в Google Colab. Чтобы узнать о каждой теме подробнее смотри [руководства по Estimator](premade_estimators.md).
Для ознакомления с дизайном этого API смотри наш [доклад на arxiv.org](https://arxiv.org/abs/1708.02637).

Обрати внимание: TensorFlow также включает в себя устаревший класс
`Estimator` в `tf.contrib.learn.Estimator`, который использовать не стоит.


## Преимущества Estimators

Estimators обеспечивают следующие преимущества:
	
*   Можно запускать модели на основе Estimators локально или на распределенном
    сервере без изменений структуры модели. Более того, ты можешь запускать модели
	на CPU, GPU и TPU без внесения изменений в код.
*   С помощью Estimators можно легче делиться своими моделями с другими разработчиками
*   Можно разрабатывать современные модели с читаемым высокоуровневым кодом. Проще говоря,
    гораздо легче создавать модели с Estimators, чем с низкоуровневым API TensorFlow
*   Сами Estimators построены на `tf.keras.layers`, которые упрощают настройку модели
    под себя
*   Estimators строят граф
*   Estimators обеспечивают простой распределенный цикл обучения, который контроллирует
    как и когда:
    *   строить граф
    *   инициализировать переменные
    *   загружать данные
    *   обрабатывать исключения
    *   создавать контрольные точки и восстанавливаться при неудачных попытках
    *   сохранять статистику в TensorBoard

При написании приложения с Estimators ты должен отделять загрузку входных данных
от самой модели. Это разделение упрощает эксперименты с разными наборами данных.


## Готовые Estimators

Готовые Estimators позволяют тебе работать на более высоком уровне, по сравнению
с базовым API TensorFlow. Тебе больше не нужно волноваться о создании вычислительного
графа или сессиях обучения, поскольку Estimators сами делают за тебя всю работу.
Таким образом Estimators сами создают и управляют объектами `tf.Graph` и 
`tf.Session`. Более того, готовые Estimators позволяют тебе экспериментировать с 
разными архитектурами с минимальными изменениями исходного кода. Например,
`tf.estimator.DNNClassifier` - это готовый класс Estimator, который обучает
классификации модели на основе нейронных сетей прямого распространения с слоями*Dense*.


### Структура готовых программ с Estimators

Программа TensorFlow на основе готовых Estimators обычно состоит из следующих
четырех шагов:
	
1.  **Написание одной или более функций для загрузки датасета**. Например,
    создадим функцию для импорта тренировочного набора и вторую функцию для 
	импорта проверного набора данных. Каждый функция для загрузки датасета
	должна возвращать два объекта:

    *   словарь, в котором ключи являются именами параметров, а значения
	    являются тензорами (или SparseTensors), содержащие соответствующие
		данные параметров
    *   тензор, содержащий одну или более меток

    Например, в коде ниже показан пример основного скелета для функции ввода
    данных:

        def input_fn(dataset):
           ...  # манипулирует датасетом, извлекая словарь параметров и метки
           return feature_dict, label

    (Смотри подбробнее в [Загрузка данных](../guide/datasets.md))

2.  **Define the feature columns.** Each `tf.feature_column`
    identifies a feature name, its type, and any input pre-processing.
    For example, the following snippet creates three feature
    columns that hold integer or floating-point data.  The first two
    feature columns simply identify the feature's name and type. The
    third feature column also specifies a lambda the program will invoke
    to scale the raw data:

        # Define three numeric feature columns.
        population = tf.feature_column.numeric_column('population')
        crime_rate = tf.feature_column.numeric_column('crime_rate')
        median_education = tf.feature_column.numeric_column('median_education',
                            normalizer_fn=lambda x: x - global_education_mean)

3.  **Instantiate the relevant pre-made Estimator.**  For example, here's
    a sample instantiation of a pre-made Estimator named `LinearClassifier`:

        # Instantiate an estimator, passing the feature columns.
        estimator = tf.estimator.LinearClassifier(
            feature_columns=[population, crime_rate, median_education],
            )

4.  **Call a training, evaluation, or inference method.**
    For example, all Estimators provide a `train` method, which trains a model.

        # my_training_set is the function created in Step 1
        estimator.train(input_fn=my_training_set, steps=2000)


### Benefits of pre-made Estimators

Pre-made Estimators encode best practices, providing the following benefits:

*   Best practices for determining where different parts of the computational
    graph should run, implementing strategies on a single machine or on a
    cluster.
*   Best practices for event (summary) writing and universally useful
    summaries.

If you don't use pre-made Estimators, you must implement the preceding
features yourself.


## Custom Estimators

The heart of every Estimator—whether pre-made or custom—is its
**model function**, which is a method that builds graphs for training,
evaluation, and prediction. When you are using a pre-made Estimator,
someone else has already implemented the model function. When relying
on a custom Estimator, you must write the model function yourself. A
[companion document](../guide/custom_estimators.md)
explains how to write the model function.


## Recommended workflow

We recommend the following workflow:

1.  Assuming a suitable pre-made Estimator exists, use it to build your
    first model and use its results to establish a baseline.
2.  Build and test your overall pipeline, including the integrity and
    reliability of your data with this pre-made Estimator.
3.  If suitable alternative pre-made Estimators are available, run
    experiments to determine which pre-made Estimator produces the
    best results.
4.  Possibly, further improve your model by building your own custom Estimator.


## Creating Estimators from Keras models

You can convert existing Keras models to Estimators. Doing so enables your Keras
model to access Estimator's strengths, such as distributed training. Call
`tf.keras.estimator.model_to_estimator` as in the
following sample:

```python
# Instantiate a Keras inception v3 model.
keras_inception_v3 = tf.keras.applications.inception_v3.InceptionV3(weights=None)
# Compile model with the optimizer, loss, and metrics you'd like to train with.
keras_inception_v3.compile(optimizer=tf.keras.optimizers.SGD(lr=0.0001, momentum=0.9),
                          loss='categorical_crossentropy',
                          metric='accuracy')
# Create an Estimator from the compiled Keras model. Note the initial model
# state of the keras model is preserved in the created Estimator.
est_inception_v3 = tf.keras.estimator.model_to_estimator(keras_model=keras_inception_v3)

# Treat the derived Estimator as you would with any other Estimator.
# First, recover the input name(s) of Keras model, so we can use them as the
# feature column name(s) of the Estimator input function:
keras_inception_v3.input_names  # print out: ['input_1']
# Once we have the input name(s), we can create the input function, for example,
# for input(s) in the format of numpy ndarray:
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"input_1": train_data},
    y=train_labels,
    num_epochs=1,
    shuffle=False)
# To train, we call Estimator's train function:
est_inception_v3.train(input_fn=train_input_fn, steps=2000)
```
Note that the names of feature columns and labels of a keras estimator come from
the corresponding compiled keras model. For example, the input key names for
`train_input_fn` above can be obtained from `keras_inception_v3.input_names`,
and similarly, the predicted output names can be obtained from
`keras_inception_v3.output_names`.

For more details, please refer to the documentation for
`tf.keras.estimator.model_to_estimator`.
