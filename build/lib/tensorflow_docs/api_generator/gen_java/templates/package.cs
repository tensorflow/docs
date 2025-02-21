<?cs include:"doctype.cs" ?>
<?cs include:"macros.cs" ?>
<html devsite>
<?cs include:"head_tag.cs" ?>
<body>
<?cs # include:"header.cs" ?>

  <div style="width:720px">
    <div class="g-unit" id="doc-content">

    <div id="api-info-block">
    <div class="api-level">
      <?cs call:since_tags(package) ?>
      <?cs call:federated_refs(package) ?>
    </div>
    </div>

    <div id="jd-header">
      <!--package
      <h1><?cs var:package.name ?></h1-->
    </div><!-- end header -->

    <div id="naMessage"></div>

    <div id="jd-content">

    <?cs if:subcount(package.descr) ?>
      <div class="jd-descr">
        <?cs call:tag_list(package.descr) ?>
      </div>
    <?cs /if ?>

    <?cs def:class_table(label, classes) ?>
      <?cs if:subcount(classes) ?>
        <h3><?cs var:label ?></h3>
        <div class="jd-sumtable">
        <?cs call:class_link_table(classes) ?>
        </div>
      <?cs /if ?>
    <?cs /def ?>

    <?cs call:class_table("Interfaces", package.interfaces) ?>
    <?cs call:class_table("Classes", package.classes) ?>
    <?cs call:class_table("Enums", package.enums) ?>
    <?cs call:class_table("Exceptions", package.exceptions) ?>
    <?cs call:class_table("Errors", package.errors) ?>

    <?cs # include:"footer.cs" ?>
    </div><!-- end jd-content -->
    </div><!-- doc-content -->

    <?cs # include:"trailer.cs" ?>
  </div>
</body>
</html>
