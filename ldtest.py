# import your libraries
from requests import get
import ldclient
from ldclient.config import Config

# define site URL and path for off
site = "https://www.iancoxey.com"
siteoff = site + "/ldoff"

# reach out and get external IP
ip_addr = get('https://api.ipify.org').text

# main using my sdk key
if __name__ == "__main__":
  sdk_key = "sdk-e77356dd-34ee-4c86-8219-018a22e6f13d"
  ldclient.set_config(Config(sdk_key))
# user data to pass through, note IP info for targeting
  user = {
    "key": "abc123",
    "firstName": "Ian",
    "lastName": "Coxey",
    "email": "ian.coxey@gmail.com",
    "ip": ip_addr
    }

# get variations, using walkthrough as basis. "test" is feature flag key
  show_feature = ldclient.get().variation("test", user, False)

# if/else statement displays based on user targeting in dashboard
  if show_feature:
    print("Your IP is allowed. You should visit " + site)
  else:
    print("Sorry, your IP is not allowed, as you can see here: " + siteoff)

# close ld
  ldclient.get().close()
