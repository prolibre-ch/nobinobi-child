from django.urls import reverse
from django.utils.translation import gettext as _
from menu import Menu, MenuItem

Menu.add_item("main",
              MenuItem(
                  title=_("Children"),
                  url="/child/",
                  icon="fa fa-child",
                  children=[
                      MenuItem(
                          title=_("Children list"),
                          url=reverse("nobinobi_child:Child_list"),
                          icon="fas fa-list"),
                      MenuItem(
                          title=_("List IOTD"),
                          url=reverse("nobinobi_child:InformationOfTheDay_list"),
                          icon="fas fa-list"),
                  ]
              )
              )

# Menu.add_item("main", MenuItem("Staff Only",
#                                reverse("reports.views.staff"),
#                                check=lambda request: request.user.is_staff))
#
# Menu.add_item("main", MenuItem("Superuser Only",
#                                reverse("reports.views.superuser"),
#                                check=lambda request: request.user.is_superuser))
