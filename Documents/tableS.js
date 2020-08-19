// creates a table 2x2
// pja 7/25/2020
function tbl2(title, body) {
ans = ''
ans = ans + ("<table border='3'>")
ans = ans + ('  <tr>')
ans = ans + ("    <td> ")
ans = ans + (title)
ans = ans + (" </td> <td> </td> </tr>")
ans = ans + ("<tr>    <td>  </td> <td> ")
ans = ans + (body)
ans = ans + (" </td>")
ans = ans + ("  </tr>")
ans = ans + ("</table>")
return(ans)
}