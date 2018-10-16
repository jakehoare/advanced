from gmusicapi import Mobileclient
from collections import defaultdict

api = Mobileclient()
# https://support.google.com/accounts/answer/185833?hl=en&ref_topic=7189145
logged_in = api.login('your.email@gmail.com', 'app-specific-password', 'android-id')
print("Logged in?", logged_in)

library = api.get_all_songs()
print("Example track data:")
for k, v in library[0].items():
    print(k, v)

# Map id to dictionary of all other information about the track
track_ids = {track["id"] : track for track in library}

# Map album names to list of ids
album_to_ids = defaultdict(list)
for track in library:
    album_to_ids[track["album"]].append(track["id"])
print(len(album_to_ids), "albums in library")

# Find songs with duplicate (title, trackNumber) in same album
total_dups, albums_with_dups = 0, 0

for album, ids in album_to_ids.items():

    #if "HSBC" not in album:     # exclude certain albums
    #    continue

    songs = set()
    album_dups = 0

    for id in ids:
        all_song_info = track_ids[id]
        song_tuple = (all_song_info["title"], all_song_info["trackNumber"])

        if song_tuple in songs:
            #print("Deleting duplicate", song_tuple, album)
            api.delete_songs(id)    # delete dupliacted
            album_dups +=1
        songs.add(song_tuple)

    if album_dups > 0:
        total_dups += album_dups
        albums_with_dups += 1
        print("Deleted", album_dups, "duplicates in", album, ", cumulative:", total_dups)

print("Total duplicates deleted:", total_dups)
print("Albums with duplicates:", albums_with_dups)
