from django.db import models

from app.modules.core.models import TimestampedModel


class Profile(TimestampedModel):

    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)

    image = models.TextField(blank=True)

    # This is an example of a Many-To-Many relationship where both sides of the
    # relationship are of the same model. In this case, the model is `Profile`.
    # As mentioned in the text, this relationship will be one-way. Just because
    # you are following mean does not mean that I am following you. This is
    # what `symmetrical=False` does for us.
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )

    # favorites = models.ManyToManyField(
    #     'exercice.Exercice',
    #     related_name='favorited_by'
    # )


    def __str__(self):
        return self.user.username

    def follow(self, profile):
        """Follow `profile` if we're not already following `profile`."""
        self.follows.add(profile)

    def unfollow(self, profile):
        """Unfollow `profile` if we're already following `profile`."""
        self.follows.remove(profile)

    def is_following(self, profile):
        """Returns True if we're following `profile`; False otherwise."""
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """Returns True if `profile` is following us; False otherwise."""
        return self.followed_by.filter(pk=profile.pk).exists()

    # def favorite(self, exercice):
    #     """Favorite `exercice` if we haven't already favorited it."""
    #     self.favorites.add(exercice)

    # def unfavorite(self, exercice):
    #     self.favorites.remove(exercice)

    # def has_favorited(self, exercice):
    #     """Returns True if we have favorited `exercice`; else False."""
    #     return self.favorites.filter(pk=exercice.pk).exists()
