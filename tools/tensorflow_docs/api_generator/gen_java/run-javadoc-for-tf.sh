#!/bin/bash
set -ex

# https://android.googlesource.com/platform/external/doclava/
# There's a debian package:
# https://packages.debian.org/unstable/doclava-aosp
# Install with:
#
#   $ sudo apt install doclava-aosp
DOCLAVA_JAR=/usr/share/java/doclava.jar

# Install java clear silver templates with:
#
#   $ sudo apt install libjsilver-aosp-java
JSILVER_JAR=/usr/share/java/jsilver.jar


######### DELETE OUTPUT_DIR #################

# Delete the output directory in case a class has been deleted
rm -rf "${OUTPUT_DIR}/reference"

############ RUN DOCLAVA ###################

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
  org.tensorflow
)


###################################################################
################### START OF POST-PROCESSING ######################
###################################################################
rm "${OUTPUT_DIR}/navtree_data.js"
rm "${OUTPUT_DIR}/reference/hierarchy.html"

find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|a href=\"reference/org/tensorflow|a href=\"${SITE_PATH}/reference/org/tensorflow|g"

JAVA_LANG=https://docs.oracle.com/javase/8/docs/api
find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place "s|a href=\"reference/java/lang|a href=\"${JAVA_LANG}/java/lang|g"

find ${OUTPUT_DIR} -name "*.html" | xargs sed --in-place 's|<pre><code>|<pre class="prettyprint"><code>|g'

rm ${OUTPUT_DIR}/timestamp.js
rm ${OUTPUT_DIR}/reference/lists.js
rm ${OUTPUT_DIR}/reference/index.html

cp ${TEMPLATES}/screen.css ${OUTPUT_DIR}/reference/


