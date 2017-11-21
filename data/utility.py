from os import listdir
from os import sep
from os.path import isdir
from os.path import isfile


def get_dirs(path='.'):
    all_dirs = dict()
    for data in listdir(path):
        if isdir(path + sep + data) and '_' not in data and len(data) == 2:
            all_dirs[data] = []
            for file in listdir(path + sep + data):
                if isfile(path + sep + data + sep + file) and '_' not in file:
                    all_dirs[data].append(file)
    return all_dirs


def get_localizations(all_dirs):
    localizations = all_dirs
    wrong_keys = set()
    for key in localizations:
        for file in ['address.py', 'job.py', 'person.py']:
            if file not in localizations[key]:
                wrong_keys.add(key)
    for key in wrong_keys:
        del localizations[key]
    return localizations.keys()


def get_pds(path='.'):
    localization_names = get_localizations(get_dirs(path))
    module_names = map(lambda x: 'data' + '.' + x + '.__init__', localization_names)
    return dict(zip(localization_names, map(lambda x: __import__(x, fromlist=['.']), module_names)))
