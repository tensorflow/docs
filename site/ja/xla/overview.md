# XLA 概要

<div style="width:50%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:50%" src="https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/compiler/xla/g3doc/images/xlalogo.png">
</div>

Note: XLAは現在開発中であるため、特定の状況でメモリ使用量の増大や性能の悪化を引き起こす場合があります。

Note: これらのドキュメントは私たちTensorFlowコミュニティが翻訳したものです。コミュニティによる
翻訳は**ベストエフォート**であるため、この翻訳が正確であることや[英語の公式ドキュメント](https://www.tensorflow.org/?hl=en)の
最新の状態を反映したものであることを保証することはできません。
この翻訳の品質を向上させるためのご意見をお持ちの方は、GitHubリポジトリ[tensorflow/docs](https://github.com/tensorflow/docs)にプルリクエストをお送りください。
\
コミュニティによる翻訳やレビューに参加していただける方は、
[docs-ja@tensorflow.org メーリングリスト](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)にご連絡ください。

XLA(Accelerated Linear Algebra)は線形代数の演算に特化したコンパイラで、XLAを使うことでTensorFlowの演算を最適化し、メモリ使用量、性能、サーバやモバイル環境での移植性の面での改善が期待できます。現在のところ、ほとんどのユーザにとってXLAを使うことによる大きな恩恵は得られないかもしれませんが、[just-in-time (JIT) コンパイル機能](https://www.tensorflow.org/xla/jit) や [ahead-of-time (AOT) コンパイル機能](https://www.tensorflow.org/xla/tfcompile) を通して、実験的にXLAを使っていただくのは歓迎です。ただし、新たなハードウエアアクセラレータの開発者については、XLAを試してみることをおすすめします。

XLAは実験的なフレームワークであり、現在活発に開発されています。既存のオペレーションのセマンティクスが変わることはほとんどないと思いますが、重要なユースケースに対応するために新たなオペレーションが追加されることがあります。XLAチームは、GitHubを通したコミュニティへの貢献や、不足している機能に関するフィードバックを歓迎します。


## なぜXLAを開発したか？

TensorFlowと連携するXLAを開発した目的はいくつかあります。

* **実行速度の向上**: サブグラフをコンパイルし、TensorFlowランタイムのオーバヘッドを削減することで、軽量なオペレーションの実行時間を短縮します。また、複数オペレーションを結合することで、メモリのオーバヘッドを削減します。さらに、既知のテンソルの形状に特化することで、より積極的に定数畳み込みができるようにします。
* **メモリ使用量の改善**: メモリ使用量の解析とスケジューリングによって、オペレーションの中間データを保持する領域を削減します。
* **独自オペレーションへの依存度削減**: 自動的に結合された低レベルなオペレーションの性能を向上させ、人手による独自オペレーションと同等の性能を得られるようにすることで、独自オペレーションを作成する必要性が無くなります。
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
