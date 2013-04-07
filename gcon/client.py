from bioblend.galaxy.histories import HistoryClient
from bioblend.galaxy import GalaxyInstance

def get_client(platform, creds):
    if platform == "genomespace":
        return GenomespaceClient(creds)
    elif platform == "galaxy":
        return GalaxyClient(creds)
    elif platform == "basespace":
        return BasespaceClient(creds)


class AbstractClient(object):
    def __init__(self, creds):
        self.creds = creds

    def get_file(self, fname):
        return fname

    def put_file(self, fname):
        pass

    def list_files(self):
        pass

    def list_dirs(self):
        pass


class GenomespaceClient(AbstractClient):
    def __init__(self, creds):
        super(GenomespaceClient, self).__init__(creds)


class BasespaceClient(AbstractClient):
    def __init__(self, creds):
        super(BasespaceClient, self).__init__(creds)


class GalaxyClient(AbstractClient):
    def __init__(self, creds):
        super(GalaxyClient, self).__init__(creds)
        self.url = creds.get("url", None)
        self.api_key = creds.get("api-key", None)
        self.gi = GalaxyInstance(self.url, self.api_key)

    def list_dirs(self):
        hc = HistoryClient(self.gi)
        return hc.get_histories()

creds = {"api-key": "2c221263a9128811911975d4ce8c98f7",
         "url": "https://main.g2.bx.psu.edu/"}
