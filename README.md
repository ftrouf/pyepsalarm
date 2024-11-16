# pyepsalarm

Python library to interface with EPS systems, operated by Homiris for instance.

Example use:

```
from pyepsalarm import EPS

token = "MYTOKEN"
username = "123456789"
password = "mypassword+"
device_token = "MY TOKEN DEVICE"
phone_type = "MY PHONE TYPE"

eps = EPS(token, username, password, device_token, phone_type)

eps.get_status()
eps.arm_night(silent=True)
eps.get_status()
eps.disarm()
```
