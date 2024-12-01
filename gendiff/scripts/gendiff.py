#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two '
                                                 'configuration files '
                                                 'and shows '
                                                 'a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    one_diff = generate_diff(args.first_file, args.second_file)
    print(one_diff)


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    allcase = set(file1.keys()).union(file2.keys())
    res = []
    for key in sorted(allcase):
        value1 = json.dumps(file1.get(key))
        value2 = json.dumps(file2.get(key))
        if key in file1 and key in file2:
            if value1 != value2:
                res.append(f" - {key}: {value1}")
                res.append(f" + {key}: {value2}")
            else:
                res.append(f"   {key}: {value1}")
        elif key in file1:
            res.append(f" - {key}: {value1}")
        elif key in file2:
            res.append(f" + {key}: {value2}")
    return "{\n" + "\n".join(res) + "\n}"


if __name__ == '__main__':
    main()
