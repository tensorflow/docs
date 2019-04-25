#!/bin/bash

function create_markdown() {
  dirname=`ls -1 site/${lang}`

  for dir in ${dirname}; do
    absdir=site/${lang}/${dir}
    if [ -d $absdir ]; then
      subdirs=`ls -1 ${absdir}`
      for subdir in ${subdirs}; do
          mkdir -p md/${lang}/${dir}/${subdir}
          jupyter nbconvert --to markdown ${absdir}/${subdir}/*.ipynb --output-dir md/${lang}/${dir}/${subdir}
      done
    fi
  done
}

function exec_redpen() {
  termfile=site/${lang}/terminologies.txt
  redpen --conf site/${lang}/redpen-conf.xml md/${lang}/*/*/*
}

echo "Please choose language."
read lang
case ${lang} in en | ja | ko | pt | ru | tr | zh-cn) echo "lang=${lang}";;
  *) echo "Please choose proper language" && exit;;
esac

create_markdown
exec_redpen
