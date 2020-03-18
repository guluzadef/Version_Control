from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

"""
{
    "usr_adm": False,
    "usr_mod": False,
    "usr_public": True,
    "usr_lastip":  "0.0.0.0",
    "usr_pay_email": "asdasd@dasd.asd",
    "usr_pay_type": "asdasd",
    "usr_disk_space": "1",
    "usr_direct_downloads": False,
    "usr_rapid_login": "asdasd",
    "usr_rapid_pass": "asdaS",
    "usr_points": 12,
    "usr_aff_id": 1
}	
"""


class UserManager(BaseUserManager):
    use_in_migrations = True

    def __user_data(self):
        now = timezone.now()
        return {
            "usr_adm": False,
            "usr_mod": False,
            "usr_public": True,
            "usr_lastip": 324,
            "usr_pay_email": "asdasd@dasd.asd",
            "usr_pay_type": "asdasd",
            "usr_disk_space": "1",
            "usr_direct_downloads": False,
            "usr_rapid_login": "asdasd",
            "usr_rapid_pass": "asdaS",
            "usr_points": 12,
            "usr_aff_id": 1,
            "usr_money": 0,
            "usr_lastlogin":now
        }

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        print("YESS" * 100)
        user = self.model(usr_login=username, usr_email=email, **extra_fields, **self.__user_data())
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, usr_login, usr_email=None, password=None, **extra_fields):
        print("BUra girdi !!!")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(usr_login, usr_email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()
