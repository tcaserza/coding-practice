#
# PROBLEM: You plan to listen to music on a bus ride.  You are given an array of song durations, and a bus ride
#          duration, find a pair of songs that will end 30 seconds before you arrive.
#


def IDsOfSongs(rideDuration, songDurations):
    song_1_id = None
    song_2_id = None
    longest_song = 0
    for i in range(0, len(songDurations) - 1):
        for j in range(i + 1, len(songDurations)):
            total_duration = songDurations[i] + songDurations[j]
            if total_duration == rideDuration - 30:
                if songDurations[i] > longest_song or songDurations[j] > longest_song:
                    song_1_id = i
                    song_2_id = j
                    if songDurations[i] > songDurations[j]:
                        longest_song = songDurations[i]
                    else:
                        longest_song = songDurations[j]

    return [song_1_id, song_2_id]


print IDsOfSongs(90,[60,1,10,59,30,30,40,20,50])