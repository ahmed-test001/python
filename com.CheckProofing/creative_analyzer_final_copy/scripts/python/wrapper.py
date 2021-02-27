from bs4 import BeautifulSoup
import json
import getopt
import sys
import os
import time
from resources import *
from custom_functions.my_function import *
import multiprocessing as mp
import itertools
from functools import partial
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import parse_qs, urlparse
#import ConfigParser

# File Name
# {campaign_label}-{segment_name}-{sl_number}

#with validation

def universal_worker(input_pair):
    function, args = input_pair
    return function(*args)

def pool_args(function, *args):
    return zip(itertools.repeat(function), zip(*args))

def sequencer(pool, soup, output_dir, output_file_name, filename):
    sys.setrecursionlimit(10 ** 6)
    print("sequencer")
    hyper_links_json = {}
    validations_json = {}
    cats = []
    breeds = []
    for cat, breed in pool.map(partial(extract_hyper_links, filename=filename), soup.find_all("a")):
        cats.append(cat)
        breeds.append(breed)
    print("ready")

    hyper_links_json['alerts'] = cats

    passed=0
    failed=0
    missed=0
    for element in breeds:
        print(element)
        passed = passed + element['pass']
        failed = failed + element['fail']
        missed = missed + element['missed']

    h_cols = [{"pass": passed, "fail": failed, "missed": missed}]

    validations_json['alerts'] = h_cols
    pool.close()
    # self.pool.join()
    #print(hyper_links_json)
    #print(validations_json)
    final_hyber_links = json.dumps(hyper_links_json, indent=4, sort_keys=False, ensure_ascii=False)
    final_validations = json.dumps(validations_json, indent=4, sort_keys=False, ensure_ascii=False)
    file = open(output_dir + "proof_files/" + output_file_name + '_' + '-'.join(filename.split('-')[-3:-1]) + ".json", "w", errors='ignore')
    file.write(final_hyber_links)
    file.close()
    validations_file = open(output_dir + "proof_files/" + output_file_name + '_Validations' + '_' + '-'.join(filename.split('-')[-3:-1]) + ".json", "w", errors='ignore')
    validations_file.write(final_validations)
    validations_file.close()


def extract_hyper_links(link, filename):
    print("#################### HREF Links ####################")
    print(filename)
    # chromedriver = "/Users/l.reddy/Downloads/chromedriver_v87"
    chromedriver = "C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/Drivers/chromedriver.exe"
    d_cols = {}
    raw_url = link.get("href")
    requests_array = []
    h_cols = {"pass": 0, "fail": 0, "missed": 0}


    try:
        chrome_options = Options()
        chrome_options.add_argument("--window-size=300,300")
        driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        driver.get(raw_url)
        decrypted_url = driver.current_url
        # r = requests.get(raw_url)
        # time.sleep(1)
        # decrypted_url = r.url
        print("Link Label: ", link.get("_label"))
        print("Raw URL: ", raw_url)
        print("Landing Page URL: ", decrypted_url, "\n")
        # for element in r.history:
        #     requests_array.append(str(element))
        driver.quit()
    except:
        print("no")
        decrypted_url = raw_url
    d_cols['inner_text'] = link.text.strip().replace("   ", "").replace("\n", "").replace("\r", "")
    d_cols['label'] = link.get("_label")
    d_cols['title'] = link.get("title")
    d_cols['href'] = decrypted_url
    d_cols['class'] = link.get("class")
    # parse url beginning
    parsed_url = urlparse(decrypted_url)
    d_cols['scheme'] = parsed_url.scheme
    d_cols['netloc'] = parsed_url.netloc
    d_cols['path'] = parsed_url.path
    # d_cols['params'] = parsed_url.params
    d_cols['query'] = parsed_url.query
    # d_cols['fragment'] = parsed_url.fragment
    # redirect history
    # r = requests.get(decrypted_url, headers=self.headers)
    # requests_array = []
    # for element in r.history:
    #     requests_array.append(str(element))
    # d_cols['redirect_history'] = requests_array
    # parse query
    pair = parse_qs(parsed_url.query)
    # print(pair.keys())

    for key in pair.keys():
        d_cols[key] = pair[key][0]

    # Replacing all null values with empty strings
    for value in d_cols:
        if d_cols[value] is None:
            d_cols[value] = ""
        d_cols[value] = d_cols[value].replace(u'\xa0', u' ')

    check_hyper_links_key_value(d_cols, '-'.join(filename.split('-')[-3:-1]))
    check_common_key_value(d_cols, 'common_links')
    # test_run(d_cols, '-'.join(self.filename.split('-')[-3:-1]))

    if not check_key_exist(d_cols, 'status_code'):
        d_cols['status_code'] = 'ORANGE'
        d_cols['exception'] = "NO_MATCH"

    if d_cols['status_code'] == "GREEN":
        h_cols['pass'] = h_cols['pass'] + 1
    elif d_cols['status_code'] == "RED":
        h_cols['fail'] = h_cols['fail'] + 1
    elif d_cols['status_code'] == "ORANGE":
        h_cols['missed'] = h_cols['missed'] + 1

    return [d_cols, h_cols]



# Main Scrapper object
def main_scrapper(argv):
    input_file = ''

    # logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    # logging.debug('Log file starts here')

    try:
        opts, args = getopt.getopt(argv, "hi:", ["input_file="])
    except getopt.GetoptError:
        print('python wrapper.py -i <input_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python wrapper.py -i <input_file>')
            print('python wrapper.py --input <input_file>')
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg

    if input_file == '':
        error_msg = "input_file cannot be null. Run 'python wrapper.py -h' to see the options"
        raise Exception(error_msg)

    epoch_time = str(int(time.time()))
    start = time.perf_counter()

    # File names
    Hyper_Links = 'Hyper_Links'
    Image_Text = 'Image_Text'
    Subject_line = 'Subject_Line'
    Visible_Text = 'Visible_Text'
    Report_File = 'Report-' + input_file.split('.')[0] + '-' + epoch_time

    print('Hyper_Links: ' + Hyper_Links)
    print('Image_Text: ' + Image_Text)
    print('Subject_line: ' + Subject_line)
    print('Visible_Text: ' + Visible_Text)
    print('Report_File: ' + Report_File)

    #pool = mp.Pool(mp.cpu_count())
    pool = mp.Pool(4)


    dir_name = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_name)
    os.chdir("../..")
    cwd = os.getcwd()
    output_file = cwd + "/data/output/"
    print("Main Directory: ", cwd)

    with open(cwd + "/data/input/" + input_file, 'rb') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
    f.close()

    # Step 1 Spawning multiplee instances for extracting Hyper Links
    # sequencer(pool, soup, output_file, Hyper_Links, Report_File)



    # Step 2 Extracting Images
    scrapper_obj = extract_images(input_html_file=soup, output_dir=output_file, Image_Text=Image_Text, Report_File=Report_File)
    scrapper_obj.extract_images()

    # Step 3 Extracting Subject line information
    scrapper_obj = extract_subj_line(input_html_file=soup, output_dir=output_file, Subject_Line=Subject_line, Report_File=Report_File)
    scrapper_obj.extract_subj_line()

    # Step 4 Extracting Visible Text out of creative
    # scrapper_obj = extract_text(input_html_file=soup, output_dir=output_file, Visible_Text=Visible_Text, Report_File=Report_File)
    # scrapper_obj.extract_text()

    # Uncomment this if pooling is not working
    # scrapper_obj = extract_hyper_links(input_html_file=soup, output_dir=output_file, Hyper_Links=Hyper_Links, Report_File=Report_File)
    # scrapper_obj.extract_hyper_links()

    # Step 5 Generating Final report
    html_converter_obj = report_generator_sub_report(input_html_file=soup, output_dir=output_file, Report_File=Report_File)
    html_converter_obj.get_html_converter()
    html_converter_obj.get_combined_sub_report()
    html_converter_obj.get_combined()

    # Capture time taken for the entire proceess to run
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds(s)')


if __name__ == "__main__":
    print(sys.argv[1:])
    main_scrapper(sys.argv[1:])
