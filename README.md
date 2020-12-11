# NRPE interface for Juju Operator Framework charms

This interface works with the [NRPE charm](https://jaas.ai/nrpe) to provide monitoring and altering in combination
with [Nagios](https://jaas.ai/nagios)


To use it, add the library to your `requirements.txt` so [charmcraft](https://github.com/canonical/charmcraft) can
embed it into your final charm:

```
ops
-e git://github.com/canonical/ops-lib-nrpe.git#egg=ops-lib-nrpe
```

Declare the use of the relation in the `provides` section of you charm's `metadata.yaml` file:

```yaml
provides:
  nrpe-external-master:
    interface: nrpe-external-master
    scope: container
```

`NRPE` must be deployed on the same machine as the unit it observes, make sure to specify `scope: container` as part of
the relation definition.

Add the following configuration options to your charm's `config.yaml` file:
```yaml
  nagios_context:
    default: "juju"
    type: string
    description: |
      Used by the nrpe subordinate charms.
      A string that will be prepended to instance name to set the host name
      in nagios. So for instance the hostname would be something like:
        juju-myservice-0
      If you're running multiple environments with the same services in them
      this allows you to differentiate between them.
  nagios_servicegroups:
    default: ""
    type: string
    description: |
      A comma-separated list of nagios servicegroups.
      If left empty, the nagios_context will be used as the servicegroup
```

## Usage

```python
from nrpe.client import NRPEClient

class MyCharm(ops.charm.CharmBase):
    _state = ops.framework.StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.nrpe_client = NRPEClient(self, 'nrpe-external-master')
        self.framework.observe(self.nrpe_client.on.nrpe_available, self.on_nrpe_available)

    def on_nrpe_available(self, event):
        check_name = "check_{}".format(self.model.unit.name.replace("/", "_"))

        self.nrpe_client.add_check(command=[
            '/usr/lib/nagios/plugins/check_tcp',
            '-H', '127.0.0.1'
            '-p', '8080'
        ], name=check_name)

        # Save all new checks to filesystem and to Nagios
        self.nrpe_client.commit()
```
