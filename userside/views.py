from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from comman.models import AboutPage, Contact, CounterSection, GalleryPage, HomePage, User
from django.contrib import messages

# Create your views here.
def index(request):
    homepage = [
        {
            "logo": item.logo.url if item.logo else "",
            "image": item.image.url if item.image else "",  
            "heading": item.heading,
            "description": item.description,
            "secondHeading": item.secondHeading,
            "secondDescription": item.secondDescription,
            "thirdHeading": item.thirdHeading,
            "thirdDescription": item.thirdDescription,
        }
        for item in HomePage.objects.order_by("-id")[:1]
    ]
    countersection = CounterSection.objects.order_by("-id").first()
    return render(request, 'userside/index.html', {'homepage': homepage, 'countersection': countersection})


def about(request):
    about_pages = [ 
        {
            "BackgroundImage": item.BackgroundImage.url if item.BackgroundImage else "",
            "FirstImage": item.FirstImage.url if item.FirstImage else "",
            "Heading": item.Heading,
            "Description": item.Description,
            "SecondImage": item.SecondImage.url if item.SecondImage else "",
        }
        for item in AboutPage.objects.all().order_by("-id")
    ]
    return render(request, 'userside/about.html', {'about': about_pages})

def gallery(request):
    gallery_pages = [
        {
            "BackgroundImage": item.BackgroundImage.url if item.BackgroundImage else "",
            "oneImage": item.oneImage.url if item.oneImage else "",
            "secondImage": item.secondImage.url if item.secondImage else "",
            "thirdImage": item.thirdImage.url if item.thirdImage else "",
            "fourthImage": item.fourthImage.url if item.fourthImage else "",
        }
        for item in GalleryPage.objects.order_by("-id")[:1]
    ]
    gallery_background = gallery_pages[0]["BackgroundImage"] if gallery_pages else ""
    return render( request,'userside/gallery.html',{'galleries': gallery_pages, 'gallery_background': gallery_background},
    )

def _contact_context():
    contact = Contact.objects.order_by("-id").first()
    return {'contact': contact}


def contact(request):
    return render(request, 'userside/contact.html', _contact_context())


def register(request):
    if request.method != "POST":
        return redirect("contact")

    form_data = {
        "name": request.POST.get("name", "").strip(),
        "email": request.POST.get("email", "").strip(),
        "mobile": request.POST.get("mobile", "").strip(),
        "subject": request.POST.get("subject", "").strip(),
        "address": request.POST.get("address", "").strip(),
    }
    required_fields = {
        "name": "Name",
        "email": "Email",
        "mobile": "Mobile number",
        "subject": "Subject",
        "address": "Address",
    }
    errors = [
        f"{label} is required."
        for field, label in required_fields.items()
        if not form_data[field]
    ]

    if form_data["email"]:
        try:
            validate_email(form_data["email"])
        except ValidationError:
            errors.append("Enter a valid email address.")

    for field, label in (
        ("name", "Name"),
        ("email", "Email"),
        ("mobile", "Mobile number"),
        ("subject", "Subject"),
        ("address", "Address"),
    ):
        if len(form_data[field]) > 175:
            errors.append(f"{label} must be 175 characters or fewer.")

    if errors:
        return render(
            request,
            "userside/contact.html",
            {**_contact_context(), "form_data": form_data, "form_errors": errors},
        )

    User.objects.create(
        userName=form_data["name"],
        emailAddress=form_data["email"],
        mobileNumber=form_data["mobile"],
        homeAddress=form_data["address"],
        subject=form_data["subject"],
    )
    messages.success(request, "Your details were submitted successfully.")
    return redirect("contact")