from hashids import Hashids
hashids = Hashids(min_length=5)
def generate_short_url(long_url):
    hashid = hashids.encode(1)  # Assuming 1 is the ID of the URL in the database
    return hashid
