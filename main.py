import csv

path = './request/'

def readad(path):
    adpath = path + 'ads/video_ad_request.csv'
    with open(adpath, 'r') as f:
        reader = csv.reader(f)
        # skip first row
        next(reader)
        #init var
        ad_total = 0
        ad_city = {}
        ad_platform = {}
        ad_device = {}
        ad_game = {}
        #read csv
        for row in reader:
            ad_total += 1
            #get city
            if row[2] in ad_city:
                ad_city[row[2]] += 1
            else:
                ad_city[row[2]] = 1
            #get os
            if row[10] in ad_platform:
                ad_platform[row[10]] += 1
            else:
                ad_platform[row[10]] = 1
            #device model
            # check that its not empty
            if row[15] != '':
                if row[15] in ad_device:
                    ad_device[row[15]] += 1
                else:
                    ad_device[row[15]] = 1
            #game
            #check that its not empty
            if row[25] != '':
                if row[25] in ad_game:
                    ad_game[row[25]] += 1
                else:
                    ad_game[row[25]] = 1


        #print results
        print('Total number of ads: ' + str(ad_total))
        #output city with most ads
        print('City with most ads: ' + max(ad_city, key=ad_city.get) + ' with ' + str(ad_city[max(ad_city, key=ad_city.get)]) + ' ads' + ( ' ( ' + str(round(ad_city[max(ad_city, key=ad_city.get)]/ad_total*100, 2)) + '% )' ))
        #output platform with most ads
        print('Platform with most ads: ' + max(ad_platform, key=ad_platform.get) + ' with ' + str(ad_platform[max(ad_platform, key=ad_platform.get)]) + ' ads' + ( ' ( ' + str(round(ad_platform[max(ad_platform, key=ad_platform.get)]/ad_total*100, 2)) + '% )' ))
        #output device with most ads
        print('Device with most ads: ' + max(ad_device, key=ad_device.get) + ' with ' + str(ad_device[max(ad_device, key=ad_device.get)]) + ' ads' )
        #output game with most ads
        print('Game with most ads: ' + max(ad_game, key=ad_game.get) + ' with ' + str(ad_game[max(ad_game, key=ad_game.get)]) + ' ads' )

def readsubs(path):
    subpath = path + 'commerce/subs/subscriptions.csv'
    with open(subpath, 'r') as f:
        reader = csv.reader(f)
        # skip first row
        next(reader)
        #init var
        sub_count = 0
        sub_name = {}
        for row in reader:
            sub_count += 1
            #get name
            if row[1] != '':
                if row[1] in sub_name:
                    sub_name[row[1]] += 1
                else:
                    sub_name[row[1]] = 1
        print('\n')
        print('Total number of subscriptions: ' + str(sub_count))
        print('Most common subscription channel: ' + max(sub_name, key=sub_name.get) + ' with ' + str(sub_name[max(sub_name, key=sub_name.get)]) + ' subscriptions' + ( ' ( ' + str(round(sub_name[max(sub_name, key=sub_name.get)]/sub_count*100, 2)) + '% )' ))

def readfollow(path):
    follow_user = path + 'community/follows/follow.csv'
    follow_game = path + 'community/follows/follow_game.csv'
    with open(follow_user, 'r') as f:
        reader = csv.reader(f)
        # skip first row
        next(reader)
        #init var
        follow_count = 0
        for row in reader:
            if(follow_count == 0):
                print('First follow: ' + str(row[7]) + ' at ' + str(row[0]))
            follow_count += 1
        print('Total number of follows: ' + str(follow_count))

def readsitehistory(path):
    chathistory = path + 'site_history/chat_messages.csv'
    with open(chathistory, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # skip first row
        next(reader)
        chat_count = 0
        chat_message = {}
        for row in reader:
            chat_count += 1
            #get messages
            if row[4] != '':
                if row[4] in chat_message:
                    chat_message[row[4]] += 1
                else:
                    chat_message[row[4]] = 1

        print('\n')
        print('Total number of chat messages: ' + str(chat_count))
        print('Most common messages:')
        for i in range(5):
            print(str(i+1) + '. ' + max(chat_message, key=chat_message.get) + ' with ' + str(chat_message[max(chat_message, key=chat_message.get)]) + ' messages' + ( ' ( ' + str(round(chat_message[max(chat_message, key=chat_message.get)]/chat_count*100, 2)) + '% )' ))
            del chat_message[max(chat_message, key=chat_message.get)]


readad(path)
readsubs(path)
readfollow(path)
readsitehistory(path)
