import string, random

class Codec:
    def __init__(self):
        self.mapper = {}
        self.available_chars = list(string.ascii_lowercase+string.ascii_uppercase+'1234567890')
        self.base_url = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        simple_hash = ''.join(random.sample(self.available_chars, 6))
        self.mapper[self.base_url + simple_hash] = longUrl
        return self.base_url + simple_hash

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.mapper.get(shortUrl, '')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))