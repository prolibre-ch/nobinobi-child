from django.contrib import admin
from django.contrib.admin import register

from nobinobi_child.models import Period, Allergy, FoodRestriction, Language, Classroom, AgeGroup, Absence, AbsenceType, \
    AbsenceGroup, ClassroomDayOff, InformationOfTheDay, Contact, Address, ChildSpecificNeed, LogChangeClassroom, Child, \
    ChildToPeriod, ChildToContact


@register(Period)
class PeriodAdmin(admin.ModelAdmin):
    """
        Admin View for Period
    """
    list_display = ('name', 'weekday', 'order')
    list_filter = ('weekday',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name',)
    sortable_by = ("weekday", "order",)


@register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    """
        Admin View for Classroom
    """
    list_display = ('name', 'capacity', 'order', 'mode')
    list_filter = ('mode',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('allowed_login',)
    readonly_fields = ('slug',)
    search_fields = ('name', 'slug', 'capacity', 'mode')


@register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    """
        Admin View for AgeGroup
    """
    list_display = ('name',)
    readonly_fields = ('slug',)
    search_fields = ('name', 'slug')


@register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    """
        Admin View for Allergy
    """
    list_display = ('name',)
    search_fields = ('name',)


@register(FoodRestriction)
class FoodRestrictionAdmin(admin.ModelAdmin):
    """
        Admin View for FoodRestriction
    """
    list_display = ('name',)
    search_fields = ('name',)


@register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """
        Admin View for Language
    """
    list_display = ('name',)
    search_fields = ('name',)


@register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    """
        Admin View for Absence
    """
    list_display = ('child', 'start_date', 'end_date', 'type')
    list_filter = ('start_date', 'end_date', 'type')
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('child',)


@register(AbsenceType)
class AbsenceTypeAdmin(admin.ModelAdmin):
    """
        Admin View for AbsenceType
    """
    list_display = ('name', 'group', 'order')
    list_filter = ('group',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name', 'group')


@register(AbsenceGroup)
class AbsenceGroupAdmin(admin.ModelAdmin):
    """
        Admin View for AbsenceGroup
    """
    list_display = ('name',)
    list_filter = ()
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name',)


class ClassroomInline(admin.TabularInline):
    model = Classroom


@register(ClassroomDayOff)
class ClassroomDayOffAdmin(admin.ModelAdmin):
    """
        Admin View for ClassroomDayOff
    """
    list_display = ('weekday',)
    list_filter = ('weekday',)
    # inlines = [
    #     ClassroomInline,
    # ]
    search_fields = ('weekday',)


@register(InformationOfTheDay)
class InformationOfTheDayAdmin(admin.ModelAdmin):
    """
        Admin View for InformationOfTheDay
    """
    list_display = ('title', 'start_date', 'end_date',)
    list_filter = ('start_date', 'end_date',)
    # /    inlines = [
    #         ClassroomInline,
    #     ]
    search_fields = ('content',)


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
        Admin View for InformationOfTheDay
    """
    list_display = ('full_name', 'email', 'phone', 'organisation', 'function')
    list_filter = ('organisation', 'function')
    # /    inlines = [
    #         ClassroomInline,
    #     ]
    search_fields = (
        'first_name', 'last_name', 'email', 'phone', 'mobile_phone', 'professional_phone', 'organisation', 'function')


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
        Admin View for Address
    """
    list_display = ('street', 'zip', 'city', 'country')
    list_filter = ('zip', 'city', 'country',)
    search_fields = ('street', 'zip', 'city', 'country')


@register(ChildSpecificNeed)
class ChildSpecificNeedAdmin(admin.ModelAdmin):
    """
        Admin View for ChildSpecificNeed
    """
    list_display = ('child', 'ihp', 'attachment')
    list_filter = ('ihp', 'attachment',)
    search_fields = ('problem', 'measure_take', 'child')


@register(LogChangeClassroom)
class LogChangeClassroomAdmin(admin.ModelAdmin):
    """
        Admin View for LogChangeClassroom
    """
    list_display = ('child', 'classroom', 'next_classroom', 'date')
    list_filter = ('classroom', 'next_classroom', 'date')
    search_fields = ('child', 'classroom', 'next_classroom', 'date',)


class ChildToPeriodInline(admin.TabularInline):
    model = ChildToPeriod
    min_num = 0
    extra = 1
    sortable_by = "period__order"
    show_change_link = False
    can_delete = True


class ChildToContactInline(admin.TabularInline):
    model = ChildToContact
    min_num = 0
    extra = 1
    show_change_link = True
    can_delete = True


class ChildSpecificNeedInline(admin.TabularInline):
    model = ChildSpecificNeed
    min_num = 0
    max_num = 1
    extra = 0
    show_change_link = True
    can_delete = True


@register(Child)
class ChildAdmin(admin.ModelAdmin):
    """
        Admin View for Child
    """
    list_display = ('first_name', 'last_name', 'usual_name', 'gender', 'birth_date', 'classroom', 'age_group', 'staff')
    list_filter = ('gender', 'classroom', 'status', 'age_group', 'staff')
    inlines = [
        ChildToPeriodInline,
        ChildToContactInline,
        ChildSpecificNeedInline,
    ]
    # raw_id_fields = ('',)
    readonly_fields = ('slug',)
    search_fields = (
        'first_name', 'last_name', 'usual_name', 'birth_date', 'classroom', 'next_classroom', 'date_next_classroom',
        'age_group', 'staff',)
