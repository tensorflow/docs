#!/bin/bash
set -ex

# https://android.googlesource.com/platform/external/doclava/
# There's a debian package:
# https://packages.debian.org/unstable/doclava-aosp
# Install with:
#
#   $ sudo apt install doclava-aosp #v 6.0.1+r55-1+build1
#
# https://unix.stackexchange.com/questions/594841/how-do-i-assign-a-value-to-a-bash-variable-iff-that-variable-is-null-unassigned
DOCLAVA_JAR=${DOCLAVA_JAR:-'/usr/share/java/doclava.jar'}

# Install java clear silver templates with:
#
#   $ sudo apt install libjsilver-aosp-java #v 6.0.1+r55-1+build1
JSILVER_JAR=${JSILVER_JAR:-'/usr/share/java/jsilver.jar'}


######### DELETE OUTPUT_DIR #################

# Empty the output directory in case a class has been deleted
rm -rf "${OUTPUT_DIR:?}"/*
############ RUN DOCLAVA ###################

# $FEDERATED_DOCS is a space-separated string of url,file pairs.
read -a api_pairs <<< "${FEDERATED_DOCS}"
FEDERATED_PARAMS=""
for i in "${!api_pairs[@]}"; do
  api_pair_str="${api_pairs[$i]}"  # "url,api.txt"
  read -a api_pair <<< "${api_pair_str//,/ }"
  # Using the index as the API "name", build the federation params. Note that
  # using 0 as an API name will evaluate to false and cause rendering bugs,
  # so we preface with "api_".
  FEDERATED_PARAMS+=" -federate api_${i} ${api_pair[0]}"
  FEDERATED_PARAMS+=" -federationapi api_${i} ${api_pair[1]}"
done

# To install javadoc, for example, use
#
#   sudo apt install openjdk-11-jdk
#
# doclava doesn't work with openjdk-13
#   ```
#   javadoc: error - Class com.google.doclava.Doclava is not a valid doclet.
#   Note: As of JDK 13, the com.sun.javadoc API is no longer supported.
#   ```
#   It's used here: https://android.googlesource.com/platform/external/doclava/+/refs/heads/master/src/com/google/doclava/Doclava.java

# Each package in $PACKAGE needs to prefaced with -subpackages, so do that.
SUBPACKAGES=""
read -r -a packages <<< "${PACKAGE}"
for pkg in "${packages[@]}"; do
  SUBPACKAGES+=" -subpackages ${pkg}"
done
( # Capture the return code. it may be non-zero for minor errors.
  javadoc \
  -sourcepath "${SOURCE_PATH}" \
  -docletpath "${DOCLAVA_JAR}:${JSILVER_JAR}" \
  -doclet com.google.doclava.Doclava \
  -d "${OUTPUT_DIR}" \
  -toroot "${SITE_PATH}"/ \
  -yaml _toc.yaml \
  -templatedir "${TEMPLATES}" \
  -public \
  -devsite \
  ${FEDERATED_PARAMS} \
  ${SUBPACKAGES}
)


mv "${OUTPUT_DIR}"/reference/* "${OUTPUT_DIR}"

###################################################################
################### START OF POST-PROCESSING ######################
###################################################################
rm "${OUTPUT_DIR}/navtree_data.js" || true
rm "${OUTPUT_DIR}/hierarchy.html" || true

find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|${SITE_PATH}/reference|${SITE_PATH}|g"
find ${OUTPUT_DIR} -name "*.yaml" | xargs sed --in-place "s|${SITE_PATH}/reference|${SITE_PATH}|g"
find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|a href=\"reference/org/tensorflow|a href=\"${SITE_PATH}/org/tensorflow|g"
find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|a href=\"reference/com/google|a href=\"${SITE_PATH}/com/google|g"

JAVA_LANG=https://docs.oracle.com/javase/8/docs/api
find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|a href=\"reference/java/lang|a href=\"${JAVA_LANG}/java/lang|g"

find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place 's|<pre><code>|<pre class="prettyprint"><code>|g'

rm ${OUTPUT_DIR}/timestamp.js || true
rm ${OUTPUT_DIR}/lists.js || true
rm ${OUTPUT_DIR}/index.html || true

cp ${TEMPLATES}/screen.css ${OUTPUT_DIR}/


