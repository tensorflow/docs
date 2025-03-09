<?cs include:"doctype.cs" ?>
<?cs include:"macros.cs" ?>
<html devsite>
<?cs include:"head_tag.cs" ?>
<body>

<div>
<p><?cs call:tag_list(root.descr) ?></p>
</div>

<?cs set:count = #1 ?>
<table>
<?cs each:pkg = docs.packages ?>
    <tr>
        <td><?cs call:package_link(pkg) ?></td>
        <td width="100%"><?cs call:tag_list(pkg.shortDescr) ?></td>
    </tr>
<?cs set:count = count + #1 ?>
<?cs /each ?>
</table>

</body>
</html>
