## License header injector

License header injector is a python package that is designed to inject licence into your project files.

You just need to provide the licence text.


## Usage
- Then importing the injector class

```python
from script import LicenceInjector

my_license_header_text = '''
# This file is part of License header injector
#
# License header injector is licensed under the GNU General Public License v3.0.
# See the LICENSE file for more details.
#
# Copyright (C) 2024 Armen-Jean Andreasian.
'''

# Yes, we pass it as a multiline string. 
# If needed, you can keep it in a file, read then assign.


injector = LicenceInjector(
    licence_header_text=my_license_header_text,  # str: The header text
    file_extensions=('.py', '.ts', '.go'),  # tuple[str]: the file types that needed to be injected
    directory = '.'  # optional parameter
)

injector.inject()

# done! check the files!
```