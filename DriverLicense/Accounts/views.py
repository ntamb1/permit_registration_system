from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView, View
from .models import Ugandan, EastAfrican, Foreigner,Renewal


class HomeView(View):
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            first_name = self.request.POST['first_name']
            last_name = self.request.POST['last_name']
            username = self.request.POST['username']
            email = self.request.POST['email']
            password = self.request.POST['password']
            password1 = self.request.POST['password1']
            if User.objects.filter(username=username).exists():
                messages.warning(self.request, "Username is already being used.")
                return redirect('App:Home')
            elif User.objects.filter(email=email).exists():
                messages.warning(self.request, "Email is already being used.")
                return redirect('App:Home')
            else:
                if password == password1:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.info(self.request, "Account Registered")
                    return redirect('App:Login')
                else:
                    messages.info(self.request, "Password doesn't match")
                    return redirect('App:Home')

    def get(self, *args, **kwargs):
        return render(self.request, 'register.html')


class LoginView(View):
    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            username = self.request.POST['username']
            password = self.request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(self.request, user)
                return redirect('App:Base')
            else:
                messages.warning(self.request, 'Invalid Credentials')
                return redirect('App:Login')

    def get(self, *args, **kwargs):
        return render(self.request, 'login.html')


class BaseView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'Home.html')


class NewForm(View):
    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            if self.request.POST.get("checkB"):
                first_name = self.request.POST['first_name']
                last_name = self.request.POST['last_name']
                nin = self.request.POST['nin']
                id_scan = self.request.POST['id_scan']
                medical_scan = self.request.POST['medical_scan']
                payment_scan = self.request.POST['payment_scan']
                if Ugandan.objects.filter(nin=nin).exists():
                    messages.warning(self.request, "NIN Number already used, check it and try again")
                    return redirect('App:New')
                else:
                    ug = Ugandan.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        nin=nin,
                        id_scan=id_scan,
                        medical_scan=medical_scan,
                        payment_scan=payment_scan

                    )
                    ug.save()
                    print("Ug Saved")
                    messages.info(self.request, "Thank you, Your application is gratefully received")
                    return redirect('App:Base')
            else:
                first_name = self.request.POST['first_name']
                last_name = self.request.POST['last_name']
                visa_no = self.request.POST['visa_no']
                visa_scan = self.request.POST['visa_scan']
                passport_no = self.request.POST['passport_no']
                passport_scan = self.request.POST['passport_scan']
                work_permit_no = self.request.POST['work_permit_no']
                wp_scan = self.request.POST['wp_scan']
                medical_scan = self.request.POST['medical_scan']
                payment_scan = self.request.POST['payment_scan']

                if Foreigner.objects.filter(visa_no=visa_no).exists():
                    messages.warning(self.request, "Visa Number already used, check it and try again")
                    return redirect('App:New')
                elif Foreigner.objects.filter(passport_no=passport_no).exists():
                    messages.warning(self.request, "Passport Number already used, check it and try again")
                    return redirect('App:New')
                elif Foreigner.objects.filter(work_permit_no=work_permit_no).exists():
                    messages.warning(self.request, "Work Permit Number already used check it and try again")
                    return redirect('App:New')
                else:
                    foreigner = Foreigner.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        visa_no=visa_no,
                        visa_scan=visa_scan,
                        passport_no=passport_no,
                        passport_scan=passport_scan,
                        work_permit_no=work_permit_no,
                        wp_scan=wp_scan,
                        medical_scan=medical_scan,
                        payment_scan=payment_scan

                    )
                    foreigner.save()
                    messages.warning(self.request, "Your form is successfully submitted, Thank You!!!")
                    return redirect('App:Base')

    def get(self, *args, **kwargs):
        return render(self.request, 'new.html')


class RenewView(View):
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            c_id = self.request.POST['c_id']
            first_name = self.request.POST['first_name']
            last_name = self.request.POST['last_name']
            expiry_date = self.request.POST['expiry_date']
            scan = self.request.POST['scan']
            payment_scan = self.request.POST['payment_scan']
            if Renewal.objects.filter(c_id=c_id).exists():
                messages.warning(self.request, "Visa Number already used, check it and try again")
                return redirect('App:Renew')
            else:
                renew = Renewal.objects.create(
                    c_id=c_id,
                    first_name=first_name,
                    last_name=last_name,
                    expiry_date=expiry_date,
                    scan=scan,
                    payment_scan=payment_scan
                )
                renew.save()
                messages.warning(self.request, "Your form is successfully submitted, Thank You!!!")
                return redirect('App:Base')

    def get(self, *args, **kwargs):
        return render(self.request, 'renew.html')






