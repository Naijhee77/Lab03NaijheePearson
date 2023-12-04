import streamlit as st
import requests

#Page Title
st.title("Movie Tracks and Recs")
st.subtitle("Keep track of your movies and find new ones")

#Genre Picker
genres = st.multiselect("Select your favorite movie genres", ["Action", "Comedy", "Drama", "Sci-Fi", "Horror","Romance"]

#Minimum Ratings
minRating = st.slider("Select minimum rating",0,10,7)

# API key (replace with your own API key from The Movie Database API)
api_key = "YOUR_TMDB_API_KEY"

# Movie Database API endpoint
api_url = "https://api.themoviedb.org/3/discover/movie"

# Random movie button
if st.button("Get Movie Recommendation"):
    try:
        # Make API request
        params = {
            "api_key": api_key,
            "sort_by": "popularity.desc",
            "vote_average.gte": min_rating,
            "with_genres": ",".join(str(genre_id) for genre_id in [28, 35, 18] if genre_id in genres),  # Map genre names to TMDB genre ids
        }
        response = requests.get(api_url, params=params)
        data = response.json()

        # Get a random movie from the response
        if data["results"]:
            random_movie = data["results"][0]
            st.subheader("Recommended Movie:")
            st.write(f"**Title:** {random_movie['title']}")
            st.write(f"**Genre:** {', '.join(genre['name'] for genre in random_movie['genres'])}")
            st.write(f"**Rating:** {random_movie['vote_average']}")
            st.write(f"**Overview:** {random_movie['overview']}")
            st.write(f"**Release Date:** {random_movie['release_date']}")
            st.write(f"**IMDb Link:** [IMDb]({f'https://www.imdb.com/title/{random_movie['imdb_id']}/'})")

        else:
            st.warning("No movies found based on your preferences. Try adjusting your criteria.")

    except Exception as e:
        st.error(f"Error: {e}")

# Refresh button
if st.button("Refresh"):
    # Clear input and results for a new recommendation
    st.multiselect("Select your favorite movie genres", ["Action", "Comedy", "Drama", "Sci-Fi", "Thriller"])
    st.slider("Select minimum rating", 0, 10, 7)
    st.experimental_rerun()
