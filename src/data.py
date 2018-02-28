import xml.etree.ElementTree



class Data:
    def __init__(self, filename):
        e = xml.etree.ElementTree.parse(filename).getroot()
