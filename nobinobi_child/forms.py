from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Hidden
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext as _


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
