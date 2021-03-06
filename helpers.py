"""
The tool to check the availability or syntax of domains, IP or URL.

::


    ██████╗ ██╗   ██╗███████╗██╗   ██╗███╗   ██╗ ██████╗███████╗██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝ █████╗  ██║   ██║██╔██╗ ██║██║     █████╗  ██████╔╝██║     █████╗
    ██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗██║     ██╔══╝
    ██║        ██║   ██║     ╚██████╔╝██║ ╚████║╚██████╗███████╗██████╔╝███████╗███████╗
    ╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ ╚══════╝╚══════╝

This provide some helper functions.

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Author:
    Nissar Chababy, @funilrys, contactTATAfunilrysTODTODcom

Special thanks:
    https://pyfunceble.github.io/special-thanks.html

Contributors:
    https://pyfunceble.github.io/contributors.html

Project link:
    https://github.com/funilrys/PyFunceble

Project documentation:
    https://pyfunceble.readthedocs.io/en/master/

Project homepage:
    https://pyfunceble.github.io/

License:
::


    Copyright 2017, 2018, 2019, 2020 Nissar Chababy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import PyFunceble
from colorama import Fore, Style
from colorama import init as initiate_colorama

# We initiate colorama.
initiate_colorama(True)


def print_test_result(subject, status):
    """
    Given the subject and its status, we print it to STDOUT.

    :param str subject: The subject we are going to print.
    :param str status: The status of the domain.
    """

    if status.lower() in PyFunceble.STATUS.list.up:
        print(f"{Fore.GREEN + Style.BRIGHT}{subject} is {status}")
    elif status.lower() in PyFunceble.STATUS.list.down:
        print(f"{Fore.RED + Style.BRIGHT}{subject} is {status}")
    else:
        print(f"{Fore.CYAN + Style.BRIGHT}{subject} is {status}")


def print_syntax_result(subject, status):
    """
    Given the subject and its validation, we print it to STDOUT.

    :param str subject: The subject we are going to print.
    :param bool status: The validation state.
    """

    if status is True:
        print(f"{Fore.GREEN + Style.BRIGHT}{subject} is VALID")
    else:
        print(f"{Fore.CYAN + Style.BRIGHT}{subject} is INVALID")
