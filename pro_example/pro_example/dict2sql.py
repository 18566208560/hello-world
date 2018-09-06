# -*- coding: utf-8 -*-

"""
@Date: 2000/00/00
@Author: 爱好者围仔
@Email: 122542231@qq.com
"""


def dict2sql_insert(t_, **kwargs):
    """
    dict to sql sentence(insert)
    :param t_: table name
    :param kwargs: (dict) columns and values
    :return: (str) sql sentence(insert)
    """

    # filter not None & bool to int
    d = {k: int(v) if isinstance(v, bool) else v for k, v in kwargs.items() if not isinstance(v, None.__class__)}

    columns = ', '.join(map(str, d.keys()))
    i_ = lambda i: str(i) if isinstance(i, (int, float)) else "'" + str(
        i) + "'"
    values = ', '.join(map(i_, d.values()))
    return 'INSERT INTO {}({}) VALUES({})'.format(str(t_), columns, values)


if __name__ == '__main__':
    d = {
        'name': 'Vision',
        'name2': '',
        'age': 32,
        'age2': 0,
        'height': 182.5,
        'height2': 0.0,
        'gender': True,
        'gender2': False,
        'NoneNone': None,
    }
    print(dict2sql_insert('qyl', **d))
    # print(dict2sql_create_table(t_='qyl222'))
