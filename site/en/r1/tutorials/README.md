# TensorFlow 1.x tutorials (archived)

Note: Please use the latest tutorials at https://www.tensorflow.org/tutorials

TensorFlow is an open-source machine learning library for research and
production. TensorFlow offers APIs for beginners and experts to develop for
desktop, mobile, web, and cloud. See the sections below to get started.

## Learn and use ML

The high-level Keras API provides building blocks to create and
train deep learning models. Start with these beginner-friendly
notebook examples, then read the [TensorFlow Keras guide](../guide/keras.ipynb).

* [Basic classification](./keras/basic_classification.ipynb)
* [Text classification](./keras/basic_text_classification.ipynb)
* [Regression](./keras/basic_regression.ipynb)
* [Overfitting and underfitting](./keras/overfit_and_underfit.ipynb)
* [Save and load](./keras/save_and_restore_models.ipynb)

```python
import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
```

Run this code in
[Google's interactive notebook](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/r1/tutorials/_index.ipynb).

## Research and experimentation

Eager execution provides an imperative, define-by-run interface for advanced
operations. Write custom layers, forward passes, and training loops with
auto‑differentiation. Start with these notebooks, then read the
[eager execution guide](../guide/eager.ipynb).

* [Eager execution basics](./eager/eager_basics.ipynb)
* [Automatic differentiation and gradient tape](./eager/automatic_differentiation.ipynb)
* [Custom training: basics](./eager/custom_training.ipynb)
* [Custom layers](./eager/custom_layers.ipynb)
* [Custom training: walkthrough](./eager/custom_training_walkthrough.ipynb)

## ML at production scale

Estimators can train large models on multiple machines in a production
environment. TensorFlow provides a collection of pre-made Estimators to
implement common ML algorithms. See the
[Estimators guide](../guide/estimators.md).

* [Build a linear model with Estimators](./estimators/linear.ipynb)
* [Boosted trees](./estimators/boosted_trees.ipynb)
* [Gradient Boosted Trees: Model understanding](./estimators/boosted_trees_model_understanding.ipynb)
* [Build a Convolutional Neural Network using Estimators](./estimators/cnn.ipynb)
* [Wide and deep learning with Estimators](https://github.com/tensorflow/models/tree/master/official/r1/wide_deep)
