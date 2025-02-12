<?cs include:"doctype.cs" ?>
<?cs include:"macros.cs" ?>
<html devsite>
<?cs include:"head_tag.cs" ?>
  <body>
  <div style="width:720px">
    <div id="api-info-block">

    <?cs # are there inherited members ?>
    <?cs each:cl=class.inherited ?>
      <?cs if:subcount(cl.methods) ?>
       <?cs set:inhmethods = #1 ?>
      <?cs /if ?>
      <?cs if:subcount(cl.constants) ?>
       <?cs set:inhconstants = #1 ?>
      <?cs /if ?>
      <?cs if:subcount(cl.fields) ?>
       <?cs set:inhfields = #1 ?>
      <?cs /if ?>
      <?cs if:subcount(cl.attrs) ?>
       <?cs set:inhattrs = #1 ?>
      <?cs /if ?>
    <?cs /each ?>

    <div class="api-level">
      <?cs call:since_tags(class) ?>
      <?cs call:federated_refs(class) ?>
    </div>
    </div><!-- end api-info-block -->

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ======== START OF CLASS DATA ======== -->


    <?cs if:page.title ?>
    <div id="jd-header">
      <?cs var:class.scope ?> <?cs var:class.static ?> <?cs var:class.final ?>  <?cs var:class.abstract ?> <?cs var:class.kind ?>
      <b><?cs var:page.title ?></b>
    </div><!-- end jd-header -->
    <?cs /if ?>

    <div id="naMessage"></div>

    <div id="jd-content">

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>

    <?cs if:subcount(class.subclasses.direct) && !class.subclasses.hidden ?>
    <table class="jd-sumtable jd-sumtable-subclasses"><tr><td colspan="3" style="border:none;margin:0;padding:0;">
    <?cs # call:expando_trigger("subclasses-direct", "closed") ?>Known Direct Subclasses
    <?cs call:expandable_class_list("subclasses-direct", class.subclasses.direct, "list") ?>
    </td></tr></table>
    <?cs /if ?>

    <?cs if:subcount(class.subclasses.indirect) && !class.subclasses.hidden ?>
    <table class="jd-sumtable jd-sumtable-subclasses"><tr><td colspan="3" style="border:none;margin:0;padding:0;font-size:85%;">
    <?cs # call:expando_trigger("subclasses-indirect", "closed") ?>Known Indirect Subclasses
    <?cs call:expandable_class_list("subclasses-indirect", class.subclasses.indirect, "list") ?>
    </td></tr></table>
    <?cs /if ?>

    <div class="jd-descr">
    <?cs call:deprecated_warning(class) ?>
    <?cs if:subcount(class.descr) ?>
    <p><?cs call:tag_list(class.descr) ?></p>
    <?cs /if ?>
    <?cs call:see_also_tags(class.seeAlso) ?>
    </div><!-- jd-descr -->


    <?cs # summary macros ?>

    <?cs def:write_method_summary(methods, included) ?>
    <?cs set:count = #1 ?>
    <?cs each:method = methods ?>
        <?cs # The apilevel-N class MUST BE LAST in the sequence of class names ?>
        <tr>
          <td class="jd-typecol">
                <?cs var:method.abstract ?>
                <?cs var:method.synchronized ?>
                <?cs var:method.final ?>
                <?cs var:method.static ?>
                <?cs call:type_link(method.generic) ?>
                <?cs call:type_link(method.returnType) ?>
          </td>
          <td class="jd-linkcol" width="100%">
              <div class="jd-hang">
                <span class="sympad"><?cs call:cond_link(method.name, toroot, method.href, included) ?></span>(<?cs call:parameter_list(method.params) ?>)
                <?cs if:subcount(method.shortDescr) || subcount(method.deprecated) ?>
                  <div class="jd-descrdiv"><?cs call:short_descr(method) ?></div>
                <?cs /if ?>
              </div>
          </td>
        </tr>
    <?cs set:count = count + #1 ?>
    <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_field_summary(fields, included) ?>
    <?cs set:count = #1 ?>
        <?cs each:field=fields ?>
          <tr>
              <td class="jd-typecol">
              <?cs var:field.scope ?>
              <?cs var:field.static ?>
              <?cs var:field.final ?>
              <?cs call:type_link(field.type) ?></td>
              <td class="jd-linkcol"><?cs call:cond_link(field.name, toroot, field.href, included) ?></td>
              <td class="jd-descrcol" width="100%"><?cs call:short_descr(field) ?></td>
          </tr>
          <?cs set:count = count + #1 ?>
        <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_constant_summary(fields, included) ?>
    <?cs set:count = #1 ?>
        <?cs each:field=fields ?>
        <tr>
            <td class="jd-typecol"><?cs call:type_link(field.type) ?></td>
            <td class="jd-linkcol"><?cs call:cond_link(field.name, toroot, field.href, included) ?></td>
            <td class="jd-descrcol" width="100%"><?cs call:short_descr(field) ?></td>
        </tr>
        <?cs set:count = count + #1 ?>
        <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_attr_summary(attrs, included) ?>
    <?cs set:count = #1 ?>
        <tr>
            <td><em>Attribute Name</em></td>
        </tr>
        <?cs each:attr=attrs ?>
        <tr>
            <td class="jd-linkcol"><?cs if:included ?><a href="<?cs var:toroot ?><?cs var:attr.href ?>"><?cs /if ?><?cs var:attr.name ?><?cs if:included ?></a><?cs /if ?></td>
        </tr>
        <?cs set:count = count + #1 ?>
        <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_inners_summary(classes) ?>
    <?cs set:count = #1 ?>
      <?cs each:cl=class.inners ?>
        <tr>
          <td class="jd-typecol">
            <?cs var:cl.scope ?>
            <?cs var:cl.static ?>
            <?cs var:cl.final ?>
            <?cs var:cl.abstract ?>
            <?cs var:cl.kind ?></td>
          <td class="jd-linkcol" colspan="2"><?cs call:type_link(cl.type) ?></td>
          <td class="jd-descrcol" width="100%"><?cs call:short_descr(cl) ?>&nbsp;</td>
        </tr>
        <?cs set:count = count + #1 ?>
        <?cs /each ?>
    <?cs /def ?>

    <?cs # end macros ?>

    <div class="jd-descr">
    <?cs # make sure there's a summary view to display ?>
    <?cs if:subcount(class.inners)
         || subcount(class.attrs)
         || inhattrs
         || subcount(class.enumConstants)
         || subcount(class.constants)
         || inhconstants
         || subcount(class.fields)
         || inhfields
         || subcount(class.ctors.public)
         || subcount(class.ctors.protected)
         || subcount(class.methods.public)
         || subcount(class.methods.protected)
         || inhmethods ?>
    <section id="xml-attributes">

    <?cs if:subcount(class.inners) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ======== NESTED CLASS SUMMARY ======== -->
    <section>
      <h3>Nested Classes</h3>
      <table id="nestedclasses" class="jd-sumtable">
        <?cs call:write_inners_summary(class.inners) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <?cs if:subcount(class.attrs) ?>
    <!-- =========== FIELD SUMMARY =========== -->
    <section id="lattrs"><h3>XML Attributes</h3>
      <?cs call:write_attr_summary(class.attrs, 1) ?>
    </section>
    <?cs /if ?>

    <?cs # if there are inherited attrs, write the table ?>
    <?cs if:inhattrs ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== FIELD SUMMARY =========== -->
    <section id="inhattrs">
      <h3>Inherited XML Attributes</h3>
    <?cs each:cl=class.inherited ?>
      <?cs if:subcount(cl.attrs) ?>
        <div class="expandable">
          <span class="showalways">
            <?cs # call:expando_trigger("inherited-attrs-"+cl.qualified, "closed") ?>
            From <?cs var:cl.kind ?>
            <?cs call:cond_link(cl.qualified, toroot, cl.link, cl.included) ?>
          </span>
          <div id="inherited-attrs-<?cs var:cl.qualified ?>">
            <div id="inherited-attrs-<?cs var:cl.qualified ?>-list"
                  class="jd-inheritedlinks">
            </div>
            <div id="inherited-attrs-<?cs var:cl.qualified ?>-summary">
              <table class="jd-sumtable-expando">
                <?cs call:write_attr_summary(cl.attrs, cl.included) ?>
              </table>
            </div>
          </div>
        </div>
      <?cs /if ?>
    <?cs /each ?>
    </section>
    <?cs /if ?>

    <?cs if:subcount(class.enumConstants) && class.kind != "enum" ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== ENUM CONSTANT SUMMARY =========== -->
    <section>
      <h3>Enum Values</h3>
      <table id="enumconstants" class="jd-sumtable">
      <?cs set:count = #1 ?>
          <?cs each:field=class.enumConstants ?>
      <?cs # BUG: This adds link to the type (which we don't want) but does NOT add a link to the enum value (which it needs).
              See PlusOneButton.Size ?>
          <tr>
              <td class="jd-linkcol"><?cs call:cond_link(field.name, toroot, field.href, cl.included) ?>&nbsp;</td>
          </tr>
          <?cs set:count = count + #1 ?>
          <?cs /each ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs if:subcount(class.constants) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== ENUM CONSTANT SUMMARY =========== -->
    <section id="constants"><h3>Constants</h3>
      <table class="jd-sumtable">
        <?cs call:write_constant_summary(class.constants, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs # if there are inherited constants, write the table ?>
    <?cs if:inhconstants ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== ENUM CONSTANT SUMMARY =========== -->
    <section id="inhconstants">
      <h3>Inherited Constants</h3>
      <?cs each:cl=class.inherited ?>
        <?cs if:subcount(cl.constants) ?>
          <div class="expandable">
            <span class="showalways">
              <?cs # call:expando_trigger("inherited-constants-"+cl.qualified, "closed") ?>From <?cs var:cl.kind ?>
              <?cs call:cond_link(cl.qualified, toroot, cl.link, cl.included) ?>
            </span>
            <div id="inherited-constants-<?cs var:cl.qualified ?>">
              <div id="inherited-constants-<?cs var:cl.qualified ?>-list"
                    class="jd-inheritedlinks">
              </div>
              <div id="inherited-constants-<?cs var:cl.qualified ?>-summary">
                <table class="jd-sumtable-expando">
                  <?cs call:write_constant_summary(cl.constants, cl.included) ?>
                </table>
              </div>
            </div>
          </div>
        <?cs /if ?>
      <?cs /each ?>
    </section>
    <?cs /if ?>

    <?cs if:subcount(class.fields) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== FIELD SUMMARY =========== -->
    <section id="lfields"><h3>Fields</h3>
      <table class="jd-sumtable">
        <?cs call:write_field_summary(class.fields, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs # if there are inherited fields, write the table ?>
    <?cs if:inhfields ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== FIELD SUMMARY =========== -->
    <section id="inhfields">
      <h3>Inherited Fields</h3>
      <?cs each:cl=class.inherited ?>
        <?cs if:subcount(cl.fields) ?>
        <div class="expandable">
          <span class="showalways">
            <?cs # call:expando_trigger("inherited-fields-"+cl.qualified, "closed") ?>From <?cs var:cl.kind ?>
            <?cs call:cond_link(cl.qualified, toroot, cl.link, cl.included) ?>
          </span>
          <div id="inherited-fields-<?cs var:cl.qualified ?>">
            <div id="inherited-fields-<?cs var:cl.qualified ?>-list"
                  class="jd-inheritedlinks">
            </div>
            <div id="inherited-fields-<?cs var:cl.qualified ?>-summary">
              <table class="jd-sumtable-expando">
              <?cs call:write_field_summary(cl.fields, cl.included) ?>
              </table>
            </div>
          </div>
        </div>
        <?cs /if ?>
      <?cs /each ?>
      </section>
    <?cs /if ?>

    <?cs if:subcount(class.ctors.public) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ======== CONSTRUCTOR SUMMARY ======== -->
    <section>
      <h3>Public Constructors</h3>
      <table id="pubctors" class="jd-sumtable">
      <?cs call:write_method_summary(class.ctors.public, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs if:subcount(class.ctors.protected) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ======== CONSTRUCTOR SUMMARY ======== -->
    <section>
      <h3>Protected Constructors</h3>
      <table id="proctors" class="jd-sumtable">
      <?cs call:write_method_summary(class.ctors.protected, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs # don't print public methods for enum types because they are not part of API ?>
    <?cs if:subcount(class.methods.public) && class.kind != "enum" ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========== METHOD SUMMARY =========== -->
    <section>
      <h3>Public Methods</h3>
      <table id="pubmethods" class="jd-sumtable">
      <?cs call:write_method_summary(class.methods.public, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs if:subcount(class.methods.protected) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========== METHOD SUMMARY =========== -->
    <section>
      <h3>Protected Methods</h3>
      <table id="promethods" class="jd-sumtable">
        <?cs call:write_method_summary(class.methods.protected, 1) ?>
      </table>
    </section>
    <?cs /if ?>

    <?cs # if there are inherited methods, write the table ?>
    <?cs if:inhmethods ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- =========== METHOD SUMMARY ============ -->
    <section id="inhmethods">
      <h3>Inherited Methods</h3>
      <?cs each:cl=class.inherited ?>
        <?cs if:subcount(cl.methods) ?>
        <div class="expandable">
          <span class="showalways">
            <?cs # call:expando_trigger("inherited-methods-"+cl.qualified, "closed") ?>From <?cs var:cl.kind ?>
            <?cs call:cond_link(cl.qualified, toroot, cl.link, cl.included) ?>
          </span>
          <div id="inherited-methods-<?cs var:cl.qualified ?>">
            <div id="inherited-methods-<?cs var:cl.qualified ?>-list"
                  class="jd-inheritedLinks">
            </div>
            <div id="inherited-methods-<?cs var:cl.qualified ?>-summary">
              <table class="jd-sumtable-expando">
              <?cs call:write_method_summary(cl.methods, cl.included) ?>
              </table>
            </div>
          </div>
        </div>
        <?cs /if ?>
      <?cs /each ?>
      </section>
    <?cs /if ?>

    </section><!--xml-attributes-->
    <?cs /if ?><!--subcount(class.inners) || subcount(class.attrs) || ...-->
    </div><!-- class="jd-descr" (end of Summary) -->

    <!-- Details -->

    <?cs def:write_field_details(fields) ?>
    <?cs each:field=fields ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <?cs # the A tag in the next line must remain where it is, so that Eclipse can parse the docs ?>
    <A NAME="<?cs var:field.anchor ?>"></A>
    <?cs # The apilevel-N class MUST BE LAST in the sequence of class names ?>
    <div class="jd-details">
        <h4 class="jd-details-title">
          <span class="normal">
            <?cs var:field.scope ?>
            <?cs var:field.static ?>
            <?cs var:field.final ?>
            <?cs # detect if the type is the same as the current page's class and if
            so, only print the label, instead of a link to reduce redundant linking.?>
            <?cs if:page.title==field.type.label ?>
              <?cs var:field.type.label ?>
            <?cs else ?>
              <?cs call:type_link(field.type) ?>
            <?cs /if ?>
          </span>
            <strong><?cs var:field.name ?></strong>
        </h4>
          <div class="api-level">
            <?cs call:since_tags(field) ?>
            <?cs call:federated_refs(field) ?>
          </div>
        <div class="jd-details-descr">
          <?cs call:description(field) ?>
        <?cs if:subcount(field.constantValue) ?>
            <div class="jd-tagdata">
            <span class="jd-tagtitle jd-tagdescr">Constant Value: </span>
            <span>
                <?cs if:field.constantValue.isString ?>
                    <?cs var:field.constantValue.str ?>
                <?cs else ?>
                    <?cs var:field.constantValue.dec ?>
                <?cs /if ?>
            </span>
            </div>
        <?cs /if ?>
        </div>
    </div>
    <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_method_details(methods) ?>
    <?cs each:method=methods ?>
    <?cs # the A tag in the next line must remain where it is, so that Eclipse can parse the docs ?>
    <A NAME="<?cs var:method.anchor ?>"></A>
    <?cs # The apilevel-N class MUST BE LAST in the sequence of class names ?>
    <div class="jd-details">
        <h4 class="jd-details-title">
          <span class="normal">
            <?cs var:method.scope ?>
            <?cs var:method.static ?>
            <?cs var:method.final ?>
            <?cs var:method.abstract ?>
            <?cs var:method.synchronized ?>
            <?cs call:type_link(method.returnType) ?>
          </span>
          <span class="sympad"><strong><?cs var:method.name ?></strong></span>
          <span class="params">(<?cs call:parameter_list(method.params) ?>)</span>
        </h4>
          <div class="api-level">
            <div><?cs call:since_tags(method) ?></div>
            <?cs call:federated_refs(method) ?>
          </div>
        <div class="jd-details-descr">
          <?cs call:description(method) ?>
        </div>
    </div>
    <?cs /each ?>
    <?cs /def ?>

    <?cs def:write_attr_details(attrs) ?>
    <?cs each:attr=attrs ?>
    <?cs # the A tag in the next line must remain where it is, so that Eclipse can parse the docs ?>
    <A NAME="<?cs var:attr.anchor ?>"></A>
    <?cs # The apilevel-N class MUST BE LAST in the sequence of class names ?>
    <div class="jd-details">
        <h4 class="jd-details-title"><?cs var:attr.name ?>
        </h4>
          <div class="api-level">
            <?cs call:since_tags(attr) ?>
          </div>
        <div class="jd-details-descr">
            <?cs call:description(attr) ?>

            <div class="jd-tagdata">
                <h5 class="jd-tagtitle">Related Methods</h5>
                <ul class="nolist">
                <?cs each:m=attr.methods ?>
                    <li><a href="<?cs var:toroot ?><?cs var:m.href ?>"><?cs var:m.name ?></a></li>
                <?cs /each ?>
                </ul>
            </div>
        </div>
    </div>
    <?cs /each ?>
    <?cs /def ?>


    <!-- XML Attributes -->
    <?cs if:subcount(class.attrs) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= FIELD DETAIL ======== -->
    <section id="xml-attributes">
      <h2>XML Attributes</h2>
      <?cs call:write_attr_details(class.attrs) ?>
    </section>
    <?cs /if ?>

    <!-- Enum Values -->
    <?cs if:subcount(class.enumConstants) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= ENUM CONSTANTS DETAIL ======== -->
    <section id="enum-values">
      <h2>Enum Values</h2>
      <?cs call:write_field_details(class.enumConstants) ?>
    </section>
    <?cs /if ?>

    <!-- Constants -->
    <?cs if:subcount(class.constants) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= ENUM CONSTANTS DETAIL ======== -->
    <section id="constants">
      <h2>Constants</h2>
      <?cs call:write_field_details(class.constants) ?>
    </section>
    <?cs /if ?>

    <!-- Fields -->
    <?cs if:subcount(class.fields) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= FIELD DETAIL ======== -->
    <section id="fields">
      <h2>Fields</h2>
      <?cs call:write_field_details(class.fields) ?>
    </section>
    <?cs /if ?>

    <!-- Public ctors -->
    <?cs if:subcount(class.ctors.public) ?>
    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= CONSTRUCTOR DETAIL ======== -->
    <section id="public-constructors">
      <h2>Public Constructors</h2>
      <?cs call:write_method_details(class.ctors.public) ?>
    </section>
    <?cs /if ?>

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= CONSTRUCTOR DETAIL ======== -->
    <!-- Protected ctors -->
    <?cs if:subcount(class.ctors.protected) ?>
    <section id="protected-constructors">
      <h2>Protected Constructors</h2>
      <?cs call:write_method_details(class.ctors.protected) ?>
    </section>
    <?cs /if ?>

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= METHOD DETAIL ======== -->
    <!-- Public methdos -->
    <?cs # don't print this section for enum class types because they are not part of API ?>
    <?cs if:subcount(class.methods.public) && class.kind != "enum" ?>
    <section id="public-methods">
      <h2>Public Methods</h2>
      <?cs call:write_method_details(class.methods.public) ?>
    </section>
    <?cs /if ?>

    <?cs # this next line must be exactly like this to be parsed by eclipse ?>
    <!-- ========= METHOD DETAIL ======== -->
    <?cs if:subcount(class.methods.protected) ?>
    <section id="protected-methods">
      <h2>Protected Methods</h2>
      <?cs call:write_method_details(class.methods.protected) ?>
    </section>
    <?cs /if ?>

    <?cs # the next two lines must be exactly like this to be parsed by eclipse ?>
    <!-- ========= END OF CLASS DATA ========= -->
    <A NAME="navbar_top"></A>

    </div> <!-- jd-content -->
  </div>
</body>
</html>
