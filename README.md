# pyepsalarm

Python library to interface with EPS systems, operated by Homiris for instance.

Example use:

```
from pyepsalarm import EPS

token = "MYTOKEN"
username = "123456789"
password = "mypassword+"
token_pair = "MYTOKEN_PAIR"
phone_type = "MY PHONE TYPE"

eps = EPS(token, username, password, token_pair, phone_type)

eps.get_status()
eps.arm_night(silent=True)
eps.get_status()
eps.disarm()
```
