# Final-Project

link to Tableau: https://public.tableau.com/app/profile/ricardo.beato/viz/Rapanalysis/Dashboard1?publish=yes


## Goal

Creating a Natural Language Processing (NLP) Machine Learning (ML) model using Recurrent Neural Networks (RNN) capable of extending existing lyrics to a rap song by following the same logic of the previous ones, with new lines of text.

## Scope
#### What should the model do?
- The model should give continuation to a set of inputed lyrics based on the context of these 
- The model should create whole lines, not just suggest words that rhyme
- The model should be able to make perfect rhymes (words with identical vowel and consonant sounds at the end. Examples include "cat" and "hat.")
    - ##### ❓​❓​ should the model also allow for near rhymes? (words with similar, but not identical, sounds. Near rhymes open up more possibilities and can create interesting variations. Examples include "cat" and "cut.") 
- 

## Process

### **The libraries used across the project:**

- **os** - this library allows us to interact with the operative system. In our case it was used several times to access files in specific folders (the "data" folder for example) and to iterate through those files. Also to build paths to create new .txts (for example the compilation of all the lyrics)
- **dotenv** - where we've used imported *load_dotenv* to hide credentials for the Genius API
- **tensorflow** - created by the BRAIN Team at Google, it was the main pilar for the creation of our RNN
- **keras** - acts as an API, running on top TensorFlow
- **numpy** - we've used NumPy in the construction and instruction of our RNN model
- **time** - mostly used to avoid/workaround API limitations when requesting lyrics to lyricsgenius (that scrapes the Genius API)
- **lyricsgenius** - instead of using the Genius API directly to fetch lyrics, we've used the lyricsgenius library
- **requests** - to collect metadata for the songs of each artist and send http requests to the Genius API and to lyricsgenius
- **json** - we've used JSON to store metadata for songs
- **pandas** - broadly used across the several phases mostly in the creation and management of dataframes
- **requests.exceptions (SSLError)** - as a workaround to bad requests to the lyricsgenius library
- **re** - [regular expressions] we've used this library to manage special characters in artists' names where the name could be a potential issue in the management of information ("A$AP Rocky" for example)
- **logging** - this was used while fetching lyrics from the lyricsgenius library as a way to avoid starting from scratch whenever the code would face an error.
- **nltk** - [natural language tool kit] while managing the content of the lyrics for each artist
- **nltk.corpus (stopwords)** - to define what words _not_ to count for statistics
- **from nltk.corpus (words)** - to check whether the words in the lyrics actually exist in the english dictionary and avoid "made-up" words by artists
- **collections (Counter)** - as a way to interact with the content of the .txt files to count words
- **string** - this library helps us cleaning the lyrics to account only for characters based words and keep "400$" for example out


### 1. **Data collection and cleaning**
    
1.1 *Collecting and cleaning songs metadata* 

This project makes use of the [Genius API](https://docs.genius.com/#annotations-h2). I set up a Genius account in their page to be able to retrieve the fundamental pieces to access their API [CLIENT_ID, CLIENT_SECRET and CLIENT_ACCESS_TOKEN]. These information is, for a matter of privacy, stored in a .env file which is accessed via a load_dotenv() function imported from the load_dotenv library.

I've set 4 functions to automate the retrieval and cleaning process of *metadata* for artists' songs.

    - clean_artist_name(artist_name)
This function handles artist's names that contain numbers or special characters as this is an issue wfor the subsequent functions. Given the example of the artist Lil’ Kim, the graphic ’ would be converted into an "_"

    BASE_URL = "https://api.genius.com"
    DATA_FOLDER = "data"
    _get(path, params=None, headers=None)
This function sends an http get request to our genius API based on a url that we've built.

    get_artist_songs(artist_name)
A function to identify the artists songs in Genius. Each song as a unique ID and this is a mapping to each artist's songs library.

    get_song_information(song_ids, artist_name)
Retrieves information about each song given a list of song IDs.

    get_tracks_info_for_artist(artist_name)
This function encapsulates the previous steps and works as an orchestrator to the data collection. It sends the https request, collects the metadata and finally dumps it into a JSON file in our "data" folder as well as a .txt with the tracklist (comprised of unique IDs) for each artist. In the given example it would create:

- Lil_ Kim Songs.json
- Lil_ Kim Genius Song IDs.txt

A further function was created to automate some surface cleaning process, namely:

    load_json_and_clean(artist_name, data_folder="data", min_count_albums=6)
This function loads the dumped JSON file into a dictionary and converts it to a Dataframe named after the passed artist _Lil_Kim_df in the example. The dataframe is then subject to two cleaning processes:

- Every row where the album count was <6 was dropped
- Every row where the album column a <'single'> (meaning an isolated song, not pertaining to an album) was also dropped.

This decision was made based on the observations for some artists where the low album count represented participations in mixtapes for example but not the own artist's album. Similarly, for the purpose of data aggregation into albums and easier processing, I am working with albums exclusively, hence the singles drop.

Notice that both **get_tracks_info_for_artist** and **load_json_and_clean** require solely the passing of the artist's name. 
Another important note: the two cleaning functions were applied to assure some superficial cleaning but further cleaning would be required if we wanted to assure we're working exclusively with the artist's albums and not mixtape/compilations participations. This unfortunatelly would require some human ad-hoc filtering as there is not an automated/logical way to do so according to my knowledge and to the libraries and web pages I found to this date.
    
1.2 *Collecting the lyrics* 

We have now a dataframe with metadata for each artist. The songs_metadata_df consolidates all the cleaned dataframe via concatenation and has got a dedicated column to all the unique songs IDs. These IDs are the key to ask the API for the lyrics for each of them.
I am setting an additional 

    fetch_lyrics(genius_track_id)
function that iterates through the songs_metadata_df column with the songs unique IDs to fetch the corresponding lyrics. In the event the function is faced with an error, it will sleep for 5 minutes before moving to the next unique ID. 


## Challenges and possible solutions
1. **Opening up to both perfect and near rhymes can add complexity to the model, but it also depends**

1.1 *Potential Simplifications*:
        
    1.1.1 Word Embeddings: If you use pre-trained word embeddings or language models, they may already capture semantic similarities that align with near rhymes

    1.1.2 User-Specified Rhyme Type: (not really into this as the model should be ready for both anyway) Allowing users to specify whether they want perfect or near rhymes could simplify the model's decision-making process 

    1.1.3 Transfer Learning: (got to explore if available) Some pre-trained models might already have some capacity to handle near rhymes, potentially simplifying the training process



## Resources and learning materials
1. [Setting up the Genius API](https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29)
2. [Genius API](https://docs.genius.com/)
3. [What is TensorFlow?](https://www.youtube.com/watch?v=9NsfX9W80rw)
    
    3.1 [What are EPOCHs and Batches?](https://www.youtube.com/watch?v=BvqerWSp1_s)
4. Previous relevant projects on the same topic:
    
    4.1 [Metadata extraction from Genius' API](https://gist.github.com/imdkm/a60247b59ff1881fa4bb8846a9b44c96)
    4.2


## Glossary
[**Tensors**](https://youtu.be/L35fFDpwIM4?si=u2Ov-IULhtX5mwwA&t=293) - a tensor is as a container that can hold different kinds of data, like numbers or strings. Think of it like a box that can store a single value, a line of values, a table of values, or even more complex structures. Tensors help organize and process information for the computer to understand and learn from.
    
- **Ragged Tensors** - these are tensors where different rows can have different lengths. In other words, it's like a table where each row can have a different number of elements. This is useful when dealing with sequences of varying lengths, like lines of the lyrics in the context of this project, that have different lengths.


[**EPOCH**](https://www.simplilearn.com/tutorials/machine-learning-tutorial/what-is-epoch-in-machine-learning) - Machine learning is a field where the learning aspect of Artificial Intelligence (AI) is the focus. This learning aspect is developed by algorithms that represent a set of data. Machine learning models are trained with specific datasets passed through the algorithm. 
Each time a dataset passes through an algorithm, it is said to have completed an epoch. Therefore, Epoch, in machine learning, refers to the one entire passing of training data through the algorithm. It's a hyperparameter that determines the process of training the machine learning model. The number of epochs is considered a hyperparameter. It defines the number of times the entire data set has to be worked through the learning algorithm. 

[**Iteration**](https://www.simplilearn.com/tutorials/machine-learning-tutorial/what-is-epoch-in-machine-learning) - The total number of batches required to complete one Epoch is called an iteration. The number of batches equals the total number of iterations for one Epoch. 

[**Batch**](https://www.simplilearn.com/tutorials/machine-learning-tutorial/what-is-epoch-in-machine-learning) - The batch is the dataset that has been divided into smaller parts to be fed into the algorithm. 

**Sequence** - in the context of this project, sequences will be the a consecutive series of characters (or their numerical representations) from the original text data. Each sequence is a subset of the original text, containing a fixed number of characters (determined by seq_length). Each sequence is used as input to the model, and the target for each sequence is the following character in the text. Sequences are organized into batches for efficient training, and each batch is processed in one iteration during training. A sequence will contain:
    
- an **input** - the string/sequence of integers representing the string which last character will not be present
- a **label** - stemming from the same sequence that originated the input but misplaced one unit to the right. 
- Practical example:
    
    - Sequence = "Rapper's delight"
    - Input = "Rapper's deligh"
    - Label = "apper's delight"

in other words, this is how we teach the model what's missing and what it should predict.

**Token** - In the context of natural language processing and machine learning, a "token" is a unit of text that has been extracted from a larger sequence. In our example, the running model will create words and tokenize them because it works in a numerical way. This numerical representation allows the model to learn patterns and relationships in the data more effectively.

**(songs)Metadata** - metadata refers, in this project, to the information collected for each artist's song and includes:
- *title*
- *album*
- *release_date*
- *featured_artists*
- *producer_artists*
- *writer_artists*
- *genius_track_id*
- *genius_album_id*