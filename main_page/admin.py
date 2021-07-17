from django.contrib import admin

from .models import Personal_info, Projects, Profesional_info, educ_info


admin.site.register(Personal_info)
admin.site.register(Profesional_info)
admin.site.register(educ_info)
admin.site.register(Projects)



