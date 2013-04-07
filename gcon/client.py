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
        self.hc = HistoryClient(self.gi)

    def list_dirs(self):
        return self.hc.get_histories()

    def list_files(self, hid, ftype):
        history_id = self._get_hid(hid)
        history_name = self._get_hname(hid)
        history = self.hc.show_history(hid)
        files = history['state_ids']['ok']
        if ftype:
            files = [x for x in files if self.show_file(hid, x)['data_type'] == ftype]
        return files

    def show_file(self, hid, fid):
        return self.hc.show_dataset(hid, fid)

    def get_file(self, hid, fid):
        return self.hc.download_dataset(hid, fid)

    def _get_hid(self, hid):
        try:
            return hid.get("id", None)
        except AttributeError:
            return hid

    def _get_hname(self, hid):
        try:
            return hid.get("name", None)
        except AttributeError:
            return hid

def fileinfo_galaxy(file_id):
    pass

def split_galaxy_id(file_id):
    if file_id:
        parts = file_id.split(":", 2)


creds = {"api-key": "2c221263a9128811911975d4ce8c98f7",
         "url": "https://main.g2.bx.psu.edu/"}
