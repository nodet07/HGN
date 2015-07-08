import StringIO
import json
import logging
import random
import urllib
import urllib2
# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2
import cal

TOKEN = '113450359:AAFqYCokS8ZCjLyVV9Lvp9vHWXFrI8U5Lgc'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)

        if text.startswith('/'):
            if 'hoj' in fr['first_name'] or 'Hoj' in fr['first_name']:
                dic = {"res":'حجت گه نخور تو از دستورات نمیتونی استفاده کنی'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            elif text == '/start':
                dic = {"res":'سلام'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
                setEnabled(chat_id, True)
            elif text == '/stopp':
                reply('Stopped Working ...')
                setEnabled(chat_id, False)
            elif text == '/date':
                reply(cal.get_date())
            elif text == '/time':
                reply(cal.get_time())
            elif text == '/hojjat':
                dic = {"res":'حجت یک گه خور به تمام معناست.'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            elif text == '/mamanhojjat':
                dic = {"res":'مادرش جندست.کیرمم دهنش'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            elif text =='/gara' or text == '/گرا':
                dic = {"res":'گرا ای گرا دختر مردم.'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            elif text == '/abbas':
                dic = {"res":'ای یه سالره بذااااا کنااااار'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            elif text == '/iman':
                if 'Hoj' in fr['first_name']:
                    dic = {"res":'بکنت'}
                    ans_ans = json.dumps(dic,ensure_ascii = False)
                    resp1 = json.loads(ans_ans)
                    back = resp1.get('res')
                    reply(back)
                else:
                    reply(str(fr['first_name']))

            elif text == '/help':
                dic = {"res":'هلپ و این کس شعرا نداریم فقط حجت نباید گه بخوره'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)
            else:
                dic = {"res":'این دستور رو ندارم'}
                ans_ans = json.dumps(dic,ensure_ascii = False)
                resp1 = json.loads(ans_ans)
                back = resp1.get('res')
                reply(back)


        # CUSTOMIZE FROM HERE

        #elif 'who are you' in text:
        #    reply('A Bot Who wants to Fuck Hojjat')
        #elif 'what time' in text:
        #    reply('/time bezan :D')
        else:
            logging.info('test')
            logging.info(fr)
            dic = {"res":"حجت خفه شو"}
            hojat_ans = json.dumps(dic,ensure_ascii = False)
            if getEnabled(chat_id) and ('hoj' in fr['first_name'] or 'Hoj' in fr['first_name'] or 'Iman' in fr['first_name']) :
                resp1 = json.loads(hojat_ans)
                back = resp1.get('res')
                reply(back)
                #if not back:
                #    reply('okay...')
                #else:
                #    reply(back)
            else:
                logging.info('not enabled for chat_id {}'.format(chat_id))


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)

#https://iman-mirzadeh-1234.appspot.com/set_webhook?url=https://iman-mirzadeh-1234.appspot.com/webhook
#https://github.com/yukuku/telebot/
