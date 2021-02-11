# LD_Homework README

This file is basic demonstration of LD, displaying the ability to use feature flags in a python script.

# Usage

Use the following command to execute this Python script in your environment:

```
python ldtest.py
```

This simple script uses the LD SDK to check if your IP address matches the targeted IP address.  If your IP address does not match the targeted IP, the prompt will display a short message directing you to a website.  If your IP address does match, it will display an alternate message.

Most of the comments should be self-explanatory and I use the ipify api to gather your external IP when you run this script.


## Credits

The LD reference [page](https://docs.launchdarkly.com/sdk/server-side/python) provided most of the code snippets used.
Additionally, the ipify [site](https://www.ipify.org/) provided the needed code sample for gathering the external IP.
