
# coding: utf-8

# In[21]:


from twilio.rest import Client

def sendmessage(body):
    sid = 'ACb387d0e71fac88acc5e784e18ceedc80'
    auth_token ='53eac279a29e28e023431ec8680ffc4a'
    client = Client(sid, auth_token)
    message = client.messages.create(to="13607420068",from_="12062028871  ",body=body)

sendmessage('test')
