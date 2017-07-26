import requests


class Client():
    """WhaleClub.co API wrapper."""
    def __init__(self, api_token):
        self._headers = self._get_headers(api_token)
        self._url = 'https://api.whaleclub.co/v1/'
        self.max_market_req = 5

    def _get_headers(self, api_token):
        """Construct header with api_token variable."""
        headers = {'Authorization': 'Bearer {}'.format(api_token)}
        return headers

    def _convert_list_to_str(self, l):
        if type(l) == list:
            return ','.join(l)
        return l

    def get_markets(self, symbol_list, multi_req=False):
        """Returns market information for one or more markets."""

        if multi_req:
            markets = {}
            # Cut symbol_list to get 5 symbols in a request
            for i in range(self.max_market_req, len(symbol_list) + self.max_market_req, self.max_market_req):
                r = self.get_markets(symbol_list=','.join(symbol_list[i - 5:i]), multi_req=False)
                markets.update(r)
            return markets

        symbol_list = self._convert_list_to_str(symbol_list)
        r = requests.get(self._url + 'markets/' + symbol_list, headers=self._headers)

        return r.json()

    def get_price(self, symbol_list, multi_req=False):
        """Returns the current bid and ask prices for one or more markets."""

        if multi_req:
            markets = {}
            for i in range(self.max_market_req, len(symbol_list) + self.max_market_req, self.max_market_req):
                r = self.get_price(symbol_list=','.join(symbol_list[i - 5:i]), multi_req=False)
                markets.update(r)
            return markets

        symbol_list = self._convert_list_to_str(symbol_list)
        r = requests.get(self._url + 'price/' + symbol_list, headers=self._headers)
        return r.json()

    def get_balance(self):
        """Returns information about your balance."""
        r = requests.get(self._url + 'balance/', headers=self._headers)
        return r.json()

    def get_transactions(self, ttype, limit=None):
        """List transactions that have occurred on your account."""
        params = {'limit': limit}
        r = requests.get(self._url + 'transactions/' + ttype, params=params, headers=self._headers)
        return r.json()

    def set_position(self, direction, market, leverage, size, entry_price=None, stop_loss=None, stop_loss_trailing=None, take_profit=None):
        """Submit a new position."""
        data = {}

        data['direction'] = direction
        data['market'] = market
        data['leverage'] = leverage
        data['size'] = size

        if entry_price != None:
            data['entry_price'] = entry_price
        if stop_loss != None:
            data['stop_loss'] = stop_loss
        if stop_loss_trailing != None:
            data['stop_loss_trailing'] = stop_loss_trailing
        if take_profit != None:
            data['take_profit'] = take_profit

        r = requests.post(self._url + 'position/new', data=data, headers=self._headers)

        return r.json()

    def get_position(self, pid):
        """Fetch information about an existing position."""
        r = requests.get(self._url + 'position/' + pid, headers=self._headers)
        return r.json()

    def update_position(self, pid, stop_loss=None, stop_loss_trailing=None, take_profit=None):
        """Update an existing position."""
        params = {}

        if stop_loss != None:
            params['stop_loss'] = stop_loss
        if stop_loss_trailing != None:
            params['stop_loss_trailing'] = stop_loss_trailing
        if take_profit != None:
            params['take_profit'] = take_profit

        r = requests.put(self._url + 'position/update/' + pid, data=params, headers=self._headers)

        return r.json()

    def close_position(self, pid_list):
        """Close one or multiple active positions at market price."""
        pid_list = self._convert_list_to_str(pid_list)
        r = requests.put(self._url + 'position/close/' + pid_list, headers=self._headers)
        return r.json()

    def cancel_position(self, pid_list):
        pid_list = self._convert_list_to_str(pid_list)
        """Cancel one or multiple pending positions."""
        r = requests.put(self._url + 'position/cancel/' + pid_list, headers=self._headers)
        return r.json()

    def split_position(self, pid, ratio):
        """Split an existing pending or active position."""
        data = {'ratio': ratio}
        r = requests.post(self._url + 'position/split/' + pid, data=data, headers=self._headers)
        return r.json()

    def list_positions(self, state, limit=None):
        """List positions."""
        params = {}

        if limit != None:
            params['limit'] = limit

        r = requests.get(self._url + 'positions/' + state, params=params, headers=self._headers)

        return r.json()

    def get_active_contracts(self):
        """Fetch a list of currently active turbo contracts."""
        r = requests.get(self._url + 'contracts/', headers=self._headers)
        return r.json()

    def set_turbo_position(self, direction, market, contract_type, size):
        """Open a new turbo position."""
        data = {}

        data['direction'] = direction
        data['market'] = market
        data['type'] = contract_type
        data['size'] = size

        r = requests.post(self._url + 'position-turbo/new', data=data, headers=self._headers)

        return r.json()

    def get_turbo_postion(self, pid):
        """Fetch information about an existing turbo position."""
        r = requests.get(self._url + 'position-turbo/' + pid, headers=self._headers)
        return r.json()

    def list_turbo_positions(self, state, limit=None):
        """List turbo positions."""
        params = {}

        if limit != None:
            params['limit'] = limit

        r = requests.get(self._url + 'positions-turbo/' + state, headers=self._headers)
        return r.json()

