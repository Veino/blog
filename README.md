# How to build a blog with Django: Rapid Development under 30 mins.
Build a seamless and simple blog using the Django web development framework.


## About the Blog
It consists of a homepage that aggregates all the blog posts on one page in descending order, each post is represented by a thumbnail image, a title, and a brief headline of the post's content. 

Clicking on a post from the homepage redirects to a single blog "detail page" which contains details from just one blog post, it includes the full title, featured image, and the full body text.

## Build and Run

### Prerequisites
- Python v3.10+
- Django v4.0+
- Virtualenv


### Running the App
1. Clone this repository
2. Open a terminal in the root of the cloned repo and install requirements.txt

```
pip install -r requirements.txt

```
3. Make Migrations

```
python manage.py makemigrations

```
4. Migrate database

```
python manage.py migrate

```
5. Start the app by running:

```
python manage.py runserver

```

## Learn More
You can add more functionality to the blog such as; commenting system, tags, categories, pagination, search functionality, social sharing, user profiles, and many more.

## Support
Facing any challenges? Get answers to your questions from the [Django Community](https://www.djangoproject.com/community/)

## Author
[Pwaveino](https://github.com/Veino)

## Contributions
Contributions are Welcome!
