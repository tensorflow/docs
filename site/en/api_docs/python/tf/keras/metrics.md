page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.keras.metrics


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/metrics">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Built-in metrics.

### Aliases:

* Module <a href="/api_docs/python/tf/keras/metrics"><code>tf.compat.v1.keras.metrics</code></a>


<!-- Placeholder for "Used in" -->


## Classes

[`class AUC`](../../tf/keras/metrics/AUC): Computes the approximate AUC (Area under the curve) via a Riemann sum.

[`class Accuracy`](../../tf/keras/metrics/Accuracy): Calculates how often predictions matches labels.

[`class BinaryAccuracy`](../../tf/keras/metrics/BinaryAccuracy): Calculates how often predictions matches labels.

[`class BinaryCrossentropy`](../../tf/keras/metrics/BinaryCrossentropy): Computes the crossentropy metric between the labels and predictions.

[`class CategoricalAccuracy`](../../tf/keras/metrics/CategoricalAccuracy): Calculates how often predictions matches labels.

[`class CategoricalCrossentropy`](../../tf/keras/metrics/CategoricalCrossentropy): Computes the crossentropy metric between the labels and predictions.

[`class CategoricalHinge`](../../tf/keras/metrics/CategoricalHinge): Computes the categorical hinge metric between `y_true` and `y_pred`.

[`class CosineSimilarity`](../../tf/keras/metrics/CosineSimilarity): Computes the cosine similarity between the labels and predictions.

[`class FalseNegatives`](../../tf/keras/metrics/FalseNegatives): Calculates the number of false negatives.

[`class FalsePositives`](../../tf/keras/metrics/FalsePositives): Calculates the number of false positives.

[`class Hinge`](../../tf/keras/metrics/Hinge): Computes the hinge metric between `y_true` and `y_pred`.

[`class KLDivergence`](../../tf/keras/metrics/KLDivergence): Computes Kullback-Leibler divergence metric between `y_true` and `y_pred`.

[`class LogCoshError`](../../tf/keras/metrics/LogCoshError): Computes the logarithm of the hyperbolic cosine of the prediction error.

[`class Mean`](../../tf/keras/metrics/Mean): Computes the (weighted) mean of the given values.

[`class MeanAbsoluteError`](../../tf/keras/metrics/MeanAbsoluteError): Computes the mean absolute error between the labels and predictions.

[`class MeanAbsolutePercentageError`](../../tf/keras/metrics/MeanAbsolutePercentageError): Computes the mean absolute percentage error between `y_true` and `y_pred`.

[`class MeanIoU`](../../tf/keras/metrics/MeanIoU): Computes the mean Intersection-Over-Union metric.

[`class MeanRelativeError`](../../tf/keras/metrics/MeanRelativeError): Computes the mean relative error by normalizing with the given values.

[`class MeanSquaredError`](../../tf/keras/metrics/MeanSquaredError): Computes the mean squared error between `y_true` and `y_pred`.

[`class MeanSquaredLogarithmicError`](../../tf/keras/metrics/MeanSquaredLogarithmicError): Computes the mean squared logarithmic error between `y_true` and `y_pred`.

[`class MeanTensor`](../../tf/keras/metrics/MeanTensor): Computes the element-wise (weighted) mean of the given tensors.

[`class Metric`](../../tf/keras/metrics/Metric): Encapsulates metric logic and state.

[`class Poisson`](../../tf/keras/metrics/Poisson): Computes the Poisson metric between `y_true` and `y_pred`.

[`class Precision`](../../tf/keras/metrics/Precision): Computes the precision of the predictions with respect to the labels.

[`class Recall`](../../tf/keras/metrics/Recall): Computes the recall of the predictions with respect to the labels.

[`class RootMeanSquaredError`](../../tf/keras/metrics/RootMeanSquaredError): Computes root mean squared error metric between `y_true` and `y_pred`.

[`class SensitivityAtSpecificity`](../../tf/keras/metrics/SensitivityAtSpecificity): Computes the sensitivity at a given specificity.

[`class SparseCategoricalAccuracy`](../../tf/keras/metrics/SparseCategoricalAccuracy): Calculates how often predictions matches integer labels.

[`class SparseCategoricalCrossentropy`](../../tf/keras/metrics/SparseCategoricalCrossentropy): Computes the crossentropy metric between the labels and predictions.

[`class SparseTopKCategoricalAccuracy`](../../tf/keras/metrics/SparseTopKCategoricalAccuracy): Computes how often integer targets are in the top `K` predictions.

[`class SpecificityAtSensitivity`](../../tf/keras/metrics/SpecificityAtSensitivity): Computes the specificity at a given sensitivity.

[`class SquaredHinge`](../../tf/keras/metrics/SquaredHinge): Computes the squared hinge metric between `y_true` and `y_pred`.

[`class Sum`](../../tf/keras/metrics/Sum): Computes the (weighted) sum of the given values.

[`class TopKCategoricalAccuracy`](../../tf/keras/metrics/TopKCategoricalAccuracy): Computes how often targets are in the top `K` predictions.

[`class TrueNegatives`](../../tf/keras/metrics/TrueNegatives): Calculates the number of true negatives.

[`class TruePositives`](../../tf/keras/metrics/TruePositives): Calculates the number of true positives.

## Functions

[`KLD(...)`](../../tf/keras/losses/KLD): Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

[`MAE(...)`](../../tf/keras/losses/MAE)

[`MAPE(...)`](../../tf/keras/losses/MAPE)

[`MSE(...)`](../../tf/keras/losses/MSE)

[`MSLE(...)`](../../tf/keras/losses/MSLE)

[`binary_accuracy(...)`](../../tf/keras/metrics/binary_accuracy)

[`binary_crossentropy(...)`](../../tf/keras/losses/binary_crossentropy)

[`categorical_accuracy(...)`](../../tf/keras/metrics/categorical_accuracy)

[`categorical_crossentropy(...)`](../../tf/keras/losses/categorical_crossentropy): Computes the categorical crossentropy loss.

[`cosine(...)`](../../tf/keras/losses/cosine): Computes the cosine similarity between labels and predictions.

[`cosine_proximity(...)`](../../tf/keras/losses/cosine): Computes the cosine similarity between labels and predictions.

[`deserialize(...)`](../../tf/keras/metrics/deserialize)

[`get(...)`](../../tf/keras/metrics/get)

[`hinge(...)`](../../tf/keras/losses/hinge): Computes the hinge loss between `y_true` and `y_pred`.

[`kld(...)`](../../tf/keras/losses/KLD): Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

[`kullback_leibler_divergence(...)`](../../tf/keras/losses/KLD): Computes Kullback-Leibler divergence loss between `y_true` and `y_pred`.

[`mae(...)`](../../tf/keras/losses/MAE)

[`mape(...)`](../../tf/keras/losses/MAPE)

[`mean_absolute_error(...)`](../../tf/keras/losses/MAE)

[`mean_absolute_percentage_error(...)`](../../tf/keras/losses/MAPE)

[`mean_squared_error(...)`](../../tf/keras/losses/MSE)

[`mean_squared_logarithmic_error(...)`](../../tf/keras/losses/MSLE)

[`mse(...)`](../../tf/keras/losses/MSE)

[`msle(...)`](../../tf/keras/losses/MSLE)

[`poisson(...)`](../../tf/keras/losses/poisson): Computes the Poisson loss between y_true and y_pred.

[`serialize(...)`](../../tf/keras/metrics/serialize)

[`sparse_categorical_accuracy(...)`](../../tf/keras/metrics/sparse_categorical_accuracy)

[`sparse_categorical_crossentropy(...)`](../../tf/keras/losses/sparse_categorical_crossentropy)

[`sparse_top_k_categorical_accuracy(...)`](../../tf/keras/metrics/sparse_top_k_categorical_accuracy)

[`squared_hinge(...)`](../../tf/keras/losses/squared_hinge): Computes the squared hinge loss between `y_true` and `y_pred`.

[`top_k_categorical_accuracy(...)`](../../tf/keras/metrics/top_k_categorical_accuracy)
