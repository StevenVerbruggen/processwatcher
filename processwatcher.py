import os
import argparse
import psutil
import time
#from slackclient import SlackClient

import json
import requests

parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS, description="Process watcher", add_help=False)

man_args = parser.add_argument_group("Mandatory parameters")
man_args.add_argument("--pid", "-p", action="store", required=True, nargs="?", metavar="int", type=int,help="PID")

opt_args = parser.add_argument_group("Optional parameters")
opt_args.add_argument("--help", "-h", action="help", help="Show help message and exit")
opt_args.add_argument("--name", "-n", action="store", required=False, nargs="?", metavar="str", default="unnamed", type=str, help="Custom name")

args = parser.parse_args()



while psutil.pid_exists(args.pid):
    time.sleep(5)


# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
# Update: it is now better to create a Slack app that allows incoming webhooks and create webhooks from there and paste them below
# More info: https://api.slack.com/messaging/webhooks
webhook_url = 'paste_your_hook_here'
slack_data = {'text': "Process "+str(args.pid)+" done: "+str(args.name)}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)


