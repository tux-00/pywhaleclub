# pywhaleclub
Whaleclub.co python API wrapper.

## Installation
`pip install pywhaleclub`

## Use
```python
from pywhaleclub import Client

api_token_demo = 'XXX'

c = Client(api_token_demo)

print(c.get_balance())
print(c.list_positions('active'))
print(c.get_markets(['BTC-USD', 'ETH-USD']))

# Use multi req paramater to get more than 5 currencies at once (5 is the current limit of Whaleclub).
print(c.get_markets(['BTC-USD', 'DASH-BTC', 'ETH-BTC', 'ETH-USD', 'LTC-USD', 'XMR-BTC']), multi_req=True)
```

## Function list
```
get_markets(symbol_list, multi_req=False)
get_price(symbol_list, multi_req=False)
get_balance()
get_transactions(ttype, limit=None)
set_position(direction, market, leverage, size, entry_price=None, stop_loss=None, stop_loss_trailing=None, take_profit=None)
get_position(pid)
update_position(pid, stop_loss=None, stop_loss_trailing=None, take_profit=None)
close_position(pid_list)
cancel_position(pid_list)
split_position(pid, ratio)
list_positions(state, limit=None)
get_active_contracts()
set_turbo_position(direction, market, contract_type, size)
get_turbo_postion(pid)
list_turbo_positions(state, limit=None)
```

## Documentation
Refer to http://docs.whaleclub.co/
