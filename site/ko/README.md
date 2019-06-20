# 커뮤니티 번역 문서들

이 문서들은 텐서플로 커뮤니티에서 번역했습니다. 커뮤니티 번역 활동의 특성상 정확한 번역과 최신 내용을 반영하기 위해 노력함에도 불구하고
[공식 영문 문서](https://www.tensorflow.org/?hl=en)의 내용과 일치하지 않을 수 있습니다. 이 번역에 개선할 부분이
있다면 [tensorflow/docs](https://github.com/tensorflow/docs) 깃헙 저장소로 풀 리퀘스트를 보내주시기
바랍니다. 문서 번역이나 리뷰에 참여하려면
[docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)로
메일을 보내주시기 바랍니다.

노트: [site/en/r2](https://github.com/tensorflow/docs/tree/master/site/en/r2)
디렉토리에 있는 [텐서플로 2.0 베타](https://www.tensorflow.org/beta) 문서를 번역하는데 촛점을 맞춰 주세요.
2.0 릴리스를 준비하기 위해 TF 1.x 커뮤니티 문서는 더 이상 업데이트되지 않습니다. 이
[공지](https://groups.google.com/a/tensorflow.org/d/msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ)를
참고하세요.

# Community translations

Our TensorFlow community has translated these documents. Because community
translations are *best-effort*, there is no guarantee that this is an accurate
and up-to-date reflection of the
[official English documentation](https://www.tensorflow.org/?hl=en) and [Tensorflow Docs-Ko Translation](http://bit.ly/tf-docs-translation-status). 
If you have suggestions to improve this translation, please send a pull request 
to the [tensorflow/docs](https://github.com/tensorflow/docs) GitHub repository. 
To volunteer to write or review community translations, contact the
[docs@tensorflow.org list](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).

Note: Please focus translation efforts on
[TensorFlow 2.0 Beta](https://www.tensorflow.org/beta) in the
[site/en/r2](https://github.com/tensorflow/docs/tree/master/site/en/r2)
directory. TF 1.x community docs will no longer be updated as we prepare for the
2.0 release. See
[the announcement](https://groups.google.com/a/tensorflow.org/d/msg/docs/vO0gQnEXcSM/YK_ybv7tBQAJ).

# 처음 참여하는 사람들에게

문서 번역에 참여해 주셔서 감사합니다.
번역에 참여하기 전에 번역된 [문서](https://github.com/tensorflow/docs/tree/master/site/ko)를
먼저 읽어 보길 권합니다.
번역 문서는 'ㅂ니다'체를 따르며 존칭이나 반말은 쓰지 않습니다.
가능한한 기존 문서의 스타일을 따라야 합니다. 

작업을 시작하려면 [텐서플로 한글 문서 기여자](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
메일링 리스트와 [Tensorflow Docs-Ko Translation](http://bit.ly/tf-docs-translation-status) 구글 스프레드 시트에 작업 중임을 알려 주세요.
다른 사람이 작업 중인 파일이 아니라면 en 폴더 안의 파일을 ko 폴더 아래 같은 위치에 복사하여 시작합니다.
site/ko/ 는 텐서플로 1.x 버전을 위한 파일입니다.
site/ko/beta/ 는 텐서플로 2.x 버전을 위한 파일입니다.

막다운(markdown)과 주석을 모두 번역합니다. 코드 셀(cell)은 실행하지 않습니다.
주피터 노트북은 조금만 수정하더라도 파일 소스 전체가 변경될 수 있습니다.
이런 파일은 깃허브에서 리뷰하기 어렵습니다.
기존 노트북에서 간단한 내용을 수정할 때는 가능하면 텍스트 편집기를 사용하여 직접 노트북 소스를 수정해야 합니다. 
노트북 파일의 번역이 완료되면 포크된 자신의 저장소에서 코랩(Colab)에서 실행이 잘되는지 확인해야 합니다.
코랩에서 실행에 문제가 없다면 리뷰를 요청합니다.

번역과 관련되어 문의 사항이 있다면 언제든지
[텐서플로 한글 문서 기여자](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
메일링 리스트로 메일을 보내 주세요.

감사합니다!

# For new contributors

Thanks for joining the translation effort.
Please read the existing
[KO documents](https://github.com/tensorflow/docs/tree/master/site/ko)
before starting your translation.
You should use 'ㅂ니다' style and not use the honorific or rude words.
Follow the style of existing documents, as possible as you can.

After your translation is complete, notify the
[Korean TensorFlow Documentation Contributors](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
mailing list to coordinate a review.

Copy a file in `en` folder to same location under `ko` folder if anybody doesn't work on the file,
and get it start.
`site/ko/` are for TensorFlow 1.x.
`site/ko/beta` are for TensorFlow 2.x.

You should translate markdown and comments. You should not run code cells.
Whole file structure can be changed even if you modify only a chunk in the notebook.
It is hard to review such a file in GitHub.
You should use a text editor when you edit a few words of existing notebook.
You should test the notebook in your repository with Colab after you finish the translation.
You can request for review if there is no error.

If you have any question about translation, feel free to contact
[Korean TensorFlow Documentation Contributors](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
mailing list.

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
