import csv
import os

companies = []


def get_abs_path(relative_path):
    return os.path.dirname(os.path.realpath(__file__)) + str(relative_path).replace("/", os.path.sep)


# read csv file
with open(get_abs_path('/companies.csv'), encoding='utf-8') as csvf:
    # load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf)

    # convert each csv row into python dict
    for row in csvReader:
        # add this python dict to json array
        companies.append(row)

