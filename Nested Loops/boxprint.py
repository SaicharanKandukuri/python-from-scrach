def box_print(rows, colomns, element, sp_char):
    header = (sp_char * colomns + "\n")
    body=""
    footer=""
    if (colomns >= 1) and (rows != 1): body = ((sp_char + (element * (colomns-2) + "\n"))*(rows-2)); footer = (sp_char * colomns)
    if (rows > 1): body = ((sp_char + (element * (colomns-2) + sp_char + "\n"))*(rows-2)); footer = (sp_char * colomns)
    if (rows == 1): body = ""; footer = ""    
    return header + body + footer

print(box_print(3, 3, " ", "+"))