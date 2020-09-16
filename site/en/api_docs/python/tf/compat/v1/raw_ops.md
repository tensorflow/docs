description: Public API for tf.raw_ops namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.raw_ops" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.raw_ops

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.raw_ops namespace.



## Functions

[`Abort(...)`](../../../tf/raw_ops/Abort.md): Raise a exception to abort the process when called.

[`Abs(...)`](../../../tf/raw_ops/Abs.md): Computes the absolute value of a tensor.

[`AccumulateNV2(...)`](../../../tf/raw_ops/AccumulateNV2.md): Returns the element-wise sum of a list of tensors.

[`AccumulatorApplyGradient(...)`](../../../tf/raw_ops/AccumulatorApplyGradient.md): Applies a gradient to a given accumulator.

[`AccumulatorNumAccumulated(...)`](../../../tf/raw_ops/AccumulatorNumAccumulated.md): Returns the number of gradients aggregated in the given accumulators.

[`AccumulatorSetGlobalStep(...)`](../../../tf/raw_ops/AccumulatorSetGlobalStep.md): Updates the accumulator with a new value for global_step.

[`AccumulatorTakeGradient(...)`](../../../tf/raw_ops/AccumulatorTakeGradient.md): Extracts the average gradient in the given ConditionalAccumulator.

[`Acos(...)`](../../../tf/raw_ops/Acos.md): Computes acos of x element-wise.

[`Acosh(...)`](../../../tf/raw_ops/Acosh.md): Computes inverse hyperbolic cosine of x element-wise.

[`Add(...)`](../../../tf/raw_ops/Add.md): Returns x + y element-wise.

[`AddManySparseToTensorsMap(...)`](../../../tf/raw_ops/AddManySparseToTensorsMap.md): Add an `N`-minibatch `SparseTensor` to a `SparseTensorsMap`, return `N` handles.

[`AddN(...)`](../../../tf/raw_ops/AddN.md): Add all input tensors element wise.

[`AddSparseToTensorsMap(...)`](../../../tf/raw_ops/AddSparseToTensorsMap.md): Add a `SparseTensor` to a `SparseTensorsMap` return its handle.

[`AddV2(...)`](../../../tf/raw_ops/AddV2.md): Returns x + y element-wise.

[`AdjustContrast(...)`](../../../tf/raw_ops/AdjustContrast.md): Deprecated. Disallowed in GraphDef version >= 2.

[`AdjustContrastv2(...)`](../../../tf/raw_ops/AdjustContrastv2.md): Adjust the contrast of one or more images.

[`AdjustHue(...)`](../../../tf/raw_ops/AdjustHue.md): Adjust the hue of one or more images.

[`AdjustSaturation(...)`](../../../tf/raw_ops/AdjustSaturation.md): Adjust the saturation of one or more images.

[`All(...)`](../../../tf/raw_ops/All.md): Computes the "logical and" of elements across dimensions of a tensor.

[`AllCandidateSampler(...)`](../../../tf/raw_ops/AllCandidateSampler.md): Generates labels for candidate sampling with a learned unigram distribution.

[`AllToAll(...)`](../../../tf/raw_ops/AllToAll.md): An Op to exchange data across TPU replicas.

[`Angle(...)`](../../../tf/raw_ops/Angle.md): Returns the argument of a complex number.

[`AnonymousIterator(...)`](../../../tf/raw_ops/AnonymousIterator.md): A container for an iterator resource.

[`AnonymousIteratorV2(...)`](../../../tf/raw_ops/AnonymousIteratorV2.md): A container for an iterator resource.

[`AnonymousMemoryCache(...)`](../../../tf/raw_ops/AnonymousMemoryCache.md)

[`AnonymousMultiDeviceIterator(...)`](../../../tf/raw_ops/AnonymousMultiDeviceIterator.md): A container for a multi device iterator resource.

[`AnonymousRandomSeedGenerator(...)`](../../../tf/raw_ops/AnonymousRandomSeedGenerator.md)

[`Any(...)`](../../../tf/raw_ops/Any.md): Computes the "logical or" of elements across dimensions of a tensor.

[`ApplyAdaMax(...)`](../../../tf/raw_ops/ApplyAdaMax.md): Update '*var' according to the AdaMax algorithm.

[`ApplyAdadelta(...)`](../../../tf/raw_ops/ApplyAdadelta.md): Update '*var' according to the adadelta scheme.

[`ApplyAdagrad(...)`](../../../tf/raw_ops/ApplyAdagrad.md): Update '*var' according to the adagrad scheme.

[`ApplyAdagradDA(...)`](../../../tf/raw_ops/ApplyAdagradDA.md): Update '*var' according to the proximal adagrad scheme.

[`ApplyAdagradV2(...)`](../../../tf/raw_ops/ApplyAdagradV2.md): Update '*var' according to the adagrad scheme.

[`ApplyAdam(...)`](../../../tf/raw_ops/ApplyAdam.md): Update '*var' according to the Adam algorithm.

[`ApplyAddSign(...)`](../../../tf/raw_ops/ApplyAddSign.md): Update '*var' according to the AddSign update.

[`ApplyCenteredRMSProp(...)`](../../../tf/raw_ops/ApplyCenteredRMSProp.md): Update '*var' according to the centered RMSProp algorithm.

[`ApplyFtrl(...)`](../../../tf/raw_ops/ApplyFtrl.md): Update '*var' according to the Ftrl-proximal scheme.

[`ApplyFtrlV2(...)`](../../../tf/raw_ops/ApplyFtrlV2.md): Update '*var' according to the Ftrl-proximal scheme.

[`ApplyGradientDescent(...)`](../../../tf/raw_ops/ApplyGradientDescent.md): Update '*var' by subtracting 'alpha' * 'delta' from it.

[`ApplyMomentum(...)`](../../../tf/raw_ops/ApplyMomentum.md): Update '*var' according to the momentum scheme.

[`ApplyPowerSign(...)`](../../../tf/raw_ops/ApplyPowerSign.md): Update '*var' according to the AddSign update.

[`ApplyProximalAdagrad(...)`](../../../tf/raw_ops/ApplyProximalAdagrad.md): Update '*var' and '*accum' according to FOBOS with Adagrad learning rate.

[`ApplyProximalGradientDescent(...)`](../../../tf/raw_ops/ApplyProximalGradientDescent.md): Update '*var' as FOBOS algorithm with fixed learning rate.

[`ApplyRMSProp(...)`](../../../tf/raw_ops/ApplyRMSProp.md): Update '*var' according to the RMSProp algorithm.

[`ApproximateEqual(...)`](../../../tf/raw_ops/ApproximateEqual.md): Returns the truth value of abs(x-y) < tolerance element-wise.

[`ArgMax(...)`](../../../tf/raw_ops/ArgMax.md): Returns the index with the largest value across dimensions of a tensor.

[`ArgMin(...)`](../../../tf/raw_ops/ArgMin.md): Returns the index with the smallest value across dimensions of a tensor.

[`AsString(...)`](../../../tf/raw_ops/AsString.md): Converts each entry in the given tensor to strings.

[`Asin(...)`](../../../tf/raw_ops/Asin.md): Computes the trignometric inverse sine of x element-wise.

[`Asinh(...)`](../../../tf/raw_ops/Asinh.md): Computes inverse hyperbolic sine of x element-wise.

[`Assert(...)`](../../../tf/raw_ops/Assert.md): Asserts that the given condition is true.

[`AssertCardinalityDataset(...)`](../../../tf/raw_ops/AssertCardinalityDataset.md)

[`AssertNextDataset(...)`](../../../tf/raw_ops/AssertNextDataset.md): A transformation that asserts which transformations happen next.

[`Assign(...)`](../../../tf/raw_ops/Assign.md): Update 'ref' by assigning 'value' to it.

[`AssignAdd(...)`](../../../tf/raw_ops/AssignAdd.md): Update 'ref' by adding 'value' to it.

[`AssignAddVariableOp(...)`](../../../tf/raw_ops/AssignAddVariableOp.md): Adds a value to the current value of a variable.

[`AssignSub(...)`](../../../tf/raw_ops/AssignSub.md): Update 'ref' by subtracting 'value' from it.

[`AssignSubVariableOp(...)`](../../../tf/raw_ops/AssignSubVariableOp.md): Subtracts a value from the current value of a variable.

[`AssignVariableOp(...)`](../../../tf/raw_ops/AssignVariableOp.md): Assigns a new value to a variable.

[`Atan(...)`](../../../tf/raw_ops/Atan.md): Computes the trignometric inverse tangent of x element-wise.

[`Atan2(...)`](../../../tf/raw_ops/Atan2.md): Computes arctangent of `y/x` element-wise, respecting signs of the arguments.

[`Atanh(...)`](../../../tf/raw_ops/Atanh.md): Computes inverse hyperbolic tangent of x element-wise.

[`AudioSpectrogram(...)`](../../../tf/raw_ops/AudioSpectrogram.md): Produces a visualization of audio data over time.

[`AudioSummary(...)`](../../../tf/raw_ops/AudioSummary.md): Outputs a `Summary` protocol buffer with audio.

[`AudioSummaryV2(...)`](../../../tf/raw_ops/AudioSummaryV2.md): Outputs a `Summary` protocol buffer with audio.

[`AutoShardDataset(...)`](../../../tf/raw_ops/AutoShardDataset.md): Creates a dataset that shards the input dataset.

[`AvgPool(...)`](../../../tf/raw_ops/AvgPool.md): Performs average pooling on the input.

[`AvgPool3D(...)`](../../../tf/raw_ops/AvgPool3D.md): Performs 3D average pooling on the input.

[`AvgPool3DGrad(...)`](../../../tf/raw_ops/AvgPool3DGrad.md): Computes gradients of average pooling function.

[`AvgPoolGrad(...)`](../../../tf/raw_ops/AvgPoolGrad.md): Computes gradients of the average pooling function.

[`Barrier(...)`](../../../tf/raw_ops/Barrier.md): Defines a barrier that persists across different graph executions.

[`BarrierClose(...)`](../../../tf/raw_ops/BarrierClose.md): Closes the given barrier.

[`BarrierIncompleteSize(...)`](../../../tf/raw_ops/BarrierIncompleteSize.md): Computes the number of incomplete elements in the given barrier.

[`BarrierInsertMany(...)`](../../../tf/raw_ops/BarrierInsertMany.md): For each key, assigns the respective value to the specified component.

[`BarrierReadySize(...)`](../../../tf/raw_ops/BarrierReadySize.md): Computes the number of complete elements in the given barrier.

[`BarrierTakeMany(...)`](../../../tf/raw_ops/BarrierTakeMany.md): Takes the given number of completed elements from a barrier.

[`Batch(...)`](../../../tf/raw_ops/Batch.md): Batches all input tensors nondeterministically.

[`BatchCholesky(...)`](../../../tf/raw_ops/BatchCholesky.md)

[`BatchCholeskyGrad(...)`](../../../tf/raw_ops/BatchCholeskyGrad.md)

[`BatchDataset(...)`](../../../tf/raw_ops/BatchDataset.md): Creates a dataset that batches `batch_size` elements from `input_dataset`.

[`BatchDatasetV2(...)`](../../../tf/raw_ops/BatchDatasetV2.md): Creates a dataset that batches `batch_size` elements from `input_dataset`.

[`BatchFFT(...)`](../../../tf/raw_ops/BatchFFT.md)

[`BatchFFT2D(...)`](../../../tf/raw_ops/BatchFFT2D.md)

[`BatchFFT3D(...)`](../../../tf/raw_ops/BatchFFT3D.md)

[`BatchFunction(...)`](../../../tf/raw_ops/BatchFunction.md): Batches all the inputs tensors to the computation done by the function.

[`BatchIFFT(...)`](../../../tf/raw_ops/BatchIFFT.md)

[`BatchIFFT2D(...)`](../../../tf/raw_ops/BatchIFFT2D.md)

[`BatchIFFT3D(...)`](../../../tf/raw_ops/BatchIFFT3D.md)

[`BatchMatMul(...)`](../../../tf/raw_ops/BatchMatMul.md): Multiplies slices of two tensors in batches.

[`BatchMatMulV2(...)`](../../../tf/raw_ops/BatchMatMulV2.md): Multiplies slices of two tensors in batches.

[`BatchMatrixBandPart(...)`](../../../tf/raw_ops/BatchMatrixBandPart.md)

[`BatchMatrixDeterminant(...)`](../../../tf/raw_ops/BatchMatrixDeterminant.md)

[`BatchMatrixDiag(...)`](../../../tf/raw_ops/BatchMatrixDiag.md)

[`BatchMatrixDiagPart(...)`](../../../tf/raw_ops/BatchMatrixDiagPart.md)

[`BatchMatrixInverse(...)`](../../../tf/raw_ops/BatchMatrixInverse.md)

[`BatchMatrixSetDiag(...)`](../../../tf/raw_ops/BatchMatrixSetDiag.md)

[`BatchMatrixSolve(...)`](../../../tf/raw_ops/BatchMatrixSolve.md)

[`BatchMatrixSolveLs(...)`](../../../tf/raw_ops/BatchMatrixSolveLs.md)

[`BatchMatrixTriangularSolve(...)`](../../../tf/raw_ops/BatchMatrixTriangularSolve.md)

[`BatchNormWithGlobalNormalization(...)`](../../../tf/raw_ops/BatchNormWithGlobalNormalization.md): Batch normalization.

[`BatchNormWithGlobalNormalizationGrad(...)`](../../../tf/raw_ops/BatchNormWithGlobalNormalizationGrad.md): Gradients for batch normalization.

[`BatchSelfAdjointEig(...)`](../../../tf/raw_ops/BatchSelfAdjointEig.md)

[`BatchSelfAdjointEigV2(...)`](../../../tf/raw_ops/BatchSelfAdjointEigV2.md)

[`BatchSvd(...)`](../../../tf/raw_ops/BatchSvd.md)

[`BatchToSpace(...)`](../../../tf/raw_ops/BatchToSpace.md): BatchToSpace for 4-D tensors of type T.

[`BatchToSpaceND(...)`](../../../tf/raw_ops/BatchToSpaceND.md): BatchToSpace for N-D tensors of type T.

[`BesselI0e(...)`](../../../tf/raw_ops/BesselI0e.md): Computes the Bessel i0e function of `x` element-wise.

[`BesselI1e(...)`](../../../tf/raw_ops/BesselI1e.md): Computes the Bessel i1e function of `x` element-wise.

[`Betainc(...)`](../../../tf/raw_ops/Betainc.md): Compute the regularized incomplete beta integral \\(I_x(a, b)\\).

[`BiasAdd(...)`](../../../tf/raw_ops/BiasAdd.md): Adds `bias` to `value`.

[`BiasAddGrad(...)`](../../../tf/raw_ops/BiasAddGrad.md): The backward operation for "BiasAdd" on the "bias" tensor.

[`BiasAddV1(...)`](../../../tf/raw_ops/BiasAddV1.md): Adds `bias` to `value`.

[`Bincount(...)`](../../../tf/raw_ops/Bincount.md): Counts the number of occurrences of each value in an integer array.

[`Bitcast(...)`](../../../tf/raw_ops/Bitcast.md): Bitcasts a tensor from one type to another without copying data.

[`BitwiseAnd(...)`](../../../tf/raw_ops/BitwiseAnd.md): Elementwise computes the bitwise AND of `x` and `y`.

[`BitwiseOr(...)`](../../../tf/raw_ops/BitwiseOr.md): Elementwise computes the bitwise OR of `x` and `y`.

[`BitwiseXor(...)`](../../../tf/raw_ops/BitwiseXor.md): Elementwise computes the bitwise XOR of `x` and `y`.

[`BlockLSTM(...)`](../../../tf/raw_ops/BlockLSTM.md): Computes the LSTM cell forward propagation for all the time steps.

[`BlockLSTMGrad(...)`](../../../tf/raw_ops/BlockLSTMGrad.md): Computes the LSTM cell backward propagation for the entire time sequence.

[`BlockLSTMGradV2(...)`](../../../tf/raw_ops/BlockLSTMGradV2.md): Computes the LSTM cell backward propagation for the entire time sequence.

[`BlockLSTMV2(...)`](../../../tf/raw_ops/BlockLSTMV2.md): Computes the LSTM cell forward propagation for all the time steps.

[`BoostedTreesAggregateStats(...)`](../../../tf/raw_ops/BoostedTreesAggregateStats.md): Aggregates the summary of accumulated stats for the batch.

[`BoostedTreesBucketize(...)`](../../../tf/raw_ops/BoostedTreesBucketize.md): Bucketize each feature based on bucket boundaries.

[`BoostedTreesCalculateBestFeatureSplit(...)`](../../../tf/raw_ops/BoostedTreesCalculateBestFeatureSplit.md): Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesCalculateBestFeatureSplitV2(...)`](../../../tf/raw_ops/BoostedTreesCalculateBestFeatureSplitV2.md): Calculates gains for each feature and returns the best possible split information for each node. However, if no split is found, then no split information is returned for that node.

[`BoostedTreesCalculateBestGainsPerFeature(...)`](../../../tf/raw_ops/BoostedTreesCalculateBestGainsPerFeature.md): Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesCenterBias(...)`](../../../tf/raw_ops/BoostedTreesCenterBias.md): Calculates the prior from the training data (the bias) and fills in the first node with the logits' prior. Returns a boolean indicating whether to continue centering.

[`BoostedTreesCreateEnsemble(...)`](../../../tf/raw_ops/BoostedTreesCreateEnsemble.md): Creates a tree ensemble model and returns a handle to it.

[`BoostedTreesCreateQuantileStreamResource(...)`](../../../tf/raw_ops/BoostedTreesCreateQuantileStreamResource.md): Create the Resource for Quantile Streams.

[`BoostedTreesDeserializeEnsemble(...)`](../../../tf/raw_ops/BoostedTreesDeserializeEnsemble.md): Deserializes a serialized tree ensemble config and replaces current tree

[`BoostedTreesEnsembleResourceHandleOp(...)`](../../../tf/raw_ops/BoostedTreesEnsembleResourceHandleOp.md): Creates a handle to a BoostedTreesEnsembleResource

[`BoostedTreesExampleDebugOutputs(...)`](../../../tf/raw_ops/BoostedTreesExampleDebugOutputs.md): Debugging/model interpretability outputs for each example.

[`BoostedTreesFlushQuantileSummaries(...)`](../../../tf/raw_ops/BoostedTreesFlushQuantileSummaries.md): Flush the quantile summaries from each quantile stream resource.

[`BoostedTreesGetEnsembleStates(...)`](../../../tf/raw_ops/BoostedTreesGetEnsembleStates.md): Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

[`BoostedTreesMakeQuantileSummaries(...)`](../../../tf/raw_ops/BoostedTreesMakeQuantileSummaries.md): Makes the summary of quantiles for the batch.

[`BoostedTreesMakeStatsSummary(...)`](../../../tf/raw_ops/BoostedTreesMakeStatsSummary.md): Makes the summary of accumulated stats for the batch.

[`BoostedTreesPredict(...)`](../../../tf/raw_ops/BoostedTreesPredict.md): Runs multiple additive regression ensemble predictors on input instances and

[`BoostedTreesQuantileStreamResourceAddSummaries(...)`](../../../tf/raw_ops/BoostedTreesQuantileStreamResourceAddSummaries.md): Add the quantile summaries to each quantile stream resource.

[`BoostedTreesQuantileStreamResourceDeserialize(...)`](../../../tf/raw_ops/BoostedTreesQuantileStreamResourceDeserialize.md): Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

[`BoostedTreesQuantileStreamResourceFlush(...)`](../../../tf/raw_ops/BoostedTreesQuantileStreamResourceFlush.md): Flush the summaries for a quantile stream resource.

[`BoostedTreesQuantileStreamResourceGetBucketBoundaries(...)`](../../../tf/raw_ops/BoostedTreesQuantileStreamResourceGetBucketBoundaries.md): Generate the bucket boundaries for each feature based on accumulated summaries.

[`BoostedTreesQuantileStreamResourceHandleOp(...)`](../../../tf/raw_ops/BoostedTreesQuantileStreamResourceHandleOp.md): Creates a handle to a BoostedTreesQuantileStreamResource.

[`BoostedTreesSerializeEnsemble(...)`](../../../tf/raw_ops/BoostedTreesSerializeEnsemble.md): Serializes the tree ensemble to a proto.

[`BoostedTreesSparseAggregateStats(...)`](../../../tf/raw_ops/BoostedTreesSparseAggregateStats.md): Aggregates the summary of accumulated stats for the batch.

[`BoostedTreesSparseCalculateBestFeatureSplit(...)`](../../../tf/raw_ops/BoostedTreesSparseCalculateBestFeatureSplit.md): Calculates gains for each feature and returns the best possible split information for the feature.

[`BoostedTreesTrainingPredict(...)`](../../../tf/raw_ops/BoostedTreesTrainingPredict.md): Runs multiple additive regression ensemble predictors on input instances and

[`BoostedTreesUpdateEnsemble(...)`](../../../tf/raw_ops/BoostedTreesUpdateEnsemble.md): Updates the tree ensemble by either adding a layer to the last tree being grown

[`BoostedTreesUpdateEnsembleV2(...)`](../../../tf/raw_ops/BoostedTreesUpdateEnsembleV2.md): Updates the tree ensemble by adding a layer to the last tree being grown

[`BroadcastArgs(...)`](../../../tf/raw_ops/BroadcastArgs.md): Return the shape of s0 op s1 with broadcast.

[`BroadcastGradientArgs(...)`](../../../tf/raw_ops/BroadcastGradientArgs.md): Return the reduction indices for computing gradients of s0 op s1 with broadcast.

[`BroadcastTo(...)`](../../../tf/raw_ops/BroadcastTo.md): Broadcast an array for a compatible shape.

[`Bucketize(...)`](../../../tf/raw_ops/Bucketize.md): Bucketizes 'input' based on 'boundaries'.

[`BytesProducedStatsDataset(...)`](../../../tf/raw_ops/BytesProducedStatsDataset.md): Records the bytes size of each element of `input_dataset` in a StatsAggregator.

[`CSRSparseMatrixComponents(...)`](../../../tf/raw_ops/CSRSparseMatrixComponents.md): Reads out the CSR components at batch `index`.

[`CSRSparseMatrixToDense(...)`](../../../tf/raw_ops/CSRSparseMatrixToDense.md): Convert a (possibly batched) CSRSparseMatrix to dense.

[`CSRSparseMatrixToSparseTensor(...)`](../../../tf/raw_ops/CSRSparseMatrixToSparseTensor.md): Converts a (possibly batched) CSRSparesMatrix to a SparseTensor.

[`CSVDataset(...)`](../../../tf/raw_ops/CSVDataset.md)

[`CTCBeamSearchDecoder(...)`](../../../tf/raw_ops/CTCBeamSearchDecoder.md): Performs beam search decoding on the logits given in input.

[`CTCGreedyDecoder(...)`](../../../tf/raw_ops/CTCGreedyDecoder.md): Performs greedy decoding on the logits given in inputs.

[`CTCLoss(...)`](../../../tf/raw_ops/CTCLoss.md): Calculates the CTC Loss (log probability) for each batch entry.  Also calculates

[`CTCLossV2(...)`](../../../tf/raw_ops/CTCLossV2.md): Calculates the CTC Loss (log probability) for each batch entry.  Also calculates

[`CacheDataset(...)`](../../../tf/raw_ops/CacheDataset.md): Creates a dataset that caches elements from `input_dataset`.

[`CacheDatasetV2(...)`](../../../tf/raw_ops/CacheDatasetV2.md)

[`Case(...)`](../../../tf/raw_ops/Case.md): An n-way switch statement which calls a single branch function.

[`Cast(...)`](../../../tf/raw_ops/Cast.md): Cast x of type SrcT to y of DstT.

[`Ceil(...)`](../../../tf/raw_ops/Ceil.md): Returns element-wise smallest integer not less than x.

[`CheckNumerics(...)`](../../../tf/raw_ops/CheckNumerics.md): Checks a tensor for NaN and Inf values.

[`CheckNumericsV2(...)`](../../../tf/raw_ops/CheckNumericsV2.md): Checks a tensor for NaN, -Inf and +Inf values.

[`Cholesky(...)`](../../../tf/raw_ops/Cholesky.md): Computes the Cholesky decomposition of one or more square matrices.

[`CholeskyGrad(...)`](../../../tf/raw_ops/CholeskyGrad.md): Computes the reverse mode backpropagated gradient of the Cholesky algorithm.

[`ChooseFastestBranchDataset(...)`](../../../tf/raw_ops/ChooseFastestBranchDataset.md)

[`ChooseFastestDataset(...)`](../../../tf/raw_ops/ChooseFastestDataset.md)

[`ClipByValue(...)`](../../../tf/raw_ops/ClipByValue.md): Clips tensor values to a specified min and max.

[`CloseSummaryWriter(...)`](../../../tf/raw_ops/CloseSummaryWriter.md)

[`CollectiveBcastRecv(...)`](../../../tf/raw_ops/CollectiveBcastRecv.md): Receives a tensor value broadcast from another device.

[`CollectiveBcastSend(...)`](../../../tf/raw_ops/CollectiveBcastSend.md): Broadcasts a tensor value to one or more other devices.

[`CollectiveGather(...)`](../../../tf/raw_ops/CollectiveGather.md): Mutually accumulates multiple tensors of identical type and shape.

[`CollectivePermute(...)`](../../../tf/raw_ops/CollectivePermute.md): An Op to permute tensors across replicated TPU instances.

[`CollectiveReduce(...)`](../../../tf/raw_ops/CollectiveReduce.md): Mutually reduces multiple tensors of identical type and shape.

[`CombinedNonMaxSuppression(...)`](../../../tf/raw_ops/CombinedNonMaxSuppression.md): Greedily selects a subset of bounding boxes in descending order of score,

[`CompareAndBitpack(...)`](../../../tf/raw_ops/CompareAndBitpack.md): Compare values of `input` to `threshold` and pack resulting bits into a `uint8`.

[`Complex(...)`](../../../tf/raw_ops/Complex.md): Converts two real numbers to a complex number.

[`ComplexAbs(...)`](../../../tf/raw_ops/ComplexAbs.md): Computes the complex absolute value of a tensor.

[`ComputeAccidentalHits(...)`](../../../tf/raw_ops/ComputeAccidentalHits.md): Computes the ids of the positions in sampled_candidates that match true_labels.

[`Concat(...)`](../../../tf/raw_ops/Concat.md): Concatenates tensors along one dimension.

[`ConcatOffset(...)`](../../../tf/raw_ops/ConcatOffset.md): Computes offsets of concat inputs within its output.

[`ConcatV2(...)`](../../../tf/raw_ops/ConcatV2.md): Concatenates tensors along one dimension.

[`ConcatenateDataset(...)`](../../../tf/raw_ops/ConcatenateDataset.md): Creates a dataset that concatenates `input_dataset` with `another_dataset`.

[`ConditionalAccumulator(...)`](../../../tf/raw_ops/ConditionalAccumulator.md): A conditional accumulator for aggregating gradients.

[`ConfigureDistributedTPU(...)`](../../../tf/raw_ops/ConfigureDistributedTPU.md): Sets up the centralized structures for a distributed TPU system.

[`ConfigureTPUEmbedding(...)`](../../../tf/raw_ops/ConfigureTPUEmbedding.md): Sets up TPUEmbedding in a distributed TPU system.

[`Conj(...)`](../../../tf/raw_ops/Conj.md): Returns the complex conjugate of a complex number.

[`ConjugateTranspose(...)`](../../../tf/raw_ops/ConjugateTranspose.md): Shuffle dimensions of x according to a permutation and conjugate the result.

[`Const(...)`](../../../tf/raw_ops/Const.md): Returns a constant tensor.

[`ConsumeMutexLock(...)`](../../../tf/raw_ops/ConsumeMutexLock.md): This op consumes a lock created by `MutexLock`.

[`ControlTrigger(...)`](../../../tf/raw_ops/ControlTrigger.md): Does nothing. Serves as a control trigger for scheduling.

[`Conv2D(...)`](../../../tf/raw_ops/Conv2D.md): Computes a 2-D convolution given 4-D `input` and `filter` tensors.

[`Conv2DBackpropFilter(...)`](../../../tf/raw_ops/Conv2DBackpropFilter.md): Computes the gradients of convolution with respect to the filter.

[`Conv2DBackpropInput(...)`](../../../tf/raw_ops/Conv2DBackpropInput.md): Computes the gradients of convolution with respect to the input.

[`Conv3D(...)`](../../../tf/raw_ops/Conv3D.md): Computes a 3-D convolution given 5-D `input` and `filter` tensors.

[`Conv3DBackpropFilter(...)`](../../../tf/raw_ops/Conv3DBackpropFilter.md): Computes the gradients of 3-D convolution with respect to the filter.

[`Conv3DBackpropFilterV2(...)`](../../../tf/raw_ops/Conv3DBackpropFilterV2.md): Computes the gradients of 3-D convolution with respect to the filter.

[`Conv3DBackpropInput(...)`](../../../tf/raw_ops/Conv3DBackpropInput.md): Computes the gradients of 3-D convolution with respect to the input.

[`Conv3DBackpropInputV2(...)`](../../../tf/raw_ops/Conv3DBackpropInputV2.md): Computes the gradients of 3-D convolution with respect to the input.

[`Copy(...)`](../../../tf/raw_ops/Copy.md): Copy a tensor from CPU-to-CPU or GPU-to-GPU.

[`CopyHost(...)`](../../../tf/raw_ops/CopyHost.md): Copy a tensor to host.

[`Cos(...)`](../../../tf/raw_ops/Cos.md): Computes cos of x element-wise.

[`Cosh(...)`](../../../tf/raw_ops/Cosh.md): Computes hyperbolic cosine of x element-wise.

[`CountUpTo(...)`](../../../tf/raw_ops/CountUpTo.md): Increments 'ref' until it reaches 'limit'.

[`CreateSummaryDbWriter(...)`](../../../tf/raw_ops/CreateSummaryDbWriter.md)

[`CreateSummaryFileWriter(...)`](../../../tf/raw_ops/CreateSummaryFileWriter.md)

[`CropAndResize(...)`](../../../tf/raw_ops/CropAndResize.md): Extracts crops from the input image tensor and resizes them.

[`CropAndResizeGradBoxes(...)`](../../../tf/raw_ops/CropAndResizeGradBoxes.md): Computes the gradient of the crop_and_resize op wrt the input boxes tensor.

[`CropAndResizeGradImage(...)`](../../../tf/raw_ops/CropAndResizeGradImage.md): Computes the gradient of the crop_and_resize op wrt the input image tensor.

[`Cross(...)`](../../../tf/raw_ops/Cross.md): Compute the pairwise cross product.

[`CrossReplicaSum(...)`](../../../tf/raw_ops/CrossReplicaSum.md): An Op to sum inputs across replicated TPU instances.

[`CudnnRNN(...)`](../../../tf/raw_ops/CudnnRNN.md): A RNN backed by cuDNN.

[`CudnnRNNBackprop(...)`](../../../tf/raw_ops/CudnnRNNBackprop.md): Backprop step of CudnnRNN.

[`CudnnRNNBackpropV2(...)`](../../../tf/raw_ops/CudnnRNNBackpropV2.md): Backprop step of CudnnRNN.

[`CudnnRNNBackpropV3(...)`](../../../tf/raw_ops/CudnnRNNBackpropV3.md): Backprop step of CudnnRNNV3.

[`CudnnRNNCanonicalToParams(...)`](../../../tf/raw_ops/CudnnRNNCanonicalToParams.md): Converts CudnnRNN params from canonical form to usable form.

[`CudnnRNNCanonicalToParamsV2(...)`](../../../tf/raw_ops/CudnnRNNCanonicalToParamsV2.md): Converts CudnnRNN params from canonical form to usable form. It supports the projection in LSTM.

[`CudnnRNNParamsSize(...)`](../../../tf/raw_ops/CudnnRNNParamsSize.md): Computes size of weights that can be used by a Cudnn RNN model.

[`CudnnRNNParamsToCanonical(...)`](../../../tf/raw_ops/CudnnRNNParamsToCanonical.md): Retrieves CudnnRNN params in canonical form.

[`CudnnRNNParamsToCanonicalV2(...)`](../../../tf/raw_ops/CudnnRNNParamsToCanonicalV2.md): Retrieves CudnnRNN params in canonical form. It supports the projection in LSTM.

[`CudnnRNNV2(...)`](../../../tf/raw_ops/CudnnRNNV2.md): A RNN backed by cuDNN.

[`CudnnRNNV3(...)`](../../../tf/raw_ops/CudnnRNNV3.md): A RNN backed by cuDNN.

[`Cumprod(...)`](../../../tf/raw_ops/Cumprod.md): Compute the cumulative product of the tensor `x` along `axis`.

[`Cumsum(...)`](../../../tf/raw_ops/Cumsum.md): Compute the cumulative sum of the tensor `x` along `axis`.

[`CumulativeLogsumexp(...)`](../../../tf/raw_ops/CumulativeLogsumexp.md): Compute the cumulative product of the tensor `x` along `axis`.

[`DataFormatDimMap(...)`](../../../tf/raw_ops/DataFormatDimMap.md): Returns the dimension index in the destination data format given the one in

[`DataFormatVecPermute(...)`](../../../tf/raw_ops/DataFormatVecPermute.md): Returns the permuted vector/tensor in the destination data format given the

[`DatasetCardinality(...)`](../../../tf/raw_ops/DatasetCardinality.md): Returns the cardinality of `input_dataset`.

[`DatasetFromGraph(...)`](../../../tf/raw_ops/DatasetFromGraph.md): Creates a dataset from the given `graph_def`.

[`DatasetToGraph(...)`](../../../tf/raw_ops/DatasetToGraph.md): Returns a serialized GraphDef representing `input_dataset`.

[`DatasetToGraphV2(...)`](../../../tf/raw_ops/DatasetToGraphV2.md): Returns a serialized GraphDef representing `input_dataset`.

[`DatasetToSingleElement(...)`](../../../tf/raw_ops/DatasetToSingleElement.md): Outputs the single element from the given dataset.

[`DatasetToTFRecord(...)`](../../../tf/raw_ops/DatasetToTFRecord.md): Writes the given dataset to the given file using the TFRecord format.

[`Dawsn(...)`](../../../tf/raw_ops/Dawsn.md)

[`DebugGradientIdentity(...)`](../../../tf/raw_ops/DebugGradientIdentity.md): Identity op for gradient debugging.

[`DebugGradientRefIdentity(...)`](../../../tf/raw_ops/DebugGradientRefIdentity.md): Identity op for gradient debugging.

[`DebugIdentity(...)`](../../../tf/raw_ops/DebugIdentity.md): Provides an identity mapping of the non-Ref type input tensor for debugging.

[`DebugIdentityV2(...)`](../../../tf/raw_ops/DebugIdentityV2.md): Debug Identity V2 Op.

[`DebugNanCount(...)`](../../../tf/raw_ops/DebugNanCount.md): Debug NaN Value Counter Op.

[`DebugNumericSummary(...)`](../../../tf/raw_ops/DebugNumericSummary.md): Debug Numeric Summary Op.

[`DebugNumericSummaryV2(...)`](../../../tf/raw_ops/DebugNumericSummaryV2.md): Debug Numeric Summary V2 Op.

[`DecodeAndCropJpeg(...)`](../../../tf/raw_ops/DecodeAndCropJpeg.md): Decode and Crop a JPEG-encoded image to a uint8 tensor.

[`DecodeBase64(...)`](../../../tf/raw_ops/DecodeBase64.md): Decode web-safe base64-encoded strings.

[`DecodeBmp(...)`](../../../tf/raw_ops/DecodeBmp.md): Decode the first frame of a BMP-encoded image to a uint8 tensor.

[`DecodeCSV(...)`](../../../tf/raw_ops/DecodeCSV.md): Convert CSV records to tensors. Each column maps to one tensor.

[`DecodeCompressed(...)`](../../../tf/raw_ops/DecodeCompressed.md): Decompress strings.

[`DecodeGif(...)`](../../../tf/raw_ops/DecodeGif.md): Decode the frame(s) of a GIF-encoded image to a uint8 tensor.

[`DecodeJSONExample(...)`](../../../tf/raw_ops/DecodeJSONExample.md): Convert JSON-encoded Example records to binary protocol buffer strings.

[`DecodeJpeg(...)`](../../../tf/raw_ops/DecodeJpeg.md): Decode a JPEG-encoded image to a uint8 tensor.

[`DecodePaddedRaw(...)`](../../../tf/raw_ops/DecodePaddedRaw.md): Reinterpret the bytes of a string as a vector of numbers.

[`DecodePng(...)`](../../../tf/raw_ops/DecodePng.md): Decode a PNG-encoded image to a uint8 or uint16 tensor.

[`DecodeProtoV2(...)`](../../../tf/raw_ops/DecodeProtoV2.md): The op extracts fields from a serialized protocol buffers message into tensors.

[`DecodeRaw(...)`](../../../tf/raw_ops/DecodeRaw.md): Reinterpret the bytes of a string as a vector of numbers.

[`DecodeWav(...)`](../../../tf/raw_ops/DecodeWav.md): Decode a 16-bit PCM WAV file to a float tensor.

[`DeepCopy(...)`](../../../tf/raw_ops/DeepCopy.md): Makes a copy of `x`.

[`DeleteIterator(...)`](../../../tf/raw_ops/DeleteIterator.md): A container for an iterator resource.

[`DeleteMemoryCache(...)`](../../../tf/raw_ops/DeleteMemoryCache.md)

[`DeleteMultiDeviceIterator(...)`](../../../tf/raw_ops/DeleteMultiDeviceIterator.md): A container for an iterator resource.

[`DeleteRandomSeedGenerator(...)`](../../../tf/raw_ops/DeleteRandomSeedGenerator.md)

[`DeleteSessionTensor(...)`](../../../tf/raw_ops/DeleteSessionTensor.md): Delete the tensor specified by its handle in the session.

[`DenseToCSRSparseMatrix(...)`](../../../tf/raw_ops/DenseToCSRSparseMatrix.md): Converts a dense tensor to a (possibly batched) CSRSparseMatrix.

[`DenseToDenseSetOperation(...)`](../../../tf/raw_ops/DenseToDenseSetOperation.md): Applies set operation along last dimension of 2 `Tensor` inputs.

[`DenseToSparseBatchDataset(...)`](../../../tf/raw_ops/DenseToSparseBatchDataset.md): Creates a dataset that batches input elements into a SparseTensor.

[`DenseToSparseSetOperation(...)`](../../../tf/raw_ops/DenseToSparseSetOperation.md): Applies set operation along last dimension of `Tensor` and `SparseTensor`.

[`DepthToSpace(...)`](../../../tf/raw_ops/DepthToSpace.md): DepthToSpace for tensors of type T.

[`DepthwiseConv2dNative(...)`](../../../tf/raw_ops/DepthwiseConv2dNative.md): Computes a 2-D depthwise convolution given 4-D `input` and `filter` tensors.

[`DepthwiseConv2dNativeBackpropFilter(...)`](../../../tf/raw_ops/DepthwiseConv2dNativeBackpropFilter.md): Computes the gradients of depthwise convolution with respect to the filter.

[`DepthwiseConv2dNativeBackpropInput(...)`](../../../tf/raw_ops/DepthwiseConv2dNativeBackpropInput.md): Computes the gradients of depthwise convolution with respect to the input.

[`Dequantize(...)`](../../../tf/raw_ops/Dequantize.md): Dequantize the 'input' tensor into a float or bfloat16 Tensor.

[`DeserializeIterator(...)`](../../../tf/raw_ops/DeserializeIterator.md): Converts the given variant tensor to an iterator and stores it in the given resource.

[`DeserializeManySparse(...)`](../../../tf/raw_ops/DeserializeManySparse.md): Deserialize and concatenate `SparseTensors` from a serialized minibatch.

[`DeserializeSparse(...)`](../../../tf/raw_ops/DeserializeSparse.md): Deserialize `SparseTensor` objects.

[`DestroyResourceOp(...)`](../../../tf/raw_ops/DestroyResourceOp.md): Deletes the resource specified by the handle.

[`DestroyTemporaryVariable(...)`](../../../tf/raw_ops/DestroyTemporaryVariable.md): Destroys the temporary variable and returns its final value.

[`Diag(...)`](../../../tf/raw_ops/Diag.md): Returns a diagonal tensor with a given diagonal values.

[`DiagPart(...)`](../../../tf/raw_ops/DiagPart.md): Returns the diagonal part of the tensor.

[`Digamma(...)`](../../../tf/raw_ops/Digamma.md): Computes Psi, the derivative of Lgamma (the log of the absolute value of

[`Dilation2D(...)`](../../../tf/raw_ops/Dilation2D.md): Computes the grayscale dilation of 4-D `input` and 3-D `filter` tensors.

[`Dilation2DBackpropFilter(...)`](../../../tf/raw_ops/Dilation2DBackpropFilter.md): Computes the gradient of morphological 2-D dilation with respect to the filter.

[`Dilation2DBackpropInput(...)`](../../../tf/raw_ops/Dilation2DBackpropInput.md): Computes the gradient of morphological 2-D dilation with respect to the input.

[`DirectedInterleaveDataset(...)`](../../../tf/raw_ops/DirectedInterleaveDataset.md): A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

[`Div(...)`](../../../tf/raw_ops/Div.md): Returns x / y element-wise.

[`DivNoNan(...)`](../../../tf/raw_ops/DivNoNan.md): Returns 0 if the denominator is zero.

[`DrawBoundingBoxes(...)`](../../../tf/raw_ops/DrawBoundingBoxes.md): Draw bounding boxes on a batch of images.

[`DrawBoundingBoxesV2(...)`](../../../tf/raw_ops/DrawBoundingBoxesV2.md): Draw bounding boxes on a batch of images.

[`DummyMemoryCache(...)`](../../../tf/raw_ops/DummyMemoryCache.md)

[`DynamicPartition(...)`](../../../tf/raw_ops/DynamicPartition.md): Partitions `data` into `num_partitions` tensors using indices from `partitions`.

[`DynamicStitch(...)`](../../../tf/raw_ops/DynamicStitch.md): Interleave the values from the `data` tensors into a single tensor.

[`EagerPyFunc(...)`](../../../tf/raw_ops/EagerPyFunc.md): Eagerly executes a python function to compute func(input)->output. The

[`EditDistance(...)`](../../../tf/raw_ops/EditDistance.md): Computes the (possibly normalized) Levenshtein Edit Distance.

[`Eig(...)`](../../../tf/raw_ops/Eig.md): Computes the eigen decomposition of one or more square matrices.

[`Einsum(...)`](../../../tf/raw_ops/Einsum.md): Tensor contraction according to Einstein summation convention.

[`Elu(...)`](../../../tf/raw_ops/Elu.md): Computes exponential linear: `exp(features) - 1` if < 0, `features` otherwise.

[`EluGrad(...)`](../../../tf/raw_ops/EluGrad.md): Computes gradients for the exponential linear (Elu) operation.

[`Empty(...)`](../../../tf/raw_ops/Empty.md): Creates a tensor with the given shape.

[`EmptyTensorList(...)`](../../../tf/raw_ops/EmptyTensorList.md): Creates and returns an empty tensor list.

[`EncodeBase64(...)`](../../../tf/raw_ops/EncodeBase64.md): Encode strings into web-safe base64 format.

[`EncodeJpeg(...)`](../../../tf/raw_ops/EncodeJpeg.md): JPEG-encode an image.

[`EncodeJpegVariableQuality(...)`](../../../tf/raw_ops/EncodeJpegVariableQuality.md): JPEG encode input image with provided compression quality.

[`EncodePng(...)`](../../../tf/raw_ops/EncodePng.md): PNG-encode an image.

[`EncodeProto(...)`](../../../tf/raw_ops/EncodeProto.md): The op serializes protobuf messages provided in the input tensors.

[`EncodeWav(...)`](../../../tf/raw_ops/EncodeWav.md): Encode audio data using the WAV file format.

[`EnqueueTPUEmbeddingIntegerBatch(...)`](../../../tf/raw_ops/EnqueueTPUEmbeddingIntegerBatch.md): An op that enqueues a list of input batch tensors to TPUEmbedding.

[`EnqueueTPUEmbeddingSparseBatch(...)`](../../../tf/raw_ops/EnqueueTPUEmbeddingSparseBatch.md): An op that enqueues TPUEmbedding input indices from a SparseTensor.

[`EnqueueTPUEmbeddingSparseTensorBatch(...)`](../../../tf/raw_ops/EnqueueTPUEmbeddingSparseTensorBatch.md): Eases the porting of code that uses tf.nn.embedding_lookup_sparse().

[`EnsureShape(...)`](../../../tf/raw_ops/EnsureShape.md): Ensures that the tensor's shape matches the expected shape.

[`Enter(...)`](../../../tf/raw_ops/Enter.md): Creates or finds a child frame, and makes `data` available to the child frame.

[`Equal(...)`](../../../tf/raw_ops/Equal.md): Returns the truth value of (x == y) element-wise.

[`Erf(...)`](../../../tf/raw_ops/Erf.md): Computes the Gauss error function of `x` element-wise.

[`Erfc(...)`](../../../tf/raw_ops/Erfc.md): Computes the complementary error function of `x` element-wise.

[`Erfinv(...)`](../../../tf/raw_ops/Erfinv.md)

[`EuclideanNorm(...)`](../../../tf/raw_ops/EuclideanNorm.md): Computes the euclidean norm of elements across dimensions of a tensor.

[`Exit(...)`](../../../tf/raw_ops/Exit.md): Exits the current frame to its parent frame.

[`Exp(...)`](../../../tf/raw_ops/Exp.md): Computes exponential of x element-wise.  \\(y = e^x\\).

[`ExpandDims(...)`](../../../tf/raw_ops/ExpandDims.md): Inserts a dimension of 1 into a tensor's shape.

[`ExperimentalAssertNextDataset(...)`](../../../tf/raw_ops/ExperimentalAssertNextDataset.md)

[`ExperimentalAutoShardDataset(...)`](../../../tf/raw_ops/ExperimentalAutoShardDataset.md): Creates a dataset that shards the input dataset.

[`ExperimentalBytesProducedStatsDataset(...)`](../../../tf/raw_ops/ExperimentalBytesProducedStatsDataset.md): Records the bytes size of each element of `input_dataset` in a StatsAggregator.

[`ExperimentalCSVDataset(...)`](../../../tf/raw_ops/ExperimentalCSVDataset.md)

[`ExperimentalChooseFastestDataset(...)`](../../../tf/raw_ops/ExperimentalChooseFastestDataset.md)

[`ExperimentalDatasetCardinality(...)`](../../../tf/raw_ops/ExperimentalDatasetCardinality.md): Returns the cardinality of `input_dataset`.

[`ExperimentalDatasetToTFRecord(...)`](../../../tf/raw_ops/ExperimentalDatasetToTFRecord.md): Writes the given dataset to the given file using the TFRecord format.

[`ExperimentalDenseToSparseBatchDataset(...)`](../../../tf/raw_ops/ExperimentalDenseToSparseBatchDataset.md): Creates a dataset that batches input elements into a SparseTensor.

[`ExperimentalDirectedInterleaveDataset(...)`](../../../tf/raw_ops/ExperimentalDirectedInterleaveDataset.md): A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

[`ExperimentalGroupByReducerDataset(...)`](../../../tf/raw_ops/ExperimentalGroupByReducerDataset.md): Creates a dataset that computes a group-by on `input_dataset`.

[`ExperimentalGroupByWindowDataset(...)`](../../../tf/raw_ops/ExperimentalGroupByWindowDataset.md): Creates a dataset that computes a windowed group-by on `input_dataset`.

[`ExperimentalIgnoreErrorsDataset(...)`](../../../tf/raw_ops/ExperimentalIgnoreErrorsDataset.md): Creates a dataset that contains the elements of `input_dataset` ignoring errors.

[`ExperimentalIteratorGetDevice(...)`](../../../tf/raw_ops/ExperimentalIteratorGetDevice.md): Returns the name of the device on which `resource` has been placed.

[`ExperimentalLMDBDataset(...)`](../../../tf/raw_ops/ExperimentalLMDBDataset.md)

[`ExperimentalLatencyStatsDataset(...)`](../../../tf/raw_ops/ExperimentalLatencyStatsDataset.md): Records the latency of producing `input_dataset` elements in a StatsAggregator.

[`ExperimentalMapAndBatchDataset(...)`](../../../tf/raw_ops/ExperimentalMapAndBatchDataset.md): Creates a dataset that fuses mapping with batching.

[`ExperimentalMapDataset(...)`](../../../tf/raw_ops/ExperimentalMapDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ExperimentalMatchingFilesDataset(...)`](../../../tf/raw_ops/ExperimentalMatchingFilesDataset.md)

[`ExperimentalMaxIntraOpParallelismDataset(...)`](../../../tf/raw_ops/ExperimentalMaxIntraOpParallelismDataset.md): Creates a dataset that overrides the maximum intra-op parallelism.

[`ExperimentalNonSerializableDataset(...)`](../../../tf/raw_ops/ExperimentalNonSerializableDataset.md)

[`ExperimentalParallelInterleaveDataset(...)`](../../../tf/raw_ops/ExperimentalParallelInterleaveDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ExperimentalParseExampleDataset(...)`](../../../tf/raw_ops/ExperimentalParseExampleDataset.md): Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ExperimentalPrivateThreadPoolDataset(...)`](../../../tf/raw_ops/ExperimentalPrivateThreadPoolDataset.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalRandomDataset(...)`](../../../tf/raw_ops/ExperimentalRandomDataset.md): Creates a Dataset that returns pseudorandom numbers.

[`ExperimentalRebatchDataset(...)`](../../../tf/raw_ops/ExperimentalRebatchDataset.md): Creates a dataset that changes the batch size.

[`ExperimentalScanDataset(...)`](../../../tf/raw_ops/ExperimentalScanDataset.md): Creates a dataset successively reduces `f` over the elements of `input_dataset`.

[`ExperimentalSetStatsAggregatorDataset(...)`](../../../tf/raw_ops/ExperimentalSetStatsAggregatorDataset.md)

[`ExperimentalSleepDataset(...)`](../../../tf/raw_ops/ExperimentalSleepDataset.md)

[`ExperimentalSlidingWindowDataset(...)`](../../../tf/raw_ops/ExperimentalSlidingWindowDataset.md): Creates a dataset that passes a sliding window over `input_dataset`.

[`ExperimentalSqlDataset(...)`](../../../tf/raw_ops/ExperimentalSqlDataset.md): Creates a dataset that executes a SQL query and emits rows of the result set.

[`ExperimentalStatsAggregatorHandle(...)`](../../../tf/raw_ops/ExperimentalStatsAggregatorHandle.md): Creates a statistics manager resource.

[`ExperimentalStatsAggregatorSummary(...)`](../../../tf/raw_ops/ExperimentalStatsAggregatorSummary.md): Produces a summary of any statistics recorded by the given statistics manager.

[`ExperimentalTakeWhileDataset(...)`](../../../tf/raw_ops/ExperimentalTakeWhileDataset.md): Creates a dataset that stops iteration when predicate` is false.

[`ExperimentalThreadPoolDataset(...)`](../../../tf/raw_ops/ExperimentalThreadPoolDataset.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalThreadPoolHandle(...)`](../../../tf/raw_ops/ExperimentalThreadPoolHandle.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ExperimentalUnbatchDataset(...)`](../../../tf/raw_ops/ExperimentalUnbatchDataset.md): A dataset that splits the elements of its input into multiple elements.

[`ExperimentalUniqueDataset(...)`](../../../tf/raw_ops/ExperimentalUniqueDataset.md): Creates a dataset that contains the unique elements of `input_dataset`.

[`Expint(...)`](../../../tf/raw_ops/Expint.md)

[`Expm1(...)`](../../../tf/raw_ops/Expm1.md): Computes `exp(x) - 1` element-wise.

[`ExtractGlimpse(...)`](../../../tf/raw_ops/ExtractGlimpse.md): Extracts a glimpse from the input tensor.

[`ExtractImagePatches(...)`](../../../tf/raw_ops/ExtractImagePatches.md): Extract `patches` from `images` and put them in the "depth" output dimension.

[`ExtractJpegShape(...)`](../../../tf/raw_ops/ExtractJpegShape.md): Extract the shape information of a JPEG-encoded image.

[`ExtractVolumePatches(...)`](../../../tf/raw_ops/ExtractVolumePatches.md): Extract `patches` from `input` and put them in the "depth" output dimension. 3D extension of `extract_image_patches`.

[`FFT(...)`](../../../tf/raw_ops/FFT.md): Fast Fourier transform.

[`FFT2D(...)`](../../../tf/raw_ops/FFT2D.md): 2D fast Fourier transform.

[`FFT3D(...)`](../../../tf/raw_ops/FFT3D.md): 3D fast Fourier transform.

[`FIFOQueue(...)`](../../../tf/raw_ops/FIFOQueue.md): A queue that produces elements in first-in first-out order.

[`FIFOQueueV2(...)`](../../../tf/raw_ops/FIFOQueueV2.md): A queue that produces elements in first-in first-out order.

[`Fact(...)`](../../../tf/raw_ops/Fact.md): Output a fact about factorials.

[`FakeParam(...)`](../../../tf/raw_ops/FakeParam.md): This op is used as a placeholder in If branch functions. It doesn't provide a

[`FakeQuantWithMinMaxArgs(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxArgs.md): Fake-quantize the 'inputs' tensor, type float to 'outputs' tensor of same type.

[`FakeQuantWithMinMaxArgsGradient(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxArgsGradient.md): Compute gradients for a FakeQuantWithMinMaxArgs operation.

[`FakeQuantWithMinMaxVars(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxVars.md): Fake-quantize the 'inputs' tensor of type float via global float scalars `min`

[`FakeQuantWithMinMaxVarsGradient(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxVarsGradient.md): Compute gradients for a FakeQuantWithMinMaxVars operation.

[`FakeQuantWithMinMaxVarsPerChannel(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxVarsPerChannel.md): Fake-quantize the 'inputs' tensor of type float and one of the shapes: `[d]`,

[`FakeQuantWithMinMaxVarsPerChannelGradient(...)`](../../../tf/raw_ops/FakeQuantWithMinMaxVarsPerChannelGradient.md): Compute gradients for a FakeQuantWithMinMaxVarsPerChannel operation.

[`FakeQueue(...)`](../../../tf/raw_ops/FakeQueue.md): Deprecated. Do not use.

[`Fill(...)`](../../../tf/raw_ops/Fill.md): Creates a tensor filled with a scalar value.

[`FilterByLastComponentDataset(...)`](../../../tf/raw_ops/FilterByLastComponentDataset.md): Creates a dataset containing elements of first component of `input_dataset` having true in the last component.

[`FilterDataset(...)`](../../../tf/raw_ops/FilterDataset.md): Creates a dataset containing elements of `input_dataset` matching `predicate`.

[`Fingerprint(...)`](../../../tf/raw_ops/Fingerprint.md): Generates fingerprint values.

[`FixedLengthRecordDataset(...)`](../../../tf/raw_ops/FixedLengthRecordDataset.md): Creates a dataset that emits the records from one or more binary files.

[`FixedLengthRecordDatasetV2(...)`](../../../tf/raw_ops/FixedLengthRecordDatasetV2.md)

[`FixedLengthRecordReader(...)`](../../../tf/raw_ops/FixedLengthRecordReader.md): A Reader that outputs fixed-length records from a file.

[`FixedLengthRecordReaderV2(...)`](../../../tf/raw_ops/FixedLengthRecordReaderV2.md): A Reader that outputs fixed-length records from a file.

[`FixedUnigramCandidateSampler(...)`](../../../tf/raw_ops/FixedUnigramCandidateSampler.md): Generates labels for candidate sampling with a learned unigram distribution.

[`FlatMapDataset(...)`](../../../tf/raw_ops/FlatMapDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Floor(...)`](../../../tf/raw_ops/Floor.md): Returns element-wise largest integer not greater than x.

[`FloorDiv(...)`](../../../tf/raw_ops/FloorDiv.md): Returns x // y element-wise.

[`FloorMod(...)`](../../../tf/raw_ops/FloorMod.md): Returns element-wise remainder of division. When `x < 0` xor `y < 0` is

[`FlushSummaryWriter(...)`](../../../tf/raw_ops/FlushSummaryWriter.md)

[`For(...)`](../../../tf/raw_ops/For.md): ```python

[`FractionalAvgPool(...)`](../../../tf/raw_ops/FractionalAvgPool.md): Performs fractional average pooling on the input.

[`FractionalAvgPoolGrad(...)`](../../../tf/raw_ops/FractionalAvgPoolGrad.md): Computes gradient of the FractionalAvgPool function.

[`FractionalMaxPool(...)`](../../../tf/raw_ops/FractionalMaxPool.md): Performs fractional max pooling on the input.

[`FractionalMaxPoolGrad(...)`](../../../tf/raw_ops/FractionalMaxPoolGrad.md): Computes gradient of the FractionalMaxPool function.

[`FresnelCos(...)`](../../../tf/raw_ops/FresnelCos.md)

[`FresnelSin(...)`](../../../tf/raw_ops/FresnelSin.md)

[`FusedBatchNorm(...)`](../../../tf/raw_ops/FusedBatchNorm.md): Batch normalization.

[`FusedBatchNormGrad(...)`](../../../tf/raw_ops/FusedBatchNormGrad.md): Gradient for batch normalization.

[`FusedBatchNormGradV2(...)`](../../../tf/raw_ops/FusedBatchNormGradV2.md): Gradient for batch normalization.

[`FusedBatchNormGradV3(...)`](../../../tf/raw_ops/FusedBatchNormGradV3.md): Gradient for batch normalization.

[`FusedBatchNormV2(...)`](../../../tf/raw_ops/FusedBatchNormV2.md): Batch normalization.

[`FusedBatchNormV3(...)`](../../../tf/raw_ops/FusedBatchNormV3.md): Batch normalization.

[`FusedPadConv2D(...)`](../../../tf/raw_ops/FusedPadConv2D.md): Performs a padding as a preprocess during a convolution.

[`FusedResizeAndPadConv2D(...)`](../../../tf/raw_ops/FusedResizeAndPadConv2D.md): Performs a resize and padding as a preprocess during a convolution.

[`GRUBlockCell(...)`](../../../tf/raw_ops/GRUBlockCell.md): Computes the GRU cell forward propagation for 1 time step.

[`GRUBlockCellGrad(...)`](../../../tf/raw_ops/GRUBlockCellGrad.md): Computes the GRU cell back-propagation for 1 time step.

[`Gather(...)`](../../../tf/raw_ops/Gather.md): Gather slices from `params` according to `indices`.

[`GatherNd(...)`](../../../tf/raw_ops/GatherNd.md): Gather slices from `params` into a Tensor with shape specified by `indices`.

[`GatherV2(...)`](../../../tf/raw_ops/GatherV2.md): Gather slices from `params` axis `axis` according to `indices`.

[`GenerateBoundingBoxProposals(...)`](../../../tf/raw_ops/GenerateBoundingBoxProposals.md): This op produces Region of Interests from given bounding boxes(bbox_deltas) encoded wrt anchors according to eq.2 in arXiv:1506.01497

[`GenerateVocabRemapping(...)`](../../../tf/raw_ops/GenerateVocabRemapping.md): Given a path to new and old vocabulary files, returns a remapping Tensor of

[`GeneratorDataset(...)`](../../../tf/raw_ops/GeneratorDataset.md): Creates a dataset that invokes a function to generate elements.

[`GetSessionHandle(...)`](../../../tf/raw_ops/GetSessionHandle.md): Store the input tensor in the state of the current session.

[`GetSessionHandleV2(...)`](../../../tf/raw_ops/GetSessionHandleV2.md): Store the input tensor in the state of the current session.

[`GetSessionTensor(...)`](../../../tf/raw_ops/GetSessionTensor.md): Get the value of the tensor specified by its handle.

[`Greater(...)`](../../../tf/raw_ops/Greater.md): Returns the truth value of (x > y) element-wise.

[`GreaterEqual(...)`](../../../tf/raw_ops/GreaterEqual.md): Returns the truth value of (x >= y) element-wise.

[`GroupByReducerDataset(...)`](../../../tf/raw_ops/GroupByReducerDataset.md): Creates a dataset that computes a group-by on `input_dataset`.

[`GroupByWindowDataset(...)`](../../../tf/raw_ops/GroupByWindowDataset.md): Creates a dataset that computes a windowed group-by on `input_dataset`.

[`GuaranteeConst(...)`](../../../tf/raw_ops/GuaranteeConst.md): Gives a guarantee to the TF runtime that the input tensor is a constant.

[`HSVToRGB(...)`](../../../tf/raw_ops/HSVToRGB.md): Convert one or more images from HSV to RGB.

[`HashTable(...)`](../../../tf/raw_ops/HashTable.md): Creates a non-initialized hash table.

[`HashTableV2(...)`](../../../tf/raw_ops/HashTableV2.md): Creates a non-initialized hash table.

[`HistogramFixedWidth(...)`](../../../tf/raw_ops/HistogramFixedWidth.md): Return histogram of values.

[`HistogramSummary(...)`](../../../tf/raw_ops/HistogramSummary.md): Outputs a `Summary` protocol buffer with a histogram.

[`IFFT(...)`](../../../tf/raw_ops/IFFT.md): Inverse fast Fourier transform.

[`IFFT2D(...)`](../../../tf/raw_ops/IFFT2D.md): Inverse 2D fast Fourier transform.

[`IFFT3D(...)`](../../../tf/raw_ops/IFFT3D.md): Inverse 3D fast Fourier transform.

[`IRFFT(...)`](../../../tf/raw_ops/IRFFT.md): Inverse real-valued fast Fourier transform.

[`IRFFT2D(...)`](../../../tf/raw_ops/IRFFT2D.md): Inverse 2D real-valued fast Fourier transform.

[`IRFFT3D(...)`](../../../tf/raw_ops/IRFFT3D.md): Inverse 3D real-valued fast Fourier transform.

[`Identity(...)`](../../../tf/raw_ops/Identity.md): Return a tensor with the same shape and contents as the input tensor or value.

[`IdentityN(...)`](../../../tf/raw_ops/IdentityN.md): Returns a list of tensors with the same shapes and contents as the input

[`IdentityReader(...)`](../../../tf/raw_ops/IdentityReader.md): A Reader that outputs the queued work as both the key and value.

[`IdentityReaderV2(...)`](../../../tf/raw_ops/IdentityReaderV2.md): A Reader that outputs the queued work as both the key and value.

[`If(...)`](../../../tf/raw_ops/If.md): output = cond ? then_branch(input) : else_branch(input)

[`Igamma(...)`](../../../tf/raw_ops/Igamma.md): Compute the lower regularized incomplete Gamma function `P(a, x)`.

[`IgammaGradA(...)`](../../../tf/raw_ops/IgammaGradA.md): Computes the gradient of `igamma(a, x)` wrt `a`.

[`Igammac(...)`](../../../tf/raw_ops/Igammac.md): Compute the upper regularized incomplete Gamma function `Q(a, x)`.

[`IgnoreErrorsDataset(...)`](../../../tf/raw_ops/IgnoreErrorsDataset.md): Creates a dataset that contains the elements of `input_dataset` ignoring errors.

[`Imag(...)`](../../../tf/raw_ops/Imag.md): Returns the imaginary part of a complex number.

[`ImageProjectiveTransformV2(...)`](../../../tf/raw_ops/ImageProjectiveTransformV2.md): Applies the given transform to each of the images.

[`ImageSummary(...)`](../../../tf/raw_ops/ImageSummary.md): Outputs a `Summary` protocol buffer with images.

[`ImmutableConst(...)`](../../../tf/raw_ops/ImmutableConst.md): Returns immutable tensor from memory region.

[`ImportEvent(...)`](../../../tf/raw_ops/ImportEvent.md)

[`InTopK(...)`](../../../tf/raw_ops/InTopK.md): Says whether the targets are in the top `K` predictions.

[`InTopKV2(...)`](../../../tf/raw_ops/InTopKV2.md): Says whether the targets are in the top `K` predictions.

[`InfeedDequeue(...)`](../../../tf/raw_ops/InfeedDequeue.md): A placeholder op for a value that will be fed into the computation.

[`InfeedDequeueTuple(...)`](../../../tf/raw_ops/InfeedDequeueTuple.md): Fetches multiple values from infeed as an XLA tuple.

[`InfeedEnqueue(...)`](../../../tf/raw_ops/InfeedEnqueue.md): An op which feeds a single Tensor value into the computation.

[`InfeedEnqueuePrelinearizedBuffer(...)`](../../../tf/raw_ops/InfeedEnqueuePrelinearizedBuffer.md): An op which enqueues prelinearized buffer into TPU infeed.

[`InfeedEnqueueTuple(...)`](../../../tf/raw_ops/InfeedEnqueueTuple.md): Feeds multiple Tensor values into the computation as an XLA tuple.

[`InitializeTable(...)`](../../../tf/raw_ops/InitializeTable.md): Table initializer that takes two tensors for keys and values respectively.

[`InitializeTableFromTextFile(...)`](../../../tf/raw_ops/InitializeTableFromTextFile.md): Initializes a table from a text file.

[`InitializeTableFromTextFileV2(...)`](../../../tf/raw_ops/InitializeTableFromTextFileV2.md): Initializes a table from a text file.

[`InitializeTableV2(...)`](../../../tf/raw_ops/InitializeTableV2.md): Table initializer that takes two tensors for keys and values respectively.

[`InplaceAdd(...)`](../../../tf/raw_ops/InplaceAdd.md): Adds v into specified rows of x.

[`InplaceSub(...)`](../../../tf/raw_ops/InplaceSub.md): Subtracts `v` into specified rows of `x`.

[`InplaceUpdate(...)`](../../../tf/raw_ops/InplaceUpdate.md): Updates specified rows with values in `v`.

[`InterleaveDataset(...)`](../../../tf/raw_ops/InterleaveDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Inv(...)`](../../../tf/raw_ops/Inv.md): Computes the reciprocal of x element-wise.

[`InvGrad(...)`](../../../tf/raw_ops/InvGrad.md): Computes the gradient for the inverse of `x` wrt its input.

[`Invert(...)`](../../../tf/raw_ops/Invert.md): Invert (flip) each bit of supported types; for example, type `uint8` value 01010101 becomes 10101010.

[`InvertPermutation(...)`](../../../tf/raw_ops/InvertPermutation.md): Computes the inverse permutation of a tensor.

[`IsBoostedTreesEnsembleInitialized(...)`](../../../tf/raw_ops/IsBoostedTreesEnsembleInitialized.md): Checks whether a tree ensemble has been initialized.

[`IsBoostedTreesQuantileStreamResourceInitialized(...)`](../../../tf/raw_ops/IsBoostedTreesQuantileStreamResourceInitialized.md): Checks whether a quantile stream has been initialized.

[`IsFinite(...)`](../../../tf/raw_ops/IsFinite.md): Returns which elements of x are finite.

[`IsInf(...)`](../../../tf/raw_ops/IsInf.md): Returns which elements of x are Inf.

[`IsNan(...)`](../../../tf/raw_ops/IsNan.md): Returns which elements of x are NaN.

[`IsVariableInitialized(...)`](../../../tf/raw_ops/IsVariableInitialized.md): Checks whether a tensor has been initialized.

[`Iterator(...)`](../../../tf/raw_ops/Iterator.md): A container for an iterator resource.

[`IteratorFromStringHandle(...)`](../../../tf/raw_ops/IteratorFromStringHandle.md): Converts the given string representing a handle to an iterator to a resource.

[`IteratorFromStringHandleV2(...)`](../../../tf/raw_ops/IteratorFromStringHandleV2.md)

[`IteratorGetDevice(...)`](../../../tf/raw_ops/IteratorGetDevice.md): Returns the name of the device on which `resource` has been placed.

[`IteratorGetNext(...)`](../../../tf/raw_ops/IteratorGetNext.md): Gets the next output from the given iterator .

[`IteratorGetNextAsOptional(...)`](../../../tf/raw_ops/IteratorGetNextAsOptional.md): Gets the next output from the given iterator as an Optional variant.

[`IteratorGetNextSync(...)`](../../../tf/raw_ops/IteratorGetNextSync.md): Gets the next output from the given iterator.

[`IteratorToStringHandle(...)`](../../../tf/raw_ops/IteratorToStringHandle.md): Converts the given `resource_handle` representing an iterator to a string.

[`IteratorV2(...)`](../../../tf/raw_ops/IteratorV2.md)

[`L2Loss(...)`](../../../tf/raw_ops/L2Loss.md): L2 Loss.

[`LMDBDataset(...)`](../../../tf/raw_ops/LMDBDataset.md): Creates a dataset that emits the key-value pairs in one or more LMDB files.

[`LMDBReader(...)`](../../../tf/raw_ops/LMDBReader.md): A Reader that outputs the records from a LMDB file.

[`LRN(...)`](../../../tf/raw_ops/LRN.md): Local Response Normalization.

[`LRNGrad(...)`](../../../tf/raw_ops/LRNGrad.md): Gradients for Local Response Normalization.

[`LSTMBlockCell(...)`](../../../tf/raw_ops/LSTMBlockCell.md): Computes the LSTM cell forward propagation for 1 time step.

[`LSTMBlockCellGrad(...)`](../../../tf/raw_ops/LSTMBlockCellGrad.md): Computes the LSTM cell backward propagation for 1 timestep.

[`LatencyStatsDataset(...)`](../../../tf/raw_ops/LatencyStatsDataset.md): Records the latency of producing `input_dataset` elements in a StatsAggregator.

[`LeakyRelu(...)`](../../../tf/raw_ops/LeakyRelu.md): Computes rectified linear: `max(features, features * alpha)`.

[`LeakyReluGrad(...)`](../../../tf/raw_ops/LeakyReluGrad.md): Computes rectified linear gradients for a LeakyRelu operation.

[`LearnedUnigramCandidateSampler(...)`](../../../tf/raw_ops/LearnedUnigramCandidateSampler.md): Generates labels for candidate sampling with a learned unigram distribution.

[`LeftShift(...)`](../../../tf/raw_ops/LeftShift.md): Elementwise computes the bitwise left-shift of `x` and `y`.

[`LegacyParallelInterleaveDatasetV2(...)`](../../../tf/raw_ops/LegacyParallelInterleaveDatasetV2.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`Less(...)`](../../../tf/raw_ops/Less.md): Returns the truth value of (x < y) element-wise.

[`LessEqual(...)`](../../../tf/raw_ops/LessEqual.md): Returns the truth value of (x <= y) element-wise.

[`Lgamma(...)`](../../../tf/raw_ops/Lgamma.md): Computes the log of the absolute value of `Gamma(x)` element-wise.

[`LinSpace(...)`](../../../tf/raw_ops/LinSpace.md): Generates values in an interval.

[`ListDiff(...)`](../../../tf/raw_ops/ListDiff.md): Computes the difference between two lists of numbers or strings.

[`LoadAndRemapMatrix(...)`](../../../tf/raw_ops/LoadAndRemapMatrix.md): Loads a 2-D (matrix) `Tensor` with name `old_tensor_name` from the checkpoint

[`LoadTPUEmbeddingADAMParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingADAMParameters.md): Load ADAM embedding parameters.

[`LoadTPUEmbeddingADAMParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingADAMParametersGradAccumDebug.md): Load ADAM embedding parameters with debug support.

[`LoadTPUEmbeddingAdadeltaParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingAdadeltaParameters.md): Load Adadelta embedding parameters.

[`LoadTPUEmbeddingAdadeltaParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingAdadeltaParametersGradAccumDebug.md): Load Adadelta parameters with debug support.

[`LoadTPUEmbeddingAdagradParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingAdagradParameters.md): Load Adagrad embedding parameters.

[`LoadTPUEmbeddingAdagradParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingAdagradParametersGradAccumDebug.md): Load Adagrad embedding parameters with debug support.

[`LoadTPUEmbeddingCenteredRMSPropParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingCenteredRMSPropParameters.md): Load centered RMSProp embedding parameters.

[`LoadTPUEmbeddingFTRLParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingFTRLParameters.md): Load FTRL embedding parameters.

[`LoadTPUEmbeddingFTRLParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingFTRLParametersGradAccumDebug.md): Load FTRL embedding parameters with debug support.

[`LoadTPUEmbeddingMDLAdagradLightParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingMDLAdagradLightParameters.md): Load MDL Adagrad Light embedding parameters.

[`LoadTPUEmbeddingMomentumParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingMomentumParameters.md): Load Momentum embedding parameters.

[`LoadTPUEmbeddingMomentumParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingMomentumParametersGradAccumDebug.md): Load Momentum embedding parameters with debug support.

[`LoadTPUEmbeddingProximalAdagradParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingProximalAdagradParameters.md): Load proximal Adagrad embedding parameters.

[`LoadTPUEmbeddingProximalAdagradParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingProximalAdagradParametersGradAccumDebug.md): Load proximal Adagrad embedding parameters with debug support.

[`LoadTPUEmbeddingRMSPropParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingRMSPropParameters.md): Load RMSProp embedding parameters.

[`LoadTPUEmbeddingRMSPropParametersGradAccumDebug(...)`](../../../tf/raw_ops/LoadTPUEmbeddingRMSPropParametersGradAccumDebug.md): Load RMSProp embedding parameters with debug support.

[`LoadTPUEmbeddingStochasticGradientDescentParameters(...)`](../../../tf/raw_ops/LoadTPUEmbeddingStochasticGradientDescentParameters.md): Load SGD embedding parameters.

[`Log(...)`](../../../tf/raw_ops/Log.md): Computes natural logarithm of x element-wise.

[`Log1p(...)`](../../../tf/raw_ops/Log1p.md): Computes natural logarithm of (1 + x) element-wise.

[`LogMatrixDeterminant(...)`](../../../tf/raw_ops/LogMatrixDeterminant.md): Computes the sign and the log of the absolute value of the determinant of

[`LogSoftmax(...)`](../../../tf/raw_ops/LogSoftmax.md): Computes log softmax activations.

[`LogUniformCandidateSampler(...)`](../../../tf/raw_ops/LogUniformCandidateSampler.md): Generates labels for candidate sampling with a log-uniform distribution.

[`LogicalAnd(...)`](../../../tf/raw_ops/LogicalAnd.md): Returns the truth value of x AND y element-wise.

[`LogicalNot(...)`](../../../tf/raw_ops/LogicalNot.md): Returns the truth value of `NOT x` element-wise.

[`LogicalOr(...)`](../../../tf/raw_ops/LogicalOr.md): Returns the truth value of x OR y element-wise.

[`LookupTableExport(...)`](../../../tf/raw_ops/LookupTableExport.md): Outputs all keys and values in the table.

[`LookupTableExportV2(...)`](../../../tf/raw_ops/LookupTableExportV2.md): Outputs all keys and values in the table.

[`LookupTableFind(...)`](../../../tf/raw_ops/LookupTableFind.md): Looks up keys in a table, outputs the corresponding values.

[`LookupTableFindV2(...)`](../../../tf/raw_ops/LookupTableFindV2.md): Looks up keys in a table, outputs the corresponding values.

[`LookupTableImport(...)`](../../../tf/raw_ops/LookupTableImport.md): Replaces the contents of the table with the specified keys and values.

[`LookupTableImportV2(...)`](../../../tf/raw_ops/LookupTableImportV2.md): Replaces the contents of the table with the specified keys and values.

[`LookupTableInsert(...)`](../../../tf/raw_ops/LookupTableInsert.md): Updates the table to associates keys with values.

[`LookupTableInsertV2(...)`](../../../tf/raw_ops/LookupTableInsertV2.md): Updates the table to associates keys with values.

[`LookupTableRemoveV2(...)`](../../../tf/raw_ops/LookupTableRemoveV2.md): Removes keys and its associated values from a table.

[`LookupTableSize(...)`](../../../tf/raw_ops/LookupTableSize.md): Computes the number of elements in the given table.

[`LookupTableSizeV2(...)`](../../../tf/raw_ops/LookupTableSizeV2.md): Computes the number of elements in the given table.

[`LoopCond(...)`](../../../tf/raw_ops/LoopCond.md): Forwards the input to the output.

[`LowerBound(...)`](../../../tf/raw_ops/LowerBound.md): Applies lower_bound(sorted_search_values, values) along each row.

[`Lu(...)`](../../../tf/raw_ops/Lu.md): Computes the LU decomposition of one or more square matrices.

[`MakeIterator(...)`](../../../tf/raw_ops/MakeIterator.md): Makes a new iterator from the given `dataset` and stores it in `iterator`.

[`MapAndBatchDataset(...)`](../../../tf/raw_ops/MapAndBatchDataset.md): Creates a dataset that fuses mapping with batching.

[`MapClear(...)`](../../../tf/raw_ops/MapClear.md): Op removes all elements in the underlying container.

[`MapDataset(...)`](../../../tf/raw_ops/MapDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`MapDefun(...)`](../../../tf/raw_ops/MapDefun.md): Maps a function on the list of tensors unpacked from arguments on dimension 0.

[`MapIncompleteSize(...)`](../../../tf/raw_ops/MapIncompleteSize.md): Op returns the number of incomplete elements in the underlying container.

[`MapPeek(...)`](../../../tf/raw_ops/MapPeek.md): Op peeks at the values at the specified key.  If the

[`MapSize(...)`](../../../tf/raw_ops/MapSize.md): Op returns the number of elements in the underlying container.

[`MapStage(...)`](../../../tf/raw_ops/MapStage.md): Stage (key, values) in the underlying container which behaves like a hashtable.

[`MapUnstage(...)`](../../../tf/raw_ops/MapUnstage.md): Op removes and returns the values associated with the key

[`MapUnstageNoKey(...)`](../../../tf/raw_ops/MapUnstageNoKey.md): Op removes and returns a random (key, value)

[`MatMul(...)`](../../../tf/raw_ops/MatMul.md): Multiply the matrix "a" by the matrix "b".

[`MatchingFiles(...)`](../../../tf/raw_ops/MatchingFiles.md): Returns the set of files matching one or more glob patterns.

[`MatchingFilesDataset(...)`](../../../tf/raw_ops/MatchingFilesDataset.md)

[`MatrixBandPart(...)`](../../../tf/raw_ops/MatrixBandPart.md): Copy a tensor setting everything outside a central band in each innermost matrix

[`MatrixDeterminant(...)`](../../../tf/raw_ops/MatrixDeterminant.md): Computes the determinant of one or more square matrices.

[`MatrixDiag(...)`](../../../tf/raw_ops/MatrixDiag.md): Returns a batched diagonal tensor with a given batched diagonal values.

[`MatrixDiagPart(...)`](../../../tf/raw_ops/MatrixDiagPart.md): Returns the batched diagonal part of a batched tensor.

[`MatrixDiagPartV2(...)`](../../../tf/raw_ops/MatrixDiagPartV2.md): Returns the batched diagonal part of a batched tensor.

[`MatrixDiagPartV3(...)`](../../../tf/raw_ops/MatrixDiagPartV3.md): Returns the batched diagonal part of a batched tensor.

[`MatrixDiagV2(...)`](../../../tf/raw_ops/MatrixDiagV2.md): Returns a batched diagonal tensor with given batched diagonal values.

[`MatrixDiagV3(...)`](../../../tf/raw_ops/MatrixDiagV3.md): Returns a batched diagonal tensor with given batched diagonal values.

[`MatrixExponential(...)`](../../../tf/raw_ops/MatrixExponential.md): Deprecated, use python implementation tf.linalg.matrix_exponential.

[`MatrixInverse(...)`](../../../tf/raw_ops/MatrixInverse.md): Computes the inverse of one or more square invertible matrices or their

[`MatrixLogarithm(...)`](../../../tf/raw_ops/MatrixLogarithm.md): Computes the matrix logarithm of one or more square matrices:

[`MatrixSetDiag(...)`](../../../tf/raw_ops/MatrixSetDiag.md): Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSetDiagV2(...)`](../../../tf/raw_ops/MatrixSetDiagV2.md): Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSetDiagV3(...)`](../../../tf/raw_ops/MatrixSetDiagV3.md): Returns a batched matrix tensor with new batched diagonal values.

[`MatrixSolve(...)`](../../../tf/raw_ops/MatrixSolve.md): Solves systems of linear equations.

[`MatrixSolveLs(...)`](../../../tf/raw_ops/MatrixSolveLs.md): Solves one or more linear least-squares problems.

[`MatrixSquareRoot(...)`](../../../tf/raw_ops/MatrixSquareRoot.md): Computes the matrix square root of one or more square matrices:

[`MatrixTriangularSolve(...)`](../../../tf/raw_ops/MatrixTriangularSolve.md): Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

[`Max(...)`](../../../tf/raw_ops/Max.md): Computes the maximum of elements across dimensions of a tensor.

[`MaxIntraOpParallelismDataset(...)`](../../../tf/raw_ops/MaxIntraOpParallelismDataset.md): Creates a dataset that overrides the maximum intra-op parallelism.

[`MaxPool(...)`](../../../tf/raw_ops/MaxPool.md): Performs max pooling on the input.

[`MaxPool3D(...)`](../../../tf/raw_ops/MaxPool3D.md): Performs 3D max pooling on the input.

[`MaxPool3DGrad(...)`](../../../tf/raw_ops/MaxPool3DGrad.md): Computes gradients of max pooling function.

[`MaxPool3DGradGrad(...)`](../../../tf/raw_ops/MaxPool3DGradGrad.md): Computes second-order gradients of the maxpooling function.

[`MaxPoolGrad(...)`](../../../tf/raw_ops/MaxPoolGrad.md): Computes gradients of the maxpooling function.

[`MaxPoolGradGrad(...)`](../../../tf/raw_ops/MaxPoolGradGrad.md): Computes second-order gradients of the maxpooling function.

[`MaxPoolGradGradV2(...)`](../../../tf/raw_ops/MaxPoolGradGradV2.md): Computes second-order gradients of the maxpooling function.

[`MaxPoolGradGradWithArgmax(...)`](../../../tf/raw_ops/MaxPoolGradGradWithArgmax.md): Computes second-order gradients of the maxpooling function.

[`MaxPoolGradV2(...)`](../../../tf/raw_ops/MaxPoolGradV2.md): Computes gradients of the maxpooling function.

[`MaxPoolGradWithArgmax(...)`](../../../tf/raw_ops/MaxPoolGradWithArgmax.md): Computes gradients of the maxpooling function.

[`MaxPoolV2(...)`](../../../tf/raw_ops/MaxPoolV2.md): Performs max pooling on the input.

[`MaxPoolWithArgmax(...)`](../../../tf/raw_ops/MaxPoolWithArgmax.md): Performs max pooling on the input and outputs both max values and indices.

[`Maximum(...)`](../../../tf/raw_ops/Maximum.md): Returns the max of x and y (i.e. x > y ? x : y) element-wise.

[`Mean(...)`](../../../tf/raw_ops/Mean.md): Computes the mean of elements across dimensions of a tensor.

[`Merge(...)`](../../../tf/raw_ops/Merge.md): Forwards the value of an available tensor from `inputs` to `output`.

[`MergeSummary(...)`](../../../tf/raw_ops/MergeSummary.md): Merges summaries.

[`MergeV2Checkpoints(...)`](../../../tf/raw_ops/MergeV2Checkpoints.md): V2 format specific: merges the metadata files of sharded checkpoints.  The

[`Mfcc(...)`](../../../tf/raw_ops/Mfcc.md): Transforms a spectrogram into a form that's useful for speech recognition.

[`Min(...)`](../../../tf/raw_ops/Min.md): Computes the minimum of elements across dimensions of a tensor.

[`Minimum(...)`](../../../tf/raw_ops/Minimum.md): Returns the min of x and y (i.e. x < y ? x : y) element-wise.

[`MirrorPad(...)`](../../../tf/raw_ops/MirrorPad.md): Pads a tensor with mirrored values.

[`MirrorPadGrad(...)`](../../../tf/raw_ops/MirrorPadGrad.md): Gradient op for `MirrorPad` op. This op folds a mirror-padded tensor.

[`Mod(...)`](../../../tf/raw_ops/Mod.md): Returns element-wise remainder of division. This emulates C semantics in that

[`ModelDataset(...)`](../../../tf/raw_ops/ModelDataset.md): Identity transformation that models performance.

[`Mul(...)`](../../../tf/raw_ops/Mul.md): Returns x * y element-wise.

[`MulNoNan(...)`](../../../tf/raw_ops/MulNoNan.md): Returns x * y element-wise. Returns zero if y is zero, even if x if infinite or NaN.

[`MultiDeviceIterator(...)`](../../../tf/raw_ops/MultiDeviceIterator.md): Creates a MultiDeviceIterator resource.

[`MultiDeviceIteratorFromStringHandle(...)`](../../../tf/raw_ops/MultiDeviceIteratorFromStringHandle.md): Generates a MultiDeviceIterator resource from its provided string handle.

[`MultiDeviceIteratorGetNextFromShard(...)`](../../../tf/raw_ops/MultiDeviceIteratorGetNextFromShard.md): Gets next element for the provided shard number.

[`MultiDeviceIteratorInit(...)`](../../../tf/raw_ops/MultiDeviceIteratorInit.md): Initializes the multi device iterator with the given dataset.

[`MultiDeviceIteratorToStringHandle(...)`](../../../tf/raw_ops/MultiDeviceIteratorToStringHandle.md): Produces a string handle for the given MultiDeviceIterator.

[`Multinomial(...)`](../../../tf/raw_ops/Multinomial.md): Draws samples from a multinomial distribution.

[`MutableDenseHashTable(...)`](../../../tf/raw_ops/MutableDenseHashTable.md): Creates an empty hash table that uses tensors as the backing store.

[`MutableDenseHashTableV2(...)`](../../../tf/raw_ops/MutableDenseHashTableV2.md): Creates an empty hash table that uses tensors as the backing store.

[`MutableHashTable(...)`](../../../tf/raw_ops/MutableHashTable.md): Creates an empty hash table.

[`MutableHashTableOfTensors(...)`](../../../tf/raw_ops/MutableHashTableOfTensors.md): Creates an empty hash table.

[`MutableHashTableOfTensorsV2(...)`](../../../tf/raw_ops/MutableHashTableOfTensorsV2.md): Creates an empty hash table.

[`MutableHashTableV2(...)`](../../../tf/raw_ops/MutableHashTableV2.md): Creates an empty hash table.

[`MutexLock(...)`](../../../tf/raw_ops/MutexLock.md): Locks a mutex resource.  The output is the lock.  So long as the lock tensor

[`MutexV2(...)`](../../../tf/raw_ops/MutexV2.md): Creates a Mutex resource that can be locked by `MutexLock`.

[`NcclAllReduce(...)`](../../../tf/raw_ops/NcclAllReduce.md): Outputs a tensor containing the reduction across all input tensors.

[`NcclBroadcast(...)`](../../../tf/raw_ops/NcclBroadcast.md): Sends `input` to all devices that are connected to the output.

[`NcclReduce(...)`](../../../tf/raw_ops/NcclReduce.md): Reduces `input` from `num_devices` using `reduction` to a single device.

[`Ndtri(...)`](../../../tf/raw_ops/Ndtri.md)

[`Neg(...)`](../../../tf/raw_ops/Neg.md): Computes numerical negative value element-wise.

[`NextAfter(...)`](../../../tf/raw_ops/NextAfter.md): Returns the next representable value of `x1` in the direction of `x2`, element-wise.

[`NextIteration(...)`](../../../tf/raw_ops/NextIteration.md): Makes its input available to the next iteration.

[`NoOp(...)`](../../../tf/raw_ops/NoOp.md): Does nothing. Only useful as a placeholder for control edges.

[`NonDeterministicInts(...)`](../../../tf/raw_ops/NonDeterministicInts.md): Non-deterministically generates some integers.

[`NonMaxSuppression(...)`](../../../tf/raw_ops/NonMaxSuppression.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV2(...)`](../../../tf/raw_ops/NonMaxSuppressionV2.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV3(...)`](../../../tf/raw_ops/NonMaxSuppressionV3.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV4(...)`](../../../tf/raw_ops/NonMaxSuppressionV4.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionV5(...)`](../../../tf/raw_ops/NonMaxSuppressionV5.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonMaxSuppressionWithOverlaps(...)`](../../../tf/raw_ops/NonMaxSuppressionWithOverlaps.md): Greedily selects a subset of bounding boxes in descending order of score,

[`NonSerializableDataset(...)`](../../../tf/raw_ops/NonSerializableDataset.md)

[`NotEqual(...)`](../../../tf/raw_ops/NotEqual.md): Returns the truth value of (x != y) element-wise.

[`NthElement(...)`](../../../tf/raw_ops/NthElement.md): Finds values of the `n`-th order statistic for the last dimension.

[`OneHot(...)`](../../../tf/raw_ops/OneHot.md): Returns a one-hot tensor.

[`OneShotIterator(...)`](../../../tf/raw_ops/OneShotIterator.md): Makes a "one-shot" iterator that can be iterated only once.

[`OnesLike(...)`](../../../tf/raw_ops/OnesLike.md): Returns a tensor of ones with the same shape and type as x.

[`OptimizeDataset(...)`](../../../tf/raw_ops/OptimizeDataset.md): Creates a dataset by applying optimizations to `input_dataset`.

[`OptionalFromValue(...)`](../../../tf/raw_ops/OptionalFromValue.md): Constructs an Optional variant from a tuple of tensors.

[`OptionalGetValue(...)`](../../../tf/raw_ops/OptionalGetValue.md): Returns the value stored in an Optional variant or raises an error if none exists.

[`OptionalHasValue(...)`](../../../tf/raw_ops/OptionalHasValue.md): Returns true if and only if the given Optional variant has a value.

[`OptionalNone(...)`](../../../tf/raw_ops/OptionalNone.md): Creates an Optional variant with no value.

[`OrderedMapClear(...)`](../../../tf/raw_ops/OrderedMapClear.md): Op removes all elements in the underlying container.

[`OrderedMapIncompleteSize(...)`](../../../tf/raw_ops/OrderedMapIncompleteSize.md): Op returns the number of incomplete elements in the underlying container.

[`OrderedMapPeek(...)`](../../../tf/raw_ops/OrderedMapPeek.md): Op peeks at the values at the specified key.  If the

[`OrderedMapSize(...)`](../../../tf/raw_ops/OrderedMapSize.md): Op returns the number of elements in the underlying container.

[`OrderedMapStage(...)`](../../../tf/raw_ops/OrderedMapStage.md): Stage (key, values) in the underlying container which behaves like a ordered

[`OrderedMapUnstage(...)`](../../../tf/raw_ops/OrderedMapUnstage.md): Op removes and returns the values associated with the key

[`OrderedMapUnstageNoKey(...)`](../../../tf/raw_ops/OrderedMapUnstageNoKey.md): Op removes and returns the (key, value) element with the smallest

[`OutfeedDequeue(...)`](../../../tf/raw_ops/OutfeedDequeue.md): Retrieves a single tensor from the computation outfeed.

[`OutfeedDequeueTuple(...)`](../../../tf/raw_ops/OutfeedDequeueTuple.md): Retrieve multiple values from the computation outfeed.

[`OutfeedEnqueue(...)`](../../../tf/raw_ops/OutfeedEnqueue.md): Enqueue a Tensor on the computation outfeed.

[`OutfeedEnqueueTuple(...)`](../../../tf/raw_ops/OutfeedEnqueueTuple.md): Enqueue multiple Tensor values on the computation outfeed.

[`Pack(...)`](../../../tf/raw_ops/Pack.md): Packs a list of `N` rank-`R` tensors into one rank-`(R+1)` tensor.

[`Pad(...)`](../../../tf/raw_ops/Pad.md): Pads a tensor with zeros.

[`PadV2(...)`](../../../tf/raw_ops/PadV2.md): Pads a tensor.

[`PaddedBatchDataset(...)`](../../../tf/raw_ops/PaddedBatchDataset.md): Creates a dataset that batches and pads `batch_size` elements from the input.

[`PaddedBatchDatasetV2(...)`](../../../tf/raw_ops/PaddedBatchDatasetV2.md): Creates a dataset that batches and pads `batch_size` elements from the input.

[`PaddingFIFOQueue(...)`](../../../tf/raw_ops/PaddingFIFOQueue.md): A queue that produces elements in first-in first-out order.

[`PaddingFIFOQueueV2(...)`](../../../tf/raw_ops/PaddingFIFOQueueV2.md): A queue that produces elements in first-in first-out order.

[`ParallelConcat(...)`](../../../tf/raw_ops/ParallelConcat.md): Concatenates a list of `N` tensors along the first dimension.

[`ParallelDynamicStitch(...)`](../../../tf/raw_ops/ParallelDynamicStitch.md): Interleave the values from the `data` tensors into a single tensor.

[`ParallelInterleaveDataset(...)`](../../../tf/raw_ops/ParallelInterleaveDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV2(...)`](../../../tf/raw_ops/ParallelInterleaveDatasetV2.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV3(...)`](../../../tf/raw_ops/ParallelInterleaveDatasetV3.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelInterleaveDatasetV4(...)`](../../../tf/raw_ops/ParallelInterleaveDatasetV4.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelMapDataset(...)`](../../../tf/raw_ops/ParallelMapDataset.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParallelMapDatasetV2(...)`](../../../tf/raw_ops/ParallelMapDatasetV2.md): Creates a dataset that applies `f` to the outputs of `input_dataset`.

[`ParameterizedTruncatedNormal(...)`](../../../tf/raw_ops/ParameterizedTruncatedNormal.md): Outputs random values from a normal distribution. The parameters may each be a

[`ParseExample(...)`](../../../tf/raw_ops/ParseExample.md): Transforms a vector of brain.Example protos (as strings) into typed tensors.

[`ParseExampleDataset(...)`](../../../tf/raw_ops/ParseExampleDataset.md): Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ParseExampleDatasetV2(...)`](../../../tf/raw_ops/ParseExampleDatasetV2.md): Transforms `input_dataset` containing `Example` protos as vectors of DT_STRING into a dataset of `Tensor` or `SparseTensor` objects representing the parsed features.

[`ParseExampleV2(...)`](../../../tf/raw_ops/ParseExampleV2.md): Transforms a vector of tf.Example protos (as strings) into typed tensors.

[`ParseSequenceExample(...)`](../../../tf/raw_ops/ParseSequenceExample.md): Transforms a vector of brain.SequenceExample protos (as strings) into typed tensors.

[`ParseSequenceExampleV2(...)`](../../../tf/raw_ops/ParseSequenceExampleV2.md): Transforms a vector of tf.io.SequenceExample protos (as strings) into

[`ParseSingleExample(...)`](../../../tf/raw_ops/ParseSingleExample.md): Transforms a tf.Example proto (as a string) into typed tensors.

[`ParseSingleSequenceExample(...)`](../../../tf/raw_ops/ParseSingleSequenceExample.md): Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

[`ParseTensor(...)`](../../../tf/raw_ops/ParseTensor.md): Transforms a serialized tensorflow.TensorProto proto into a Tensor.

[`PartitionedCall(...)`](../../../tf/raw_ops/PartitionedCall.md): returns `f(inputs)`, where `f`'s body is placed and partitioned.

[`Placeholder(...)`](../../../tf/raw_ops/Placeholder.md): A placeholder op for a value that will be fed into the computation.

[`PlaceholderV2(...)`](../../../tf/raw_ops/PlaceholderV2.md): A placeholder op for a value that will be fed into the computation.

[`PlaceholderWithDefault(...)`](../../../tf/raw_ops/PlaceholderWithDefault.md): A placeholder op that passes through `input` when its output is not fed.

[`Polygamma(...)`](../../../tf/raw_ops/Polygamma.md): Compute the polygamma function \\(\psi^{(n)}(x)\\).

[`PopulationCount(...)`](../../../tf/raw_ops/PopulationCount.md): Computes element-wise population count (a.k.a. popcount, bitsum, bitcount).

[`Pow(...)`](../../../tf/raw_ops/Pow.md): Computes the power of one value to another.

[`PrefetchDataset(...)`](../../../tf/raw_ops/PrefetchDataset.md): Creates a dataset that asynchronously prefetches elements from `input_dataset`.

[`Prelinearize(...)`](../../../tf/raw_ops/Prelinearize.md): An op which linearizes one Tensor value to an opaque variant tensor.

[`PrelinearizeTuple(...)`](../../../tf/raw_ops/PrelinearizeTuple.md): An op which linearizes multiple Tensor values to an opaque variant tensor.

[`PreventGradient(...)`](../../../tf/raw_ops/PreventGradient.md): An identity op that triggers an error if a gradient is requested.

[`Print(...)`](../../../tf/raw_ops/Print.md): Prints a list of tensors.

[`PrintV2(...)`](../../../tf/raw_ops/PrintV2.md): Prints a string scalar.

[`PriorityQueue(...)`](../../../tf/raw_ops/PriorityQueue.md): A queue that produces elements sorted by the first component value.

[`PriorityQueueV2(...)`](../../../tf/raw_ops/PriorityQueueV2.md): A queue that produces elements sorted by the first component value.

[`PrivateThreadPoolDataset(...)`](../../../tf/raw_ops/PrivateThreadPoolDataset.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`Prod(...)`](../../../tf/raw_ops/Prod.md): Computes the product of elements across dimensions of a tensor.

[`PyFunc(...)`](../../../tf/raw_ops/PyFunc.md): Invokes a python function to compute func(input)->output.

[`PyFuncStateless(...)`](../../../tf/raw_ops/PyFuncStateless.md): A stateless version of PyFunc.

[`Qr(...)`](../../../tf/raw_ops/Qr.md): Computes the QR decompositions of one or more matrices.

[`QuantizeAndDequantize(...)`](../../../tf/raw_ops/QuantizeAndDequantize.md): Use QuantizeAndDequantizeV2 instead.

[`QuantizeAndDequantizeV2(...)`](../../../tf/raw_ops/QuantizeAndDequantizeV2.md): Quantizes then dequantizes a tensor.

[`QuantizeAndDequantizeV3(...)`](../../../tf/raw_ops/QuantizeAndDequantizeV3.md): Quantizes then dequantizes a tensor.

[`QuantizeDownAndShrinkRange(...)`](../../../tf/raw_ops/QuantizeDownAndShrinkRange.md): Convert the quantized 'input' tensor into a lower-precision 'output', using the

[`QuantizeV2(...)`](../../../tf/raw_ops/QuantizeV2.md): Quantize the 'input' tensor of type float to 'output' tensor of type 'T'.

[`QuantizedAdd(...)`](../../../tf/raw_ops/QuantizedAdd.md): Returns x + y element-wise, working on quantized buffers.

[`QuantizedAvgPool(...)`](../../../tf/raw_ops/QuantizedAvgPool.md): Produces the average pool of the input tensor for quantized types.

[`QuantizedBatchNormWithGlobalNormalization(...)`](../../../tf/raw_ops/QuantizedBatchNormWithGlobalNormalization.md): Quantized Batch normalization.

[`QuantizedBiasAdd(...)`](../../../tf/raw_ops/QuantizedBiasAdd.md): Adds Tensor 'bias' to Tensor 'input' for Quantized types.

[`QuantizedConcat(...)`](../../../tf/raw_ops/QuantizedConcat.md): Concatenates quantized tensors along one dimension.

[`QuantizedConv2D(...)`](../../../tf/raw_ops/QuantizedConv2D.md): Computes a 2D convolution given quantized 4D input and filter tensors.

[`QuantizedConv2DAndRelu(...)`](../../../tf/raw_ops/QuantizedConv2DAndRelu.md)

[`QuantizedConv2DAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DAndReluAndRequantize.md)

[`QuantizedConv2DAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DAndRequantize.md)

[`QuantizedConv2DPerChannel(...)`](../../../tf/raw_ops/QuantizedConv2DPerChannel.md): Computes QuantizedConv2D per channel.

[`QuantizedConv2DWithBias(...)`](../../../tf/raw_ops/QuantizedConv2DWithBias.md)

[`QuantizedConv2DWithBiasAndRelu(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasAndRelu.md)

[`QuantizedConv2DWithBiasAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasAndReluAndRequantize.md)

[`QuantizedConv2DWithBiasAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasAndRequantize.md)

[`QuantizedConv2DWithBiasSignedSumAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasSignedSumAndReluAndRequantize.md)

[`QuantizedConv2DWithBiasSumAndRelu(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasSumAndRelu.md)

[`QuantizedConv2DWithBiasSumAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedConv2DWithBiasSumAndReluAndRequantize.md)

[`QuantizedDepthwiseConv2D(...)`](../../../tf/raw_ops/QuantizedDepthwiseConv2D.md): Computes quantized depthwise Conv2D.

[`QuantizedDepthwiseConv2DWithBias(...)`](../../../tf/raw_ops/QuantizedDepthwiseConv2DWithBias.md): Computes quantized depthwise Conv2D with Bias.

[`QuantizedDepthwiseConv2DWithBiasAndRelu(...)`](../../../tf/raw_ops/QuantizedDepthwiseConv2DWithBiasAndRelu.md): Computes quantized depthwise Conv2D with Bias and Relu.

[`QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedDepthwiseConv2DWithBiasAndReluAndRequantize.md): Computes quantized depthwise Conv2D with Bias, Relu and Requantize.

[`QuantizedInstanceNorm(...)`](../../../tf/raw_ops/QuantizedInstanceNorm.md): Quantized Instance normalization.

[`QuantizedMatMul(...)`](../../../tf/raw_ops/QuantizedMatMul.md): Perform a quantized matrix multiplication of  `a` by the matrix `b`.

[`QuantizedMatMulWithBias(...)`](../../../tf/raw_ops/QuantizedMatMulWithBias.md): Performs a quantized matrix multiplication of `a` by the matrix `b` with bias

[`QuantizedMatMulWithBiasAndDequantize(...)`](../../../tf/raw_ops/QuantizedMatMulWithBiasAndDequantize.md)

[`QuantizedMatMulWithBiasAndRelu(...)`](../../../tf/raw_ops/QuantizedMatMulWithBiasAndRelu.md): Perform a quantized matrix multiplication of  `a` by the matrix `b` with bias

[`QuantizedMatMulWithBiasAndReluAndRequantize(...)`](../../../tf/raw_ops/QuantizedMatMulWithBiasAndReluAndRequantize.md): Perform a quantized matrix multiplication of  `a` by the matrix `b` with bias

[`QuantizedMatMulWithBiasAndRequantize(...)`](../../../tf/raw_ops/QuantizedMatMulWithBiasAndRequantize.md)

[`QuantizedMaxPool(...)`](../../../tf/raw_ops/QuantizedMaxPool.md): Produces the max pool of the input tensor for quantized types.

[`QuantizedMul(...)`](../../../tf/raw_ops/QuantizedMul.md): Returns x * y element-wise, working on quantized buffers.

[`QuantizedRelu(...)`](../../../tf/raw_ops/QuantizedRelu.md): Computes Quantized Rectified Linear: `max(features, 0)`

[`QuantizedRelu6(...)`](../../../tf/raw_ops/QuantizedRelu6.md): Computes Quantized Rectified Linear 6: `min(max(features, 0), 6)`

[`QuantizedReluX(...)`](../../../tf/raw_ops/QuantizedReluX.md): Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

[`QuantizedReshape(...)`](../../../tf/raw_ops/QuantizedReshape.md): Reshapes a quantized tensor as per the Reshape op.

[`QuantizedResizeBilinear(...)`](../../../tf/raw_ops/QuantizedResizeBilinear.md): Resize quantized `images` to `size` using quantized bilinear interpolation.

[`QueueClose(...)`](../../../tf/raw_ops/QueueClose.md): Closes the given queue.

[`QueueCloseV2(...)`](../../../tf/raw_ops/QueueCloseV2.md): Closes the given queue.

[`QueueDequeue(...)`](../../../tf/raw_ops/QueueDequeue.md): Dequeues a tuple of one or more tensors from the given queue.

[`QueueDequeueMany(...)`](../../../tf/raw_ops/QueueDequeueMany.md): Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueManyV2(...)`](../../../tf/raw_ops/QueueDequeueManyV2.md): Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueUpTo(...)`](../../../tf/raw_ops/QueueDequeueUpTo.md): Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueUpToV2(...)`](../../../tf/raw_ops/QueueDequeueUpToV2.md): Dequeues `n` tuples of one or more tensors from the given queue.

[`QueueDequeueV2(...)`](../../../tf/raw_ops/QueueDequeueV2.md): Dequeues a tuple of one or more tensors from the given queue.

[`QueueEnqueue(...)`](../../../tf/raw_ops/QueueEnqueue.md): Enqueues a tuple of one or more tensors in the given queue.

[`QueueEnqueueMany(...)`](../../../tf/raw_ops/QueueEnqueueMany.md): Enqueues zero or more tuples of one or more tensors in the given queue.

[`QueueEnqueueManyV2(...)`](../../../tf/raw_ops/QueueEnqueueManyV2.md): Enqueues zero or more tuples of one or more tensors in the given queue.

[`QueueEnqueueV2(...)`](../../../tf/raw_ops/QueueEnqueueV2.md): Enqueues a tuple of one or more tensors in the given queue.

[`QueueIsClosed(...)`](../../../tf/raw_ops/QueueIsClosed.md): Returns true if queue is closed.

[`QueueIsClosedV2(...)`](../../../tf/raw_ops/QueueIsClosedV2.md): Returns true if queue is closed.

[`QueueSize(...)`](../../../tf/raw_ops/QueueSize.md): Computes the number of elements in the given queue.

[`QueueSizeV2(...)`](../../../tf/raw_ops/QueueSizeV2.md): Computes the number of elements in the given queue.

[`RFFT(...)`](../../../tf/raw_ops/RFFT.md): Real-valued fast Fourier transform.

[`RFFT2D(...)`](../../../tf/raw_ops/RFFT2D.md): 2D real-valued fast Fourier transform.

[`RFFT3D(...)`](../../../tf/raw_ops/RFFT3D.md): 3D real-valued fast Fourier transform.

[`RGBToHSV(...)`](../../../tf/raw_ops/RGBToHSV.md): Converts one or more images from RGB to HSV.

[`RaggedGather(...)`](../../../tf/raw_ops/RaggedGather.md): Gather ragged slices from `params` axis `0` according to `indices`.

[`RaggedRange(...)`](../../../tf/raw_ops/RaggedRange.md): Returns a `RaggedTensor` containing the specified sequences of numbers.

[`RaggedTensorFromVariant(...)`](../../../tf/raw_ops/RaggedTensorFromVariant.md): Decodes a `variant` Tensor into a `RaggedTensor`.

[`RaggedTensorToSparse(...)`](../../../tf/raw_ops/RaggedTensorToSparse.md): Converts a `RaggedTensor` into a `SparseTensor` with the same values.

[`RaggedTensorToTensor(...)`](../../../tf/raw_ops/RaggedTensorToTensor.md): Create a dense tensor from a ragged tensor, possibly altering its shape.

[`RaggedTensorToVariant(...)`](../../../tf/raw_ops/RaggedTensorToVariant.md): Encodes a `RaggedTensor` into a `variant` Tensor.

[`RandomCrop(...)`](../../../tf/raw_ops/RandomCrop.md): Randomly crop `image`.

[`RandomDataset(...)`](../../../tf/raw_ops/RandomDataset.md): Creates a Dataset that returns pseudorandom numbers.

[`RandomGamma(...)`](../../../tf/raw_ops/RandomGamma.md): Outputs random values from the Gamma distribution(s) described by alpha.

[`RandomGammaGrad(...)`](../../../tf/raw_ops/RandomGammaGrad.md): Computes the derivative of a Gamma random sample w.r.t. `alpha`.

[`RandomPoisson(...)`](../../../tf/raw_ops/RandomPoisson.md): Use RandomPoissonV2 instead.

[`RandomPoissonV2(...)`](../../../tf/raw_ops/RandomPoissonV2.md): Outputs random values from the Poisson distribution(s) described by rate.

[`RandomShuffle(...)`](../../../tf/raw_ops/RandomShuffle.md): Randomly shuffles a tensor along its first dimension.

[`RandomShuffleQueue(...)`](../../../tf/raw_ops/RandomShuffleQueue.md): A queue that randomizes the order of elements.

[`RandomShuffleQueueV2(...)`](../../../tf/raw_ops/RandomShuffleQueueV2.md): A queue that randomizes the order of elements.

[`RandomStandardNormal(...)`](../../../tf/raw_ops/RandomStandardNormal.md): Outputs random values from a normal distribution.

[`RandomUniform(...)`](../../../tf/raw_ops/RandomUniform.md): Outputs random values from a uniform distribution.

[`RandomUniformInt(...)`](../../../tf/raw_ops/RandomUniformInt.md): Outputs random integers from a uniform distribution.

[`Range(...)`](../../../tf/raw_ops/Range.md): Creates a sequence of numbers.

[`RangeDataset(...)`](../../../tf/raw_ops/RangeDataset.md): Creates a dataset with a range of values. Corresponds to python's xrange.

[`Rank(...)`](../../../tf/raw_ops/Rank.md): Returns the rank of a tensor.

[`ReadFile(...)`](../../../tf/raw_ops/ReadFile.md): Reads and outputs the entire contents of the input filename.

[`ReadVariableOp(...)`](../../../tf/raw_ops/ReadVariableOp.md): Reads the value of a variable.

[`ReaderNumRecordsProduced(...)`](../../../tf/raw_ops/ReaderNumRecordsProduced.md): Returns the number of records this Reader has produced.

[`ReaderNumRecordsProducedV2(...)`](../../../tf/raw_ops/ReaderNumRecordsProducedV2.md): Returns the number of records this Reader has produced.

[`ReaderNumWorkUnitsCompleted(...)`](../../../tf/raw_ops/ReaderNumWorkUnitsCompleted.md): Returns the number of work units this Reader has finished processing.

[`ReaderNumWorkUnitsCompletedV2(...)`](../../../tf/raw_ops/ReaderNumWorkUnitsCompletedV2.md): Returns the number of work units this Reader has finished processing.

[`ReaderRead(...)`](../../../tf/raw_ops/ReaderRead.md): Returns the next record (key, value pair) produced by a Reader.

[`ReaderReadUpTo(...)`](../../../tf/raw_ops/ReaderReadUpTo.md): Returns up to `num_records` (key, value) pairs produced by a Reader.

[`ReaderReadUpToV2(...)`](../../../tf/raw_ops/ReaderReadUpToV2.md): Returns up to `num_records` (key, value) pairs produced by a Reader.

[`ReaderReadV2(...)`](../../../tf/raw_ops/ReaderReadV2.md): Returns the next record (key, value pair) produced by a Reader.

[`ReaderReset(...)`](../../../tf/raw_ops/ReaderReset.md): Restore a Reader to its initial clean state.

[`ReaderResetV2(...)`](../../../tf/raw_ops/ReaderResetV2.md): Restore a Reader to its initial clean state.

[`ReaderRestoreState(...)`](../../../tf/raw_ops/ReaderRestoreState.md): Restore a reader to a previously saved state.

[`ReaderRestoreStateV2(...)`](../../../tf/raw_ops/ReaderRestoreStateV2.md): Restore a reader to a previously saved state.

[`ReaderSerializeState(...)`](../../../tf/raw_ops/ReaderSerializeState.md): Produce a string tensor that encodes the state of a Reader.

[`ReaderSerializeStateV2(...)`](../../../tf/raw_ops/ReaderSerializeStateV2.md): Produce a string tensor that encodes the state of a Reader.

[`Real(...)`](../../../tf/raw_ops/Real.md): Returns the real part of a complex number.

[`RealDiv(...)`](../../../tf/raw_ops/RealDiv.md): Returns x / y element-wise for real types.

[`RebatchDataset(...)`](../../../tf/raw_ops/RebatchDataset.md): Creates a dataset that changes the batch size.

[`Reciprocal(...)`](../../../tf/raw_ops/Reciprocal.md): Computes the reciprocal of x element-wise.

[`ReciprocalGrad(...)`](../../../tf/raw_ops/ReciprocalGrad.md): Computes the gradient for the inverse of `x` wrt its input.

[`RecordInput(...)`](../../../tf/raw_ops/RecordInput.md): Emits randomized records.

[`Recv(...)`](../../../tf/raw_ops/Recv.md): Receives the named tensor from send_device on recv_device.

[`RecvTPUEmbeddingActivations(...)`](../../../tf/raw_ops/RecvTPUEmbeddingActivations.md): An op that receives embedding activations on the TPU.

[`ReduceDataset(...)`](../../../tf/raw_ops/ReduceDataset.md): Reduces the input dataset to a singleton using a reduce function.

[`ReduceJoin(...)`](../../../tf/raw_ops/ReduceJoin.md): Joins a string Tensor across the given dimensions.

[`RefEnter(...)`](../../../tf/raw_ops/RefEnter.md): Creates or finds a child frame, and makes `data` available to the child frame.

[`RefExit(...)`](../../../tf/raw_ops/RefExit.md): Exits the current frame to its parent frame.

[`RefIdentity(...)`](../../../tf/raw_ops/RefIdentity.md): Return the same ref tensor as the input ref tensor.

[`RefMerge(...)`](../../../tf/raw_ops/RefMerge.md): Forwards the value of an available tensor from `inputs` to `output`.

[`RefNextIteration(...)`](../../../tf/raw_ops/RefNextIteration.md): Makes its input available to the next iteration.

[`RefSelect(...)`](../../../tf/raw_ops/RefSelect.md): Forwards the `index`th element of `inputs` to `output`.

[`RefSwitch(...)`](../../../tf/raw_ops/RefSwitch.md): Forwards the ref tensor `data` to the output port determined by `pred`.

[`RegexFullMatch(...)`](../../../tf/raw_ops/RegexFullMatch.md): Check if the input matches the regex pattern.

[`RegexReplace(...)`](../../../tf/raw_ops/RegexReplace.md): Replaces matches of the `pattern` regular expression in `input` with the

[`Relu(...)`](../../../tf/raw_ops/Relu.md): Computes rectified linear: `max(features, 0)`.

[`Relu6(...)`](../../../tf/raw_ops/Relu6.md): Computes rectified linear 6: `min(max(features, 0), 6)`.

[`Relu6Grad(...)`](../../../tf/raw_ops/Relu6Grad.md): Computes rectified linear 6 gradients for a Relu6 operation.

[`ReluGrad(...)`](../../../tf/raw_ops/ReluGrad.md): Computes rectified linear gradients for a Relu operation.

[`RemoteCall(...)`](../../../tf/raw_ops/RemoteCall.md): Runs function `f` on a remote device indicated by `target`.

[`RepeatDataset(...)`](../../../tf/raw_ops/RepeatDataset.md): Creates a dataset that emits the outputs of `input_dataset` `count` times.

[`RequantizationRange(...)`](../../../tf/raw_ops/RequantizationRange.md): Computes a range that covers the actual values present in a quantized tensor.

[`RequantizationRangePerChannel(...)`](../../../tf/raw_ops/RequantizationRangePerChannel.md): Computes requantization range per channel.

[`Requantize(...)`](../../../tf/raw_ops/Requantize.md): Converts the quantized `input` tensor into a lower-precision `output`.

[`RequantizePerChannel(...)`](../../../tf/raw_ops/RequantizePerChannel.md): Requantizes input with min and max values known per channel.

[`Reshape(...)`](../../../tf/raw_ops/Reshape.md): Reshapes a tensor.

[`ResizeArea(...)`](../../../tf/raw_ops/ResizeArea.md): Resize `images` to `size` using area interpolation.

[`ResizeBicubic(...)`](../../../tf/raw_ops/ResizeBicubic.md): Resize `images` to `size` using bicubic interpolation.

[`ResizeBicubicGrad(...)`](../../../tf/raw_ops/ResizeBicubicGrad.md): Computes the gradient of bicubic interpolation.

[`ResizeBilinear(...)`](../../../tf/raw_ops/ResizeBilinear.md): Resize `images` to `size` using bilinear interpolation.

[`ResizeBilinearGrad(...)`](../../../tf/raw_ops/ResizeBilinearGrad.md): Computes the gradient of bilinear interpolation.

[`ResizeNearestNeighbor(...)`](../../../tf/raw_ops/ResizeNearestNeighbor.md): Resize `images` to `size` using nearest neighbor interpolation.

[`ResizeNearestNeighborGrad(...)`](../../../tf/raw_ops/ResizeNearestNeighborGrad.md): Computes the gradient of nearest neighbor interpolation.

[`ResourceAccumulatorApplyGradient(...)`](../../../tf/raw_ops/ResourceAccumulatorApplyGradient.md): Applies a gradient to a given accumulator.

[`ResourceAccumulatorNumAccumulated(...)`](../../../tf/raw_ops/ResourceAccumulatorNumAccumulated.md): Returns the number of gradients aggregated in the given accumulators.

[`ResourceAccumulatorSetGlobalStep(...)`](../../../tf/raw_ops/ResourceAccumulatorSetGlobalStep.md): Updates the accumulator with a new value for global_step.

[`ResourceAccumulatorTakeGradient(...)`](../../../tf/raw_ops/ResourceAccumulatorTakeGradient.md): Extracts the average gradient in the given ConditionalAccumulator.

[`ResourceApplyAdaMax(...)`](../../../tf/raw_ops/ResourceApplyAdaMax.md): Update '*var' according to the AdaMax algorithm.

[`ResourceApplyAdadelta(...)`](../../../tf/raw_ops/ResourceApplyAdadelta.md): Update '*var' according to the adadelta scheme.

[`ResourceApplyAdagrad(...)`](../../../tf/raw_ops/ResourceApplyAdagrad.md): Update '*var' according to the adagrad scheme.

[`ResourceApplyAdagradDA(...)`](../../../tf/raw_ops/ResourceApplyAdagradDA.md): Update '*var' according to the proximal adagrad scheme.

[`ResourceApplyAdagradV2(...)`](../../../tf/raw_ops/ResourceApplyAdagradV2.md): Update '*var' according to the adagrad scheme.

[`ResourceApplyAdam(...)`](../../../tf/raw_ops/ResourceApplyAdam.md): Update '*var' according to the Adam algorithm.

[`ResourceApplyAdamWithAmsgrad(...)`](../../../tf/raw_ops/ResourceApplyAdamWithAmsgrad.md): Update '*var' according to the Adam algorithm.

[`ResourceApplyAddSign(...)`](../../../tf/raw_ops/ResourceApplyAddSign.md): Update '*var' according to the AddSign update.

[`ResourceApplyCenteredRMSProp(...)`](../../../tf/raw_ops/ResourceApplyCenteredRMSProp.md): Update '*var' according to the centered RMSProp algorithm.

[`ResourceApplyFtrl(...)`](../../../tf/raw_ops/ResourceApplyFtrl.md): Update '*var' according to the Ftrl-proximal scheme.

[`ResourceApplyFtrlV2(...)`](../../../tf/raw_ops/ResourceApplyFtrlV2.md): Update '*var' according to the Ftrl-proximal scheme.

[`ResourceApplyGradientDescent(...)`](../../../tf/raw_ops/ResourceApplyGradientDescent.md): Update '*var' by subtracting 'alpha' * 'delta' from it.

[`ResourceApplyKerasMomentum(...)`](../../../tf/raw_ops/ResourceApplyKerasMomentum.md): Update '*var' according to the momentum scheme.

[`ResourceApplyMomentum(...)`](../../../tf/raw_ops/ResourceApplyMomentum.md): Update '*var' according to the momentum scheme. Set use_nesterov = True if you

[`ResourceApplyPowerSign(...)`](../../../tf/raw_ops/ResourceApplyPowerSign.md): Update '*var' according to the AddSign update.

[`ResourceApplyProximalAdagrad(...)`](../../../tf/raw_ops/ResourceApplyProximalAdagrad.md): Update '*var' and '*accum' according to FOBOS with Adagrad learning rate.

[`ResourceApplyProximalGradientDescent(...)`](../../../tf/raw_ops/ResourceApplyProximalGradientDescent.md): Update '*var' as FOBOS algorithm with fixed learning rate.

[`ResourceApplyRMSProp(...)`](../../../tf/raw_ops/ResourceApplyRMSProp.md): Update '*var' according to the RMSProp algorithm.

[`ResourceConditionalAccumulator(...)`](../../../tf/raw_ops/ResourceConditionalAccumulator.md): A conditional accumulator for aggregating gradients.

[`ResourceCountUpTo(...)`](../../../tf/raw_ops/ResourceCountUpTo.md): Increments variable pointed to by 'resource' until it reaches 'limit'.

[`ResourceGather(...)`](../../../tf/raw_ops/ResourceGather.md): Gather slices from the variable pointed to by `resource` according to `indices`.

[`ResourceGatherNd(...)`](../../../tf/raw_ops/ResourceGatherNd.md)

[`ResourceScatterAdd(...)`](../../../tf/raw_ops/ResourceScatterAdd.md): Adds sparse updates to the variable referenced by `resource`.

[`ResourceScatterDiv(...)`](../../../tf/raw_ops/ResourceScatterDiv.md): Divides sparse updates into the variable referenced by `resource`.

[`ResourceScatterMax(...)`](../../../tf/raw_ops/ResourceScatterMax.md): Reduces sparse updates into the variable referenced by `resource` using the `max` operation.

[`ResourceScatterMin(...)`](../../../tf/raw_ops/ResourceScatterMin.md): Reduces sparse updates into the variable referenced by `resource` using the `min` operation.

[`ResourceScatterMul(...)`](../../../tf/raw_ops/ResourceScatterMul.md): Multiplies sparse updates into the variable referenced by `resource`.

[`ResourceScatterNdAdd(...)`](../../../tf/raw_ops/ResourceScatterNdAdd.md): Applies sparse addition to individual values or slices in a Variable.

[`ResourceScatterNdSub(...)`](../../../tf/raw_ops/ResourceScatterNdSub.md): Applies sparse subtraction to individual values or slices in a Variable.

[`ResourceScatterNdUpdate(...)`](../../../tf/raw_ops/ResourceScatterNdUpdate.md): Applies sparse `updates` to individual values or slices within a given

[`ResourceScatterSub(...)`](../../../tf/raw_ops/ResourceScatterSub.md): Subtracts sparse updates from the variable referenced by `resource`.

[`ResourceScatterUpdate(...)`](../../../tf/raw_ops/ResourceScatterUpdate.md): Assigns sparse updates to the variable referenced by `resource`.

[`ResourceSparseApplyAdadelta(...)`](../../../tf/raw_ops/ResourceSparseApplyAdadelta.md): var: Should be from a Variable().

[`ResourceSparseApplyAdagrad(...)`](../../../tf/raw_ops/ResourceSparseApplyAdagrad.md): Update relevant entries in '*var' and '*accum' according to the adagrad scheme.

[`ResourceSparseApplyAdagradDA(...)`](../../../tf/raw_ops/ResourceSparseApplyAdagradDA.md): Update entries in '*var' and '*accum' according to the proximal adagrad scheme.

[`ResourceSparseApplyAdagradV2(...)`](../../../tf/raw_ops/ResourceSparseApplyAdagradV2.md): Update relevant entries in '*var' and '*accum' according to the adagrad scheme.

[`ResourceSparseApplyCenteredRMSProp(...)`](../../../tf/raw_ops/ResourceSparseApplyCenteredRMSProp.md): Update '*var' according to the centered RMSProp algorithm.

[`ResourceSparseApplyFtrl(...)`](../../../tf/raw_ops/ResourceSparseApplyFtrl.md): Update relevant entries in '*var' according to the Ftrl-proximal scheme.

[`ResourceSparseApplyFtrlV2(...)`](../../../tf/raw_ops/ResourceSparseApplyFtrlV2.md): Update relevant entries in '*var' according to the Ftrl-proximal scheme.

[`ResourceSparseApplyKerasMomentum(...)`](../../../tf/raw_ops/ResourceSparseApplyKerasMomentum.md): Update relevant entries in '*var' and '*accum' according to the momentum scheme.

[`ResourceSparseApplyMomentum(...)`](../../../tf/raw_ops/ResourceSparseApplyMomentum.md): Update relevant entries in '*var' and '*accum' according to the momentum scheme.

[`ResourceSparseApplyProximalAdagrad(...)`](../../../tf/raw_ops/ResourceSparseApplyProximalAdagrad.md): Sparse update entries in '*var' and '*accum' according to FOBOS algorithm.

[`ResourceSparseApplyProximalGradientDescent(...)`](../../../tf/raw_ops/ResourceSparseApplyProximalGradientDescent.md): Sparse update '*var' as FOBOS algorithm with fixed learning rate.

[`ResourceSparseApplyRMSProp(...)`](../../../tf/raw_ops/ResourceSparseApplyRMSProp.md): Update '*var' according to the RMSProp algorithm.

[`ResourceStridedSliceAssign(...)`](../../../tf/raw_ops/ResourceStridedSliceAssign.md): Assign `value` to the sliced l-value reference of `ref`.

[`Restore(...)`](../../../tf/raw_ops/Restore.md): Restores a tensor from checkpoint files.

[`RestoreSlice(...)`](../../../tf/raw_ops/RestoreSlice.md): Restores a tensor from checkpoint files.

[`RestoreV2(...)`](../../../tf/raw_ops/RestoreV2.md): Restores tensors from a V2 checkpoint.

[`RetrieveTPUEmbeddingADAMParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingADAMParameters.md): Retrieve ADAM embedding parameters.

[`RetrieveTPUEmbeddingADAMParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingADAMParametersGradAccumDebug.md): Retrieve ADAM embedding parameters with debug support.

[`RetrieveTPUEmbeddingAdadeltaParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingAdadeltaParameters.md): Retrieve Adadelta embedding parameters.

[`RetrieveTPUEmbeddingAdadeltaParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingAdadeltaParametersGradAccumDebug.md): Retrieve Adadelta embedding parameters with debug support.

[`RetrieveTPUEmbeddingAdagradParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingAdagradParameters.md): Retrieve Adagrad embedding parameters.

[`RetrieveTPUEmbeddingAdagradParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingAdagradParametersGradAccumDebug.md): Retrieve Adagrad embedding parameters with debug support.

[`RetrieveTPUEmbeddingCenteredRMSPropParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingCenteredRMSPropParameters.md): Retrieve centered RMSProp embedding parameters.

[`RetrieveTPUEmbeddingFTRLParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingFTRLParameters.md): Retrieve FTRL embedding parameters.

[`RetrieveTPUEmbeddingFTRLParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingFTRLParametersGradAccumDebug.md): Retrieve FTRL embedding parameters with debug support.

[`RetrieveTPUEmbeddingMDLAdagradLightParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingMDLAdagradLightParameters.md): Retrieve MDL Adagrad Light embedding parameters.

[`RetrieveTPUEmbeddingMomentumParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingMomentumParameters.md): Retrieve Momentum embedding parameters.

[`RetrieveTPUEmbeddingMomentumParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingMomentumParametersGradAccumDebug.md): Retrieve Momentum embedding parameters with debug support.

[`RetrieveTPUEmbeddingProximalAdagradParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParameters.md): Retrieve proximal Adagrad embedding parameters.

[`RetrieveTPUEmbeddingProximalAdagradParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingProximalAdagradParametersGradAccumDebug.md): Retrieve proximal Adagrad embedding parameters with debug support.

[`RetrieveTPUEmbeddingRMSPropParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingRMSPropParameters.md): Retrieve RMSProp embedding parameters.

[`RetrieveTPUEmbeddingRMSPropParametersGradAccumDebug(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingRMSPropParametersGradAccumDebug.md): Retrieve RMSProp embedding parameters with debug support.

[`RetrieveTPUEmbeddingStochasticGradientDescentParameters(...)`](../../../tf/raw_ops/RetrieveTPUEmbeddingStochasticGradientDescentParameters.md): Retrieve SGD embedding parameters.

[`Reverse(...)`](../../../tf/raw_ops/Reverse.md): Reverses specific dimensions of a tensor.

[`ReverseSequence(...)`](../../../tf/raw_ops/ReverseSequence.md): Reverses variable length slices.

[`ReverseV2(...)`](../../../tf/raw_ops/ReverseV2.md): Reverses specific dimensions of a tensor.

[`RightShift(...)`](../../../tf/raw_ops/RightShift.md): Elementwise computes the bitwise right-shift of `x` and `y`.

[`Rint(...)`](../../../tf/raw_ops/Rint.md): Returns element-wise integer closest to x.

[`RngSkip(...)`](../../../tf/raw_ops/RngSkip.md): Advance the counter of a counter-based RNG.

[`Roll(...)`](../../../tf/raw_ops/Roll.md): Rolls the elements of a tensor along an axis.

[`Round(...)`](../../../tf/raw_ops/Round.md): Rounds the values of a tensor to the nearest integer, element-wise.

[`Rsqrt(...)`](../../../tf/raw_ops/Rsqrt.md): Computes reciprocal of square root of x element-wise.

[`RsqrtGrad(...)`](../../../tf/raw_ops/RsqrtGrad.md): Computes the gradient for the rsqrt of `x` wrt its input.

[`SampleDistortedBoundingBox(...)`](../../../tf/raw_ops/SampleDistortedBoundingBox.md): Generate a single randomly distorted bounding box for an image.

[`SampleDistortedBoundingBoxV2(...)`](../../../tf/raw_ops/SampleDistortedBoundingBoxV2.md): Generate a single randomly distorted bounding box for an image.

[`SamplingDataset(...)`](../../../tf/raw_ops/SamplingDataset.md): Creates a dataset that takes a Bernoulli sample of the contents of another dataset.

[`Save(...)`](../../../tf/raw_ops/Save.md): Saves the input tensors to disk.

[`SaveSlices(...)`](../../../tf/raw_ops/SaveSlices.md): Saves input tensors slices to disk.

[`SaveV2(...)`](../../../tf/raw_ops/SaveV2.md): Saves tensors in V2 checkpoint format.

[`ScalarSummary(...)`](../../../tf/raw_ops/ScalarSummary.md): Outputs a `Summary` protocol buffer with scalar values.

[`ScaleAndTranslate(...)`](../../../tf/raw_ops/ScaleAndTranslate.md)

[`ScaleAndTranslateGrad(...)`](../../../tf/raw_ops/ScaleAndTranslateGrad.md)

[`ScanDataset(...)`](../../../tf/raw_ops/ScanDataset.md): Creates a dataset successively reduces `f` over the elements of `input_dataset`.

[`ScatterAdd(...)`](../../../tf/raw_ops/ScatterAdd.md): Adds sparse updates to a variable reference.

[`ScatterDiv(...)`](../../../tf/raw_ops/ScatterDiv.md): Divides a variable reference by sparse updates.

[`ScatterMax(...)`](../../../tf/raw_ops/ScatterMax.md): Reduces sparse updates into a variable reference using the `max` operation.

[`ScatterMin(...)`](../../../tf/raw_ops/ScatterMin.md): Reduces sparse updates into a variable reference using the `min` operation.

[`ScatterMul(...)`](../../../tf/raw_ops/ScatterMul.md): Multiplies sparse updates into a variable reference.

[`ScatterNd(...)`](../../../tf/raw_ops/ScatterNd.md): Scatter `updates` into a new tensor according to `indices`.

[`ScatterNdAdd(...)`](../../../tf/raw_ops/ScatterNdAdd.md): Applies sparse addition to individual values or slices in a Variable.

[`ScatterNdNonAliasingAdd(...)`](../../../tf/raw_ops/ScatterNdNonAliasingAdd.md): Applies sparse addition to `input` using individual values or slices

[`ScatterNdSub(...)`](../../../tf/raw_ops/ScatterNdSub.md): Applies sparse subtraction to individual values or slices in a Variable.

[`ScatterNdUpdate(...)`](../../../tf/raw_ops/ScatterNdUpdate.md): Applies sparse `updates` to individual values or slices within a given

[`ScatterSub(...)`](../../../tf/raw_ops/ScatterSub.md): Subtracts sparse updates to a variable reference.

[`ScatterUpdate(...)`](../../../tf/raw_ops/ScatterUpdate.md): Applies sparse updates to a variable reference.

[`SdcaFprint(...)`](../../../tf/raw_ops/SdcaFprint.md): Computes fingerprints of the input strings.

[`SdcaOptimizer(...)`](../../../tf/raw_ops/SdcaOptimizer.md): Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

[`SdcaOptimizerV2(...)`](../../../tf/raw_ops/SdcaOptimizerV2.md): Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

[`SdcaShrinkL1(...)`](../../../tf/raw_ops/SdcaShrinkL1.md): Applies L1 regularization shrink step on the parameters.

[`SegmentMax(...)`](../../../tf/raw_ops/SegmentMax.md): Computes the maximum along segments of a tensor.

[`SegmentMean(...)`](../../../tf/raw_ops/SegmentMean.md): Computes the mean along segments of a tensor.

[`SegmentMin(...)`](../../../tf/raw_ops/SegmentMin.md): Computes the minimum along segments of a tensor.

[`SegmentProd(...)`](../../../tf/raw_ops/SegmentProd.md): Computes the product along segments of a tensor.

[`SegmentSum(...)`](../../../tf/raw_ops/SegmentSum.md): Computes the sum along segments of a tensor.

[`Select(...)`](../../../tf/raw_ops/Select.md): Selects elements from `x` or `y`, depending on `condition`.

[`SelectV2(...)`](../../../tf/raw_ops/SelectV2.md)

[`SelfAdjointEig(...)`](../../../tf/raw_ops/SelfAdjointEig.md): Computes the Eigen Decomposition of a batch of square self-adjoint matrices.

[`SelfAdjointEigV2(...)`](../../../tf/raw_ops/SelfAdjointEigV2.md): Computes the eigen decomposition of one or more square self-adjoint matrices.

[`Selu(...)`](../../../tf/raw_ops/Selu.md): Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

[`SeluGrad(...)`](../../../tf/raw_ops/SeluGrad.md): Computes gradients for the scaled exponential linear (Selu) operation.

[`Send(...)`](../../../tf/raw_ops/Send.md): Sends the named tensor from send_device to recv_device.

[`SendTPUEmbeddingGradients(...)`](../../../tf/raw_ops/SendTPUEmbeddingGradients.md): Performs gradient updates of embedding tables.

[`SerializeIterator(...)`](../../../tf/raw_ops/SerializeIterator.md): Converts the given `resource_handle` representing an iterator to a variant tensor.

[`SerializeManySparse(...)`](../../../tf/raw_ops/SerializeManySparse.md): Serialize an `N`-minibatch `SparseTensor` into an `[N, 3]` `Tensor` object.

[`SerializeSparse(...)`](../../../tf/raw_ops/SerializeSparse.md): Serialize a `SparseTensor` into a `[3]` `Tensor` object.

[`SerializeTensor(...)`](../../../tf/raw_ops/SerializeTensor.md): Transforms a Tensor into a serialized TensorProto proto.

[`SetSize(...)`](../../../tf/raw_ops/SetSize.md): Number of unique elements along last dimension of input `set`.

[`SetStatsAggregatorDataset(...)`](../../../tf/raw_ops/SetStatsAggregatorDataset.md)

[`Shape(...)`](../../../tf/raw_ops/Shape.md): Returns the shape of a tensor.

[`ShapeN(...)`](../../../tf/raw_ops/ShapeN.md): Returns shape of tensors.

[`ShardDataset(...)`](../../../tf/raw_ops/ShardDataset.md): Creates a `Dataset` that includes only 1/`num_shards` of this dataset.

[`ShardedFilename(...)`](../../../tf/raw_ops/ShardedFilename.md): Generate a sharded filename. The filename is printf formatted as

[`ShardedFilespec(...)`](../../../tf/raw_ops/ShardedFilespec.md): Generate a glob pattern matching all sharded file names.

[`ShuffleAndRepeatDataset(...)`](../../../tf/raw_ops/ShuffleAndRepeatDataset.md): Creates a dataset that shuffles and repeats elements from `input_dataset`

[`ShuffleDataset(...)`](../../../tf/raw_ops/ShuffleDataset.md): Creates a dataset that shuffles elements from `input_dataset` pseudorandomly.

[`ShuffleDatasetV2(...)`](../../../tf/raw_ops/ShuffleDatasetV2.md)

[`ShutdownDistributedTPU(...)`](../../../tf/raw_ops/ShutdownDistributedTPU.md): Shuts down a running distributed TPU system.

[`Sigmoid(...)`](../../../tf/raw_ops/Sigmoid.md): Computes sigmoid of `x` element-wise.

[`SigmoidGrad(...)`](../../../tf/raw_ops/SigmoidGrad.md): Computes the gradient of the sigmoid of `x` wrt its input.

[`Sign(...)`](../../../tf/raw_ops/Sign.md): Returns an element-wise indication of the sign of a number.

[`Sin(...)`](../../../tf/raw_ops/Sin.md): Computes sine of x element-wise.

[`Sinh(...)`](../../../tf/raw_ops/Sinh.md): Computes hyperbolic sine of x element-wise.

[`Size(...)`](../../../tf/raw_ops/Size.md): Returns the size of a tensor.

[`SkipDataset(...)`](../../../tf/raw_ops/SkipDataset.md): Creates a dataset that skips `count` elements from the `input_dataset`.

[`SleepDataset(...)`](../../../tf/raw_ops/SleepDataset.md)

[`Slice(...)`](../../../tf/raw_ops/Slice.md): Return a slice from 'input'.

[`SlidingWindowDataset(...)`](../../../tf/raw_ops/SlidingWindowDataset.md): Creates a dataset that passes a sliding window over `input_dataset`.

[`Snapshot(...)`](../../../tf/raw_ops/Snapshot.md): Returns a copy of the input tensor.

[`SnapshotDataset(...)`](../../../tf/raw_ops/SnapshotDataset.md): Creates a dataset that will write to / read from a snapshot.

[`SobolSample(...)`](../../../tf/raw_ops/SobolSample.md): Generates points from the Sobol sequence.

[`Softmax(...)`](../../../tf/raw_ops/Softmax.md): Computes softmax activations.

[`SoftmaxCrossEntropyWithLogits(...)`](../../../tf/raw_ops/SoftmaxCrossEntropyWithLogits.md): Computes softmax cross entropy cost and gradients to backpropagate.

[`Softplus(...)`](../../../tf/raw_ops/Softplus.md): Computes softplus: `log(exp(features) + 1)`.

[`SoftplusGrad(...)`](../../../tf/raw_ops/SoftplusGrad.md): Computes softplus gradients for a softplus operation.

[`Softsign(...)`](../../../tf/raw_ops/Softsign.md): Computes softsign: `features / (abs(features) + 1)`.

[`SoftsignGrad(...)`](../../../tf/raw_ops/SoftsignGrad.md): Computes softsign gradients for a softsign operation.

[`SpaceToBatch(...)`](../../../tf/raw_ops/SpaceToBatch.md): SpaceToBatch for 4-D tensors of type T.

[`SpaceToBatchND(...)`](../../../tf/raw_ops/SpaceToBatchND.md): SpaceToBatch for N-D tensors of type T.

[`SpaceToDepth(...)`](../../../tf/raw_ops/SpaceToDepth.md): SpaceToDepth for tensors of type T.

[`SparseAccumulatorApplyGradient(...)`](../../../tf/raw_ops/SparseAccumulatorApplyGradient.md): Applies a sparse gradient to a given accumulator.

[`SparseAccumulatorTakeGradient(...)`](../../../tf/raw_ops/SparseAccumulatorTakeGradient.md): Extracts the average sparse gradient in a SparseConditionalAccumulator.

[`SparseAdd(...)`](../../../tf/raw_ops/SparseAdd.md): Adds two `SparseTensor` objects to produce another `SparseTensor`.

[`SparseAddGrad(...)`](../../../tf/raw_ops/SparseAddGrad.md): The gradient operator for the SparseAdd op.

[`SparseApplyAdadelta(...)`](../../../tf/raw_ops/SparseApplyAdadelta.md): var: Should be from a Variable().

[`SparseApplyAdagrad(...)`](../../../tf/raw_ops/SparseApplyAdagrad.md): Update relevant entries in '*var' and '*accum' according to the adagrad scheme.

[`SparseApplyAdagradDA(...)`](../../../tf/raw_ops/SparseApplyAdagradDA.md): Update entries in '*var' and '*accum' according to the proximal adagrad scheme.

[`SparseApplyAdagradV2(...)`](../../../tf/raw_ops/SparseApplyAdagradV2.md): Update relevant entries in '*var' and '*accum' according to the adagrad scheme.

[`SparseApplyCenteredRMSProp(...)`](../../../tf/raw_ops/SparseApplyCenteredRMSProp.md): Update '*var' according to the centered RMSProp algorithm.

[`SparseApplyFtrl(...)`](../../../tf/raw_ops/SparseApplyFtrl.md): Update relevant entries in '*var' according to the Ftrl-proximal scheme.

[`SparseApplyFtrlV2(...)`](../../../tf/raw_ops/SparseApplyFtrlV2.md): Update relevant entries in '*var' according to the Ftrl-proximal scheme.

[`SparseApplyMomentum(...)`](../../../tf/raw_ops/SparseApplyMomentum.md): Update relevant entries in '*var' and '*accum' according to the momentum scheme.

[`SparseApplyProximalAdagrad(...)`](../../../tf/raw_ops/SparseApplyProximalAdagrad.md): Sparse update entries in '*var' and '*accum' according to FOBOS algorithm.

[`SparseApplyProximalGradientDescent(...)`](../../../tf/raw_ops/SparseApplyProximalGradientDescent.md): Sparse update '*var' as FOBOS algorithm with fixed learning rate.

[`SparseApplyRMSProp(...)`](../../../tf/raw_ops/SparseApplyRMSProp.md): Update '*var' according to the RMSProp algorithm.

[`SparseConcat(...)`](../../../tf/raw_ops/SparseConcat.md): Concatenates a list of `SparseTensor` along the specified dimension.

[`SparseConditionalAccumulator(...)`](../../../tf/raw_ops/SparseConditionalAccumulator.md): A conditional accumulator for aggregating sparse gradients.

[`SparseCross(...)`](../../../tf/raw_ops/SparseCross.md): Generates sparse cross from a list of sparse and dense tensors.

[`SparseDenseCwiseAdd(...)`](../../../tf/raw_ops/SparseDenseCwiseAdd.md): Adds up a SparseTensor and a dense Tensor, using these special rules:

[`SparseDenseCwiseDiv(...)`](../../../tf/raw_ops/SparseDenseCwiseDiv.md): Component-wise divides a SparseTensor by a dense Tensor.

[`SparseDenseCwiseMul(...)`](../../../tf/raw_ops/SparseDenseCwiseMul.md): Component-wise multiplies a SparseTensor by a dense Tensor.

[`SparseFillEmptyRows(...)`](../../../tf/raw_ops/SparseFillEmptyRows.md): Fills empty rows in the input 2-D `SparseTensor` with a default value.

[`SparseFillEmptyRowsGrad(...)`](../../../tf/raw_ops/SparseFillEmptyRowsGrad.md): The gradient of SparseFillEmptyRows.

[`SparseMatMul(...)`](../../../tf/raw_ops/SparseMatMul.md): Multiply matrix "a" by matrix "b".

[`SparseMatrixAdd(...)`](../../../tf/raw_ops/SparseMatrixAdd.md): Sparse addition of two CSR matrices, C = alpha * A + beta * B.

[`SparseMatrixMatMul(...)`](../../../tf/raw_ops/SparseMatrixMatMul.md): Matrix-multiplies a sparse matrix with a dense matrix.

[`SparseMatrixMul(...)`](../../../tf/raw_ops/SparseMatrixMul.md): Element-wise multiplication of a sparse matrix with a dense tensor.

[`SparseMatrixNNZ(...)`](../../../tf/raw_ops/SparseMatrixNNZ.md): Returns the number of nonzeroes of `sparse_matrix`.

[`SparseMatrixOrderingAMD(...)`](../../../tf/raw_ops/SparseMatrixOrderingAMD.md): Computes the Approximate Minimum Degree (AMD) ordering of `input`.

[`SparseMatrixSoftmax(...)`](../../../tf/raw_ops/SparseMatrixSoftmax.md): Calculates the softmax of a CSRSparseMatrix.

[`SparseMatrixSoftmaxGrad(...)`](../../../tf/raw_ops/SparseMatrixSoftmaxGrad.md): Calculates the gradient of the SparseMatrixSoftmax op.

[`SparseMatrixSparseCholesky(...)`](../../../tf/raw_ops/SparseMatrixSparseCholesky.md): Computes the sparse Cholesky decomposition of `input`.

[`SparseMatrixSparseMatMul(...)`](../../../tf/raw_ops/SparseMatrixSparseMatMul.md): Sparse-matrix-multiplies two CSR matrices `a` and `b`.

[`SparseMatrixTranspose(...)`](../../../tf/raw_ops/SparseMatrixTranspose.md): Transposes the inner (matrix) dimensions of a CSRSparseMatrix.

[`SparseMatrixZeros(...)`](../../../tf/raw_ops/SparseMatrixZeros.md): Creates an all-zeros CSRSparseMatrix with shape `dense_shape`.

[`SparseReduceMax(...)`](../../../tf/raw_ops/SparseReduceMax.md): Computes the max of elements across dimensions of a SparseTensor.

[`SparseReduceMaxSparse(...)`](../../../tf/raw_ops/SparseReduceMaxSparse.md): Computes the max of elements across dimensions of a SparseTensor.

[`SparseReduceSum(...)`](../../../tf/raw_ops/SparseReduceSum.md): Computes the sum of elements across dimensions of a SparseTensor.

[`SparseReduceSumSparse(...)`](../../../tf/raw_ops/SparseReduceSumSparse.md): Computes the sum of elements across dimensions of a SparseTensor.

[`SparseReorder(...)`](../../../tf/raw_ops/SparseReorder.md): Reorders a SparseTensor into the canonical, row-major ordering.

[`SparseReshape(...)`](../../../tf/raw_ops/SparseReshape.md): Reshapes a SparseTensor to represent values in a new dense shape.

[`SparseSegmentMean(...)`](../../../tf/raw_ops/SparseSegmentMean.md): Computes the mean along sparse segments of a tensor.

[`SparseSegmentMeanGrad(...)`](../../../tf/raw_ops/SparseSegmentMeanGrad.md): Computes gradients for SparseSegmentMean.

[`SparseSegmentMeanWithNumSegments(...)`](../../../tf/raw_ops/SparseSegmentMeanWithNumSegments.md): Computes the mean along sparse segments of a tensor.

[`SparseSegmentSqrtN(...)`](../../../tf/raw_ops/SparseSegmentSqrtN.md): Computes the sum along sparse segments of a tensor divided by the sqrt of N.

[`SparseSegmentSqrtNGrad(...)`](../../../tf/raw_ops/SparseSegmentSqrtNGrad.md): Computes gradients for SparseSegmentSqrtN.

[`SparseSegmentSqrtNWithNumSegments(...)`](../../../tf/raw_ops/SparseSegmentSqrtNWithNumSegments.md): Computes the sum along sparse segments of a tensor divided by the sqrt of N.

[`SparseSegmentSum(...)`](../../../tf/raw_ops/SparseSegmentSum.md): Computes the sum along sparse segments of a tensor.

[`SparseSegmentSumWithNumSegments(...)`](../../../tf/raw_ops/SparseSegmentSumWithNumSegments.md): Computes the sum along sparse segments of a tensor.

[`SparseSlice(...)`](../../../tf/raw_ops/SparseSlice.md): Slice a `SparseTensor` based on the `start` and `size`.

[`SparseSliceGrad(...)`](../../../tf/raw_ops/SparseSliceGrad.md): The gradient operator for the SparseSlice op.

[`SparseSoftmax(...)`](../../../tf/raw_ops/SparseSoftmax.md): Applies softmax to a batched N-D `SparseTensor`.

[`SparseSoftmaxCrossEntropyWithLogits(...)`](../../../tf/raw_ops/SparseSoftmaxCrossEntropyWithLogits.md): Computes softmax cross entropy cost and gradients to backpropagate.

[`SparseSparseMaximum(...)`](../../../tf/raw_ops/SparseSparseMaximum.md): Returns the element-wise max of two SparseTensors.

[`SparseSparseMinimum(...)`](../../../tf/raw_ops/SparseSparseMinimum.md): Returns the element-wise min of two SparseTensors.

[`SparseSplit(...)`](../../../tf/raw_ops/SparseSplit.md): Split a `SparseTensor` into `num_split` tensors along one dimension.

[`SparseTensorDenseAdd(...)`](../../../tf/raw_ops/SparseTensorDenseAdd.md): Adds up a `SparseTensor` and a dense `Tensor`, producing a dense `Tensor`.

[`SparseTensorDenseMatMul(...)`](../../../tf/raw_ops/SparseTensorDenseMatMul.md): Multiply SparseTensor (of rank 2) "A" by dense matrix "B".

[`SparseTensorSliceDataset(...)`](../../../tf/raw_ops/SparseTensorSliceDataset.md): Creates a dataset that splits a SparseTensor into elements row-wise.

[`SparseTensorToCSRSparseMatrix(...)`](../../../tf/raw_ops/SparseTensorToCSRSparseMatrix.md): Converts a SparseTensor to a (possibly batched) CSRSparseMatrix.

[`SparseToDense(...)`](../../../tf/raw_ops/SparseToDense.md): Converts a sparse representation into a dense tensor.

[`SparseToSparseSetOperation(...)`](../../../tf/raw_ops/SparseToSparseSetOperation.md): Applies set operation along last dimension of 2 `SparseTensor` inputs.

[`Spence(...)`](../../../tf/raw_ops/Spence.md)

[`Split(...)`](../../../tf/raw_ops/Split.md): Splits a tensor into `num_split` tensors along one dimension.

[`SplitV(...)`](../../../tf/raw_ops/SplitV.md): Splits a tensor into `num_split` tensors along one dimension.

[`SqlDataset(...)`](../../../tf/raw_ops/SqlDataset.md): Creates a dataset that executes a SQL query and emits rows of the result set.

[`Sqrt(...)`](../../../tf/raw_ops/Sqrt.md): Computes square root of x element-wise.

[`SqrtGrad(...)`](../../../tf/raw_ops/SqrtGrad.md): Computes the gradient for the sqrt of `x` wrt its input.

[`Square(...)`](../../../tf/raw_ops/Square.md): Computes square of x element-wise.

[`SquaredDifference(...)`](../../../tf/raw_ops/SquaredDifference.md): Returns (x - y)(x - y) element-wise.

[`Squeeze(...)`](../../../tf/raw_ops/Squeeze.md): Removes dimensions of size 1 from the shape of a tensor.

[`Stack(...)`](../../../tf/raw_ops/Stack.md): Deprecated, use StackV2.

[`StackClose(...)`](../../../tf/raw_ops/StackClose.md): Deprecated, use StackCloseV2.

[`StackCloseV2(...)`](../../../tf/raw_ops/StackCloseV2.md): Delete the stack from its resource container.

[`StackPop(...)`](../../../tf/raw_ops/StackPop.md): Deprecated, use StackPopV2.

[`StackPopV2(...)`](../../../tf/raw_ops/StackPopV2.md): Pop the element at the top of the stack.

[`StackPush(...)`](../../../tf/raw_ops/StackPush.md): Deprecated, use StackPushV2.

[`StackPushV2(...)`](../../../tf/raw_ops/StackPushV2.md): Push an element onto the stack.

[`StackV2(...)`](../../../tf/raw_ops/StackV2.md): A stack that produces elements in first-in last-out order.

[`Stage(...)`](../../../tf/raw_ops/Stage.md): Stage values similar to a lightweight Enqueue.

[`StageClear(...)`](../../../tf/raw_ops/StageClear.md): Op removes all elements in the underlying container.

[`StagePeek(...)`](../../../tf/raw_ops/StagePeek.md): Op peeks at the values at the specified index.  If the

[`StageSize(...)`](../../../tf/raw_ops/StageSize.md): Op returns the number of elements in the underlying container.

[`StatefulPartitionedCall(...)`](../../../tf/raw_ops/StatefulPartitionedCall.md): returns `f(inputs)`, where `f`'s body is placed and partitioned.

[`StatefulRandomBinomial(...)`](../../../tf/raw_ops/StatefulRandomBinomial.md)

[`StatefulStandardNormal(...)`](../../../tf/raw_ops/StatefulStandardNormal.md): Outputs random values from a normal distribution. This op is deprecated in favor of op 'StatefulStandardNormalV2'

[`StatefulStandardNormalV2(...)`](../../../tf/raw_ops/StatefulStandardNormalV2.md): Outputs random values from a normal distribution.

[`StatefulTruncatedNormal(...)`](../../../tf/raw_ops/StatefulTruncatedNormal.md): Outputs random values from a truncated normal distribution.

[`StatefulUniform(...)`](../../../tf/raw_ops/StatefulUniform.md): Outputs random values from a uniform distribution.

[`StatefulUniformFullInt(...)`](../../../tf/raw_ops/StatefulUniformFullInt.md): Outputs random integers from a uniform distribution.

[`StatefulUniformInt(...)`](../../../tf/raw_ops/StatefulUniformInt.md): Outputs random integers from a uniform distribution.

[`StatelessIf(...)`](../../../tf/raw_ops/StatelessIf.md): output = cond ? then_branch(input) : else_branch(input)

[`StatelessMultinomial(...)`](../../../tf/raw_ops/StatelessMultinomial.md): Draws samples from a multinomial distribution.

[`StatelessRandomBinomial(...)`](../../../tf/raw_ops/StatelessRandomBinomial.md): Outputs deterministic pseudorandom random numbers from a binomial distribution.

[`StatelessRandomGammaV2(...)`](../../../tf/raw_ops/StatelessRandomGammaV2.md): Outputs deterministic pseudorandom random numbers from a gamma distribution.

[`StatelessRandomNormal(...)`](../../../tf/raw_ops/StatelessRandomNormal.md): Outputs deterministic pseudorandom values from a normal distribution.

[`StatelessRandomPoisson(...)`](../../../tf/raw_ops/StatelessRandomPoisson.md): Outputs deterministic pseudorandom random numbers from a Poisson distribution.

[`StatelessRandomUniform(...)`](../../../tf/raw_ops/StatelessRandomUniform.md): Outputs deterministic pseudorandom random values from a uniform distribution.

[`StatelessRandomUniformFullInt(...)`](../../../tf/raw_ops/StatelessRandomUniformFullInt.md): Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessRandomUniformInt(...)`](../../../tf/raw_ops/StatelessRandomUniformInt.md): Outputs deterministic pseudorandom random integers from a uniform distribution.

[`StatelessTruncatedNormal(...)`](../../../tf/raw_ops/StatelessTruncatedNormal.md): Outputs deterministic pseudorandom values from a truncated normal distribution.

[`StatelessWhile(...)`](../../../tf/raw_ops/StatelessWhile.md): output = input; While (Cond(output)) { output = Body(output) }

[`StaticRegexFullMatch(...)`](../../../tf/raw_ops/StaticRegexFullMatch.md): Check if the input matches the regex pattern.

[`StaticRegexReplace(...)`](../../../tf/raw_ops/StaticRegexReplace.md): Replaces the match of pattern in input with rewrite.

[`StatsAggregatorHandle(...)`](../../../tf/raw_ops/StatsAggregatorHandle.md): Creates a statistics manager resource.

[`StatsAggregatorHandleV2(...)`](../../../tf/raw_ops/StatsAggregatorHandleV2.md)

[`StatsAggregatorSetSummaryWriter(...)`](../../../tf/raw_ops/StatsAggregatorSetSummaryWriter.md): Set a summary_writer_interface to record statistics using given stats_aggregator.

[`StatsAggregatorSummary(...)`](../../../tf/raw_ops/StatsAggregatorSummary.md): Produces a summary of any statistics recorded by the given statistics manager.

[`StopGradient(...)`](../../../tf/raw_ops/StopGradient.md): Stops gradient computation.

[`StridedSlice(...)`](../../../tf/raw_ops/StridedSlice.md): Return a strided slice from `input`.

[`StridedSliceAssign(...)`](../../../tf/raw_ops/StridedSliceAssign.md): Assign `value` to the sliced l-value reference of `ref`.

[`StridedSliceGrad(...)`](../../../tf/raw_ops/StridedSliceGrad.md): Returns the gradient of `StridedSlice`.

[`StringFormat(...)`](../../../tf/raw_ops/StringFormat.md): Formats a string template using a list of tensors.

[`StringJoin(...)`](../../../tf/raw_ops/StringJoin.md): Joins the strings in the given list of string tensors into one tensor;

[`StringLength(...)`](../../../tf/raw_ops/StringLength.md): String lengths of `input`.

[`StringLower(...)`](../../../tf/raw_ops/StringLower.md): Converts all uppercase characters into their respective lowercase replacements.

[`StringNGrams(...)`](../../../tf/raw_ops/StringNGrams.md): Creates ngrams from ragged string data.

[`StringSplit(...)`](../../../tf/raw_ops/StringSplit.md): Split elements of `input` based on `delimiter` into a `SparseTensor`.

[`StringSplitV2(...)`](../../../tf/raw_ops/StringSplitV2.md): Split elements of `source` based on `sep` into a `SparseTensor`.

[`StringStrip(...)`](../../../tf/raw_ops/StringStrip.md): Strip leading and trailing whitespaces from the Tensor.

[`StringToHashBucket(...)`](../../../tf/raw_ops/StringToHashBucket.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToHashBucketFast(...)`](../../../tf/raw_ops/StringToHashBucketFast.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToHashBucketStrong(...)`](../../../tf/raw_ops/StringToHashBucketStrong.md): Converts each string in the input Tensor to its hash mod by a number of buckets.

[`StringToNumber(...)`](../../../tf/raw_ops/StringToNumber.md): Converts each string in the input Tensor to the specified numeric type.

[`StringUpper(...)`](../../../tf/raw_ops/StringUpper.md): Converts all lowercase characters into their respective uppercase replacements.

[`Sub(...)`](../../../tf/raw_ops/Sub.md): Returns x - y element-wise.

[`Substr(...)`](../../../tf/raw_ops/Substr.md): Return substrings from `Tensor` of strings.

[`Sum(...)`](../../../tf/raw_ops/Sum.md): Computes the sum of elements across dimensions of a tensor.

[`SummaryWriter(...)`](../../../tf/raw_ops/SummaryWriter.md)

[`Svd(...)`](../../../tf/raw_ops/Svd.md): Computes the singular value decompositions of one or more matrices.

[`Switch(...)`](../../../tf/raw_ops/Switch.md): Forwards `data` to the output port determined by `pred`.

[`SymbolicGradient(...)`](../../../tf/raw_ops/SymbolicGradient.md): Computes the gradient function for function f via backpropagation.

[`TFRecordDataset(...)`](../../../tf/raw_ops/TFRecordDataset.md): Creates a dataset that emits the records from one or more TFRecord files.

[`TFRecordReader(...)`](../../../tf/raw_ops/TFRecordReader.md): A Reader that outputs the records from a TensorFlow Records file.

[`TFRecordReaderV2(...)`](../../../tf/raw_ops/TFRecordReaderV2.md): A Reader that outputs the records from a TensorFlow Records file.

[`TPUCompilationResult(...)`](../../../tf/raw_ops/TPUCompilationResult.md): Returns the result of a TPU compilation.

[`TPUEmbeddingActivations(...)`](../../../tf/raw_ops/TPUEmbeddingActivations.md): An op enabling differentiation of TPU Embeddings.

[`TPUOrdinalSelector(...)`](../../../tf/raw_ops/TPUOrdinalSelector.md): A TPU core selector Op.

[`TPUPartitionedCall(...)`](../../../tf/raw_ops/TPUPartitionedCall.md): Calls a function placed on a specified TPU device.

[`TPUReplicateMetadata(...)`](../../../tf/raw_ops/TPUReplicateMetadata.md): Metadata indicating how the TPU computation should be replicated.

[`TPUReplicatedInput(...)`](../../../tf/raw_ops/TPUReplicatedInput.md): Connects N inputs to an N-way replicated TPU computation.

[`TPUReplicatedOutput(...)`](../../../tf/raw_ops/TPUReplicatedOutput.md): Connects N outputs from an N-way replicated TPU computation.

[`TakeDataset(...)`](../../../tf/raw_ops/TakeDataset.md): Creates a dataset that contains `count` elements from the `input_dataset`.

[`TakeManySparseFromTensorsMap(...)`](../../../tf/raw_ops/TakeManySparseFromTensorsMap.md): Read `SparseTensors` from a `SparseTensorsMap` and concatenate them.

[`TakeWhileDataset(...)`](../../../tf/raw_ops/TakeWhileDataset.md): Creates a dataset that stops iteration when predicate` is false.

[`Tan(...)`](../../../tf/raw_ops/Tan.md): Computes tan of x element-wise.

[`Tanh(...)`](../../../tf/raw_ops/Tanh.md): Computes hyperbolic tangent of `x` element-wise.

[`TanhGrad(...)`](../../../tf/raw_ops/TanhGrad.md): Computes the gradient for the tanh of `x` wrt its input.

[`TemporaryVariable(...)`](../../../tf/raw_ops/TemporaryVariable.md): Returns a tensor that may be mutated, but only persists within a single step.

[`TensorArray(...)`](../../../tf/raw_ops/TensorArray.md)

[`TensorArrayClose(...)`](../../../tf/raw_ops/TensorArrayClose.md)

[`TensorArrayCloseV2(...)`](../../../tf/raw_ops/TensorArrayCloseV2.md): Deprecated. Use TensorArrayCloseV3

[`TensorArrayCloseV3(...)`](../../../tf/raw_ops/TensorArrayCloseV3.md): Delete the TensorArray from its resource container.

[`TensorArrayConcat(...)`](../../../tf/raw_ops/TensorArrayConcat.md)

[`TensorArrayConcatV2(...)`](../../../tf/raw_ops/TensorArrayConcatV2.md): Deprecated. Use TensorArrayConcatV3

[`TensorArrayConcatV3(...)`](../../../tf/raw_ops/TensorArrayConcatV3.md): Concat the elements from the TensorArray into value `value`.

[`TensorArrayGather(...)`](../../../tf/raw_ops/TensorArrayGather.md)

[`TensorArrayGatherV2(...)`](../../../tf/raw_ops/TensorArrayGatherV2.md): Deprecated. Use TensorArrayGatherV3

[`TensorArrayGatherV3(...)`](../../../tf/raw_ops/TensorArrayGatherV3.md): Gather specific elements from the TensorArray into output `value`.

[`TensorArrayGrad(...)`](../../../tf/raw_ops/TensorArrayGrad.md)

[`TensorArrayGradV2(...)`](../../../tf/raw_ops/TensorArrayGradV2.md): Deprecated. Use TensorArrayGradV3

[`TensorArrayGradV3(...)`](../../../tf/raw_ops/TensorArrayGradV3.md): Creates a TensorArray for storing the gradients of values in the given handle.

[`TensorArrayGradWithShape(...)`](../../../tf/raw_ops/TensorArrayGradWithShape.md): Creates a TensorArray for storing multiple gradients of values in the given handle.

[`TensorArrayPack(...)`](../../../tf/raw_ops/TensorArrayPack.md)

[`TensorArrayRead(...)`](../../../tf/raw_ops/TensorArrayRead.md)

[`TensorArrayReadV2(...)`](../../../tf/raw_ops/TensorArrayReadV2.md): Deprecated. Use TensorArrayReadV3

[`TensorArrayReadV3(...)`](../../../tf/raw_ops/TensorArrayReadV3.md): Read an element from the TensorArray into output `value`.

[`TensorArrayScatter(...)`](../../../tf/raw_ops/TensorArrayScatter.md)

[`TensorArrayScatterV2(...)`](../../../tf/raw_ops/TensorArrayScatterV2.md): Deprecated. Use TensorArrayScatterV3

[`TensorArrayScatterV3(...)`](../../../tf/raw_ops/TensorArrayScatterV3.md): Scatter the data from the input value into specific TensorArray elements.

[`TensorArraySize(...)`](../../../tf/raw_ops/TensorArraySize.md)

[`TensorArraySizeV2(...)`](../../../tf/raw_ops/TensorArraySizeV2.md): Deprecated. Use TensorArraySizeV3

[`TensorArraySizeV3(...)`](../../../tf/raw_ops/TensorArraySizeV3.md): Get the current size of the TensorArray.

[`TensorArraySplit(...)`](../../../tf/raw_ops/TensorArraySplit.md)

[`TensorArraySplitV2(...)`](../../../tf/raw_ops/TensorArraySplitV2.md): Deprecated. Use TensorArraySplitV3

[`TensorArraySplitV3(...)`](../../../tf/raw_ops/TensorArraySplitV3.md): Split the data from the input value into TensorArray elements.

[`TensorArrayUnpack(...)`](../../../tf/raw_ops/TensorArrayUnpack.md)

[`TensorArrayV2(...)`](../../../tf/raw_ops/TensorArrayV2.md): Deprecated. Use TensorArrayV3

[`TensorArrayV3(...)`](../../../tf/raw_ops/TensorArrayV3.md): An array of Tensors of given size.

[`TensorArrayWrite(...)`](../../../tf/raw_ops/TensorArrayWrite.md)

[`TensorArrayWriteV2(...)`](../../../tf/raw_ops/TensorArrayWriteV2.md): Deprecated. Use TensorArrayGradV3

[`TensorArrayWriteV3(...)`](../../../tf/raw_ops/TensorArrayWriteV3.md): Push an element onto the tensor_array.

[`TensorDataset(...)`](../../../tf/raw_ops/TensorDataset.md): Creates a dataset that emits `components` as a tuple of tensors once.

[`TensorListConcat(...)`](../../../tf/raw_ops/TensorListConcat.md): Concats all tensors in the list along the 0th dimension.

[`TensorListConcatLists(...)`](../../../tf/raw_ops/TensorListConcatLists.md)

[`TensorListConcatV2(...)`](../../../tf/raw_ops/TensorListConcatV2.md): Concats all tensors in the list along the 0th dimension.

[`TensorListElementShape(...)`](../../../tf/raw_ops/TensorListElementShape.md): The shape of the elements of the given list, as a tensor.

[`TensorListFromTensor(...)`](../../../tf/raw_ops/TensorListFromTensor.md): Creates a TensorList which, when stacked, has the value of `tensor`.

[`TensorListGather(...)`](../../../tf/raw_ops/TensorListGather.md): Creates a Tensor by indexing into the TensorList.

[`TensorListGetItem(...)`](../../../tf/raw_ops/TensorListGetItem.md): Returns the item in the list with the given index.

[`TensorListLength(...)`](../../../tf/raw_ops/TensorListLength.md): Returns the number of tensors in the input tensor list.

[`TensorListPopBack(...)`](../../../tf/raw_ops/TensorListPopBack.md): Returns the last element of the input list as well as a list with all but that element.

[`TensorListPushBack(...)`](../../../tf/raw_ops/TensorListPushBack.md): Returns a list which has the passed-in `Tensor` as last element and the other elements of the given list in `input_handle`.

[`TensorListPushBackBatch(...)`](../../../tf/raw_ops/TensorListPushBackBatch.md)

[`TensorListReserve(...)`](../../../tf/raw_ops/TensorListReserve.md): List of the given size with empty elements.

[`TensorListResize(...)`](../../../tf/raw_ops/TensorListResize.md): Resizes the list.

[`TensorListScatter(...)`](../../../tf/raw_ops/TensorListScatter.md): Creates a TensorList by indexing into a Tensor.

[`TensorListScatterIntoExistingList(...)`](../../../tf/raw_ops/TensorListScatterIntoExistingList.md): Scatters tensor at indices in an input list.

[`TensorListScatterV2(...)`](../../../tf/raw_ops/TensorListScatterV2.md): Creates a TensorList by indexing into a Tensor.

[`TensorListSetItem(...)`](../../../tf/raw_ops/TensorListSetItem.md): Sets the index-th position of the list to contain the given tensor.

[`TensorListSplit(...)`](../../../tf/raw_ops/TensorListSplit.md): Splits a tensor into a list.

[`TensorListStack(...)`](../../../tf/raw_ops/TensorListStack.md): Stacks all tensors in the list.

[`TensorScatterAdd(...)`](../../../tf/raw_ops/TensorScatterAdd.md): Adds sparse `updates` to an existing tensor according to `indices`.

[`TensorScatterSub(...)`](../../../tf/raw_ops/TensorScatterSub.md): Subtracts sparse `updates` from an existing tensor according to `indices`.

[`TensorScatterUpdate(...)`](../../../tf/raw_ops/TensorScatterUpdate.md): Scatter `updates` into an existing tensor according to `indices`.

[`TensorSliceDataset(...)`](../../../tf/raw_ops/TensorSliceDataset.md): Creates a dataset that emits each dim-0 slice of `components` once.

[`TensorStridedSliceUpdate(...)`](../../../tf/raw_ops/TensorStridedSliceUpdate.md): Assign `value` to the sliced l-value reference of `input`.

[`TensorSummary(...)`](../../../tf/raw_ops/TensorSummary.md): Outputs a `Summary` protocol buffer with a tensor.

[`TensorSummaryV2(...)`](../../../tf/raw_ops/TensorSummaryV2.md): Outputs a `Summary` protocol buffer with a tensor and per-plugin data.

[`TextLineDataset(...)`](../../../tf/raw_ops/TextLineDataset.md): Creates a dataset that emits the lines of one or more text files.

[`TextLineReader(...)`](../../../tf/raw_ops/TextLineReader.md): A Reader that outputs the lines of a file delimited by '\n'.

[`TextLineReaderV2(...)`](../../../tf/raw_ops/TextLineReaderV2.md): A Reader that outputs the lines of a file delimited by '\n'.

[`ThreadPoolDataset(...)`](../../../tf/raw_ops/ThreadPoolDataset.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ThreadPoolHandle(...)`](../../../tf/raw_ops/ThreadPoolHandle.md): Creates a dataset that uses a custom thread pool to compute `input_dataset`.

[`ThreadUnsafeUnigramCandidateSampler(...)`](../../../tf/raw_ops/ThreadUnsafeUnigramCandidateSampler.md): Generates labels for candidate sampling with a learned unigram distribution.

[`Tile(...)`](../../../tf/raw_ops/Tile.md): Constructs a tensor by tiling a given tensor.

[`TileGrad(...)`](../../../tf/raw_ops/TileGrad.md): Returns the gradient of `Tile`.

[`Timestamp(...)`](../../../tf/raw_ops/Timestamp.md): Provides the time since epoch in seconds.

[`ToBool(...)`](../../../tf/raw_ops/ToBool.md): Converts a tensor to a scalar predicate.

[`TopK(...)`](../../../tf/raw_ops/TopK.md): Finds values and indices of the `k` largest elements for the last dimension.

[`TopKV2(...)`](../../../tf/raw_ops/TopKV2.md): Finds values and indices of the `k` largest elements for the last dimension.

[`Transpose(...)`](../../../tf/raw_ops/Transpose.md): Shuffle dimensions of x according to a permutation.

[`TridiagonalMatMul(...)`](../../../tf/raw_ops/TridiagonalMatMul.md): Calculate product with tridiagonal matrix.

[`TridiagonalSolve(...)`](../../../tf/raw_ops/TridiagonalSolve.md): Solves tridiagonal systems of equations.

[`TruncateDiv(...)`](../../../tf/raw_ops/TruncateDiv.md): Returns x / y element-wise for integer types.

[`TruncateMod(...)`](../../../tf/raw_ops/TruncateMod.md): Returns element-wise remainder of division. This emulates C semantics in that

[`TruncatedNormal(...)`](../../../tf/raw_ops/TruncatedNormal.md): Outputs random values from a truncated normal distribution.

[`Unbatch(...)`](../../../tf/raw_ops/Unbatch.md): Reverses the operation of Batch for a single output Tensor.

[`UnbatchDataset(...)`](../../../tf/raw_ops/UnbatchDataset.md): A dataset that splits the elements of its input into multiple elements.

[`UnbatchGrad(...)`](../../../tf/raw_ops/UnbatchGrad.md): Gradient of Unbatch.

[`UnicodeDecode(...)`](../../../tf/raw_ops/UnicodeDecode.md): Decodes each string in `input` into a sequence of Unicode code points.

[`UnicodeDecodeWithOffsets(...)`](../../../tf/raw_ops/UnicodeDecodeWithOffsets.md): Decodes each string in `input` into a sequence of Unicode code points.

[`UnicodeEncode(...)`](../../../tf/raw_ops/UnicodeEncode.md): Encode a tensor of ints into unicode strings.

[`UnicodeScript(...)`](../../../tf/raw_ops/UnicodeScript.md): Determine the script codes of a given tensor of Unicode integer code points.

[`UnicodeTranscode(...)`](../../../tf/raw_ops/UnicodeTranscode.md): Transcode the input text from a source encoding to a destination encoding.

[`UniformCandidateSampler(...)`](../../../tf/raw_ops/UniformCandidateSampler.md): Generates labels for candidate sampling with a uniform distribution.

[`Unique(...)`](../../../tf/raw_ops/Unique.md): Finds unique elements in a 1-D tensor.

[`UniqueDataset(...)`](../../../tf/raw_ops/UniqueDataset.md): Creates a dataset that contains the unique elements of `input_dataset`.

[`UniqueV2(...)`](../../../tf/raw_ops/UniqueV2.md): Finds unique elements along an axis of a tensor.

[`UniqueWithCounts(...)`](../../../tf/raw_ops/UniqueWithCounts.md): Finds unique elements in a 1-D tensor.

[`UniqueWithCountsV2(...)`](../../../tf/raw_ops/UniqueWithCountsV2.md): Finds unique elements along an axis of a tensor.

[`Unpack(...)`](../../../tf/raw_ops/Unpack.md): Unpacks a given dimension of a rank-`R` tensor into `num` rank-`(R-1)` tensors.

[`UnravelIndex(...)`](../../../tf/raw_ops/UnravelIndex.md): Converts an array of flat indices into a tuple of coordinate arrays.

[`UnsortedSegmentJoin(...)`](../../../tf/raw_ops/UnsortedSegmentJoin.md): Joins the elements of `inputs` based on `segment_ids`.

[`UnsortedSegmentMax(...)`](../../../tf/raw_ops/UnsortedSegmentMax.md): Computes the maximum along segments of a tensor.

[`UnsortedSegmentMin(...)`](../../../tf/raw_ops/UnsortedSegmentMin.md): Computes the minimum along segments of a tensor.

[`UnsortedSegmentProd(...)`](../../../tf/raw_ops/UnsortedSegmentProd.md): Computes the product along segments of a tensor.

[`UnsortedSegmentSum(...)`](../../../tf/raw_ops/UnsortedSegmentSum.md): Computes the sum along segments of a tensor.

[`Unstage(...)`](../../../tf/raw_ops/Unstage.md): Op is similar to a lightweight Dequeue.

[`UnwrapDatasetVariant(...)`](../../../tf/raw_ops/UnwrapDatasetVariant.md)

[`UpperBound(...)`](../../../tf/raw_ops/UpperBound.md): Applies upper_bound(sorted_search_values, values) along each row.

[`VarHandleOp(...)`](../../../tf/raw_ops/VarHandleOp.md): Creates a handle to a Variable resource.

[`VarIsInitializedOp(...)`](../../../tf/raw_ops/VarIsInitializedOp.md): Checks whether a resource handle-based variable has been initialized.

[`Variable(...)`](../../../tf/raw_ops/Variable.md): Use VariableV2 instead.

[`VariableShape(...)`](../../../tf/raw_ops/VariableShape.md): Returns the shape of the variable pointed to by `resource`.

[`VariableV2(...)`](../../../tf/raw_ops/VariableV2.md): Holds state in the form of a tensor that persists across steps.

[`Where(...)`](../../../tf/raw_ops/Where.md): Returns locations of nonzero / true values in a tensor.

[`While(...)`](../../../tf/raw_ops/While.md): output = input; While (Cond(output)) { output = Body(output) }

[`WholeFileReader(...)`](../../../tf/raw_ops/WholeFileReader.md): A Reader that outputs the entire contents of a file as a value.

[`WholeFileReaderV2(...)`](../../../tf/raw_ops/WholeFileReaderV2.md): A Reader that outputs the entire contents of a file as a value.

[`WindowDataset(...)`](../../../tf/raw_ops/WindowDataset.md): Combines (nests of) input elements into a dataset of (nests of) windows.

[`WorkerHeartbeat(...)`](../../../tf/raw_ops/WorkerHeartbeat.md): Worker heartbeat op.

[`WrapDatasetVariant(...)`](../../../tf/raw_ops/WrapDatasetVariant.md)

[`WriteAudioSummary(...)`](../../../tf/raw_ops/WriteAudioSummary.md)

[`WriteFile(...)`](../../../tf/raw_ops/WriteFile.md): Writes contents to the file at input filename. Creates file and recursively

[`WriteGraphSummary(...)`](../../../tf/raw_ops/WriteGraphSummary.md)

[`WriteHistogramSummary(...)`](../../../tf/raw_ops/WriteHistogramSummary.md)

[`WriteImageSummary(...)`](../../../tf/raw_ops/WriteImageSummary.md)

[`WriteRawProtoSummary(...)`](../../../tf/raw_ops/WriteRawProtoSummary.md)

[`WriteScalarSummary(...)`](../../../tf/raw_ops/WriteScalarSummary.md)

[`WriteSummary(...)`](../../../tf/raw_ops/WriteSummary.md)

[`Xdivy(...)`](../../../tf/raw_ops/Xdivy.md): Returns 0 if x == 0, and x / y otherwise, elementwise.

[`Xlog1py(...)`](../../../tf/raw_ops/Xlog1py.md): Returns 0 if x == 0, and x * log1p(y) otherwise, elementwise.

[`Xlogy(...)`](../../../tf/raw_ops/Xlogy.md): Returns 0 if x == 0, and x * log(y) otherwise, elementwise.

[`ZerosLike(...)`](../../../tf/raw_ops/ZerosLike.md): Returns a tensor of zeros with the same shape and type as x.

[`Zeta(...)`](../../../tf/raw_ops/Zeta.md): Compute the Hurwitz zeta function \\(\zeta(x, q)\\).

[`ZipDataset(...)`](../../../tf/raw_ops/ZipDataset.md): Creates a dataset that zips together `input_datasets`.

