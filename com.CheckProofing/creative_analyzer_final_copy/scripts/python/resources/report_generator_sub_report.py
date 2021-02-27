import json
import os

class report_generator_sub_report:
    def __init__(self, **kwargs):
        self.input_html_file = kwargs['input_html_file']
        self.output_dir = kwargs['output_dir']
        self.filename = kwargs['Report_File']

        self.table_start = """<table>"""
        self.table_end = """</table>"""
        self.in_line_start = """<tr>"""
        self.in_line_end = """</tr>"""
        self.in_line_start_color_yellow = """<tr bgcolor="yellow">"""
        self.in_line_start_color_green = """<tr bgcolor="lightgreen">"""
        self.in_line_start_color_red = """<tr bgcolor="red">"""
        self.in_line_start_color_orange = """<tr bgcolor="orange">"""
        self.table_header_start = """<th>"""
        self.table_header_end = """</th>"""
        self.table_data_start = """<td>"""
        self.table_data_end = """</td>"""
        self.unordered_list_start = """<ol>"""
        self.list_start = """<li>"""
        self.list_end = """</li>"""
        self.unordered_list_end = """</ol>"""
        self.header = """<!DOCTYPE html>
                                <html lang="en">
                                    <head>
                                        <meta charset="UTF-8">
                                        <title>QC Reports</title>
                                        <script>
                                        function show(shown, hidden) {
                                            document.getElementById(shown).style.display='block';
                                            document.getElementById(hidden).style.display='none';
                                            return false;
                                        }
                                        </script>
                                        <style>
                                            .header {
                                            background-color: #F1F1F1;
                                            text-align: center;
                                            padding: 20px;
                                            font-size: 20px;
                                            }
                                            .button {
                                            background-color: #F1F1F1;
                                            border-radius: 15px;
                                            border: none;
                                            color: black;
                                            padding: 10px 20px;
                                            text-align: center;
                                            text-decoration: none;
                                            display: inline-block;
                                            font-size: 15px;
                                            margin: 4px 2px;
                                            cursor: pointer;
                                            }
                                            .button:hover {
                                            background-color: #4CAF50;
                                            color: white;
                                            }
                                        </style>
                                    </head>
                                    <body>"""
        self.style = """<style>
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
        self.footer = """</body>
                        </html>"""

        self.caption = """<caption><p><b><font color=#E74C3C>{caption_text} for {creative_name}</font></b></p></caption>"""
        self.empty_row1 = """<tr class="blank_row">
                                        <td bgcolor="#FCF3CF" colspan="3"></td>
                                    </tr>"""
        self.empty_row = """<tr height = 20px></tr>"""

        self.match_text = "https://www.samsung.com/us/smartphones/galaxy-note20-5g/buy/?offerCID=preorder&filterCarrier=verizon&skipOffer=OFFER-ETIC802&utm_source=samsung&utm_medium=email&utm_campaign=N20_ReserveBoost&marsLinkCategory=mphone:mphone&MKM_RID=0143250457&MKM_MID=FCP_535534015_PDM157139&cid=eml-mb-cph-920-3003-Verizon&bpid=0143250457"

        self.div_end = """</div>"""

        self.new_header = """<!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1", charset="UTF-8">
        <style>
        body {font-family: Arial;}

                /* Style the tab */
        .tab {
          overflow: hidden;
          border: 1px solid #ccc;
          border-radius: 15px;
          background: #73AD21;
          padding: 10px;
          background-color: #D5DBDB;
        }

        /* Style the buttons inside the tab */
        .tab button {
          background-color: inherit;
          border-radius: 10px;
          float: left;
          border: none;
          outline: none;
          cursor: pointer;
          padding: 14px 16px;
          transition: 0.3s;
          font-size: 12px;
        }

        /* Change background color of buttons on hover */
        .tab button:hover {
          background-color: #4CAF50;
        }

        /* Create an active/current tablink class */
        .tab button.active {
          background-color: #4CAF50;
          color: white;
        }

        /* Fade in tabs */
        @-webkit-keyframes fadeEffect {
          from {opacity: 0;}
          to {opacity: 1;}
        }

        @keyframes fadeEffect {
          from {opacity: 0;}
          to {opacity: 1;}
        }

        </style>
        </head>
        <body>"""

        self.new_footer = """<script>
        function openCity(evt, cityName) {
          var i, tabcontent, tablinks;
          tabcontent = document.getElementsByClassName("tabcontent");
          for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
          }
          tablinks = document.getElementsByClassName("tablinks");
          for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
          }
          document.getElementById(cityName).style.display = "block";
          evt.currentTarget.className += " active";
        }
        </script>
        </body>
        </html>"""

    def main_page_div_section(self, **kwargs):
        first_step = """<div class="header" id="MainPage">"""
        second_step = """QC Reports
        <caption><p><b><font color=#E74C3C>Main Page Details</font></b></p></caption><br><br>"""
        div_break = """</div>"""
        result_string = first_step + second_step
        for arguments in kwargs['html_file_list']:
            # print(kwargs[arguments])
            href_string = """<a href="#" class="button" onclick="return show('{placeholder_string}','MainPage');">{placeholder_string}</a>""".format(
                placeholder_string=arguments)
            break_string = """<br></br>"""
            result_string = result_string + href_string + break_string
        # print(result_string)
        return result_string + div_break


    def sub_page_div_section(self, section_name):
        result_string = """<div id="{placeholder_string}" style="display:none">
        Current Page: {placeholder_string}<br></br>
        <a href="#" class="button" onclick="return show('MainPage','{placeholder_string}');">Back</a>""".format(
            placeholder_string=section_name)
        return result_string



    def main_page_div_section_new(self,**kwargs):
        first_step="""<h3>Main Page</h3>
        <div class="tab">"""
        div_break="""</div>"""
        result_string=first_step
        for arguments in kwargs['html_file_list']:
            #print(kwargs[arguments])
            href_string="""<button class="tablinks" onclick="openCity(event, '{placeholder_string}')">{placeholder_string}</button>""".format(placeholder_string=arguments)
            #break_string="""<br></br>"""
            result_string=result_string+href_string #+break_string
        #print(result_string)
        return result_string+div_break

    def sub_page_div_section_new(self, section_name):
        result_string="""<div id="{placeholder_string}" class="tabcontent">""".format(placeholder_string=section_name)
        return result_string



    def get_html_converter(self):
        print("#################### Converting Json --> Html Start ####################")
        json_file_list = [f.split('.')[0] for f in os.listdir(self.output_dir + 'proof_files') if f.endswith(".json")]
        for file_name in json_file_list:
            # file_path = os.path.join(self.output_dir + 'proof_files', file_name)
            file_path = os.path.join(self.output_dir + 'proof_files', file_name)
            with open(file_path + '.json', 'r') as outfile:
                lokesh = json.load(outfile)
                count = 0
                with open(file_path + '.html', 'w+') as output_file:
                    #main_text = self.caption.format(caption_text=file_name, creative_name=self.filename) + self.style + self.table_data_start + self.unordered_list_start
                    main_text = self.style + self.table_data_start + self.unordered_list_start
                    output_file.write(main_text)
                    for i in lokesh['alerts']:
                        output_file.write(self.list_start)
                        output_file.write(self.table_start)
                        for j in i:
                            table_header = j
                            table_data = str(lokesh['alerts'][count][j])
                            if table_data == 'Preheader':
                                self.match_text = lokesh['alerts'][count]['href']

                            if table_header == 'redirect_history' and len(lokesh['alerts'][count][j]) > 0:
                                redirect_history = []
                                for history in lokesh['alerts'][count][j]:
                                    redirect_history.append(history.replace("<", "&lt;").replace(">", "&gt;"))
                                table_data = str(redirect_history)

                            if table_data is None:
                                table_data = ""

                            if str(j) in ('inner_text', 'label'):
                                lines = self.in_line_start_color_yellow + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) == 'status_code' and lokesh['alerts'][count]['status_code'].strip() == 'GREEN':
                                lines = self.in_line_start_color_green + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) == 'status_code' and lokesh['alerts'][count]['status_code'].strip() == 'RED':
                                lines = self.in_line_start_color_red + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) == 'status_code' and lokesh['alerts'][count]['status_code'].strip() == 'ORANGE':
                                lines = self.in_line_start_color_orange + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) in ('data', 'alt') and lokesh['alerts'][count]['alt'].strip() == lokesh['alerts'][count]['data'].strip():
                                lines = self.in_line_start_color_green + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) == 'href' and str(lokesh['alerts'][count][j]) == self.match_text:
                                lines = self.in_line_start_color_green + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            elif str(j) == 'redirect_history' and len(lokesh['alerts'][count][j]) > 0:
                                lines = self.in_line_start_color_red + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            else:
                                lines = self.in_line_start + self.table_header_start + table_header + self.table_header_end + self.table_data_start + table_data + self.table_data_end + self.in_line_end
                            output_file.write(lines)
                        output_file.write(self.empty_row)
                        output_file.write(self.table_end)
                        output_file.write(self.list_end)
                        count = count + 1
                    final_tbl_structure = self.unordered_list_end + self.table_data_end
                    output_file.write(final_tbl_structure)
                output_file.close()
            outfile.close()
            print("#################### Converting Json --> Html End ####################")

    def get_combined(self):
        print("#################### Generating HTML Final Report Start ####################")
        html_file_list = [f.split('.')[0] for f in os.listdir(self.output_dir + 'proof_reports') if f.endswith(".html")]
        with open(self.output_dir + 'proof_reports/main_reports/' + '-'.join(self.filename.split('-')[0:2]) + '.html', 'w+') as combined_html:
            combined_html.write(self.header)
            main_string=self.main_page_div_section(html_file_list=html_file_list)
            combined_html.write(main_string)
            for file_name in html_file_list:
                file_path = os.path.join(self.output_dir + 'proof_reports', file_name)
                output_file = open(file_path + '.html', 'r').read()
                sub_string=self.sub_page_div_section(file_name)
                combined_html.write(sub_string)
                combined_html.write(output_file)
                combined_html.write(self.div_end)
            combined_html.write(self.footer)
        combined_html.close()
        print("#################### Generating HTML Final Report End ####################")


    def get_combined_sub_report(self):
        print("#################### Generating HTML Final Report Start ####################")
        html_file_list = [f.split('.')[0] for f in os.listdir(self.output_dir + 'proof_files') if f.endswith(".html") and '-'.join(self.filename.split('-')[-3:-1]) in f]
        with open(self.output_dir + 'proof_reports/' + '-'.join(self.filename.split('-')[-3:-1]) + '.html', 'w+') as combined_html:
            combined_html.write(self.new_header)
            main_string = self.main_page_div_section_new(html_file_list=html_file_list)
            combined_html.write(main_string)
            for file_name in html_file_list:
                file_path = os.path.join(self.output_dir + 'proof_files', file_name)
                output_file = open(file_path + '.html', 'r').read()
                sub_string=self.sub_page_div_section_new(file_name)
                combined_html.write(sub_string)
                combined_html.write(output_file)
                combined_html.write(self.div_end)
            combined_html.write(self.new_footer)
        combined_html.close()
        print("#################### Generating HTML Final Report End ####################")
