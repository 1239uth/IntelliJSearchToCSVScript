from sys import argv
from pandas import DataFrame
from Constants import MODULES, MODULE, REFERENCE, PROJECT, TYPE, COLUMNS


########################## COMMAND LINE PARSING ##########################
def verify_argv() -> None:
    """
    Verify only 1 command line argument is passed and exit if there isn't.

    :return: None
    """
    input_format = f'Input Format: `python {__file__} <filename>`'
    if len(argv) != 2:
        print(input_format)
        exit(1)


########################## FILE PARSING ##########################
entries: {str: list} = {}
# Initialize entries with empty lists
for header in COLUMNS:
    entries[header] = []


def get_num_tabs(line: str) -> int:
    """
    Get number of tabs in a given string.

    Tab size is expected to be 4 spaces.

    >>> get_num_tabs('        2 tabs before this')
    2
    >>> get_num_tabs('no tabs')
    0

    :param line: string representing a line of text which contains tabs (of 4 spaces) at the start
    :return: number of tabs that are at the start of the given line (number of blank spaces / 4)
    """
    tab_size = 4
    return (len(line) - len(line.lstrip(' '))) // tab_size


def remove_brackets(string: str) -> str:
    """
    Cut string at start of brackets.

    >>> remove_brackets('core  (171 usages found)')
    'core'
    >>> remove_brackets('core')
    'core'

    :param string: string to cut
    :return: string after cutting brackets off
    """
    return string.split('(')[0].strip()


def get_module_from(references: [str]) -> str:
    f"""
    Gets the module name if it is a part of either of the references, or returns empty string otherwise.

    >>> get_module_from(['this_is_test_for_' + MODULES[0], 'some_project'])
    {MODULES[0]}
    >>> get_module_from(['some_reference', 'some_' + MODULES[1]])
    {MODULES[1]}
    >>> get_module_from(['no_module_in_reference', 'no_module_in_project'])
    ''
    
    :param references: list of references to check if module exists in either of them
    :return: name of a module if exists in any of the references, or empty string otherwise
    """
    for module in MODULES:
        for reference in references:
            if module.lower() in reference.lower():
                return module
    return ''


def add_to_entries(current_file_name: str, current_file_path: str,
                   current_project: str, current_type: str, line_number: str) -> None:
    """
    Add data to the 'entries' dictionary.

    :param current_file_name:
    :param current_file_path:
    :param current_project:
    :param current_type:
    :param line_number:
    :return: None
    """
    reference = f'{current_file_path}\\{current_file_name}:{line_number}'
    entries[REFERENCE].append(reference)
    entries[PROJECT].append(current_project)
    module = get_module_from([reference, current_project])
    entries[MODULE].append(module)
    entries[TYPE].append(current_type)


def parse_file(txt_file: str) -> None:
    """
    Read the given text file and add the data to the entries dictionary after parsing.

    :param txt_file: Text file to parse
    :return: None
    """
    current_type = ''
    current_project = ''
    current_file_path = ''
    current_file_name = ''
    with open(txt_file) as file:
        for line in file:
            tabs = get_num_tabs(line)
            line = remove_brackets(line)
            if tabs == 1:
                current_type = line
            elif tabs == 2:
                current_project = line
            elif tabs == 3:
                current_file_path = line
            elif tabs == 4:
                current_file_name = line
            elif tabs == 5:
                add_to_entries(current_file_name, current_file_path, current_project, current_type, line.split(' ')[0])


def replace_extension(filename: str, new_extension: str) -> str:
    """
    Replace an extension with a new given one

    >>> replace_extension('data.json', '.py')
    'data.py'
    >>> replace_extension('data.json', '')
    'data'

    :param filename:
    :param new_extension:
    :return:
    """
    return filename.split('.')[0] + new_extension


if __name__ == '__main__':
    verify_argv()
    parse_file(argv[1])
    data_frame = DataFrame(entries, columns=COLUMNS)
    data_frame.to_excel(replace_extension(argv[1], '.xlsx'), header=True, index_label='#',
                        sheet_name=replace_extension(argv[1], ''))
