# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
    TemplateView)
from rest_framework import viewsets

from nobinobi_child.forms import LoginAuthenticationForm
from nobinobi_child.serializers import ChildSerializer
from nobinobi_child.utils import get_display_contact_address
from .models import (
    Child,
    Language,
    Absence,
    Classroom,
    AgeGroup,
    AbsenceType,
    AbsenceGroup,
    ClassroomDayOff,
    ChildToPeriod,
    Period,
    InformationOfTheDay,
    Allergy,
    ChildToContact,
    Contact,
    Address,
    FoodRestriction,
    ChildSpecificNeed,
)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "nobinobi_child/home.html"


class AuthLoginView(LoginView):
    template_name = 'nobinobi_child/pages/login/login.html'
    redirect_authenticated_user = True
    form_class = LoginAuthenticationForm


class ChildCreateView(CreateView):
    model = Child


class ChildDeleteView(DeleteView):
    model = Child


class ChildDetailView(DetailView):
    model = Child

    def get_context_data(self, **kwargs):
        context = super(ChildDetailView, self).get_context_data(**kwargs)
        context['title'] = _("{}'s details").format(context['child'].full_name)
        context['display_contacts_address'] = get_display_contact_address()
        context['periods'] = Period.objects.all()
        child_periods = context['child'].childtoperiod_set.all()
        table_periods_used = {}
        # construction table
        for period in context['periods']:
            if period.weekday not in table_periods_used:
                table_periods_used[period.weekday] = {}
            table_periods_used[period.weekday][period.order] = False

        # fill table
        for ctp in child_periods:
            table_periods_used[ctp.period.weekday][ctp.period.order] = True

        context['table_periods_used'] = table_periods_used
        return context


class ChildUpdateView(UpdateView):
    model = Child


class ChildListView(ListView):
    model = Child

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ChildListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = _("Child list")
        return context


class ChildViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class LanguageCreateView(CreateView):
    model = Language


class LanguageDeleteView(DeleteView):
    model = Language


class LanguageDetailView(DetailView):
    model = Language


class LanguageUpdateView(UpdateView):
    model = Language


class LanguageListView(ListView):
    model = Language


class AbsenceCreateView(CreateView):
    model = Absence


class AbsenceDeleteView(DeleteView):
    model = Absence


class AbsenceDetailView(DetailView):
    model = Absence


class AbsenceUpdateView(UpdateView):
    model = Absence


class AbsenceListView(ListView):
    model = Absence


class ClassroomCreateView(CreateView):
    model = Classroom


class ClassroomDeleteView(DeleteView):
    model = Classroom


class ClassroomDetailView(DetailView):
    model = Classroom


class ClassroomUpdateView(UpdateView):
    model = Classroom


class ClassroomListView(ListView):
    model = Classroom


class AgeGroupCreateView(CreateView):
    model = AgeGroup


class AgeGroupDeleteView(DeleteView):
    model = AgeGroup


class AgeGroupDetailView(DetailView):
    model = AgeGroup


class AgeGroupUpdateView(UpdateView):
    model = AgeGroup


class AgeGroupListView(ListView):
    model = AgeGroup


class AbsenceTypeCreateView(CreateView):
    model = AbsenceType


class AbsenceTypeDeleteView(DeleteView):
    model = AbsenceType


class AbsenceTypeDetailView(DetailView):
    model = AbsenceType


class AbsenceTypeUpdateView(UpdateView):
    model = AbsenceType


class AbsenceTypeListView(ListView):
    model = AbsenceType


class AbsenceGroupCreateView(CreateView):
    model = AbsenceGroup


class AbsenceGroupDeleteView(DeleteView):
    model = AbsenceGroup


class AbsenceGroupDetailView(DetailView):
    model = AbsenceGroup


class AbsenceGroupUpdateView(UpdateView):
    model = AbsenceGroup


class AbsenceGroupListView(ListView):
    model = AbsenceGroup


class ClassroomDayOffCreateView(CreateView):
    model = ClassroomDayOff


class ClassroomDayOffDeleteView(DeleteView):
    model = ClassroomDayOff


class ClassroomDayOffDetailView(DetailView):
    model = ClassroomDayOff


class ClassroomDayOffUpdateView(UpdateView):
    model = ClassroomDayOff


class ClassroomDayOffListView(ListView):
    model = ClassroomDayOff


class ChildToPeriodCreateView(CreateView):
    model = ChildToPeriod


class ChildToPeriodDeleteView(DeleteView):
    model = ChildToPeriod


class ChildToPeriodDetailView(DetailView):
    model = ChildToPeriod


class ChildToPeriodUpdateView(UpdateView):
    model = ChildToPeriod


class ChildToPeriodListView(ListView):
    model = ChildToPeriod


class PeriodCreateView(CreateView):
    model = Period


class PeriodDeleteView(DeleteView):
    model = Period


class PeriodDetailView(DetailView):
    model = Period


class PeriodUpdateView(UpdateView):
    model = Period


class PeriodListView(ListView):
    model = Period


class InformationOfTheDayCreateView(CreateView):
    model = InformationOfTheDay


class InformationOfTheDayDeleteView(DeleteView):
    model = InformationOfTheDay


class InformationOfTheDayDetailView(DetailView):
    model = InformationOfTheDay


class InformationOfTheDayUpdateView(UpdateView):
    model = InformationOfTheDay


class InformationOfTheDayListView(ListView):
    model = InformationOfTheDay


class AllergyCreateView(CreateView):
    model = Allergy


class AllergyDeleteView(DeleteView):
    model = Allergy


class AllergyDetailView(DetailView):
    model = Allergy


class AllergyUpdateView(UpdateView):
    model = Allergy


class AllergyListView(ListView):
    model = Allergy


class ChildToContactCreateView(CreateView):
    model = ChildToContact


class ChildToContactDeleteView(DeleteView):
    model = ChildToContact


class ChildToContactDetailView(DetailView):
    model = ChildToContact


class ChildToContactUpdateView(UpdateView):
    model = ChildToContact


class ChildToContactListView(ListView):
    model = ChildToContact


class ContactCreateView(CreateView):
    model = Contact


class ContactDeleteView(DeleteView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact


class ContactUpdateView(UpdateView):
    model = Contact


class ContactListView(ListView):
    model = Contact


class AddressCreateView(CreateView):
    model = Address


class AddressDeleteView(DeleteView):
    model = Address


class AddressDetailView(DetailView):
    model = Address


class AddressUpdateView(UpdateView):
    model = Address


class AddressListView(ListView):
    model = Address


class FoodRestrictionCreateView(CreateView):
    model = FoodRestriction


class FoodRestrictionDeleteView(DeleteView):
    model = FoodRestriction


class FoodRestrictionDetailView(DetailView):
    model = FoodRestriction


class FoodRestrictionUpdateView(UpdateView):
    model = FoodRestriction


class FoodRestrictionListView(ListView):
    model = FoodRestriction


class ChildSpecificNeedCreateView(CreateView):
    model = ChildSpecificNeed


class ChildSpecificNeedDeleteView(DeleteView):
    model = ChildSpecificNeed


class ChildSpecificNeedDetailView(DetailView):
    model = ChildSpecificNeed


class ChildSpecificNeedUpdateView(UpdateView):
    model = ChildSpecificNeed


class ChildSpecificNeedListView(ListView):
    model = ChildSpecificNeed
