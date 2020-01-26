from setuptools import setup

setup(
    name='scr',
    version='2.0',
    py_modules=['scr'],
    install_requires=[
        'click', 'colorama', 'tabulate'
    ],
    entry_points='''
        [console_scripts]
        scr=scr:cli
    ''',
)
