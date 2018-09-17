# Plot Style

Basic plot styles for use with  `matplotlib` in Python.
A somewhat bespoke elaboration of
`matplotlibrc` files that allows setting of config items using
hierarchical YAML, and sets several sane defaults that can be
overridden.

- Loads YAML configuration from file defined by `PLOT_STYLE_SETTINGS`
  environment variable or from internal `rc-settings.yaml`.
- Provides functions `despine` (direct from `seaborn`) and
  `axis_labels(*axes, **kwargs)` This function creates labels for each
  axis in a set; `pad`, `ypos`, `offset`, and all keywords accepted
  by `ax.text` can be passed..

