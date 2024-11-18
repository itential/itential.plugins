# Copyright 2024, Itential Inc. All Rights Reserved

# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

DOCUMENTATION = """
---
name: cyberark_ccp
author: Itential

short_description: Retrieve senstive information from Cyberark CCP

description:
  - The lookup plugin will authenticate to an instance of Cyberark CCP and
    retriev the specified serects for use in an Ansible playbook run.

options:
  host:
    description:
      - The hostname or IP address of the CCP server
    type: string
    required: true

  port:
    description:
      - The port used to connect to the server
    type: int

  use_tls:
    description:
      - Enable or disable the use of TLS
    type: bool
    default: true

  certificate_file:
    description:
      - The full path to the certificate file to use for authentication
    type: string

  private_key_file:
    description:
      - The full path to the private key file used for authentication
    type: string

  appid:
    description:
      - Sets the unique ID of the application issuing the password request
    type: string
    required: true

  safe:
    description:
      - Sets the name of the safe where the password is stored
    type: string

  username:
    description:
      - Defines the search criteria accroding to the UserName account property
    type: string

  folder:
    description:
      - Specifies the name of the folder where the password is stored.
    type: string

  object:
    description:
      - Specifies the name of the password object to retrieve.
    type: string

  address:
    description:
      - Defines search criteria according to the Address account property.
    type: string

  database:
    description:
      - Defines search criteria according to the Database account property.
    type: string

  policyid:
    description:
      - Defines the format that will be used in the setPolicyID method.
    type: string

  reason:
    description:
      - The reason for retrieving the password. This reason will be audited in the Credential Provider audit log
    type: string

"""

EXAMPLES = """
- name: lookup a password
  ansible.builtin.set_fact:
    password: "{{ lookup('itential.plugins.cyberark_ccp', appid='app', username='myuser' safe='mysafe') }}"
"""

RETURN = """
_raw:
  description:
    - a password
  type: list
  elements: str
"""


from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase

from ansible_collections.itential.core.plugins.module_utils import http
from ansible_collections.itential.core.plugins.module_utils import display


PARAMETERS = frozenset((
    ("AppID", "appid"),
    ("Safe", "safe"),
    ("Username", "username"),
    ("Folder", "folder"),
    ("Object", "object"),
    ("Address", "address"),
    ("Database", "database"),
    ("PolicyID", "policyid"),
    ("Reason", "reason"),
))


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        ret = []

        host = kwargs.get("host")
        if host is None:
            raise AnsibleError("missing requirement argument: host")

        port = kwargs.get("port")
        if port:
            try:
                port = int(port)
            except ValueError as exc:
                raise AnsibleError("value for port must be a number")

        use_tls = kwargs.get("use_tls") or self.get_option("use_tls")
        if use_tls == "true":
            use_tls = True
        elif use_tls == "false":
            use_tls = False

        verify = kwargs.get("verify")

        url = http.make_url(host, "/AIMWebService/api/Accounts", port=port, use_tls=use_tls)

        params = {}

        for key, option in PARAMETERS:
            value = kwargs.get(option)
            if value is not None:
                params[key] = value

        if "AppID" not in params:
            raise AnsibleError("missing required value: appid")

        if len(params) < 2:
            raise AnsibleError("must specify a query parameter")

        headers = {
            "Content-Type": "application/json"
        }

        http_kwargs = {
            "headers": headers,
            "params": params,
        }

        if verify is not None:
            http_kwargs["verify"] = verify

        if use_tls is True:
            certificate_file = kwargs.get("certificate_file")
            private_key_file = kwargs.get("private_key_file")

            if certificate_file is not None and private_key_file is None:
                http_kwargs.update({
                    "certificate_file": certificate_file,
                    "private_key_file": private_key_file
                })

        display.vvvvv(f"url: {url}")
        display.vvvvv(f"Request: {http_kwargs}")

        resp = http.get(url, **http_kwargs)

        try:
            resp.raise_for_status()
        except Exception as exc:
            raise AnsibleError(str(exc))

        content = resp.Json().get("Content")
        if not content:
            raise AnsibleError("error trying to retrieve password")

        ret.append(content)

        return ret
