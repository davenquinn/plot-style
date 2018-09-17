from setuptools import setup

setup(
    name='plot_style',
    version='0.1',
    package_dir={'plot_style': 'plot_style'},
    install_requires=['matplotlib', 'seaborn', 'pyyaml'],
    package_data={'plot_style': ['rc-settings.yaml']}
)
