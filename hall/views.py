import os

from django.http import request
from django.shortcuts import render
from django.contrib import  messages
from comman.models import Admin, User
from django.shortcuts import redirect, get_object_or_404
from comman.models import AboutPage, Contact, CounterSection, GalleryPage, HomePage
from django.utils.text import get_valid_filename
from django.conf import settings


# Create your views here.
def dashbord(request):
    if not request.session.get('admin_logged_in'):
          messages.error(request, "Please login first!")
          return redirect('login')
    total_registered_users = User.objects.filter(status__iexact='registered').count()
    total_approved_users = User.objects.filter(status__iexact='approved').count()
    total_rejected_users = User.objects.filter(status__iexact='rejected').count()
    
    return render(request, 'hall/dashbord.html', {
        'total_registered_users': total_registered_users,
        'total_approved_users': total_approved_users,
        'total_rejected_users': total_rejected_users
    })

 # ------___------____------____----_____HOME PAGE ------____----_____-----____---_______------____--

def homepage(request):
    if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')

    if request.method == "POST":
        logo = request.FILES.get("logo")
        image = request.FILES.get("image")
        heading = request.POST.get("heading", "").strip()
        description = request.POST.get("description", "").strip()
        second_heading = request.POST.get("secondHeading", "").strip()
        second_description = request.POST.get("secondDescription", "").strip()
        third_heading = request.POST.get("thirdHeading", "").strip()
        third_description = request.POST.get("thirdDescription", "").strip()

        if not all((
            logo,
            image,
            heading,
            description,
            second_heading,
            second_description,
            third_heading,
            third_description,
        )):
            messages.error(request, "Please complete all fields and select both images.")
            return render(request, "hall/homepage.html")

        HomePage.objects.create(
            logo=logo,
            image=image,
            heading=heading,
            description=description,
            secondHeading=second_heading,
            secondDescription=second_description,
            thirdHeading=third_heading,
            thirdDescription=third_description,
        )

        messages.success(request, "Homepage details added successfully!")
        return redirect("homepagelist")

    return render(request, "hall/homepage.html")

def homepagelist(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     homepages = HomePage.objects.all()
     return render(request, 'hall/homepagelist.html', {'homepages': homepages})

def homepageUpdate(request, homepage_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     homepage = get_object_or_404(HomePage, pk=homepage_id)

     if request.method == "POST":
          heading = request.POST.get("heading", "").strip()
          description = request.POST.get("description", "").strip()
          second_heading = request.POST.get("secondHeading", "").strip()
          second_description = request.POST.get("secondDescription", "").strip()
          third_heading = request.POST.get("thirdHeading", "").strip()
          third_description = request.POST.get("thirdDescription", "").strip()

          if not all((
               heading,
               description,
               second_heading,
               second_description,
               third_heading,
               third_description,
          )):
               messages.error(request, "Please complete all text fields.")
               return render(request, "hall/homepageUpdate.html", {"homepage": homepage})

          homepage.heading = heading
          homepage.description = description
          homepage.secondHeading = second_heading
          homepage.secondDescription = second_description
          homepage.thirdHeading = third_heading
          homepage.thirdDescription = third_description

          logo = request.FILES.get("logo")
          image = request.FILES.get("image")
          if logo:
               homepage.logo = logo
          if image:
               homepage.image = image

          homepage.save()
          messages.success(request, "Homepage details updated successfully!")
          return redirect("homepagelist")

     return render(request, "hall/homepageUpdate.html", {"homepage": homepage})

def homepageDelete(request, homepage_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method != "POST":
          return redirect("homepagelist")

     homepage = get_object_or_404(HomePage, pk=homepage_id)
     homepage.delete()
     messages.success(request, "Homepage details deleted successfully!")
     return redirect("homepagelist")

 # ------___------____------____----_____ABOUT PAGE ------____----_____-----____---_______------____--

def aboutpage(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method == "POST":
          background_image = request.FILES.get("bgimg")
          first_image = request.FILES.get("fgimg")
          heading = request.POST.get("heading", "").strip()
          caption = request.POST.get("caption", "").strip()
          second_image = request.FILES.get("simg")

          if not all((
              background_image,
              first_image,
              heading,
              caption,
              second_image,
          )):
               messages.error(request, "Please complete all fields and select all three images.")
               return render(request, 'hall/aboutpage.html')

          AboutPage.objects.create(
              BackgroundImage=background_image,
              FirstImage=first_image,
              Heading=heading,
              Description=caption,
              SecondImage=second_image,
          )

          messages.success(request, "Aboutpage Details Added Successfully..!")
          return redirect("aboutpagelist")
     return render(request, "hall/aboutpage.html")

def aboutpagelist(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     aboutpages = AboutPage.objects.all()
     return render(request, 'hall/aboutpagelist.html', {'aboutpage': aboutpages})

def aboutpageUpdate(request, about_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     about = get_object_or_404(AboutPage, pk=about_id)

     if request.method == "POST":
          heading = request.POST.get("heading", "").strip()
          description = request.POST.get("caption", "").strip()

          if not heading or not description:
               messages.error(request, "Please complete the heading and caption.")
               return render(request, "hall/aboutpageUpdate.html", {"about": about})

          about.Heading = heading
          about.Description = description

          background_image = request.FILES.get("bgimg")
          first_image = request.FILES.get("fgimg")
          second_image = request.FILES.get("simg")
          if background_image:
               about.BackgroundImage = background_image
          if first_image:
               about.FirstImage = first_image
          if second_image:
               about.SecondImage = second_image

          about.save()
          messages.success(request, "About page details updated successfully.")
          return redirect("aboutpagelist")

     return render(request, "hall/aboutpageUpdate.html", {"about": about})

def aboutpageDelete(request, about_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method != "POST":
          return redirect("aboutpagelist")

     about = get_object_or_404(AboutPage, pk=about_id)
     about.delete()
     messages.success(request, "About page details deleted successfully.")
     return redirect("aboutpagelist")

 # ------___------____------____----_____GALLERY PAGE ------____----_____-----____---_______------____--

def gallerypage(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method == "POST": 
          background_image = request.FILES.get("bgimg")
          one_image = request.FILES.get("oneImage")
          second_image = request.FILES.get("secondImage")
          third_image = request.FILES.get("thirdImage")
          fourth_image = request.FILES.get("fourthImage")

          if not all((background_image, one_image, second_image, third_image, fourth_image)):
               messages.error(request, "Please select all five images.")
               return render(request, 'hall/gallarypage.html')

          GalleryPage.objects.create(
               BackgroundImage=background_image,
               oneImage=one_image,
               secondImage=second_image,
               thirdImage=third_image,
               fourthImage=fourth_image,
          )
          messages.success(request, "Gallery page details added successfully!")
          return redirect("gallerypagelist")
     return render(request, 'hall/gallarypage.html')

def gallerypagelist(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     gallerypages = GalleryPage.objects.all()
     return render(request, 'hall/gallerypagelist.html', {'gallerypage': gallerypages})

def gallerypageUpdate(request, gallery_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     gallery = get_object_or_404(GalleryPage, pk=gallery_id)

     if request.method == "POST":
          image_fields = (
               ("BackgroundImage", "bgimg"),
               ("oneImage", "oneImage"),
               ("secondImage", "secondImage"),
               ("thirdImage", "thirdImage"),
               ("fourthImage", "fourthImage"),
          )
          for model_field, input_name in image_fields:
               uploaded_image = request.FILES.get(input_name)
               if uploaded_image:
                    setattr(gallery, model_field, uploaded_image)

          gallery.save()
          messages.success(request, "Gallery page details updated successfully!")
          return redirect("gallerypagelist")

     return render(request, "hall/gallerypageUpdate.html", {"gallery": gallery})

def gallerypageDelete(request, gallery_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method != "POST":
          return redirect("gallerypagelist")

     gallery = get_object_or_404(GalleryPage, pk=gallery_id)
     gallery.delete()
     messages.success(request, "Gallery page details deleted successfully!")
     return redirect("gallerypagelist")

 # ------___------____------____----_____CONTACT PAGE ------____----_____-----____---_______------____--

def contactpage(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     if request.method == "POST":
         background_image = request.FILES.get("bgimg")
         address = request.POST.get("address", "").strip()
         mobile_number = request.POST.get("mobile", "").strip()
         email_address = request.POST.get("email", "").strip()

         if not all((background_image, address, mobile_number, email_address)):
             messages.error(request, "Please complete all fields and select the background image.")
             return render(request, 'hall/contactpage.html')
         Contact.objects.create(
             BackgroundImage=background_image,
             Address=address,
             MobeliNumbar=mobile_number,
             EmailAddress=email_address,
         )
         messages.success(request, "Contact page details added successfully!")
         return redirect("contactpagelist")

     return render(request, 'hall/contactpage.html')


def contactpagelist(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     
     contacts = Contact.objects.all()
     return render(request, 'hall/contactpagelist.html', {'contacts': contacts})

def contactpageUpdate(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     
     return render(request, 'hall/contactpageUpdate.html')

 # ------___------____------____----_____STATIC PAGE ------____----_____-----____---_______------____--

def staticadd(request):
      if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
      
      if request.method == "POST":
               number_of_weddings = request.POST.get("now", "").strip()
               number_of_birthdays = request.POST.get("nobp", "").strip()
               number_of_farewells = request.POST.get("nof", "").strip()
               number_of_seminars = request.POST.get("nos", "").strip()
     
               if not all((number_of_weddings, number_of_birthdays, number_of_farewells, number_of_seminars)):
                    messages.error(request, "Please complete all fields.")
                    return render(request, 'hall/staticadd.html')

               CounterSection.objects.create(
                    NumberOfWedding=number_of_weddings,
                    NumberOfBirthday=number_of_birthdays,
                    NumberOfFerewell=number_of_farewells,
                    NumberOfSeminar=number_of_seminars,
               )
               messages.success(request, "Static page details added successfully!")
               return redirect("staticlist")
      return render(request, 'hall/staticadd.html')

def staticlist(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
     
     statics = CounterSection.objects.all()
     return render(request, 'hall/staticlist.html', {'statics': statics})

def staticUpdate(request, counter_id):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')

     counter = get_object_or_404(CounterSection, pk=counter_id)

     if request.method == "POST":
          number_of_weddings = request.POST.get("now", "").strip()
          number_of_birthdays = request.POST.get("nobp", "").strip()
          number_of_farewells = request.POST.get("nof", "").strip()
          number_of_seminars = request.POST.get("nos", "").strip()

          if not all((number_of_weddings, number_of_birthdays, number_of_farewells, number_of_seminars)):
               messages.error(request, "Please complete all fields.")
               return render(request, 'hall/staticUpdate.html', {'counter': counter})

          counter.NumberOfWedding = number_of_weddings
          counter.NumberOfBirthday = number_of_birthdays
          counter.NumberOfFerewell = number_of_farewells
          counter.NumberOfSeminar = number_of_seminars
          counter.save()

          messages.success(request, "Counter section details updated successfully!")
          return redirect("staticlist")

     return render(request, 'hall/staticUpdate.html', {'counter': counter})

def staticDelete(request, counter_id):
     if not request.session.get('admin_logged_in'):
          messages.error(request, "Please login first!")
          return redirect('login')
     if request.method != "POST":
          return redirect("staticlist")

     counter = get_object_or_404(CounterSection, pk=counter_id)
     counter.delete()
     messages.success(request, "Counter section record deleted successfully!")
     return redirect("staticlist")

#------___------____------____----_____REGISTERED USERS PAGE ------____----_____-----____---_______------____--
def registereduserlist(request):
    if not request.session.get('admin_logged_in'):
         messages.error(request, "Please login first!")
         return redirect('login')
    users = User.objects.filter(status__iexact='registered')
    return render(request, 'hall/registereduserlist.html', {'users': users})


def approve_user(request, user_id):
    if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
    if request.method != "POST":
        return redirect('registereduserlist')

    user = get_object_or_404(User, pk=user_id)
    current_status = user.status.lower()
    if current_status not in {'registered', 'rejected'}:
        messages.error(request, "This user cannot be approved from the current list.")
        return redirect('registereduserlist')

    user.status = 'Approved'
    user.reason = None
    user.save(update_fields=['status', 'reason'])
    messages.success(request, "User approved successfully.")
    if current_status == 'rejected':
        return redirect('rejecteduserlist')
    return redirect('registereduserlist')


def reject_user(request, user_id):
    if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
    if request.method != "POST":
        return redirect('registereduserlist')

    user = get_object_or_404(User, pk=user_id)
    current_status = user.status.lower()
    if current_status not in {'registered', 'approved'}:
        messages.error(request, "This user cannot be rejected from the current list.")
        return redirect('registereduserlist')

    reason = request.POST.get('reason', '').strip()
    if not reason:
        messages.error(request, "A rejection reason is required.")
        return redirect('registereduserlist')
    if len(reason) > 255:
        messages.error(request, "The rejection reason must be 255 characters or fewer.")
        return redirect('registereduserlist')

    user.status = 'Rejected'
    user.reason = reason
    user.save(update_fields=['status', 'reason'])
    messages.success(request, "User rejected successfully.")
    if current_status == 'approved':
        return redirect('approveduserlist')
    return redirect('registereduserlist')


def rejecteduserlist(request):
    if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
    users = User.objects.filter(status__iexact='rejected')
    return render(request, 'hall/regecteduserlist.html', {'users': users})

def approveduserlist(request):
    if not request.session.get('admin_logged_in'):
         messages.error(request, "Please login first!")
         return redirect('login')
    users = User.objects.filter(status__iexact='approved')
    return render(request, 'hall/approveduserlist.html', {'users': users})

 # ------___------____------____----_____LOGIN PAGE ------____----_____-----____---______------____--

def login(request):
    if request.session.get('admin_logged_in'):
        return redirect('dashbord')

    if request.method == 'POST':
        email = request.POST.get('emailAddress')
        password = request.POST.get('password')

        try:
            admin_obj = Admin.objects.get(
                emailAddress=email,
                password=password
            )

            request.session['admin_logged_in'] = True
            request.session['admin_id'] = admin_obj.id
            request.session['admin_name'] = admin_obj.adminName
            request.session['hall_name'] = admin_obj.hallName
            request.session['admin_mobile'] = admin_obj.mobileNumber
            request.session['admin_image'] = (
                admin_obj.image.name if admin_obj.image else ""
            )

            messages.success(
                request,
                "Login successful! Welcome to Wedding Hall Dashboard!"
            )
            return redirect('dashbord')

        except Admin.DoesNotExist:
            messages.error(request, "Invalid email or password!")

    return render(request, 'hall/login.html')

def logout(request):

    # Remove specific session keys
    request.session.pop('admin_logged_in', None)
    request.session.pop('admin_id', None)
    request.session.pop('admin_name', None)
    request.session.pop('hall_name', None)
    request.session.pop('admin_mobile', None)
    request.session.pop('admin_image', None)

    messages.success(request, "Logged out successfully!")

    return redirect('login')
 # ------___------____------____----_____PROFILE PAGE ------____----_____-----____---_______------____--

def profile(request):
    """Show profile form."""
    if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')

    admin = get_object_or_404(
        Admin,
        id=request.session.get('admin_id'),
    )

    if request.method == "POST":
        admin.hallName = request.POST.get("hallName", "").strip()
        admin.adminName = request.POST.get("adminName", "").strip()
        admin.emailAddress = request.POST.get("emailAddress", "").strip()
        admin.mobileNumber = request.POST.get("mobileNumber", "").strip()
#_______________________________________________image uploade code____________
        uploaded_image = request.FILES.get("image")
        if uploaded_image:
            file_ext = os.path.splitext(uploaded_image.name)[1].lower()
            if file_ext in {'.heic', '.heif'}:
                messages.error(request, "HEIC/HEIF files are not supported in browser preview. Please upload JPG, PNG, or WEBP image.")
                return redirect('profile')

            image_folder = os.path.join(settings.MEDIA_ROOT, "hall")
            os.makedirs(image_folder, exist_ok=True)
            image_name = get_valid_filename(
                f"hall_{admin.id}_{uploaded_image.name}"
            )
            image_path = os.path.join(image_folder, image_name)
            with open(image_path, "wb+") as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)
            admin.image = f"hall/{image_name}"
    #______________________________________________________________imagecode___________
        admin.save(update_fields=[
            "adminName",
            "hallName",
            "emailAddress",
            "mobileNumber",
            "image",
        ]) 

        request.session["admin_name"] = admin.adminName
        request.session["hall_name"] = admin.hallName
        request.session["admin_mobile"] = admin.mobileNumber
        request.session["admin_image"] = admin.image.name if admin.image else ""
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
   
    return render(request, "hall/profile.html", {"admin": admin})

 # ------___------____------____----_____CHANGE PASSWORD PAGE ------____----_____-----____---_______------____--

def changepassword(request):
     if not request.session.get('admin_logged_in'):
        messages.error(request, "Please login first!")
        return redirect('login')
    # Check admin login
    
     if request.method == "POST":
        currentPassword = request.POST.get("currentPassword", "").strip()
        newPassword = request.POST.get("newPassword", "").strip()
        confirmPassword = request.POST.get("confirmPassword", "").strip()

        hall_id = request.session.get('hall_id')

        # Get logged-in admin
        admin = Admin.objects.get(id=request.session.get('admin_id'))

        # Check current password
        if admin.password != currentPassword:
            messages.error(request, "Current password is incorrect!")
            return redirect('changepassword')

        # Check new and confirm password
        if newPassword != confirmPassword:
            messages.error(request,"New password and confirm password do not match!")
            return redirect('changepassword')

        # Update password
        admin.password = newPassword
        admin.save()
        
        messages.success(request, "Password changed successfully!")
        return redirect('changepassword')
    
     return render(request, 'hall/changepassword.html')
     