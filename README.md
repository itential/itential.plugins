# Ansible Collection - itential.plugins

The `itential.plugins` collection provides Ansible plugins for use in playbooks
executed from Itential Automation Gateway.

All plugins provided in this collection are provided freely to the Ansible
community and are fully community supported.

## Plugins

This collection provides plugins that can be used in Ansible.

## Building the collection

To build the collection from the source code, use the following command
```bash
ansible-galaxy collection build <path to collection source code> --output-path <path to tarball>
```

## Installing the collection

The collection can be installed using either the Itential Automation Gateway UI
or the Ansible Galaxy CLI directly or defined as part of a `requirements.yaml`
file.

To install the collection on a server running Itential Automation Gateway,
simply click the "Install a collection" from the main page toolbar.

See the [Itential documentation](https//docs.itential.com) for more details about installing a collection
on an Itential Automation Gateway server.

Alternatively, the Ansible Galaxy CLI can be used to install the collection.
To use the Galaxy CLI, run the following command in your development
environment or on the Itential Automation Gateway server.

```bash
ansible-galaxy collection install itential.plugins
```

The collection can also be installed by adding it to an Ansible Galaxy
`requirements.yaml` file as shown below.

```yaml
---
collections:
  - name: itential.plugins
```

Once installed, the collection is available for use.
## Inventory

| Name                          | Description                        |
|-------------------------------|------------------------------------|
| `itential.plugins.solarwinds` | Pull inventory from Solarwinds NCM.  See the example configuration file [here](docs/solarwinds.example.yaml) |

## Lookup

| Name                           | Description                        |
|--------------------------------|------------------------------------|
| `itential.plugins.cyberark_ccp` | Retrieve secrets from CyberArk CCP |


## Contributing

Contributions to this collection are welcomed.  This includes new features,
enhancements, bug fixes as well as updates to the documentation.  If you
encounter any problems using this collection, please open an issue
[here](https://github.com/itential/itential.plugins/issues) or open a pull request with your proposed changes [here](https://github.com/itential/itential.plugins/pulls).

For additional details please consult the Itential Community Guide found
[here](CONTRIBUTING.md)


## Code of Conduct

This project is managed by the Itential community and sponsored by Itential and
governed by a Code of Conduct.  Please familiarize yourself with our Code of
Conduct available [here](CODE_OF_CONDUCT.md)

## Release Notes

The release notes provide a quick glance with regards to new and/or changed
features and bug fixes available in each release.  The release notes are
updated for each release and can be found [here](CHANGELOG.md)


## More Information

Additional information about Itential Automation Gateway can be found at
http://itential.com.


# License

GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) to see the full text.