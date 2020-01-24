import logging
import pprint


from requests_oauthlib import OAuth2Session
from urllib3.exceptions import NewConnectionError

import inspect


logger = logging.getLogger(__name__)


class LatigoAuthSession(OAuth2Session):

    """
    A wrapper for OAuth2Session that allows us to do debugging and adal refresh among other things.
    See https://requests.readthedocs.io/en/latest/_modules/requests/sessions/#Session
    See https://requests-oauthlib.readthedocs.io/en/latest/api.html#oauth-2-0-session
    """

    def __init__(self, client_id=None, client=None, auto_refresh_url=None, auto_refresh_kwargs=None, scope=None, redirect_uri=None, token=None, state=None, token_updater=None, **kwargs):
        logging.info(f"@@@ Latigo Session: __init__(client_id={client_id}, auto_refresh_url={auto_refresh_url}, scope={scope}, redirect_uri={redirect_uri}).")
        super(LatigoAuthSession, self).__init__(client_id=client_id, client=client, auto_refresh_url=auto_refresh_url, auto_refresh_kwargs=auto_refresh_kwargs, scope=scope, redirect_uri=redirect_uri, token=token, state=state, token_updater=token_updater, **kwargs)

    def prepare_request(self, request):
        logging.info(f"@@@ Latigo Session: prepare_request(request={request}).")
        return super(LatigoAuthSession, self).prepare_request(request)

    def request(self, method, url, data=None, headers=None, withhold_token=False, client_id=None, client_secret=None, **kwargs):
        logging.info(f"@@@ Latigo Session: request(method={method}).")
        try:
            response = super(LatigoAuthSession, self).request(method=method, url=url, data=data, headers=headers, withhold_token=withhold_token, client_id=client_id, client_secret=client_secret, **kwargs)
            return response
        except NewConnectionError as nce:
            logger.error(f"Could not connect (method={method}, url='{url}'): {nce}")
        except Exception as e:
            logger.error(f"Could not perform request(method={method}, url='{url}'): {e}")
        #            raise e
        return None

    def send(self, request, **kwargs):
        logging.info(f"@@@ Latigo Session: send().")
        return super(LatigoAuthSession, self).send(request, **kwargs)

    def close(self):
        logging.info(f"@@@ Latigo Session: close().")
        return super(LatigoAuthSession, self).close()
