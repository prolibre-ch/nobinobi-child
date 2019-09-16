# -*- coding: utf-8 -*-
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView, BSModalReadView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
    TemplateView)
from nobinobi_staff.models import Staff
from notifications.settings import get_config
from notifications.utils import id2slug
from notifications.views import JsonResponse
from rest_framework import viewsets

from nobinobi_child.forms import LoginAuthenticationForm, AbsenceCreateForm
from nobinobi_child.models import (
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
from nobinobi_child.serializers import ChildSerializer, AbsenceSerializer
from nobinobi_child.utils import get_display_contact_address


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


class ChildDetailView(LoginRequiredMixin, DetailView):
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


class ChildListView(LoginRequiredMixin, ListView):
    model = Child

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ChildListView, self).get_context_data(object_list=None, **kwargs)
        context['classrooms'] = Classroom.objects.all().values_list("name", flat=True)
        context['title'] = _("Child list")
        return context


class ChildViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class AbsenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer


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


class AbsenceCreateView(BSModalCreateView):
    template_name = 'nobinobi_child/absence/absence_create.html'
    form_class = AbsenceCreateForm
    success_message = 'Success: Absence was created.'
    success_url = reverse_lazy('nobinobi_child:Absence_list')


# Read
class AbsenceDetailView(BSModalReadView):
    model = Absence
    template_name = 'nobinobi_child/absence/absence_detail.html'


# Delete
class AbsenceDeleteView(BSModalDeleteView):
    model = Absence
    template_name = 'nobinobi_child/absence/absence_confirm_delete.html'
    success_message = 'Success: Absence was deleted.'
    success_url = reverse_lazy('nobinobi_child:Absence_list')


class AbsenceUpdateView(BSModalUpdateView):
    model = Absence
    template_name = 'nobinobi_child/absence/absence_update.html'
    form_class = AbsenceCreateForm
    success_message = 'Success: Absence was updated.'
    success_url = reverse_lazy('nobinobi_child:Absence_list')


class AbsenceListView(LoginRequiredMixin, ListView):
    model = Absence
    template_name = "nobinobi_child/absence/absence_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AbsenceListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = _("Absences list")
        return context


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


class InformationOfTheDayListView(LoginRequiredMixin, ListView):
    model = InformationOfTheDay

    def get_queryset(self):
        if self.request.user:
            iotds = self.model.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now(),
                                              classrooms__allowed_login=self.request.user)
        else:
            iotds = []
        return iotds


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


class StaffListView(ListView):
    model = Staff
    template_name = "nobinobi_child/staff/staff_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StaffListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = _("Staffs list")
        return context


def dfu_live_all_notification_list(request):
    ''' Return a json with a unread notification list '''
    try:
        user_is_authenticated = request.user.is_authenticated()
    except TypeError:  # Django >= 1.11
        user_is_authenticated = request.user.is_authenticated

    if not user_is_authenticated:
        data = {
            'all_count': 0,
            'all_list': []
        }
        return JsonResponse(data)

    default_num_to_fetch = get_config()['NUM_TO_FETCH']
    try:
        # If they don't specify, make it 5.
        num_to_fetch = request.GET.get('max', default_num_to_fetch)
        num_to_fetch = int(num_to_fetch)
        if not (1 <= num_to_fetch <= 100):
            num_to_fetch = default_num_to_fetch
    except ValueError:  # If casting to an int fails.
        num_to_fetch = default_num_to_fetch

    all_list = []

    for notification in request.user.notifications.filter(timestamp__lte=timezone.localtime())[0:num_to_fetch]:
        struct = model_to_dict(notification)
        struct['slug'] = id2slug(notification.id)
        if notification.actor:
            struct['actor'] = str(notification.actor)
        if notification.target:
            struct['target'] = str(notification.target)
        if notification.action_object:
            struct['action_object'] = str(notification.action_object)
        if notification.data:
            struct['data'] = notification.data
        all_list.append(struct)
        if request.GET.get('mark_as_read'):
            notification.mark_as_read()
    data = {
        'all_count': request.user.notifications.filter(timestamp__lte=timezone.localtime()).count(),
        'all_list': all_list
    }
    return JsonResponse(data)


def dfu_live_all_notification_count(request):
    try:
        user_is_authenticated = request.user.is_authenticated()
    except TypeError:  # Django >= 1.11
        user_is_authenticated = request.user.is_authenticated

    if not user_is_authenticated:
        data = {
            'all_count': 0
        }
    else:
        data = {
            'all_count': request.user.notifications.filter(timestamp__lte=timezone.localtime()).count(),
        }
    return JsonResponse(data)
