# from django.contrib import admin
#
# from models import Projects
#
#
# class ProjectsAdmin(admin.ModelAdmin):
#     exclude = ('creator',)
#
#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.creator = request.user
#         obj.save()
#
# admin.site.register(Projects, ProjectsAdmin)