# 커뮤니티 번역 문서들

이 문서들은 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도
불구하고 [공식 영문 문서](https://www.tensorflow.org/?hl=en)의 내용과 일치하지 않을 수 있습니다.
이 번역에 개선할 부분이 있다면
[tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기 바랍니다.
문서 번역이나 리뷰에 참여하려면 
[docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs)로
메일을 보내주시기 바랍니다.

# Community translations

Our TensorFlow community has translated these documents. Because community
translations are *best-effort*, there is no guarantee that this is an accurate
and up-to-date reflection of the
[official English documentation](https://www.tensorflow.org/?hl=en). 
If you have suggestions to improve this translation, please send a pull request 
to the [tensorflow/docs](https://github.com/tensorflow/docs) GitHub repository. 
To volunteer to write or review community translations, contact the
[docs@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).

# For new contributors

문서 번역에 참여해 주셔서 감사합니다.
번역에 참여하기 전에 번역된 [문서](https://github.com/tensorflow/docs/tree/master/site/ko)를 먼저 읽어 보길 권합니다.
번역 문서는 'ㅂ니다'체를 따르며 존칭이나 반말은 쓰지 않습니다.
가능한한 기존 문서의 스타일을 따라야 합니다. 

작업을 시작할 때 깃허브의 [드래프트 PR](https://help.github.com/en/articles/about-pull-requests#draft-pull-requests) 기능을 사용하여 작업 중임을 알려 주세요.
다른 사람이 작업 중인 파일이 아니라면 en 폴더 안의 파일을 ko 폴더 아래 같은 위치에 복사하여 시작합니다.
site/ko/ 는 텐서플로 1.x 버전을 위한 파일입니다.
site/ko/alpha/ 는 텐서플로 2.x 버전을 위한 파일입니다.

막다운(markdown)과 주석을 모두 번역합니다. 코드 셀(cell)은 실행하지 않습니다.
주피터 노트북은 조금만 수정하더라도 파일 소스 전체가 변경될 수 있습니다.
이런 파일은 깃허브에서 리뷰하기 어렵습니다.
기존 노트북에서 간단한 내용을 수정할 때는 가능하면 텍스트 편집기를 사용하여 직접 노트북 소스를 수정해야 합니다. 
노트북 파일의 번역이 완료되면 포크된 자신의 저장소에서 코랩(Colab)에서 실행이 잘되는지 확인해야 합니다.
코랩에서 실행에 문제가 없다면 리뷰를 요청합니다.

감사합니다!

Thanks for joining translation.
You should read existing [KO documents](https://github.com/tensorflow/docs/tree/master/site/ko) before starting translation.
You should use 'ㅂ니다' style, and not use the honorific or rude words.
You should follow the style of existing documents, as possible as you can.

Notify the work using Github's [Draft PR](https://help.github.com/en/articles/about-pull-requests#draft-pull-requests), when you start translating.
Copy a file in `en` folder to same location under `ko` folder if anybody doesn't work on the file,
and get it start.
`site/ko/` are for TensorFlow 1.x.
`site/ko/alpha` are for TensorFlow 2.x.

You should translate markdown and comments. You should not run code cells.
Whole file structure can be changed even if you modify only a chunk in the notebook.
It is hard to review such a file in Github.
You should use a text editor when you edit a few words of existing notebook.
You should test the notebook in your repository with Colab after you finish the translation.
You can request for review if there is no error.

Thanks!

# Korean translation guide

Some technical words in English do not have a natural translation. Do *not*
translate the following words:

*   mini-batch
*   batch
*   label
*   class
*   helper
*   hyperparameter
*   optimizer
*   one-hot encoding
*   epoch
*   callback
*   sequence
*   dictionary (in python)
*   embedding
*   padding
*   unit
*   node
*   nueron
*   target
*   import
*   checkpoint
*   compile
*   dropout
*   penalty
