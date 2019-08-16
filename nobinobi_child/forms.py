from bootstrap_datepicker_plus import DateTimePickerInput
from bootstrap_modal_forms.forms import BSModalForm
from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden, Div, Field
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _
from django_select2.forms import ModelSelect2Widget

from nobinobi_child.models import Absence, Child, AbsenceType


class LoginAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/accounts/login/'
        self.helper.form_show_labels = False
        self.helper.form_tag = True
        self.helper.layout = Layout(
            AppendedText('username', '<i class="fas fa-user"></i>', placeholder=_("Username")),
            AppendedText('password', '<i class="fas fa-key"></i>', placeholder=_("Password")),
            Hidden('next', '/'),
            Submit("login", _("Sign In"), css_class='btn btn-primary btn-block btn-flat'),
        )


class AbsenceCreateForm(BSModalForm):
    child = forms.ModelChoiceField(
        queryset=Child.objects.filter(status=Child.STATUS.in_progress),
        # widget=ModelSelect2Widget(
        #     model=Child,
        #     search_fields=['first_name__icontains', 'last_name__icontains']
        # ),
    )
    # type = forms.ModelChoiceField(
    #     queryset=AbsenceType.objects.all(),
    #     widget=ModelSelect2Widget(
    #         model=AbsenceType,
    #         search_fields=['name__icontains', 'group__name__icontains']
    #     )
    # )

    class Meta:
        model = Absence
        fields = ["child", "start_date", "end_date", "type"]
        widgets = {
            "start_date": DateTimePickerInput(options={"locale": "fr", "format": "DD/MM/YYYY HH:MM"}),
            "end_date": DateTimePickerInput(options={"locale": "fr", "format": "DD/MM/YYYY HH:MM"}),
        }

    def __init__(self, *args, **kwargs):
        super(AbsenceCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.label_class = "col-lg-2"
        # self.field_class = "col-lg-10"
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field("child", wrapper_class="col-sm-12"),
                Field("start_date", wrapper_class="col-sm-12 col-md-6"),
                Field("end_date", wrapper_class="col-sm-12 col-md-6"),
                Field("type", wrapper_class="col-sm-12"),
                # Submit('submit', _('Submit'), wrapper_class="col-sm-12"),
                css_class="row"
            )
        )
