import json

class extract_text:
    def __init__(self, **kwargs):
        self.config_file = {}
        self.input_html_file = kwargs['input_html_file']
        self.output_dir = kwargs['output_dir']
        self.output_file_name = kwargs['Visible_Text']
        self.filename = kwargs['Report_File']
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                       }
        # self.query_list = ['offerCID', 'promoCode', 'skipCarrier', 'tradeIn', 'utm_source', 'utm_medium', 'utm_campaign', 'marsLinkCategory', 'MKM_RID', 'MKM_MID', 'cid', 'bpid']

    def extract_text(self):
        print("#################### Extract Visible HTML Text Start ####################")

        try:
            gdp_table = self.input_html_file.get_text()  # get all the text from HTML
            # gdp_table = self.driver.current_url.get_text()  # get all the text from HTML
            gdp_table_data = gdp_table.split("\n\n\n\n\n")  # split string to list

            ahref_links = []
            hyper_links_json = {}

            for every_tr in gdp_table_data:
                d_cols = {}
                value = every_tr.strip().replace("   ", "")
                if len(value) != 0:
                    d_cols['baseline'] = value.strip().replace("   ", "")
                    ahref_links.append(d_cols)
            hyper_links_json['alerts'] = ahref_links

            final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
            file = open(self.output_dir + "proof_files/" + self.output_file_name + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w")
            file.write(final_hyber_links)
            file.close()
            print("#################### Extract Visible HTML Text End ####################")

        except:
            print("error")
