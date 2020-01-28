import typing

from .session_factory import create_auth_session


class AuthVerifier:
    def __init__(self, config: typing.Dict):
        self.config = config

    def test_auth(self, url: str) -> typing.Tuple[bool, typing.Optional[str]]:
        try:
            self.auth_session = create_auth_session(auth_config=self.config)
            res = self.auth_session.get(url)
            # logger.info(pprint.pformat(res))
            if None == res:
                raise Exception("No response object returned")
            if not res:
                res.raise_for_status()
        except Exception as e:
            # Failure
            raise e
            return False, f"{e}"
        # Success
        return True, None