from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    class Meta:
        unique_together = ('nome', 'idade')  # Define a restrição de unicidade




# Configurar o modelo de usuário -------------------------------------
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password=password)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class MyUser(AbstractUser):
#     username = models.CharField(max_length=150, unique=True, default='default_username')
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin
