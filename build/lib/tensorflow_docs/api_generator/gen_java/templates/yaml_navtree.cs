<?cs
  set longestWordLength = 0
?><?cs
  set wideStyleCharacterLimit = 20
?><?cs
  set pathPrefix = toroot
?><?cs

# walk the children pages and print them nested below the parent
page: the node to insert a label, link and check for children
whitespace: Whitespace to insert before any text in the structure, which helps
 with nesting children on recursion.
isRoot: treat this node as if it has children and insert a section node.

?><?cs
def:write_child_nodes(page,whitespace,isRoot) ?><?cs
  if:longestWordLength < string.length(page.label)?><?cs
    set longestWordLength = string.length(page.label)?><?cs
  /if?>
<?cs var:whitespace ?>- title: "<?cs var:page.label ?>"
<?cs var:whitespace ?>  path: <?cs var:pathPrefix+page.link ?><?cs
  if:subcount(page.children) || isRoot ?>
<?cs var:whitespace ?>  section: <?cs
 /if?><?cs
  each:child = page.children?><?cs
    if:!subcount(child.children) ?>
<?cs var:whitespace ?>  - title: "<?cs var:child.shortname ?>"
<?cs var:whitespace ?>    path: <?cs var:pathPrefix+child.link ?><?cs
    /if ?><?cs
    if:subcount(child.children) ?><?cs
    call:write_child_nodes(child,whitespace + "  ",0) ?><?cs
    /if ?><?cs
    /each ?><?cs
/def ?><?cs

# print out the yaml nav starting with the toc entry and using the first item,
which is generally the package summary as the root element with the rest of the
pages as children beneath the package summary.
?>
toc:<?cs each:page = docs.pages?><?cs
  if:page.type == "package"?><?cs
  call:write_child_nodes(page,"",1) ?><?cs
  else?>
    <?cs
    call:write_child_nodes(page,"  ",0) ?><?cs
  /if?><?cs
/each ?>