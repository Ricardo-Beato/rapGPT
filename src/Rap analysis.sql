use rap_vocab_dirty;
select * from all_artists_stats_clean;

-- exploring a bit the numbers this table gives us:
-- 1. ordering the rappers by their vocabulary range:

select all_artists_stats_clean.artist, all_artists_stats_clean.number_of_unique_words from all_artists_stats_clean
order by all_artists_stats_clean.number_of_unique_words DESC;

-- Aesop Rock being in the first place is coherent with some other analysis on the web and in the hip hop community, the guy Rocks! (get it?)
-- Ice Spice, she's being penalized for the low volume of songs we have in our database for her. This was a result of intensive data cleaning

-- 2. ordering the rappers by their vocabulary range, but pondered by the words per song:
select all_artists_stats_clean.artist, (all_artists_stats_clean.number_of_unique_words / all_artists_stats_clean.number_of_songs) as unique_words_per_song,
DENSE_RANK() over (order by (all_artists_stats_clean.number_of_unique_words / all_artists_stats_clean.number_of_songs) DESC) as artist_rank_new_words_per_song
from all_artists_stats_clean
order by unique_words_per_song DESC;

-- it's not super logical to understand these numbers, but essentially what they mean is "how many new words, on average, does one artist come up in each song"
-- it's as if in each song, Hopsin raps 434 new words he hasn't used before, that's a lot!! Maybe he's just got very few songs?

-- 3. ordering the rappers by their portfolio volume:
select all_artists_stats_clean.artist, all_artists_stats_clean.number_of_songs, DENSE_RANK() over(order by all_artists_stats_clean.number_of_songs DESC) as artist_rank_number_of_songs
from all_artists_stats_clean
order by all_artists_stats_clean.number_of_songs DESC;

-- indeed, with only songs in our analysis, Hopsin is one of the least represented rappers here

-- 4. what is the most used word 
select most_repeated_word, SUM(most_repeated_word_count) as total_word_count, 
dense_rank() over(order by SUM(most_repeated_word_count) DESC) as word_rank 
from all_artists_stats_clean
group by most_repeated_word
order by word_rank;

-- YEAAAH. Notice how the words are legit in the english language even if they are used in an offensive way. The 
-- same ranking would look different for the "dirty" dataset where a language library in Python did NOT filter words:

-- 5. same but with the dirty dataset:
select * from all_artists_stats_dirty;
select most_repeated_word, SUM(most_repeated_word_count) as total_wo`songs_metadata_df_with_counts_and_tops - mysql ready`rd_count, 
dense_rank() over(order by SUM(most_repeated_word_count) DESC) as word_rank 
from all_artists_stats_dirty
group by most_repeated_word
order by word_rank;

-- Very depreciative word in second place. We can also see come "grrah" and "woo" which don't have a meaning as words. 
-- what can we look at in songs_metadata_df_with_counts_and_tops?
select * from songs_metadata_df_with_counts_and_tops;

-- 6. the distribution of our albums and singles per year!
select release_date, count(distinct(album)) as count_albums, count(distinct(title))as count_songs from songs_metadata_df_with_counts_and_tops
group by release_date
order by release_date ASC;


select * from `songs_metadata_df_with_counts_and_tops - mysql ready`;



