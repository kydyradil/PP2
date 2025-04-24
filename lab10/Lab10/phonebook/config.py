from configparser import ConfigParser
import os
print(os.path.abspath('database.ini'))


def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    print(f'Читаем файл {filename}')
    parser.read(filename)
    print(f'Найдены секции: {parser.sections()}')

    if parser.has_section(section):
        params = parser.items(section)
        return {param[0]: param[1] for param in params}
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

config = load_config()
print(config)
