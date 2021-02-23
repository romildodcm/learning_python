# MININS [MULTIPLE INHERITANCE]
# -> Inherit from multiple classes
# Many modern languages only suport single inheritance
# USES
# Enable functionality for frameworks such as Django
# Streamline repetitive operations

# The scenario
# - What I want to create:
#   Helper database class
#   Create different types for different databases
# - What I want it to be able to do
#   Connect to a database
#   Log whats it's doing 

# Supporting classes
class Loggable:
    def __init__(self) -> None:
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self) -> None:
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

# Create our 'framework'
def framework(item):
    # Perform the connection
    if isinstance(item, Connection):
        item.connect()
    # Log the operation
    if isinstance(item, Loggable):
        item.log()

# Create our database class
class SqlDatabase(Connection, Loggable):
    def __init__(self) -> None:
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_server'

class JustLog(Loggable):
    def __init__(self) -> None:
        self.title = 'Just logging'

# Create an instance of our class
sql_connection = SqlDatabase()
# Use our framework
framework(sql_connection) # connects and logs

print('---------------------------')
# Create an instance of our class
just_log = JustLog()
# Use our framework
framework(just_log)