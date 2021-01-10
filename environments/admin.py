from django.contrib import admin

from .models import Environments

@admin.register(Environments)
class EnvironmentsAdmin(admin.ModelAdmin):

    """ Customizing the Admin panel to give us personalized view """
    list_display = ['date_created', 'name','env_stage', 'platform', 'database', 'run_stack', 'web_server', 'ip', 'status']
    list_filter = ("date_created", )
    search_fields = ('name', 'email', 'body')
admin.site.site_header = "Standard Bank Data Solution - (Data Manager)"
""" Registering our models to the admin apnel for future use """



