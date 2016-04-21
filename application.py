from flask import Flask
import json

# print a nice greeting.
def say_hello(username = "World"):
    return json.dumps('Hello %s!' % username)

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', lambda: say_hello())

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', lambda username: say_hello(username) )

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()