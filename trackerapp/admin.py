from django.contrib import admin
from models import UserExtend
# Register your models here.

class UserExtendAdmin(admin.ModelAdmin):
	list_display = ["username", "gender", "dob", "emi", "subscription", "subscription_date"]
	class Meta:
		model = UserExtend

admin.site.register(UserExtend, UserExtendAdmin)
