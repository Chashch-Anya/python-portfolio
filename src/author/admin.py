from django.contrib import admin

from author.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'github',
        'resume',
        'email',
        'created_at',
        "updated_at",
    )

    
    search_fields = (
        'github',
        'resume',
        'email',
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
