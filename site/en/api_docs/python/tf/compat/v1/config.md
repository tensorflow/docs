description: Public API for tf.config namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.config" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.config

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.config namespace.



## Modules

[`experimental`](../../../tf/compat/v1/config/experimental.md) module: Public API for tf.config.experimental namespace.

[`optimizer`](../../../tf/compat/v1/config/optimizer.md) module: Public API for tf.config.optimizer namespace.

[`threading`](../../../tf/compat/v1/config/threading.md) module: Public API for tf.config.threading namespace.

## Classes

[`class LogicalDevice`](../../../tf/config/LogicalDevice.md): Abstraction for a logical device initialized by the runtime.

[`class LogicalDeviceConfiguration`](../../../tf/config/LogicalDeviceConfiguration.md): Configuration class for a logical devices.

[`class PhysicalDevice`](../../../tf/config/PhysicalDevice.md): Abstraction for a locally visible physical device.

## Functions

[`experimental_connect_to_cluster(...)`](../../../tf/config/experimental_connect_to_cluster.md): Connects to the given cluster.

[`experimental_connect_to_host(...)`](../../../tf/config/experimental_connect_to_host.md): Connects to a single machine to enable remote execution on it.

[`experimental_functions_run_eagerly(...)`](../../../tf/config/experimental_functions_run_eagerly.md): Returns the value of the `experimental_run_functions_eagerly` setting. (deprecated)

[`experimental_run_functions_eagerly(...)`](../../../tf/config/experimental_run_functions_eagerly.md): Enables / disables eager execution of <a href="../../../tf/function.md"><code>tf.function</code></a>s. (deprecated)

[`functions_run_eagerly(...)`](../../../tf/config/functions_run_eagerly.md): Returns the value of the `run_functions_eagerly` setting.

[`get_logical_device_configuration(...)`](../../../tf/config/get_logical_device_configuration.md): Get the virtual device configuration for a <a href="../../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

[`get_soft_device_placement(...)`](../../../tf/config/get_soft_device_placement.md): Get if soft device placement is enabled.

[`get_visible_devices(...)`](../../../tf/config/get_visible_devices.md): Get the list of visible physical devices.

[`list_logical_devices(...)`](../../../tf/config/list_logical_devices.md): Return a list of logical devices created by runtime.

[`list_physical_devices(...)`](../../../tf/config/list_physical_devices.md): Return a list of physical devices visible to the host runtime.

[`run_functions_eagerly(...)`](../../../tf/config/run_functions_eagerly.md): Enables / disables eager execution of <a href="../../../tf/function.md"><code>tf.function</code></a>s.

[`set_logical_device_configuration(...)`](../../../tf/config/set_logical_device_configuration.md): Set the logical device configuration for a <a href="../../../tf/config/PhysicalDevice.md"><code>tf.config.PhysicalDevice</code></a>.

[`set_soft_device_placement(...)`](../../../tf/config/set_soft_device_placement.md): Set if soft device placement is enabled.

[`set_visible_devices(...)`](../../../tf/config/set_visible_devices.md): Set the list of visible devices.

