"""
** CONTAINER NOTES. NEVER GOT IT WORKING THOUGH **
Guide here: https://tsmx.net/docker-local-mongodb/
`docker network inspect bridge`: choose the "Gateway" address
in the command to run mongo include `--add-host=mongoservice:172.17.0.1`
also have to set mongo conf file to bind that ip. see the web instructions
    - and then replace the original conf file with a new one. see the docker run command below for that.
docker command to start up local mongo:
    `docker run -v /Users/stacy.walker/personal/personal_python/database-stuff:/etc/mongo --add-host=mongoservice:172.17.0.1 -e MONGO_INITDB_ROOT_USERNAME=mongo -e MONGO_INITDB_ROOT_PASSWORD=password mongo --config /etc/mongo/mongod.conf`
now my uri is `mongodb://mongoservice:27017/<mydb>`
for mongo container startup options see: https://hub.docker.com/_/mongo

** INSTALL AND RUN LOCALLY **
https://zellwk.com/blog/local-mongodb/
- had to make the data/db folder in /Users/stacy.walker/data/db
- then to run `mongod --dbpath=/Users/stacy.walker/data/db`
"""

from mongo_adapter import MongoAdapter, get_client

# # Example of an initial easy setup/connection
# db_name = 'test'
# uri = 'mongodb://127.0.0.1:27017'
# client = get_client(uri=uri)
# adapter = MongoAdapter(client, db_name)

# assert adapter.db_name == db_name
# print(adapter.db)
# print(adapter.db_name)
# print(dir(adapter))

# Override defualt setup and follow a more useful pattern.
class LibraryAdapter(MongoAdapter):
    def setup(self, db_name='library'):
        """Overrides the basic setup method"""
        if self.client is None:
            raise SyntaxError("No client is available")
        if self.db is None:
            self.db = self.client[db_name]
            self.db_name = db_name

        self.books_collection = self.db.book
        self.user_collection = self.db.book
        print(" ** IN SETUP **")

db_name = 'test'
uri = 'mongodb://127.0.0.1:27017'
client = get_client(uri=uri)
adapter = LibraryAdapter(client, db_name)
print(adapter)

