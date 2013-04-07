
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
        pass

    def put_file(self, fname):
        pass

    def list_files(self):
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
