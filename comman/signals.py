from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_data(sender, **kwargs):

    if sender.name != 'comman':
        return

    from comman.models import Admin

    if not Admin.objects.filter(emailAddress="sumit@gmail.com").exists():

        Admin.objects.create(
            emailAddress="sumit@gmail.com",
            password="sumit@123",
            hallName="Name of Hall",
            adminName="Name of Admin",
            mobileNumber="8799865996",
            image=""
        )

        print("=" * 80)
        print("Default Admin Created")
        print("Email    : sumit@gmail.com")
        print("Password : sumit@123")
        print("=" * 80)

    else:
        print("Default Admin already Exists")