<!-- adding apps -->

before you do any migrations dont forget to add the apps in the projects settings.py

<!-- pillow -->

we have to install pillow using # pip install pillow whenever we tried to use image in our model

# after adding the image **DONT FORGET TO ADD MEDIA_ROOT AND MEDIA_URL** to the project's settings.

THEN static file servings
urlpatterns = [

  <!-- your media url -->

] + static(settings.MEDIA_URL,document_root = MEDIA_ROOT)
