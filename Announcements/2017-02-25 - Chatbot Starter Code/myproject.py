import os
import json
import random
import requests
import time

from flask import Flask, request, Response


application = Flask(__name__)

# FILL THESE IN WITH YOUR INFO
my_bot_name = '' #e.g. zac_bot
my_slack_username = '' #e.g. zac.wentzell


slack_inbound_url = ''


# this handles POST requests sent to your server at SERVERIP:41953/slack
@application.route('/slack', methods=['POST'])
def inbound():
    # Adding a delay so that all bots don't answer at once (could overload the API).
    # This will randomly choose a value between 0 and 10 using a uniform distribution.
    delay = random.uniform(0, 10)
    time.sleep(delay)

    print '========POST REQUEST @ /slack========='
    response = {'username': my_bot_name, 'icon_emoji': ':robot_face:', 'text': ''}
    print 'FORM DATA RECEIVED IS:'
    print request.form

    channel = request.form.get('channel_name') #this is the channel name where the message was sent from
    username = request.form.get('user_name') #this is the username of the person who sent the message
    text = request.form.get('text') #this is the text of the message that was sent
    inbound_message = username + " in " + channel + " says: " + text
    print '\n\nMessage:\n' + inbound_message

    if username in [my_slack_username, 'zac.wentzell']:
        # Your code for the assignment must stay within this if statement

        # A sample response:
        if text == "What's your favorite color?":
        # you can use print statments to debug your code
            print 'Bot is responding to favorite color question'
            response['text'] = 'Blue! (Waited for {}s before responding)'.format(delay)
            print 'Response text set correctly'
            print response['text']


        if slack_inbound_url and response['text']:
            r = requests.post(slack_inbound_url, json=response)

    print '========REQUEST HANDLING COMPLETE========\n\n'

    return Response(), 200


# this handles GET requests sent to your server at SERVERIP:41953/
@application.route('/', methods=['GET'])
def test():
    return Response('Your flask app is running!')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=41953)