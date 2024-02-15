# Facebook Image Posts Analytics Script
## The script uses FB Graph API to list the image posts from the past 7 days in descending order of virality.
The script which is be able to login with Facebook, give it the permissions it needs, then it should just list all images posted in the last 7 days from all my facebook pages, filtered descending from the image with the biggest number of likes to the image with the smallest number of likes.

## Steps

To run the script here are the steps:
1. Go to FB Graph API explorer https://developers.facebook.com/tools/explorer/ and select your app Id. Generate access token and copy it.
2. Open http://app.py file and replace with your FB credentials of APP_ID, APP_SECRET and ACCESS_TOKEN (copied from FB Graph API explorer)
3. Run the the command to install packages: 
   `pip install facebook-sdk`
4. Run the command to run the script:
  `python app.py`
5. The script will run and show the expected results on index.html web page.

## Following permissions are required in FB APP

pages_manage_cta, 
pages_manage_instant_articles, 
pages_show_list,
read_page_mailboxes,
pages_messaging,
pages_messaging_subscriptions,
page_events,
pages_read_engagement,
pages_manage_metadata,
pages_read_user_content,
pages_manage_ads,
pages_manage_posts,
pages_manage_engagement
