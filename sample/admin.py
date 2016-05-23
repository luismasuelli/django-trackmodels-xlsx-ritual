from django.contrib.admin import site, ModelAdmin
from django.utils.translation import ugettext_lazy as _
from grimoire.django.tracked.admin import TrackedLiveAdmin
from grimoire.django.tracked_xls.reports import XLSReport
from .models import SampleRecord, uppercase_content


class CustomCSVReport(XLSReport):

    list_report = ('id', 'content', 'created_on', 'updated_on', uppercase_content)

    def get_cell_format(self, request, column_spec, column_display, column_index, row_index,
                        cell_value, cell_serialized_value):
        if row_index is None:
            return {'bold': True}
        else:
            return {}


class SampleAdmin(TrackedLiveAdmin, ModelAdmin):

    report_generators = [CustomCSVReport('xls', _('XLS Report'))]
    list_display = ('id', 'content', 'created_on', 'updated_on')


site.register(SampleRecord, SampleAdmin)