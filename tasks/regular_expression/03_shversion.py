import re

ver_pattern=r'/(junos-version).+\n\s+{\n\s+"data" : "(\d.+)"$/gm'
model_pattern=r'/(product-name).+\n\s+{\n\s+"data" : "(\w.+)"$/gm'