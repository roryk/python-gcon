from bioblend.galaxy import GalaxyInstance
import uuid
import collections

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
        return self.gi.histories.get_histories()

    def list_files(self, ftype=None):
        histories = self.list_dirs()
        history_ids = self._get_history_ids(histories)
        files = flatten(map(self._list_files_in_history, history_ids))
        fileinfos = map(self.gi.datasets.show_dataset, files)
        if ftype:
            fileinfos = [x for x in fileinfos if x['data_type'] == ftype]
            fileinfos = filter(self._is_file_accessible, fileinfos)
        return fileinfos

    def get_file(self, hid, fid):
        return self.gi.histories.download_dataset(hid, fid)

    def _get_history_ids(self, histories):
        return [x["id"] for x in histories]

    def _is_file_accessible(self, finfo):
        return finfo["accessible"]

    def _list_files_in_history(self, hid):
        history = self.gi.histories.show_history(hid)
        return history['state_ids']['ok']

    def put_file(self, hid, fid):
        """
        final Map<String, String> uploadParameters = new HashMap<String, String>();
        uploadParameters.put("dbkey", dbKey);
        uploadParameters.put("file_type", fileType);
        uploadParameters.put("files_0|NAME", file.getName());
        uploadParameters.put("files_0|type", "upload_dataset");
        """
        lib_id = str(uuid.uuid4())
        self.lc.create_library(lib_id)

    def _prep_put(self, hid, fid):
        pass

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

    def _get_user_info(self):
        user_info = self.gi.users.get_current_user()
        if not user_info:
            return None
        elif "username" in user_info:
            return user_info.get("username")
        elif "email" in user_info:
            return user_info.get("email")
        else:
            return None

def flatten(l):
    """
    flatten an irregular list of lists
    example: flatten([[[1, 2, 3], [4, 5]], 6]) -> [1, 2, 3, 4, 5, 6]
    lifted from: http://stackoverflow.com/questions/2158395/

    """
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el,
                                                                   basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el

# just for testing atm
creds = {"api-key": "2c221263a9128811911975d4ce8c98f7",
         "url": "https://main.g2.bx.psu.edu/"}
