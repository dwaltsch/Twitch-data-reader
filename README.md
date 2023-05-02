# Twitch data reader

## Functions

### readad(path)
This function reads the `video_ad_request.csv` file and extracts the following information:
- Total number of ads
- City with most ads
- Platform with most ads
- Device with most ads
- Game with most ads

### readsubs(path)
This function reads the `subscriptions.csv` file and extracts the following information:
- Total number of subscriptions
- Most common subscription channel

### readfollow(path)
This function reads the `follow.csv` and `follow_game.csv` files and extracts the following information:
- First follow
- Total number of follows

### readsitehistory(path)
This function reads the `chat_messages.csv` file and extracts the following information:
- Total number of chat messages
- Most common chat messages

[read more](https://spblue.tech/content/posts/twitchdata.html)
