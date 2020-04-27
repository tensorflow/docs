<?cs include:"doctype.cs" ?>
<?cs include:"macros.cs" ?>
<html>
<?cs include:"head_tag.cs" ?>
<body>
<?cs include:"header.cs" ?>

<div class="g-unit" id="doc-content">

<div id="api-info-block">
<div>
  <?cs call:since_tags(package) ?>
  <?cs call:federated_refs(package) ?>
</div>
</div>

<div id="jd-header">
  package
  <h1><?cs var:package.name ?></b></h1>
  <div class="jd-nav">
      <a class="jd-navlink" href="package-summary.html">Classes</a> | Description
  </div>
</div><!-- end header -->

<div id="naMessage"></div>

<div id="jd-content">
<div class="jd-descr">
<p><?cs call:tag_list(package.descr) ?></p>
</div>

<?cs include:"footer.cs" ?>
</div><!-- end jd-content -->
</div> <!-- end doc-content -->

<?cs include:"trailer.cs" ?>

</body>
</html>
