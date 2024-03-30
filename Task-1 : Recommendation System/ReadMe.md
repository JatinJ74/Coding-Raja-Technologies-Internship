# Movie Recommendation System

This is a movie recommendation system project that provides personalized movie recommendations based on user input. It utilizes a content-based recommendation approach, where movies are recommended based on their similarity to the input movie.

## Overview

The recommendation system is built using Python and Flask framework. It uses a dataset of movies and ratings to generate recommendations. The system also includes an autocomplete feature to suggest movie titles as users type.

## Features

- **Movie Search**: Users can search for movies by entering partial titles.
- **Autocomplete**: The system suggests movie titles as users type in the search bar.
- **Personalized Recommendations**: Based on the input movie, the system provides personalized recommendations.
- **Ranking**: Recommended movies are ranked based on their similarity and average ratings.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

4. To access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Enter a partial movie title in the search bar.
2. Select a movie from the autocomplete suggestions or type the full title.
3. Click on "Get Recommendations" to see personalized movie recommendations.

## Data Sources

- [Movie Dataset]([ink-to-movie-dataset](https://files.grouplens.org/datasets/movielens/ml-10m.zip)): You can download the dataset from given link in zip file.

## Credits

- **Dataset**: [MovieLens]
- **Flask**: [Flask documentation](https://flask.palletsprojects.com/)
- **Scikit-learn**: [Scikit-learn documentation](https://scikit-learn.org/stable/)
