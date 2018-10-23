

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# Module: tf.contrib.learn



Defined in [`tensorflow/contrib/learn/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/learn/__init__.py).

High level API for learning.

See the [Learn (contrib)](../../../../api_guides/python/contrib.learn) guide.







## Modules

[`datasets`](../../tf/contrib/learn/datasets) module: Dataset utilities and synthetic/reference datasets.

[`graph_actions`](../../tf/contrib/learn/graph_actions) module: High level operations on graphs.

[`head`](../../tf/contrib/learn/head) module: Abstractions for the head(s) of a model.

[`io`](../../tf/contrib/learn/io) module: Tools to allow different io formats.

[`learn_runner`](../../tf/contrib/learn/learn_runner) module: Utilities to run and tune an Experiment.

[`models`](../../tf/contrib/learn/models) module: Various high level TF models.

[`monitors`](../../tf/contrib/learn/monitors) module: Monitors instrument the training process.

[`ops`](../../tf/contrib/learn/ops) module: Various TensorFlow Ops.

[`preprocessing`](../../tf/contrib/learn/preprocessing) module: Preprocessing tools useful for building models.

[`utils`](../../tf/contrib/learn/utils) module: TensorFlow Learn Utils.

## Classes

[`class BaseEstimator`](../../tf/contrib/learn/BaseEstimator): Abstract BaseEstimator class to train and evaluate TensorFlow models.

[`class DNNClassifier`](../../tf/contrib/learn/DNNClassifier): A classifier for TensorFlow DNN models.

[`class DNNEstimator`](../../tf/contrib/learn/DNNEstimator): A Estimator for TensorFlow DNN models with user specified _Head.

[`class DNNLinearCombinedClassifier`](../../tf/contrib/learn/DNNLinearCombinedClassifier): A classifier for TensorFlow Linear and DNN joined training models.

[`class DNNLinearCombinedEstimator`](../../tf/contrib/learn/DNNLinearCombinedEstimator): An estimator for TensorFlow Linear and DNN joined training models.

[`class DNNLinearCombinedRegressor`](../../tf/contrib/learn/DNNLinearCombinedRegressor): A regressor for TensorFlow Linear and DNN joined training models.

[`class DNNRegressor`](../../tf/contrib/learn/DNNRegressor): A regressor for TensorFlow DNN models.

[`class DynamicRnnEstimator`](../../tf/contrib/learn/DynamicRnnEstimator)

[`class Estimator`](../../tf/contrib/learn/Estimator): Estimator class is the basic TensorFlow model trainer/evaluator.

[`class Evaluable`](../../tf/contrib/learn/Evaluable): Interface for objects that are evaluatable by, e.g., `Experiment`.

[`class Experiment`](../../tf/contrib/learn/Experiment): Experiment is a class containing all information needed to train a model.

[`class ExportStrategy`](../../tf/contrib/learn/ExportStrategy): A class representing a type of model export.

[`class Head`](../../tf/contrib/learn/Head): Interface for the head/top of a model.

[`class InputFnOps`](../../tf/contrib/learn/InputFnOps): A return type for an input_fn.

[`class KMeansClustering`](../../tf/contrib/learn/KMeansClustering): An Estimator for K-Means clustering.

[`class LinearClassifier`](../../tf/contrib/learn/LinearClassifier): Linear classifier model.

[`class LinearEstimator`](../../tf/contrib/learn/LinearEstimator): Linear model with user specified head.

[`class LinearRegressor`](../../tf/contrib/learn/LinearRegressor): Linear regressor model.

[`class MetricSpec`](../../tf/contrib/learn/MetricSpec): MetricSpec connects a model to metric functions.

[`class ModeKeys`](../../tf/contrib/learn/ModeKeys): Standard names for model modes.

[`class ModelFnOps`](../../tf/contrib/learn/ModelFnOps): Ops returned from a model_fn.

[`class NanLossDuringTrainingError`](../../tf/contrib/learn/NanLossDuringTrainingError)

[`class NotFittedError`](../../tf/contrib/learn/NotFittedError): Exception class to raise if estimator is used before fitting.

[`class PredictionKey`](../../tf/contrib/learn/PredictionKey)

[`class ProblemType`](../../tf/contrib/learn/ProblemType): Enum-like values for the type of problem that the model solves.

[`class RunConfig`](../../tf/contrib/learn/RunConfig): This class specifies the configurations for an `Estimator` run.

[`class SKCompat`](../../tf/contrib/learn/SKCompat): Scikit learn wrapper for TensorFlow Learn Estimator.

[`class SVM`](../../tf/contrib/learn/SVM): Support Vector Machine (SVM) model for binary classification.

[`class TaskType`](../../tf/contrib/learn/TaskType)

[`class Trainable`](../../tf/contrib/learn/Trainable): Interface for objects that are trainable by, e.g., `Experiment`.

## Functions

[`LogisticRegressor(...)`](../../tf/contrib/learn/LogisticRegressor): Builds a logistic regression Estimator for binary classification.

[`binary_svm_head(...)`](../../tf/contrib/learn/binary_svm_head): Creates a `Head` for binary classification with SVMs.

[`build_parsing_serving_input_fn(...)`](../../tf/contrib/learn/build_parsing_serving_input_fn): Build an input_fn appropriate for serving, expecting fed tf.Examples.

[`evaluate(...)`](../../tf/contrib/learn/evaluate): Evaluate a model loaded from a checkpoint. (deprecated)

[`extract_dask_data(...)`](../../tf/contrib/learn/extract_dask_data): Extract data from dask.Series or dask.DataFrame for predictors.

[`extract_dask_labels(...)`](../../tf/contrib/learn/extract_dask_labels): Extract data from dask.Series or dask.DataFrame for labels.

[`extract_pandas_data(...)`](../../tf/contrib/learn/extract_pandas_data): Extract data from pandas.DataFrame for predictors.

[`extract_pandas_labels(...)`](../../tf/contrib/learn/extract_pandas_labels): Extract data from pandas.DataFrame for labels.

[`extract_pandas_matrix(...)`](../../tf/contrib/learn/extract_pandas_matrix): Extracts numpy matrix from pandas DataFrame.

[`infer(...)`](../../tf/contrib/learn/infer): Restore graph from `restore_checkpoint_path` and run `output_dict` tensors. (deprecated)

[`infer_real_valued_columns_from_input(...)`](../../tf/contrib/learn/infer_real_valued_columns_from_input): Creates `FeatureColumn` objects for inputs defined by input `x`.

[`infer_real_valued_columns_from_input_fn(...)`](../../tf/contrib/learn/infer_real_valued_columns_from_input_fn): Creates `FeatureColumn` objects for inputs defined by `input_fn`.

[`make_export_strategy(...)`](../../tf/contrib/learn/make_export_strategy): Create an ExportStrategy for use with Experiment.

[`multi_class_head(...)`](../../tf/contrib/learn/multi_class_head): Creates a `Head` for multi class single label classification.

[`multi_head(...)`](../../tf/contrib/learn/multi_head): Creates a MultiHead stemming from same logits/hidden layer.

[`multi_label_head(...)`](../../tf/contrib/learn/multi_label_head): Creates a Head for multi label classification.

[`no_op_train_fn(...)`](../../tf/contrib/learn/no_op_train_fn)

[`poisson_regression_head(...)`](../../tf/contrib/learn/poisson_regression_head): Creates a `Head` for poisson regression.

[`read_batch_examples(...)`](../../tf/contrib/learn/read_batch_examples): Adds operations to read, queue, batch `Example` protos.

[`read_batch_features(...)`](../../tf/contrib/learn/read_batch_features): Adds operations to read, queue, batch and parse `Example` protos.

[`read_batch_record_features(...)`](../../tf/contrib/learn/read_batch_record_features): Reads TFRecord, queues, batches and parses `Example` proto.

[`regression_head(...)`](../../tf/contrib/learn/regression_head): Creates a `Head` for linear regression.

[`run_feeds(...)`](../../tf/contrib/learn/run_feeds): See run_feeds_iter(). Returns a `list` instead of an iterator. (deprecated)

[`run_n(...)`](../../tf/contrib/learn/run_n): Run `output_dict` tensors `n` times, with the same `feed_dict` each run. (deprecated)

[`train(...)`](../../tf/contrib/learn/train): Train a model. (deprecated)

