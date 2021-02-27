import json

header = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>"""

footer = """</body>
</html>"""

style = """<style>
                table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                        padding-left: 20px;
                        padding-right: 20px;
                        font-family: Calibri, sans-serif;
                        font-size: 13px;
                }
                tr:nth-child(even){{background-color: #f2f2f2}}
                th {
                     background-color:#FCF3CF;
                     color:black;
                }
                p {
                     background-color: #AED6F1 ;
                     font color: red;
                }
                caption {
                    font-family: Calibri, sans-serif;
                    font-size: 25px;
                    font color: red;
                    text-align: center;
                }
                </style>"""

caption = """<caption><p><b><font color=#E74C3C>{caption_text}</font></b></p></caption>""".format(caption_text="Hyperlinks in Canvas Creative")

empty_row1 = """<tr class="blank_row">
    <td bgcolor="#FCF3CF" colspan="3"></td>
</tr>"""

empty_row = """<tr height = 20px></tr>"""

hyper_links = "./output_json_files/hyper_links"
template_images = "./output_json_files/template_images"
proofs_baseline_text = "./output_json_files/proofs_baseline_text"

file_list = [hyper_links, template_images, proofs_baseline_text]

for file_name in file_list:
    with open(file_name+'.json', 'r') as outfile:
        lokesh = json.load(outfile)
        count = 0
        table_start = """<table>"""
        table_end = """</table>"""
        in_line_start = """<tr>"""
        in_line_end = """</tr>"""
        in_line_start_color_yellow = """<tr bgcolor="yellow">"""
        in_line_start_color_green = """<tr bgcolor="lightgreen">"""
        in_line_start_color_red = """<tr bgcolor="red">"""
        table_header_start = """<th>"""
        table_header_end = """</th>"""
        table_data_start = """<td>"""
        table_data_end = """</td>"""
        unordered_list_start = """<ol>"""
        list_start = """<li>"""
        list_end = """</li>"""
        unordered_list_end = """</ol>"""
        with open(file_name+'.html', 'w+', encoding="utf-8") as output_file:
            main_text = header + caption + style + table_data_start + unordered_list_start
            output_file.write(main_text)
            for i in lokesh['alerts']:
                output_file.write(list_start)
                output_file.write(table_start)
                for j in i:
                    table_header = j
                    table_data = str(lokesh['alerts'][count][j])
                    if table_data == 'Preheader':
                        match_text = lokesh['alerts'][count]['href']
                    if table_header == 'redirect_history' and len(lokesh['alerts'][count][j]) > 0:
                        redirect_history = []
                        for history in lokesh['alerts'][count][j]:
                            redirect_history.append(history.replace("<", "&lt;").replace(">", "&gt;"))
                        table_data = str(redirect_history)
                    if table_data is None:
                        table_data = ""
                    if str(j) in ('inner_text', 'label',):
                        lines = in_line_start_color_yellow + table_header_start + table_header + table_header_end + table_data_start + table_data + table_data_end + in_line_end
                    elif str(j) in ('data', 'alt') and lokesh['alerts'][count]['alt'].strip() == lokesh['alerts'][count]['data'].strip():
                        lines = in_line_start_color_green + table_header_start + table_header + table_header_end + table_data_start + table_data + table_data_end + in_line_end
                    elif str(lokesh['alerts'][count][j]) == match_text:
                        lines = in_line_start_color_green + table_header_start + table_header + table_header_end + table_data_start + table_data + table_data_end + in_line_end
                    elif str(j) == 'redirect_history' and len(lokesh['alerts'][count][j]) > 0:
                        lines = in_line_start_color_red + table_header_start + table_header + table_header_end + table_data_start + table_data + table_data_end + in_line_end
                    else:
                        lines = in_line_start + table_header_start + table_header + table_header_end + table_data_start + table_data + table_data_end + in_line_end
                    output_file.write(lines)
                output_file.write(empty_row)
                output_file.write(table_end)
                output_file.write(list_end)
                count = count + 1
            final_tbl_structure = unordered_list_end + table_data_end
            output_file.write(final_tbl_structure)
            output_file.write(footer)
        output_file.close()
    outfile.close()


report_tuples = [
    # ('file:///Users/l.reddy/PycharmProjects/seleniumAutomation/output_json_files/template_images.html', "All images"),
    # ('file:///Users/l.reddy/PycharmProjects/seleniumAutomation/output_json_files/hyper_links.html', "All Hyper Links"),
    # ('file:///Users/l.reddy/PycharmProjects/seleniumAutomation/output_json_files/proofs_baseline_text.html', "Extracted Visible Text")

    ('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_scrapping/creative_scrapping/output_json_files/template_images.html',
     "All images"),
    ('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_scrapping/creative_scrapping/output_json_files/hyper_links.html',
     "All Hyper Links"),
    ('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_scrapping/creative_scrapping/output_json_files/proofs_baseline_text.html',
     "Extracted Visible Text")
]
html = """
<!DOCTYPE html>
<html>
<head>
<title>Reports</title>
</head>
<body>

<h1>Template Reports</h1>"""

html += unordered_list_start
for r in report_tuples:
    html += list_start
    html += '<h3>%s</h3>' % (str(r[1])) + '<a href="%s">Click Here to view</a>' % (r[0])
    html += list_end

html += unordered_list_end
html += """</body>
           </html>"""
with open("./output_json_files/combined_html.html", "w+") as combined_output:
    combined_output.write(html)

combined_output.close()
