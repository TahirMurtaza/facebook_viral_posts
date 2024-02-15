import facebook
from datetime import datetime, timedelta
import json
import os
import webbrowser

# Replace with your Facebook App credentials
APP_ID = ""
APP_SECRET = ""
ACCESS_TOKEN = ""
# Initialize the Facebook Graph API
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version="3.1")


def get_pages_post():
    # Get your Facebook pages
    pages = graph.get_object("me/accounts")["data"]
    pages_posts = []
    # # Loop through each page
    for page in pages:
        page_id = page["id"]
        page_name = page["name"]
        page_access_token = page["access_token"]
        # Get posts from the page in the last 7 days
        seven_days_ago = datetime.now() - timedelta(days=7)
        posts = graph.get_connections(
            access_token=page_access_token,
            id=page_id,
            connection_name="posts",
            fields="id,message,created_time,full_picture,status_type,updated_time,access_token",
        )

        for post in posts["data"]:
            post_id = post["id"]

            post_likes = graph.get_connections(
                id=post_id,
                connection_name="likes",
                access_token=page_access_token,
                since=seven_days_ago.strftime("%Y-%m-%dT%H:%M:%S"),
                summary=True,
            )

            if post.get("full_picture", None) != None and "external" not in post.get(
                "full_picture", None
            ):
                # Now 'summary' contains the likes for the current post
                post["page_name"] = page_name
                post["likes_count"] = post_likes["summary"]["total_count"]
                print(post)
                pages_posts.append(post)

    # Sort posts by the number of reactions/likes in descending order
    sorted_posts = sorted(
        pages_posts,
        key=lambda x: x["likes_count"],
        reverse=True,
    )
    save_and_open_results(sorted_posts)


def save_and_open_results(sorted_posts):
    file_path = "data.js"
    print(f"Saving Posts to {file_path}")

    json_data = json.dumps(sorted_posts, indent=4)

    # Write JSON data to JavaScript file
    with open(file_path, "w") as js_file:
        js_file.write(f"var socialData = {json_data};")

    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the file path to the index.html file
    html_file_path = os.path.join(current_directory, "index.html")
    webbrowser.open("file://" + html_file_path, new=2)


if __name__ == "__main__":
    get_pages_post()
