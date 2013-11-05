import capstone.dev_settings

#NEWS FEED STRINGS
NEWSFEED_PROJECT_CREATE = "{0} just created a new project named {1}"
NEWSFEED_PROJECT_COMMIT = "{0} just commited a change to {1}"
NEWSFEED_FORUM_THREAD_NEW = "{0} created a new thread in {1}: {2}"



NEWSFEED_PROJECT_INVITED = "{0} join project {1}"

IMAGE_URL_BEGIN = "<img class='thread_view_user_link_img' src='"
IMAGE_URL_END = "' />"

VIDEO_URL_BEGIN = "<embed src='http://www.youtube.com/v/"
VIDEO_URL_END = "' type='application/x-shockwave-flash' wmode='transparent' width='380' height='280'></embed>"


def ROOT_URL(path):
    if 'capstone' in path:
        return '/capstone'
    else:
        return ''