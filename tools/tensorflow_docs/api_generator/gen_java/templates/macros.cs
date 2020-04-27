<?cs # A link to a package ?><?cs
def:package_link(pkg) ?>
  <a href="<?cs var:toroot ?><?cs var:pkg.link ?>"><?cs var:pkg.name ?></a><?cs
/def ?>

<?cs # A link to a type, or not if it's a primitive type
        link: whether to create a link at the top level, always creates links in
              recursive invocations.
              Overloaded version to support use of 'nav' parameter, which when true,
              will not include the generics in the class name (good for sidenav lists)
        Expects the following fields:
            .name
            .link
            .isPrimitive
            .superBounds.N.(more links)   (... super ... & ...)
            .extendsBounds.N.(more links) (... extends ... & ...)
            .typeArguments.N.(more links) (< ... >)
?><?cs
def:type_link_impl(type, link) ?><?cs call:type_link_impl2(type, link, "false") ?><?cs /def ?><?cs
def:type_link_impl2(type, link, nav) ?><?cs
  if:type.link && link=="true" ?><?cs
    if:type.federated ?><a href="<?cs var:type.link ?>"><?cs
      var:type.label ?></a><?cs
    else ?><a href="<?cs var:toroot ?><?cs var:type.link ?>"><?cs var:type.label ?></a><?cs
    /if ?><?cs
  else ?><?cs var:type.label ?><?cs
  /if ?><?cs
  if:subcount(type.extendsBounds) ?><?cs
      each:t=type.extendsBounds ?><?cs
          if:first(t) ?>&nbsp;extends&nbsp;<?cs else ?>&nbsp;&amp;&nbsp;<?cs /if ?><?cs
          call:type_link_impl(t, "true") ?><?cs
      /each ?><?cs
  /if ?><?cs
  if:subcount(type.superBounds) ?><?cs
      each:t=type.superBounds ?><?cs
          if:first(t) ?>&nbsp;super&nbsp;<?cs else ?>&nbsp;&amp;&nbsp;<?cs /if ?><?cs
          call:type_link_impl(t, "true") ?><?cs
      /each ?><?cs
  /if ?><?cs
  if:subcount(type.typeArguments) && nav=="false"
      ?>&lt;<?cs each:t=type.typeArguments ?><?cs call:type_link_impl(t, "true") ?><?cs
          if:!last(t) ?>,&nbsp;<?cs /if ?><?cs
      /each ?>&gt;<?cs
  /if ?><?cs
/def ?>

<?cs def:class_name(type) ?><?cs call:type_link_impl(type, "false") ?><?cs /def ?>
<?cs def:type_link2(type,nav) ?><?cs call:type_link_impl2(type, "true", nav) ?><?cs /def ?>
<?cs def:type_link(type) ?><?cs call:type_link2(type, "false") ?><?cs /def ?>

<?cs # a conditional link.
      if the "condition" parameter evals to true then the link is displayed
      otherwise only the text is displayed
?><?cs
def:cond_link(text, root, path, condition) ?><?cs
  if:condition ?><a href="<?cs var:root ?><?cs var:path ?>"><?cs /if ?><?cs var:text ?><?cs if:condition ?></a><?cs /if ?><?cs
/def ?>

<?cs # A comma separated parameter list ?><?cs
def:parameter_list(params) ?><?cs
  each:param = params ?><?cs
      call:type_link(param.type)?> <?cs
      var:param.name ?><?cs
      if: name(param)!=subcount(params)-1?>, <?cs /if ?><?cs
  /each ?><?cs
/def ?>

<?cs # Print a list of tags (e.g. description text ?><?cs
def:tag_list(tags) ?><?cs
  each:tag = tags ?><?cs
      if:tag.name == "Text" ?><?cs var:tag.text?><?cs
      elif:tag.kind == "@more" ?><p><?cs
      elif:tag.kind == "@see" ?><code><a href="<?cs if:string.find(tag.href, federatedUrl) == -1 ?><?cs var:toroot ?><?cs /if ?><?cs var:tag.href ?>"><?cs var:html_escape(tag.label) ?></a></code><?cs
      elif:tag.kind == "@seeHref" ?><a href="<?cs var:tag.href ?>"><?cs var:tag.label ?></a><?cs
      elif:tag.kind == "@seeJustLabel" ?><?cs var:tag.label ?><?cs
      elif:tag.kind == "@value" ?><code><a href="<?cs if:string.find(tag.href, federatedUrl) == -1 ?><?cs var:toroot ?><?cs /if ?>"><?cs var:html_escape(tag.text) ?></a></code><?cs
      elif:tag.kind == "@code" ?><code><?cs var:html_escape(tag.text) ?></code><?cs
      elif:tag.kind == "@samplecode" ?><pre><?cs var:tag.text ?></pre><?cs
      elif:tag.name == "@sample" ?><pre><?cs var:tag.text ?></pre><?cs
      elif:tag.name == "@include" ?><?cs var:tag.text ?><?cs
      elif:tag.kind == "@docRoot" ?><?cs var:toroot ?><?cs
      elif:tag.kind == "@sdkCurrent" ?><?cs var:sdk.current ?><?cs
      elif:tag.kind == "@sdkCurrentVersion" ?><?cs var:sdk.version ?><?cs
      elif:tag.kind == "@sdkCurrentRelId" ?><?cs var:sdk.rel.id ?><?cs
      elif:tag.kind == "@sdkPlatformVersion" ?><?cs var:sdk.platform.version ?><?cs
      elif:tag.kind == "@sdkPlatformApiLevel" ?><?cs var:sdk.platform.apiLevel ?><?cs
      elif:tag.kind == "@sdkPlatformMajorMinor" ?><?cs var:sdk.platform.majorMinor ?><?cs
      elif:tag.kind == "@sdkPlatformReleaseDate" ?><?cs var:sdk.platform.releaseDate ?><?cs
      elif:tag.kind == "@sdkPlatformDeployableDate" ?><?cs var:sdk.platform.deployableDate ?><?cs
      elif:tag.kind == "@adtZipVersion" ?><?cs var:adt.zip.version ?><?cs
      elif:tag.kind == "@adtZipDownload" ?><?cs var:adt.zip.download ?><?cs
      elif:tag.kind == "@adtZipBytes" ?><?cs var:adt.zip.bytes ?><?cs
      elif:tag.kind == "@adtZipChecksum" ?><?cs var:adt.zip.checksum ?><?cs
      elif:tag.kind == "@inheritDoc" ?><?cs # This is the case when @inheritDoc is in something
                                              that doesn't inherit from anything?><?cs
      elif:tag.kind == "@attr" ?><?cs
      else ?>{<?cs var:tag.name?> <?cs var:tag.text ?>}<?cs
      /if ?><?cs
  /each ?><?cs
/def ?>

<?cs # Show the short-form description of something.  These come from shortDescr and deprecated ?><?cs
def:short_descr(obj) ?><?cs
  if:subcount(obj.deprecated) ?>
      <em>This <?cs var:obj.kind ?> was deprecated
      in API level <?cs var:obj.deprecatedsince ?>.
      <?cs call:tag_list(obj.deprecated) ?></em><?cs
  else ?><?cs call:tag_list(obj.shortDescr) ?><?cs
  /if ?><?cs
/def ?>

<?cs # Show the red box with the deprecated warning ?><?cs
def:deprecated_warning(obj) ?><?cs
  if:subcount(obj.deprecated) ?><p>
  <p class="caution">
      <strong>This <?cs var:obj.kind ?> was deprecated
      in API level <?cs var:obj.deprecatedsince ?></strong>.<br/> <?cs
      call:tag_list(obj.deprecated) ?>
  </p><?cs
  /if ?><?cs
/def ?>

<?cs # print the See Also: section ?><?cs
def:see_also_tags(also) ?><?cs
  if:subcount(also) ?>
  <div class="jd-tagdata">
      <h5 class="jd-tagtitle">See Also</h5>
      <ul class="nolist"><?cs
        each:tag=also ?><li><?cs
            if:tag.kind == "@see" ?><code><a href="<?cs var:toroot ?><?cs var:tag.href ?>"><?cs
                    var:tag.label ?></a></code><?cs
            elif:tag.kind == "@seeHref" ?><a href="<?cs var:tag.href ?>"><?cs var:tag.label ?></a><?cs
            elif:tag.kind == "@seeJustLabel" ?><?cs var:tag.label ?><?cs
            else ?>[ERROR: Unknown @see kind]<?cs
            /if ?></li><?cs
        /each ?>
      </ul>
  </div><?cs
  /if ?>
<?cs /def ?>

<?cs # print the API Level ?><?cs
def:since_tags(obj) ?><?cs
if:reference.apilevels && obj.since ?>
  Added in API level <?cs var:obj.since ?><?cs
/if ?><?cs
/def ?>
<?cs def:federated_refs(obj) ?>
  <?cs if:subcount(obj.federated) ?>
    <div>
    Also:
    <?cs each:federated=obj.federated ?>
      <a href="<?cs var:federated.url ?>"><?cs var:federated.name ?></a><?cs
      if:!last(federated) ?>,<?cs /if ?>
    <?cs /each ?>
    </div>
  <?cs /if ?>
<?cs /def ?>
<?cs # Print the long-form description for something.
       Uses the following fields: deprecated descr seeAlso since ?><?cs
def:description(obj) ?><?cs
  call:deprecated_warning(obj) ?>
  <div class="jd-tagdata jd-tagdescr"><p><?cs call:tag_list(obj.descr) ?></p></div><?cs
  if:subcount(obj.attrRefs) ?>
  <div class="jd-tagdata">
      <h5 class="jd-tagtitle">Related XML Attributes</h5>
      <ul class="nolist"><?cs
        each:attr=obj.attrRefs ?>
            <li><a href="<?cs var:toroot ?><?cs var:attr.href ?>"><?cs var:attr.name ?></a></li><?cs
        /each ?>
      </ul>
  </div><?cs
  /if ?><?cs
  if:subcount(obj.paramTags) ?>
  <div class="jd-tagdata">
      <h5 class="jd-tagtitle">Parameters</h5>
      <table class="jd-tagtable"><?cs
      each:tag=obj.paramTags ?>
        <tr>
          <th><?cs if:tag.isTypeParameter ?>&lt;<?cs /if ?><?cs var:tag.name
                  ?><?cs if:tag.isTypeParameter ?>&gt;<?cs /if ?></th>
          <td><?cs call:tag_list(tag.comment) ?></td>
        </tr><?cs
      /each ?>
      </table>
  </div><?cs
  /if ?><?cs
  if:subcount(obj.returns) ?>
  <div class="jd-tagdata">
      <h5 class="jd-tagtitle">Returns</h5>
      <ul class="nolist"><li><?cs call:tag_list(obj.returns) ?></li></ul>
  </div><?cs
  /if ?><?cs
  if:subcount(obj.throws) ?>
  <div class="jd-tagdata">
      <h5 class="jd-tagtitle">Throws</h5>
      <table class="jd-tagtable"><?cs
      each:tag=obj.throws ?>
        <tr>
            <th><?cs call:type_link(tag.type) ?></th>
            <td><?cs call:tag_list(tag.comment) ?></td>
        </tr><?cs
      /each ?>
      </table>
  </div><?cs
  /if ?><?cs
  call:see_also_tags(obj.seeAlso) ?><?cs
/def ?>

<?cs # A table of links to classes with descriptions, as in a package file or the nested classes ?><?cs
def:class_link_table(classes) ?><?cs
  set:count = #1 ?>
  <table class="jd-sumtable-expando"><?cs
      each:cl=classes ?>
        <tr class="<?cs if:count % #2 ?>alt-color<?cs /if ?> api apilevel-<?cs var:cl.type.since ?>" >
              <td class="jd-linkcol"><?cs call:type_link(cl.type) ?></td>
              <td class="jd-descrcol" width="100%"><?cs call:short_descr(cl) ?>&nbsp;</td>
          </tr><?cs set:count = count + #1 ?><?cs
      /each ?>
  </table><?cs
/def ?>

<?cs # A list of links to classes, for use in the side navigation of classes when viewing a package (panel nav) ?><?cs
def:class_link_list(label, classes) ?><?cs
  if:subcount(classes) ?>
    <li><h2><?cs var:label ?></h2>
      <ul><?cs
      each:cl=classes ?>
        <li class="api apilevel-<?cs var:cl.type.since ?>"><?cs call:type_link2(cl.type,"true") ?></li><?cs
      /each ?>
      </ul>
    </li><?cs
  /if ?><?cs
/def ?>

<?cs # A list of links to classes, for use in the side navigation of classes when viewing a class (panel nav) ?><?cs
def:list(label, classes) ?><?cs
  if:subcount(classes) ?>
    <li><h2><?cs var:label ?></h2>
      <ul><?cs
      each:cl=classes ?>
          <li class="<?cs if:class.name == cl.label?>selected <?cs /if ?>api apilevel-<?cs var:cl.since ?>"><?cs call:type_link2(cl,"true") ?></li><?cs
      /each ?>
      </ul>
    </li><?cs
  /if ?><?cs
/def ?>

<?cs # A list of links to packages, for use in the side navigation of packages (panel nav) ?><?cs
def:package_link_list(packages) ?><?cs
  each:pkg=packages ?>
    <li class="<?cs if:(class.package.name == pkg.name) || (package.name == pkg.name)?>selected <?cs /if ?>api apilevel-<?cs var:pkg.since ?>"><?cs call:package_link(pkg) ?></li><?cs
  /each ?><?cs
/def ?>

<?cs # An expando trigger ?><?cs
def:expando_trigger(id, default) ?>
  <a href="#" onclick="return toggleInherited(this, null)" id="<?cs var:id ?>" class="jd-expando-trigger closed"
          ><img id="<?cs var:id ?>-trigger"
          src="<?cs var:toroot ?>assets/images/triangle-<?cs var:default ?>.png"
          class="jd-expando-trigger-img" /></a><?cs
/def ?>

<?cs # An expandable list of classes ?><?cs
def:expandable_class_list(id, classes, default) ?>
  <div id="<?cs var:id ?>">
      <div id="<?cs var:id ?>-list"
              class="jd-inheritedlinks"
              <?cs if:default != "list" ?>style="display: none;"<?cs /if ?>
              >
          <?cs if:subcount(classes) <= #20 ?>
            <?cs each:cl=classes ?>
              <?cs call:type_link(cl.type) ?><?cs if:!last(cl) ?>,<?cs /if ?>
            <?cs /each ?>
          <?cs else ?>
            <?cs set:leftovers = subcount(classes) - #15 ?>
            <?cs loop:i = #0, #14, #1 ?>
              <?cs with:cl=classes[i] ?>
                <?cs call:type_link(cl.type) ?>,
              <?cs /with ?>
              <?cs  if:(#i == #14) ?>and
                <a href="#" onclick="return toggleInherited(document.getElementById('<?cs
                   var:id ?>', null))"><?cs var:leftovers ?> others.</a>
              <?cs /if ?>
            <?cs /loop ?>
          <?cs /if ?>
      </div>
      <div id="<?cs var:id ?>-summary"
              <?cs if:default != "summary" ?>style="display: none;"<?cs /if ?>
              ><?cs
          call:class_link_table(classes) ?>
      </div>
  </div><?cs
/def ?>

<?cs include:"components.cs" ?>

