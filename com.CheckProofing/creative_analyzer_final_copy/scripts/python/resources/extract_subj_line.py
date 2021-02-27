import json

class extract_subj_line:
    def __init__(self, **kwargs):
        self.config_file = {}
        self.input_html_file = kwargs['input_html_file']
        self.output_dir = kwargs['output_dir']
        self.output_file_name = kwargs['Subject_Line']
        self.filename = kwargs['Report_File']
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
                       }
        self.query_list = ['offerCID', 'promoCode', 'skipCarrier', 'tradeIn', 'utm_source', 'utm_medium', 'utm_campaign', 'marsLinkCategory', 'MKM_RID', 'MKM_MID', 'cid', 'bpid']

    def extract_subj_line(self):
        print("#################### Subject Line Text Start ####################")
        # {proof_number}-{campaign_label}-{segment_name}-{sl_number}-{cid}
        ahref_links = []
        hyper_links_json = {}
        results = self.input_html_file.find_all(class_="MsoNormal")
        i = results[3].find_all('span')
        for j in i:
            d_cols = {}
            string_value = j.text.strip()
            if len(string_value) != 0 and string_value != 'Subject:':
                sl_text = string_value.split(']')[1].strip()
                proof_number = string_value.split(']')[0].strip().split('[')[1].strip().split('-')[0]
                campaign_label = string_value.split(']')[0].strip().split('[')[1].strip().split('-')[1]
                # segment_name = string_value.split(']')[0].strip().split('[')[1].strip().split('-')[2]
                # sl_number = string_value.split(']')[0].strip().split('[')[1].strip().split('-')[3]
                # cid = '-'.join(string_value.split(']')[0].strip().split('[')[1].strip().split('-')[4:])
                d_cols['proof_number'] = proof_number
                d_cols['campaign_label'] = campaign_label
                # d_cols['segment_name'] = segment_name
                # d_cols['sline_number'] = sl_number
                d_cols['sline_text'] = sl_text
                # d_cols['cid'] = cid
                ahref_links.append(d_cols)
        hyper_links_json['alerts'] = ahref_links
        final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
        file = open(self.output_dir + "proof_files/" + self.output_file_name + '_' + '-'.join(self.filename.split('-')[-3:-1]) + ".json", "w", encoding="utf-8")
        file.write(final_hyber_links)
        file.close()
        print("#################### Subject Line Text End ####################")


