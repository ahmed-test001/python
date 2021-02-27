import json


# check if key exists in dict
def check_key_exist(test_dict, key):
    try:
        value = test_dict[key]
        return True
    except KeyError:
        return False


def check_hyper_links_key_value(d_cols, section):
    validation_file = open('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_analyzer_final_copy/data/validation/hyper_link_validation.json', 'r')
    validation_data = json.load(validation_file)

    for json_index in validation_data[section]:
        # query segments order marithe endi mari??
        # compare segments count with reference
        #
        if d_cols['label'] == json_index['label'] and d_cols['inner_text'] == json_index['inner_text']:

            if d_cols['href'] == json_index['href']:
                print("in if block")
                d_cols['status_code'] = "GREEN"
                d_cols['exception'] = "PASSED"
                break
            else:
                print("in else block")
                d_cols['status_code'] = "RED"
                d_cols['exception'] = "FAILURE"
                break

    validation_file.close()

def check_common_key_value(d_cols, section):
    validation_file = open('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_analyzer_final_copy/data/validation/common_links_validation.json', 'r')
    validation_data = json.load(validation_file)

    for json_index in validation_data[section]:
        if d_cols['label'] == json_index['label'] and d_cols['inner_text'] == json_index['inner_text']:

            if json_index['href'] in d_cols['href']:
                print("in if block")
                d_cols['status_code'] = "GREEN"
                d_cols['exception'] = "PASSED"
                break
            else:
                print("in else block")
                d_cols['status_code'] = "RED"
                d_cols['exception'] = "FAILURE"
                break

    validation_file.close()

def test_run(d_cols, section):
    validation_file = open('C:/Users/a.ferdous.CORP/PycharmProjects/com.CheckProofing/creative_analyzer_final_copy/data/validation/hyper_link_validation_copy_ignore.json', 'r')
    validation_data = json.load(validation_file)

    for json_index in validation_data[section]:
        # query segments order marithe endi mari??
        # compare segments count with reference
        #
        for element in validation_data[json_index['module']]:
            if d_cols['label'] == element['label'] and d_cols['inner_text'] == element['inner_text']:

                if d_cols['href'] == element['href']:
                    print("in if block")
                    d_cols['status_code'] = "GREEN"
                    d_cols['exception'] = "PASSED"
                    break
                else:
                    print("in else block")
                    d_cols['status_code'] = "RED"
                    d_cols['exception'] = "FAILURE"
                    break

    validation_file.close()