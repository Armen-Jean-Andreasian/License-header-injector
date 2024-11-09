## License Header Injector

**License Header Injector** is a Python package designed to easily insert license headers into your project's source files. Simply provide the license text, specify the file types, and let the script handle the rest.

### Usage

1. Extract the script file and include it in your project.

2. Use the following example to initialize the injector and insert the license headers:

   ```python
   from script import LicenseInjector

   # Define your license header text as a multiline string
   license_header_text = '''
   # This file is part of License Header Injector.
   #
   # License Header Injector is licensed under the GNU General Public License v3.0.
   # See the LICENSE file for more details.
   #
   # Copyright (C) 2024 Armen-Jean Andreasian.
   '''

   # Initialize the LicenseInjector with the desired parameters
   injector = LicenseInjector(
       license_header_text=license_header_text,  # str: The license header text
       file_extensions=('.py', '.ts', '.go'),    # tuple[str]: File types to inject into
       directory='.'                             # optional parameter, default is current directory
   )

   # Run the injector to add headers to the specified files
   injector.inject()

   # License headers have now been added to the specified files!
   ```
