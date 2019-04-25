# XLA 概要

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:50%" src="https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/xlalogo.png">
</div>

> 注意：XLAは現在開発中であるため、特定の状況でメモリ使用量の増大や性能の悪化を引き起こす場合があります。

XLA(Accelerated Linear Algebra)は線形代数の演算に特化したコンパイラで、XLAを使うことでTensorFlowの演算を最適化し、メモリ使用量、性能、サーバやモバイル環境での移植性の面での改善が期待できます。ほとんどのユーザにとって、XLAを使うことによる大きな恩恵は得られないかもしれません。このため、[just-in-time (JIT) コンパイル機能](https://www.tensorflow.org/xla/jit) や [ahead-of-time (AOT) コンパイル機能](https://www.tensorflow.org/xla/tfcompile) を通してXLA実験的に使ってもらえればと思います。ただし、新たなハードウエアアクセラレータの開発者については、XLAを試してみることをおすすめします。


## なぜXLAを開発したか？

TensorFlowと連携するXLAを開発した目的はいくつかあります。

* **実行速度の向上**: サブグラフをコンパイルすることで、TensorFlowのランタイムによるオーバヘッド削減、複数オペレーションの結合によるメモリのオーバヘッド削減、テンソルの形が決まることによる定数畳み込みの促進により、軽量なオペレーションの実行時間を短縮することができます。
* **メモリ使用量の改善**: メモリ使用量の解析とスケジューリングによって、オペレーションの中間データを保持する領域を削減します。
* **独自オペレーションへの依存度削減**: 低レベルのオペレーションを自動的に結合することにより、人の手で独自の結合オペレーションを作成する必要がなくなります。
* **モバイル環境でのディスク占有スペース削減**: サブグラフをAOTコンパイルし、他のアプリケーションに直接リンク可能なオブジェクトとヘッダを出力することで、TensorFlowのランタイムを削除します。これによって、モバイルでの推論時のディスク占有スペースを桁違いに削減できます。
* **移植性の向上**: TensorFlowのプログラムの大部分を修正することなく、新しいハードウェア向けのバックエンドを書くことが容易になります。これは、TensorFlowのプログラムを書き換えて新しいハードウェア向けのオペレーションを作る方式とは全く異なるものです。


## XLAはどのように動くのか？

XLAの入力となる言語は、"HLO IR"または単にHLO(High Level Optimizer)と呼ばれます。HLOのセマンティクスは、[Operation Semantics](https://www.tensorflow.org/xla/operation_semantics) に記載されています。HLOは、コンパイラで扱う [中間表現](https://ja.wikipedia.org/wiki/%E4%B8%AD%E9%96%93%E8%A1%A8%E7%8F%BE) と考えるとわかりやすいかもしれません。

XLAはHLOで定義されたグラフ("Computations")を、様々なハードウェアアーキテクチャの実行コードにコンパイルします。[Developing a new backend for XLA](https://www.tensorflow.org/xla/developing_new_backend) に記載されているように、XLAを新たなハードウェアで動作させることが容易であるという点で、XLAはモジュール化されていると言えます。[CPU (x86-64、ARM64) 向けの処理](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/cpu) と [NVIDIA GPU向けの処理](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla/service/gpu) は、TensorFlowのメインのソースコードツリーから参照することができます。

次に示す図は、XLAの内部で行われているコンパイル処理を示しています。

![](https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/how-does-xla-work.png)

XLAは、[CSE](https://ja.wikipedia.org/wiki/%E5%85%B1%E9%80%9A%E9%83%A8%E5%88%86%E5%BC%8F%E9%99%A4%E5%8E%BB) やオペレーション結合、計算時のメモリ割り当て解析といった、ターゲットに依存しない最適化や解析を行います。

ターゲットに依存しない最適化処理の後、XLAはHLO computationをバックエンドに転送します。バックエンドでは、ターゲット固有の情報を考慮してHLOレベルでの最適化を行います。例えば、バックエンドがXLA GPUである場合、よりGPUのプログラミングモデルに適したオペレーションの結合に加え、computationを複数のストリームへ分割して割り当てる方法も決定します。さらにバックエンドは、オペレーションの集合パターンが、最適化されたライブラリ呼び出しと一致するか確認します。

次に、ターゲット固有のコードを生成します。XLAに付随するCPUとGPUのバックエンドは、low-level IRとして [LLVM](http://llvm.org/) を採用し、最適化やコード生成もLLVMを使って行います。これらのバックエンドは、XLAのHLO computationを表現するために効率的なLLVM IRを出力し、LLVMを使ってLLVM IRからネイティブコードを生成します。

現在、GPUのバックエンドはLLVM NVPTXのバックエンド経由でNVIDIA GPUをサポートし、CPUのバックエンドは複数のCPUのISAをサポートしています。


## サポートするプラットフォーム

XLAは、x86-64とNVIDIA GPU向けに [JITコンパイル機能](https://www.tensorflow.org/xla/jit) を、x86-64とARM向けに [AOTコンパイル機能](https://www.tensorflow.org/xla/tfcompile) をサポートしています。
