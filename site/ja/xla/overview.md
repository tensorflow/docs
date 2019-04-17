# XLAとは？

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:50%" src="https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/xlalogo.png">
</div>

> 注意：XLAは現在開発中であるため、特定の状況でメモリ使用量の増大や性能の悪化を引き起こす場合があります。

XLAは線形代数の演算に特化したコンパイラで、XLAを使うことでTensorFlowの演算を最適化し、メモリ使用量の削減や性能の向上を期待できます。  
XLAは、実行時にTensorFlowの計算グラフをコンパイルして実行する [just-in-time (JIT) コンパイル機能](https://www.tensorflow.org/xla/jit) と、TensorFlowの計算グラフを実行コードにコンパイルする [ahead-of-time (AOT) コンパイル機能](https://www.tensorflow.org/xla/tfcompile) の2つの機能を提供しています。  


## XLAの目的

* 実行速度の向上
  * TensorFlowの計算グラフの一部をコンパイルすることで、TensorFlowのランタイム上で軽量なオペレーションを実行することによるオーバヘッドを削減できます。
  * 複数のオペレーションを結合することで、各オペレーションで発生するメモリ割り当てと解放によるオーバヘッドを削減します。
* メモリ使用量の改善
  * 演算をスケジューリングして中間データを削減することにより、ピークのメモリ使用量が少なくなるようにします。
* 独自オペレーションの必要性削減
  * 性能を向上することを目的とした複数オペレーションの結合を、独自に行う必要がなくなります。
* モバイル環境でのディスク占有スペース削減
  * AOTコンパイル機能によって、計算グラフをコンパイルして1つの実行プログラムにすることで、TensorFlowのランタイムが不要になるため、モバイルでの推論時のディスク占有スペースを削減できます。
* 可搬性の向上
  * XLAのバックエンドの処理はモジュール化されているため、新しいバックエンドでTensorFlowを動かすためにTensorFlowの大量のソースコードを修正する必要がありません。


## XLAの動作概要

XLAの入力となる中間表現は、HLO IRまたは単にHLOと呼ばれます。  
HLOはHigh Level Optimizerの略で、HLOのオペレーションのセマンティクスは、[Operation Semantics](https://www.tensorflow.org/xla/operation_semantics) に記載されています。  
HLOは、コンパイラで扱う [中間表現](https://ja.wikipedia.org/wiki/%E4%B8%AD%E9%96%93%E8%A1%A8%E7%8F%BE) と考えるとわかりやすいかもしれません。

> 注意: XLAは現在開発中であるため、HLOのセマンティクスが変更になる場合があります。

XLAはHLOで定義された計算グラフを、様々なハードウェアアーキテクチャの実行コードにコンパイルします。  
XLAのバックエンドはモジュール化されているため、XLAを新たなハードウェアで動作させることは、[Developing a new backend for XLA](https://www.tensorflow.org/xla/developing_new_backend) に記載されているとおり、TensorFlowのソースコードを修正することと比較して容易に行えます。  
例えば、[CPU (x86-64、ARM64) 向けの処理](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/cpu) と [NVIDIA GPU向けの処理](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/gpu) は、TensorFlowのメインのソースコードツリーから参照することができます。

次に示す図は、XLAがHLOからバックエンドの実行コードにコンパイルする過程を示しています。

![](https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/how-does-xla-work.png)

XLAは最初に、HLOレベルでターゲットデバイスに依存しない最適化 (例えば、[CSE](https://ja.wikipedia.org/wiki/%E5%85%B1%E9%80%9A%E9%83%A8%E5%88%86%E5%BC%8F%E9%99%A4%E5%8E%BB)やオペレーションの結合) を行いつつ、各オペレーションにおけるメモリ割り当てと解放の解析を行います。

続いてXLAは、HLOレベルでターゲットデバイスに依存する最適化を適用します。  
ターゲットデバイスがGPUである場合は、オペレーションを実行するStreamの割り当ての最適化や、GPUでの性能向上が見込めるオペレーションの結合などが行われます。  
またバックエンドによっては、XLAを使って出力した実行コードよりも独自のライブラリを利用する方が性能がよい場合があるため、ライブラリを呼び出すようにHLOを最適化することも可能です。

最後に、HLOからターゲットデバイスに最適化された実行コードを生成します。  
XLAは、CPUやGPUの実行コードを生成するために [LLVM](http://llvm.org/) を使用しています。HLOからLLVM IRを生成し、LLVMを呼び出してLLVM IRから実行コードを生成します。


## サポートするプラットフォーム

XLAは、x86-64とNVIDIA GPU向けに [JITコンパイル機能](https://www.tensorflow.org/xla/jit) を、x86-64とARM向けに [AOTコンパイル機能](https://www.tensorflow.org/xla/tfcompile) をサポートしています。
