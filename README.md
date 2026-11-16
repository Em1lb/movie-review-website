# movie-review-website
Website for reviewing movies

- Users can review and rate movies. The reviews include the basic information of the movies being reviewed.
- Users can see all the reviews posted on the website.
- Users can create accounts and log into the website.
- Users can create, edit and remove their own reviews.
- Users can search for reviews by movie name.
- The user page shows how many reviews the user has made and a list of all the user's reviews.
- Users can choose classifications for a review:
	* Genre
	* Language
- Users can comment on other users' reviews. 

## Testing the application

1. Clone the repository and move into its directory
2. Create a virtual environment and install Flask:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```
3. Create the database:
   ```
   sqlite3 database.db < schema.sql
   ```
4. Start the application:
   ```
   flask run
   ```
