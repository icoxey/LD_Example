# import your libraries
import sys
import string
import random
from requests import get
import ldclient
from ldclient.config import Config

# define site URL and path for off
site = "https://www.iancoxey.com"
siteoff = site + "/ldoff"

# define character sets for the user key
key_set = string.ascii_lowercase + string.ascii_uppercase + string.digits

# reach out and get external IP
ip_addr = get('https://api.ipify.org').text

# function to create a random key for this session
def make_key():
      return ''.join(
        random.choice(key_set) 
        for _ in range(8)
    )

# main using my sdk key
if __name__ == "__main__":
  sdk_key = "sdk-e77356dd-34ee-4c86-8219-018a22e6f13d"
  ldclient.set_config(Config(sdk_key))

# get inputs from user
  firstname = input("Please enter your first name: ")
  lastname = input("Please enter your last name: ")
  emailaddr = input("Please enter your email address: ")

# create the user key
  make_key()
  key = make_key()

# user data to pass through, note IP info for targeting
  user = {
    "key": key,
    "firstName": firstname,
    "lastName": lastname,
    "email": emailaddr,
    "ip": ip_addr
    }

# get variations, using walkthrough as basis. "test" is feature flag key
  show_feature = ldclient.get().variation("test", user, False)

# if/else statement displays based on user targeting in dashboard
  if show_feature:
    print("Thank you, " + firstname + " " + lastname + ", your IP is allowed. You should visit " + site)
  else:
    print("Sorry, your IP is not allowed, as you can see here: " + siteoff)

# close ld
  ldclient.get().close()
