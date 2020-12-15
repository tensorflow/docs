description: Exception types for TensorFlow errors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.errors" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="ABORTED"/>
<meta itemprop="property" content="ALREADY_EXISTS"/>
<meta itemprop="property" content="CANCELLED"/>
<meta itemprop="property" content="DATA_LOSS"/>
<meta itemprop="property" content="DEADLINE_EXCEEDED"/>
<meta itemprop="property" content="FAILED_PRECONDITION"/>
<meta itemprop="property" content="INTERNAL"/>
<meta itemprop="property" content="INVALID_ARGUMENT"/>
<meta itemprop="property" content="NOT_FOUND"/>
<meta itemprop="property" content="OK"/>
<meta itemprop="property" content="OUT_OF_RANGE"/>
<meta itemprop="property" content="PERMISSION_DENIED"/>
<meta itemprop="property" content="RESOURCE_EXHAUSTED"/>
<meta itemprop="property" content="UNAUTHENTICATED"/>
<meta itemprop="property" content="UNAVAILABLE"/>
<meta itemprop="property" content="UNIMPLEMENTED"/>
<meta itemprop="property" content="UNKNOWN"/>
</div>

# Module: tf.errors

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Exception types for TensorFlow errors.



## Classes

[`class AbortedError`](../tf/errors/AbortedError.md): The operation was aborted, typically due to a concurrent action.

[`class AlreadyExistsError`](../tf/errors/AlreadyExistsError.md): Raised when an entity that we attempted to create already exists.

[`class CancelledError`](../tf/errors/CancelledError.md): Raised when an operation or step is cancelled.

[`class DataLossError`](../tf/errors/DataLossError.md): Raised when unrecoverable data loss or corruption is encountered.

[`class DeadlineExceededError`](../tf/errors/DeadlineExceededError.md): Raised when a deadline expires before an operation could complete.

[`class FailedPreconditionError`](../tf/errors/FailedPreconditionError.md): Operation was rejected because the system is not in a state to execute it.

[`class InternalError`](../tf/errors/InternalError.md): Raised when the system experiences an internal error.

[`class InvalidArgumentError`](../tf/errors/InvalidArgumentError.md): Raised when an operation receives an invalid argument.

[`class NotFoundError`](../tf/errors/NotFoundError.md): Raised when a requested entity (e.g., a file or directory) was not found.

[`class OpError`](../tf/errors/OpError.md): A generic error that is raised when TensorFlow execution fails.

[`class OperatorNotAllowedInGraphError`](../tf/errors/OperatorNotAllowedInGraphError.md): An error is raised for unsupported operator in Graph execution.

[`class OutOfRangeError`](../tf/errors/OutOfRangeError.md): Raised when an operation iterates past the valid input range.

[`class PermissionDeniedError`](../tf/errors/PermissionDeniedError.md): Raised when the caller does not have permission to run an operation.

[`class ResourceExhaustedError`](../tf/errors/ResourceExhaustedError.md): Some resource has been exhausted.

[`class UnauthenticatedError`](../tf/errors/UnauthenticatedError.md): The request does not have valid authentication credentials.

[`class UnavailableError`](../tf/errors/UnavailableError.md): Raised when the runtime is currently unavailable.

[`class UnimplementedError`](../tf/errors/UnimplementedError.md): Raised when an operation has not been implemented.

[`class UnknownError`](../tf/errors/UnknownError.md): Unknown error.

## Other Members

* `ABORTED = 10` <a id="ABORTED"></a>
* `ALREADY_EXISTS = 6` <a id="ALREADY_EXISTS"></a>
* `CANCELLED = 1` <a id="CANCELLED"></a>
* `DATA_LOSS = 15` <a id="DATA_LOSS"></a>
* `DEADLINE_EXCEEDED = 4` <a id="DEADLINE_EXCEEDED"></a>
* `FAILED_PRECONDITION = 9` <a id="FAILED_PRECONDITION"></a>
* `INTERNAL = 13` <a id="INTERNAL"></a>
* `INVALID_ARGUMENT = 3` <a id="INVALID_ARGUMENT"></a>
* `NOT_FOUND = 5` <a id="NOT_FOUND"></a>
* `OK = 0` <a id="OK"></a>
* `OUT_OF_RANGE = 11` <a id="OUT_OF_RANGE"></a>
* `PERMISSION_DENIED = 7` <a id="PERMISSION_DENIED"></a>
* `RESOURCE_EXHAUSTED = 8` <a id="RESOURCE_EXHAUSTED"></a>
* `UNAUTHENTICATED = 16` <a id="UNAUTHENTICATED"></a>
* `UNAVAILABLE = 14` <a id="UNAVAILABLE"></a>
* `UNIMPLEMENTED = 12` <a id="UNIMPLEMENTED"></a>
* `UNKNOWN = 2` <a id="UNKNOWN"></a>
