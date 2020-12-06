from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient(hosts='http://localhost:8529')

# Connect to "test" database as root user.
db = client.db('fastapidemo', username='root', password='1234')
