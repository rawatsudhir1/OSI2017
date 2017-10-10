import httplib, urllib, base64, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key of Emotion API.
subscription_key = 'REPLACE_EMOTION_API_KEY'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({
    # Request parameters. All of them are optional.
})

# The URL of a JPEG image to analyze. Assigned any link in body paramter. Open a browser to see the image. 
# Customer 1 :- http://easysol.in/wp-content/uploads/2016/04/Happy-Store-Customer.jpg
# Customer 2 :- http://www.fireflystoresolutions.com/retail-design-blog/wp-content/uploads/keep-your-customers-happy-with-a-tidy-store_16001235_800788128_0_0_14060666_500.jpg
# Customer 3 :- http://l7.alamy.com/zooms/ced9ffbb4ebd4e3380682014b9605ce9/funny-customer-checking-her-wallet-in-a-department-store-j0mjbw.jpg
# 
body = "{'url':'http://l7.alamy.com/zooms/ced9ffbb4ebd4e3380682014b9605ce9/funny-customer-checking-her-wallet-in-a-department-store-j0mjbw.jpg'}"

try:
    emotionscores=''
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print 'Here is the raw output'
    print (json.dumps(parsed, sort_keys=True, indent=2))
    print ''
   
    if (parsed[0]['scores']['anger'] > 0.60) and (parsed[0]['scores']['anger'] < 1):
        emotionscores = " ANGRY"
    if (parsed[0]['scores']['sadness'] > 0.60) and (parsed[0]['scores']['sadness'] < 1):
        emotionscores = " SAD"
    if (parsed[0]['scores']['neutral'] > 0.60) and (parsed[0]['scores']['neutral'] < 1):
        emotionscores = " NEUTRAL"
    if (parsed[0]['scores']['contempt'] > 0.60) and (parsed[0]['scores']['contempt'] < 1):
        emotionscores = " CONTEMPT"
    if (parsed[0]['scores']['disgust'] > 0.60) and (parsed[0]['scores']['disgust'] < 1):
        emotionscores = " DISGUST"
    if (parsed[0]['scores']['surprise'] > 0.60) and (parsed[0]['scores']['surprise'] < 1):
        emotionscores = " SURPRISE"
    if (parsed[0]['scores']['fear'] > 0.60) and (parsed[0]['scores']['fear'] < 1):
        emotionscores = " FEAR"
    if (parsed[0]['scores']['happiness'] > 0.60) and (parsed[0]['scores']['happiness'] < 1):
        emotionscores = " HAPPY"

    if emotionscores == '':
        print 'Not able to detect emotion.'
        print ''
    if emotionscores <> '':
        print 'Customer Emotion is ' + emotionscores
        print ''
        
    conn.close()

# Let's analyze developer experience. Provide accessKey for Text Analytics API Key 
    testvar= raw_input ("Tell me how is your experience at #OSI2017 in one line?  I will detect your emotions :- ")

    uri = 'westus.api.cognitive.microsoft.com'
    path = '/text/analytics/v2.0/sentiment'
    accessKey ='REPLACE_TEXT_ANALYTICS_API_KEY'
    
    def GetSentiment (documents):
        "Gets the sentiments for a set of documents and returns the information."

        headers = {'Ocp-Apim-Subscription-Key': accessKey}
        conn = httplib.HTTPSConnection (uri)
        body = json.dumps (documents)
        conn.request ("POST", path, body, headers)
        response = conn.getresponse ()
        return response.read ()
        conn.close()
    documents = { 'documents': [
        { 'id': '1', 'language': 'en', 'text': testvar }
        ]}
    print 'Please wait a moment for the results to appear.\n'
    result = GetSentiment (documents)
    resultintxt = json.dumps(json.loads(result), indent=4)
    resultinjson = json.loads(resultintxt)
    print 'Here is the raw output'
    print resultintxt
    print ''
    
    if (resultinjson['documents'][0]['score'] >0.50):
        print "Glad that your experience at #OSI2017 is very good so far. Have a nice day!"
    if (resultinjson['documents'][0]['score'] == 0.50):
        print "You seems like netural at #OSI2017. Have a nice day!"
    if (resultinjson['documents'][0]['score'] < 0.50):
        print "Sorry to hear that your expereince is not good. Hope it will be become better going forward. Have a nice day!"

except Exception as e:
    print('Error:')
    print(e)
