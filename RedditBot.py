import praw
sublist = [] #Up to you!
reddit = praw.Reddit(client_id = '<client_id>', client_secret='<client_secret>', user_agent='<console_header>')
def get_videos(sub):
  subreddit = reddit.subreddit(sub)
  url_verif = '<dummy url>'
  hot_posts = [i for i in subreddit.hot(limit = 20)]
  def find_video(limit):
      saved = 0
      posts = hot_posts[limit-1]
      if '.jpg' or '.png' not in posts.url:
          url = posts.url
          for comment in posts.comments:
              if hasattr(comment, "body"):
                  commented = comment.body
                  if 'u/save' in commented:
                      saved = saved + 1
          return [url, saved]
  
  videos = []
  for i in range(1,20):
      url, saver_num = find_video(i)
      if '.jpg' in find_video(i)[0]:
          pass
      else:
          if saver_num>=6:
              videos.append(url)
  return videos
if __name__ == "__main__":
  for i in sublist:
    print(get_videos(i))
