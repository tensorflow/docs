


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.learn

### Module `tf.contrib.learn`

High level API for learning. See the [Learn (contrib)](../../../../api_guides/python/contrib.learn) guide.






## Members

[`class BaseEstimator`](../../tf/contrib/learn/BaseEstimator): Abstract BaseEstimator class to train and evaluate TensorFlow models.

[`class DNNClassifier`](../../tf/contrib/learn/DNNClassifier): A classifier for TensorFlow DNN models.

[`class DNNLinearCombinedClassifier`](../../tf/contrib/learn/DNNLinearCombinedClassifier): A classifier for TensorFlow Linear and DNN joined training models.

[`class DNNLinearCombinedRegressor`](../../tf/contrib/learn/DNNLinearCombinedRegressor): A regressor for TensorFlow Linear and DNN joined training models.

[`class DNNRegressor`](../../tf/contrib/learn/DNNRegressor): A regressor for TensorFlow DNN models.

[`class Estimator`](../../tf/contrib/learn/Estimator): Estimator class is the basic TensorFlow model trainer/evaluator.

[`class Evaluable`](../../tf/contrib/learn/Evaluable): Interface for objects that are evaluatable by, e.g., `Experiment`.

[`class Experiment`](../../tf/contrib/learn/Experiment): Experiment is a class containing all information needed to train a model.

[`class ExportStrategy`](../../tf/contrib/learn/ExportStrategy)

[`class KMeansClustering`](../../tf/contrib/learn/KMeansClustering): An Estimator fo rK-Means clustering.

[`class LinearClassifier`](../../tf/contrib/learn/LinearClassifier): Linear classifier model.

[`class LinearRegressor`](../../tf/contrib/learn/LinearRegressor): Linear regressor model.

[`LogisticRegressor(...)`](../../tf/contrib/learn/LogisticRegressor): Builds a logistic regression Estimator for binary classification.

[`class MetricSpec`](../../tf/contrib/learn/MetricSpec): MetricSpec connects a model to metric functions.

[`class ModeKeys`](../../tf/contrib/learn/ModeKeys): Standard names for model modes.

[`class ModelFnOps`](../../tf/contrib/learn/ModelFnOps): Ops returned from a model_fn.

[`class NanLossDuringTrainingError`](../../tf/contrib/learn/NanLossDuringTrainingError)

[`class NotFittedError`](../../tf/contrib/learn/NotFittedError): Exception class to raise if estimator is used before fitting.

[`class PredictionKey`](../../tf/contrib/learn/PredictionKey)

[`class ProblemType`](../../tf/contrib/learn/ProblemType)

[`class RunConfig`](../../tf/contrib/learn/RunConfig): This class specifies the configurations for an `Estimator` run.

[`class TaskType`](../../tf/contrib/learn/TaskType)

[`class Trainable`](../../tf/contrib/learn/Trainable): Interface for objects that are trainable by, e.g., `Experiment`.

[`build_parsing_serving_input_fn(...)`](../../tf/contrib/learn/build_parsing_serving_input_fn): Build an input_fn appropriate for serving, expecting fed tf.Examples.

[`datasets`](../../tf/contrib/learn/datasets) module: Dataset utilities and synthetic/reference datasets.

[`evaluate(...)`](../../tf/contrib/learn/evaluate): Evaluate a model loaded from a checkpoint. (deprecated)

[`extract_dask_data(...)`](../../tf/contrib/learn/extract_dask_data): Extract data from dask.Series or dask.DataFrame for predictors.

[`extract_dask_labels(...)`](../../tf/contrib/learn/extract_dask_labels): Extract data from dask.Series or dask.DataFrame for labels.

[`extract_pandas_data(...)`](../../tf/contrib/learn/extract_pandas_data): Extract data from pandas.DataFrame for predictors.

[`extract_pandas_labels(...)`](../../tf/contrib/learn/extract_pandas_labels): Extract data from pandas.DataFrame for labels.

[`extract_pandas_matrix(...)`](../../tf/contrib/learn/extract_pandas_matrix): Extracts numpy matrix from pandas DataFrame.

[`graph_actions`](../../tf/contrib/learn/graph_actions) module: High level operations on graphs.

[`head`](../../tf/contrib/learn/head) module: Abstractions for the head(s) of a model.

[`infer(...)`](../../tf/contrib/learn/infer): Restore graph from `restore_checkpoint_path` and run `output_dict` tensors. (deprecated)

[`infer_real_valued_columns_from_input(...)`](../../tf/contrib/learn/infer_real_valued_columns_from_input): Creates `FeatureColumn` objects for inputs defined by input `x`.

[`infer_real_valued_columns_from_input_fn(...)`](../../tf/contrib/learn/infer_real_valued_columns_from_input_fn): Creates `FeatureColumn` objects for inputs defined by `input_fn`.

[`io`](../../tf/contrib/learn/io) module: Tools to allow different io formats.

[`models`](../../tf/contrib/learn/models) module: Various high level TF models.

[`monitors`](../../tf/contrib/learn/monitors) module: Monitors instrument the training process.

[`ops`](../../tf/contrib/learn/ops) module: Various TensorFlow Ops.

[`preprocessing`](../../tf/contrib/learn/preprocessing) module: Preprocessing tools useful for building models.

[`read_batch_examples(...)`](../../tf/contrib/learn/read_batch_examples): Adds operations to read, queue, batch `Example` protos.

[`read_batch_features(...)`](../../tf/contrib/learn/read_batch_features): Adds operations to read, queue, batch and parse `Example` protos.

[`read_batch_record_features(...)`](../../tf/contrib/learn/read_batch_record_features): Reads TFRecord, queues, batches and parses `Example` proto.

[`run_feeds(...)`](../../tf/contrib/learn/run_feeds): See run_feeds_iter(). Returns a `list` instead of an iterator. (deprecated)

[`run_n(...)`](../../tf/contrib/learn/run_n): Run `output_dict` tensors `n` times, with the same `feed_dict` each run. (deprecated)

[`train(...)`](../../tf/contrib/learn/train): Train a model. (deprecated)

[`utils`](../../tf/contrib/learn/utils) module: TensorFlow Learn Utils.

Defined in [`tensorflow/contrib/learn/__init__.py`](https://www.tensorflow.org/code/tensorflow/contrib/learn/__init__.py).

