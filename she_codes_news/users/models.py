from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #this is wehre I would put custom fields for users
    pass

    def __str__(self):
        return self.username
