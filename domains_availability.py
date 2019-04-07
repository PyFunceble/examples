"""
The tool to check the availability or syntax of domains, IPv4 or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This is an example which repond to the following problematic(s):

    * How can I get the avaibility of a domain or IP with PyFunceble ?

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.readthedocs.io/en/2.x.x/special-thanks.html

Contributors:
    http://pyfunceble.readthedocs.io/en/2.x.x/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/2.x.x/

Project homepage:
    https://funilrys.github.io/PyFunceble/

License:
::


    MIT License

    Copyright (c) 2017, 2018, 2019 Nissar Chababy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# We want some coloration so we import the tool do to that :)
from PyFunceble import initiate, Fore, Style
# We import the tool to print the colored CLI logo.
from PyFunceble.cli_core import CLICore
# We import the configuration loader.
from PyFunceble import load_config
# We import the test method of the PyFunceble API.
from PyFunceble import test as PyFunceble

# We initiate the list of domains we are going to test.
DOMAINS = ["google.com", "tweeetttter.com" , "github.com", "examplessss.ooooorgg", "twitter.com"]

# We initiate colorama.
initiate(True)

# We load our configuration.
#
# Note: We need this to print the logo but if you
# doesn't need the logo, you can ignore this.
load_config(generate_directory_structure=False)

# We print the PyFunceble logo.
CLICore.colorify_logo(home=True)

def print_result(subject, status):
    """
    Given the subject and its status, we print it to STDOUT.

    :param str subject: The subject we are going to print.
    :param str status: The status of the domain.
    """

    if status == "ACTIVE":
        print(f"{Fore.GREEN + Style.BRIGHT}{domain} is {status}")
    elif status == "INACTIVE":
        print(f"{Fore.RED + Style.BRIGHT}{domain} is {status}")
    else:
        print(f"{Fore.CYAN + Style.BRIGHT}{domain} is {status}")

for domain in DOMAINS:
    # We loop through the list of domain.

    # And we print the colored!
    print_result(domain, PyFunceble(domain))

