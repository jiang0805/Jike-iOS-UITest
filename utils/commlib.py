import yaml
import os


def get_test_data(test_data_path):

    case = []
    http = []
    expected = []
    f = open(test_data_path)
    text = f.read()
    dat = yaml.load(text, Loader=yaml.FullLoader)
    test = dat['tests']
    for td in test:
        case.append(td.get('case', ''))
        http.append(td.get('http', {}))
        expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters
