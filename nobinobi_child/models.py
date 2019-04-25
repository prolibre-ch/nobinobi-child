# -*- coding: utf-8 -*-
import os
import uuid

from django.contrib.postgres.fields import DateTimeRangeField, DateRangeField
from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField, SplitField
from model_utils.models import TimeStampedModel, StatusModel
from nobinobi_staff.models import Staff
from phonenumber_field.modelfields import PhoneNumberField

from nobinobi_child.utils import get_unique_slug

WEEKDAY_CHOICES = Choices(
    (1, "monday", _("Monday")),
    (2, "tuesday", _("Tuesday")),
    (3, "wednesday", _("Wednesday")),
    (4, "thursday", _("Thursday")),
    (5, "friday", _("Friday")),
    (6, "saturday", _("Saturday")),
    (7, "sunday", _("Sunday")),
)


class Child(StatusModel, TimeStampedModel):
    def upload_picture_child(self, filename):
        f, ext = os.path.splitext(filename)
        upload_to = "child/%s/" % self.slug
        return '%s%s%s' % (upload_to, uuid.uuid4().hex, ext)

    STATUS = Choices(
        ("in_progress", _('In progress')),
        ("archived", _('Archived')),
        ("future", _('Future'))
    )
    GENDER_CHOICES = Choices(
        ("boy", _("Boy")),
        ("girl", _("Girl")),
        ("other", _("Other")),
    )
    """
    Model to store child
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    usual_name = models.CharField(_("Usual name"), max_length=100)
    gender = StatusField(_("Gender"), choices_name="GENDER_CHOICES", blank=False, null=True)
    slug = models.SlugField(_("Slug"))
    picture = models.ImageField(_("Picture"), upload_to=upload_picture_child, blank=True, null=True)
    birth_date = models.DateField(_("Birth date"), blank=True, null=True)
    languages = models.ManyToManyField(
        to="Language",
        verbose_name=_("Languages"),
        related_name="languages",
    )
    red_list = models.CharField(_("Red list"), max_length=255, blank=True, null=True)
    comment = models.CharField(_("Comment"), max_length=255, blank=True, null=True)
    renewal_date = models.DateField(_("Renewal date"), blank=True, null=True)

    classroom = models.ForeignKey(
        to="Classroom",
        verbose_name=_("Classroom"),
        on_delete=models.SET_NULL,
        related_name="classroom",
        db_index=True,
        blank=True,
        null=True,
    )

    next_classroom = models.ForeignKey(
        to="Classroom",
        verbose_name=_("Next classroom"),
        on_delete=models.SET_NULL,
        related_name="next_classroom",
        blank=True,
        null=True,
    )
    date_next_classroom = models.DateField(verbose_name=_("Date next classroom"), blank=True, null=True)

    age_group = models.ForeignKey(
        to="AgeGroup",
        verbose_name=_("Age group"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    staff = models.ForeignKey(
        to=Staff,
        verbose_name=_("Staff"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    food_restrictions = models.ManyToManyField(
        to="FoodRestriction",
        verbose_name=_("Food restrictions"),
        related_name="food_restrictions",
        blank=True,
    )
    allergies = models.ManyToManyField(
        to="Allergy",
        verbose_name=_("Allergies"),
        related_name="allergies",
        blank=True,
    )
    periods = models.ManyToManyField(
        to="Period",
        through="ChildToPeriod",
        through_fields=("child", "period"),
        verbose_name=_("Periods"),
        related_name="periods",
        blank=True,
    )
    contacts = models.ManyToManyField(
        to="Contact",
        through="ChildToContact",
        through_fields=("child", "contact"),
        verbose_name=_("Contacts"),
        related_name="contacts",
        blank=True,
    )

    class Meta:
        ordering = ('first_name', 'last_name', "created",)
        verbose_name = _('Child')
        verbose_name_plural = _('Children')

    def __str__(self):
        return "{}".format(self.get_full_name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # set slug, title field
        self.slug = get_unique_slug(self, 'get_full_name', 'slug')
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.usual_name = self.usual_name.title()
        return super(Child, self).save()

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    get_full_name.fget.short_description = _("Full name")

    @property
    def is_active(self):
        # return true if child is in progress else false
        return True if self.status == self.STATUS.in_progress else False


class Language(TimeStampedModel):
    """
    Models to store language
    """
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ("name", "created",)
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        # return name of language
        return self.name


class Absence(TimeStampedModel):
    """
    Models to store child absence
    """
    child = models.ForeignKey(
        to=Child,
        verbose_name=_("Child"),
        on_delete=models.CASCADE,
    )
    date = DateTimeRangeField(verbose_name=_("Date"), help_text=_("Start date to end date"))
    type = models.ForeignKey(
        to="AbsenceType",
        verbose_name=_("Type"),
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ('date', 'child',)
        verbose_name = _('Absence')
        verbose_name_plural = _('Absences')

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.child, self.type)


class AbsenceType(TimeStampedModel):
    """
    Models to store type of absence
    """
    name = models.CharField(_("Name"), max_length=50)
    group = models.ForeignKey(
        to="AbsenceGroup",
        verbose_name=_("Group"),
        on_delete=models.PROTECT,
    )
    order = models.PositiveIntegerField(_("Order"))

    class Meta:
        ordering = ('order', "group", "name")
        verbose_name = _('Absence type')
        verbose_name_plural = _('Absence types')

    def __str__(self):
        return self.name


class AbsenceGroup(TimeStampedModel):
    """
    Models to store group for absence type
    """
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Absence group')
        verbose_name_plural = _('Absence groups')

    def __str__(self):
        return self.name


class AgeGroup(TimeStampedModel):
    """
    Models to store age group
    """
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"))
    order = models.PositiveIntegerField(_("Order"), unique=True)

    class Meta:
        ordering = ('order', 'name',)
        verbose_name = _('Age group')
        verbose_name_plural = _('Age groups')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # set slug unique
        self.slug = get_unique_slug(self, 'name', 'slug')
        # set name in title
        self.name = self.name.title()
        super().save(*args, **kwargs)


class Classroom(TimeStampedModel):
    """
    Models to store classroom
    """
    OPERATION_MODE = Choices(
        ("creche", _("Creche")),
        ("kindergarten", _("Kindergarten"))
    )

    name = models.CharField(_("Name"), unique=True, max_length=50)
    slug = models.SlugField(_("Slug"), unique=True)
    order = models.PositiveIntegerField(_("Order"), unique=True)
    capacity = models.PositiveIntegerField(_("Capacity"), default=20)
    mode = StatusField(verbose_name=_("Mode"), choices_name="OPERATION_MODE", default=OPERATION_MODE.creche,
                       max_length=15)
    allowed_login = models.ManyToManyField(
        to='auth.User',
        verbose_name=_("Allowed login")
    )

    class Meta:
        ordering = ('order', 'name',)
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # set slug unique
        self.slug = get_unique_slug(self, 'name', 'slug')
        # set name in title
        self.name = self.name.title()
        super().save(*args, **kwargs)


class ClassroomDayOff(TimeStampedModel):
    """
    Models to store the day off classroom
    """

    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, verbose_name=_("Weekday"))
    classrooms = models.ManyToManyField(
        to=Classroom,
        verbose_name=_("Classroom"),
    )

    class Meta:
        ordering = ('weekday',)
        verbose_name = _('Classroom day off')
        verbose_name_plural = _('Classrooms days off')

    def __str__(self):
        return self._get_FIELD_display("weekday")


class ChildToPeriod(TimeStampedModel):
    """
    Models between child and period to store date
    """
    child = models.ForeignKey(
        to="Child",
        verbose_name=_("Child"),
        on_delete=models.CASCADE,
    )
    period = models.ForeignKey(
        to="Period",
        verbose_name=_("Period"),
        on_delete=models.CASCADE,
    )
    date = DateRangeField(_("Date"), help_text=_("Date range for period"))

    class Meta:
        ordering = ('date', 'child', "period")
        verbose_name = _('Child to period')
        verbose_name_plural = _('Children to periods')

    def __str__(self):
        return "{} - {} - {}".format(self.date, self.child, self.period)


class Period(TimeStampedModel):
    """
    Models to store period
    """
    name = models.CharField(_("Name"), max_length=50)
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, verbose_name=_("Weekday"))
    order = models.PositiveIntegerField(_("Order"))

    # TODO: MAX CHILD to implement future

    class Meta:
        ordering = ("weekday", 'order', "name",)
        unique_together = ("weekday", "order")
        verbose_name = _('Period')
        verbose_name_plural = _('Periods')

    def __str__(self):
        return "{} {}".format(self.get_weekday_display(), self.name)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.title()
        return super(Period, self).save(force_insert=False, force_update=False, using=None,
                                        update_fields=None)


class InformationOfTheDay(TimeStampedModel):
    classrooms = models.ManyToManyField(
        to=Classroom,
        verbose_name=_("Classroom"),
        related_name="classrooms"
    )
    date = DateTimeRangeField(_("Date"), help_text=_("Date time range for information"))
    content = SplitField(_("Content"))

    class Meta:
        ordering = ('date',)
        verbose_name = _('Information of the day')
        verbose_name_plural = _('Information of the days')

    def __str__(self):
        return "IOTD: {}".format(self.date)


class Allergy(TimeStampedModel):
    """
    Models to store allergy
    """
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Allergy')
        verbose_name_plural = _('Allergies')

    def __str__(self):
        return self.name


class ChildToContact(TimeStampedModel):
    """
    Models between child and contact to store type
    """
    child = models.ForeignKey(
        to="Child",
        verbose_name=_("Child"),
        on_delete=models.CASCADE,
    )
    contact = models.ForeignKey(
        to="Contact",
        verbose_name=_("Contact"),
        on_delete=models.CASCADE,
    )
    link_with_child = models.CharField(verbose_name=_("Link with child"),
                                       help_text=_("Type contact: Example Father, Mother ..."), max_length=50)
    order = models.PositiveIntegerField(verbose_name=_('Order'))

    class Meta:
        ordering = ("child", 'order',)
        verbose_name = _('Child to contact')
        verbose_name_plural = _('Children to contacts')

    def __str__(self):
        return self.link_with_child


class Contact(TimeStampedModel):
    """
    Models to store contacts
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    address = models.ForeignKey(
        to="Address",
        verbose_name=_("Address"),
        on_delete=models.PROTECT,
    )
    email = models.EmailField(_("Email"))
    phone = PhoneNumberField(verbose_name=_("Phone"))
    mobile_phone = PhoneNumberField(verbose_name=_("Mobile phone"), blank=True)
    professional_phone = PhoneNumberField(verbose_name=_("Professional phone"), blank=True)
    organisation = models.CharField(_("Organisation"), max_length=100, blank=True, null=True)
    function = models.CharField(_("Function"), max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('first_name', 'last_name',)
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Address(TimeStampedModel):
    """
    Models to store the address from contacts
    """
    street = models.CharField(_("Street"), max_length=100)
    zip = models.PositiveIntegerField(_("ZIP"))
    city = models.CharField(_("City"), max_length=50)
    country = models.CharField(_("Country"), max_length=50, default=_("Switzerland"))

    class Meta:
        ordering = ('country', 'zip', 'city', 'street')
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return "{}, {} {}, {}".format(self.street, self.zip, self.city, self.country)


class FoodRestriction(TimeStampedModel):
    """
    Models to store Food restriction
    """
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Food restriction')
        verbose_name_plural = _('Food restrictions')

    def __str__(self):
        return self.name


class ChildSpecificNeed(TimeStampedModel):
    """
    Models to store Child with specific problem
    """

    def upload_attachment_child(self, filename):
        f, ext = os.path.splitext(filename)
        upload_to = "child/%s/special/" % self.child.slug
        return '%s%s%s' % (upload_to, uuid.uuid4().hex, ext)

    problem = SplitField(_("Problem"))
    ihp = models.BooleanField(_("Individual home project"), default=True)
    attachment = models.FileField(_("Attachment"), upload_to=upload_attachment_child)
    measure_take = SplitField(_("Measure to take"))
    child = models.OneToOneField(
        to="Child",
        verbose_name=_("Child"),
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('child',)
        verbose_name = _('Child specific need')
        verbose_name_plural = _('Children specific needs')

    def __str__(self):
        return self.child.get_full_name


class LogChangeClassroom(TimeStampedModel):
    """
    Models to store the change classroom for child
    """
    child = models.ForeignKey(
        to=Child,
        verbose_name=_("Child"),
        on_delete=models.CASCADE,
    )
    classroom = models.ForeignKey(
        to=Classroom,
        verbose_name=_("Classroom"),
        on_delete=models.SET_NULL,
        related_name="log_change_classroom",
        blank=True,
        null=True,
    )
    next_classroom = models.ForeignKey(
        to=Classroom,
        verbose_name=_("Next classroom"),
        on_delete=models.SET_NULL,
        related_name="log_change_next_classroom",
        blank=False,
        null=True
    )
    date = models.DateField(_("Date"))

    class Meta:
        ordering = ("date",)
        unique_together = ("child", "classroom")
        verbose_name = _("Log change classroom")
        verbose_name_plural = _("Logs changed classrooms")

    def __str__(self):  # __unicode__ on Python 2
        return '%s | %s -> %s | %s' % (self.child, self.classroom, self.next_classroom, self.date)
