import argparse
import sys

from sites.sdk import SitesClient
from sites.sdk.sites import Site, Authenticator


parser = argparse.ArgumentParser()
parser.add_argument("--token", type=str)
parser.add_argument("--path", type=str)
parser.add_argument("--space", type=str)
parser.add_argument("--name", type=str)

args = parser.parse_args()

error = False
for k, v in vars(args).items():
    if not v:
        print(f'::error::Input "{k}" not provided!')
        error = True

if error:
    sys.exit(1)

# setup authenticated content manager instance
site_authenticator = Authenticator.from_token(token=args.token)
client = SitesClient(authenticator=site_authenticator)
site = Site.from_space_and_name(space=args.space, name=args.name)
site_content_manager = client.content(site=site)

# upload all the contents of a directory
print("Uploading...")
res = site_content_manager.upload(local_path=args.path, recursive=True)
print(res)
if isinstance(res, list) and len(res):
    print(f"Successfully uploaded to sites.ecmwf.int/{args.space}/{args.name}")
else:
    print("::error::Upload failed!")
    sys.exit(1)
