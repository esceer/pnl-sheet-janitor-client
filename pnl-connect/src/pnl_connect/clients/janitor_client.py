class JanitorClient:

    def __init__(self):
        import requests
        self._requests = requests

    def fetch_summary(self):
        response = self._requests.get(JanitorClient._get_fetch_summary_url())
        return response.json()

    @staticmethod
    def _get_fetch_summary_url() -> str:
        return JanitorClient._get_base_path() + '/'

    @staticmethod
    def _get_base_path() -> str:
        return 'http://%s:%s/%s' % (
            '192.168.1.100',
            '8090',
            'pnl-janitor'
        )
