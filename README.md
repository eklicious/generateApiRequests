# generateApiRequests
Python commandline application to generate HTTP GET requests to MongoDB Atlas/Stitch Webhook

1 - The webhook is called from the Python Load Generator.  Webhook is defined as a Service called apiService.  The Webhook is getProductsWebhook.  This function will call a separate function to log the transaction (logTransactionFunction) and will increment the apiAccess counter by +1 by using an upsert.

2 - The trigger is defined by capturing any Insert, Update, or Replace on the apiAccessLog collection.  The trigger source is userExceededLimitTriggerFunction.  The function will write several log messages to the Stitch Log Console to indicate what changeEvent occurred.  It will access the apiLimit collection by user to determine the api threshold.  If the number of times the api has been accessed according to the user has exceeded the defined apiLimit, a notification is sent (sendNotificationFunction).  The sendNotificationFunction will log the notification and then send a notification via Twilio/Slack/Email/etc.  The actual notification is still being completed.

3 - Finally, once the notification has been inserted, the resetApiAccessedCount function is fired to reset the api access count to 0 and update the apiResetCountDate.

The Python Load Generator is here: https://github.com/blainemincey/generateApiRequests

It includes an .env.example file but I have attached the contents of the .env file I used to this email.  You will need to rename from my-dot-env-file to .env in the project root.

Keep in mind, you may have to run a 'pip install' for a couple of Python modules.  

If you want to access the cluster via Compass, the user is fedExUser and the password is fedExUser123 .
