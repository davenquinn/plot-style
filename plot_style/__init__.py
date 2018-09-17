from os import path, environ
import matplotlib
import yaml
from matplotlib import pyplot
from string import ascii_uppercase
from seaborn.apionly import despine

pyplot.rcdefaults()

fn = path.join(path.dirname(__file__),'rc-settings.yaml')
fn = environ.get("PLOT_STYLE_SETTINGS",fn)

with open(fn) as f:
    style_object = yaml.load(f)
for k,v in style_object.items():
    matplotlib.rc(k,**v)

def axis_labels(*axes, pad=0.14, ypos=1, **kwargs):
    offset = kwargs.pop("offset", 0)
    defaults = dict(
        color="#888888", fontsize=20,
        weight='bold', va='top')
    defaults.update(kwargs)

    for i, a in enumerate(axes):
        a.text(-pad,ypos, ascii_uppercase[i+offset],
               transform=a.transAxes, **defaults)


