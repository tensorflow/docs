<?cs include:"doctype.cs" ?>
<?cs include:"macros.cs" ?>
<html devsite>
<?cs include:"head_tag.cs" ?>
<body>

<div class="jd-letterlist"><?cs each:letter=docs.classes ?>
    <a href="#letter_<?cs name:letter ?>"><?cs name:letter ?></a><?cs /each?>
</div>

<?cs each:letter=docs.classes ?>
<?cs set:count = #1 ?>
<h2 id="letter_<?cs name:letter ?>"><?cs name:letter ?></h2>
<table class="jd-sumtable">
    <?cs set:cur_row = #0 ?>
    <?cs each:cl = letter ?>
        <tr>
            <td class="jd-linkcol"><?cs call:type_link(cl.type) ?></td>
            <td class="jd-descrcol" width="100%"><?cs call:short_descr(cl) ?>&nbsp;</td>
        </tr>
    <?cs set:count = count + #1 ?>
    <?cs /each ?>
</table>
<?cs /each ?>

</body>
</html>
