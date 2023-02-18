from django.contrib import admin
from .models import User,Product,Wishlist,Cart,Transaction
# Register your models here.

admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Transaction)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	search_fields = ['fname']
	list_display = ("id","fname", "lname","email")